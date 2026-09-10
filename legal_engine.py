"""
legal_engine.py
AI Legal Assistant Engine powered by Google Gemini.
Provides citizen-friendly legal rights guidance in Bengali, Hindi, and English.
"""

import os
from typing import Generator, Optional
from dotenv import load_dotenv
from google import genai
from google.genai import types

from legal_knowledge import CORE_LEGAL_GROUNDING

# Load environment variables
load_dotenv()

SYSTEM_INSTRUCTION = f"""
You are "AdhikarSathi" (অধিকারসাথী / अधिकारसाथी), an empathetic, accessible, and knowledgeable Local Language Legal Rights Assistant for Indian citizens.

Your primary mission is to empower everyday citizens with simple, actionable knowledge about their rights under Indian law, specifically focusing on:
1. TENANT RIGHTS (किरायेदार अधिकार / ভাড়াটিয়ার অধিকার): Security deposits, eviction notices, landlord harassment, rent receipts, repair responsibilities.
2. CONSUMER COMPLAINTS (उपभोक्ता संरक्षण / ক্রেতা সুরক্ষা): Defective products, e-commerce refund refusals, deficient services, misleading ads, unfair trade practices, National Consumer Helpline (NCH 1915), and e-Daakhil portal.
3. BASIC CITIZEN & POLICE RIGHTS: Zero FIR, grounds of arrest, NALSA free legal aid (15100), RTI queries, cyber fraud (1930).

REFERENCE KNOWLEDGE BASE:
{CORE_LEGAL_GROUNDING}

CRITICAL RULES FOR RESPONSES:
1. LANGUAGE ADAPTABILITY:
   - Fluent in Bengali (বাংলা), Hindi (हिन्दी), and English.
   - If the user asks in Bengali, answer in simple, warm, and natural Bengali.
   - If the user asks in Hindi, answer in simple, clear Hindi.
   - If the user asks in Hinglish or Banglish (Roman script), answer in very clean, simple Hindi/Bengali or conversational bilingual text that is easiest for them to read.
   - If a language preference is explicitly specified by the system prompt or user, prioritize that language.

2. CITIZEN-FRIENDLY & NO SCARY JARGON:
   - Do NOT dump dense statutory sections without translating them into plain meaning.
   - Break answers down into:
     - 📌 **আপনার অধিকার / आपका अधिकार / Your Right** (What the law says simply)
     - 🪜 **কী করবেন - ধাপে ধাপে / क्या करें - स्टेप-बाई-स्टेप / Actionable Steps** (Step 1, Step 2, Step 3)
     - 📞 **জরুরি নম্বর ও পোর্টাল / जरूरी हेल्पलाइन व पोर्टल / Helplines & Portals** (e.g. NCH 1915, e-Daakhil, NALSA 15100)
     - 💡 **জরুরি টিপস / जरूरी सलाह / Pro-Tip** (e.g. keep written records, WhatsApp screenshots, bank receipts)

3. PRACTICAL TEMPLATES & SAMPLES:
   - Offer or provide short draft messages that the user can copy and send to their landlord or seller.

4. MANDATORY LEGAL DISCLAIMER:
   - Always conclude with a brief 1-line note:
     * English: "*Disclaimer: This is legal awareness information under Indian law, not formal advocate counsel.*"
     * Hindi: "*अस्वीकरण: यह केवल भारतीय कानून की सामान्य जानकारी है, किसी वकील की औपचारिक कानूनी सलाह नहीं।* "
     * Bengali: "*সতর্কবার্তা: এটি ভারতীয় আইন সম্পর্কে সাধারণ আইনি সচেতনতামূলক তথ্য, কোনও আইনজীবীর পেশাদার পরামর্শ নয়।*"
"""

FALLBACK_MODELS = [
    "gemini-3.1-flash-lite",
    "gemini-2.5-flash",
    "gemini-3.6-flash"
]

class LegalRightsBot:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set. Please set it in your .env file or pass it to LegalRightsBot."
            )
        self.client = genai.Client(api_key=self.api_key)
        self.models = FALLBACK_MODELS
        self.model = FALLBACK_MODELS[0]

    def _get_generation_config(self, preferred_language: Optional[str] = None) -> types.GenerateContentConfig:
        instruction = SYSTEM_INSTRUCTION
        if preferred_language == "bn":
            instruction += "\n\nCRITICAL OVERRIDE: YOU MUST PROVIDE YOUR RESPONSE ENTIRELY IN BENGALI (বাংলা). DO NOT USE ENGLISH EXCEPT FOR ACT NAMES OR CODES."
        elif preferred_language == "hi":
            instruction += "\n\nCRITICAL OVERRIDE: YOU MUST PROVIDE YOUR RESPONSE ENTIRELY IN HINDI (हिन्दी). DO NOT USE ENGLISH EXCEPT FOR ACT NAMES OR CODES."
        elif preferred_language == "en":
            instruction += "\n\nCRITICAL OVERRIDE: YOU MUST PROVIDE YOUR RESPONSE ENTIRELY IN ENGLISH."

        return types.GenerateContentConfig(
            system_instruction=instruction,
            temperature=0.3,
            max_output_tokens=1500,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
        )

    def create_chat(self, preferred_language: Optional[str] = None):
        """Creates a stateful multi-turn chat session with Gemini with model fallback."""
        config = self._get_generation_config(preferred_language)
        for model_name in self.models:
            try:
                chat = self.client.chats.create(
                    model=model_name,
                    config=config
                )
                self.model = model_name
                return chat
            except Exception:
                continue
        # Fallback to default
        return self.client.chats.create(model=self.models[0], config=config)

    def ask(self, query: str, preferred_language: Optional[str] = None) -> str:
        """Single turn query execution with automatic fallback across models on 429 quota."""
        config = self._get_generation_config(preferred_language)
        last_err = None
        for model_name in self.models:
            try:
                response = self.client.models.generate_content(
                    model=model_name,
                    contents=query,
                    config=config
                )
                self.model = model_name
                return response.text or ""
            except Exception as e:
                last_err = e
                continue
        return f"⚠️ AI server is temporarily busy or rate-limited. Please retry in 30 seconds. ({last_err})"

    def stream_ask(self, query: str, preferred_language: Optional[str] = None) -> Generator[str, None, None]:
        """Single turn streaming query execution."""
        config = self._get_generation_config(preferred_language)
        response_stream = self.client.models.generate_content_stream(
            model=self.model,
            contents=query,
            config=config
        )
        for chunk in response_stream:
            if chunk.text:
                yield chunk.text
