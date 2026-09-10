# ⚖️ AdhikarSathi (অধিকারসাথী / अधिकारसाथी)
### Local Language Legal Rights Bot (Bengali, Hindi, English)

An AI-powered multilingual citizen legal assistant designed to demystify everyday Indian law — empowering citizens with actionable knowledge about **Tenant Rights**, **Consumer Complaints**, and **Basic Civil Rights** in simple **Bengali (বাংলা)**, **Hindi (हिन्दी)**, and **English** (with full conversational Hinglish/Banglish comprehension).

---

## 🎯 Problem Statement
Everyday citizens in India face intimidating legal jargon and steep costs when dealing with common civil disputes:
- **Tenancy Harassment**: Landlords unlawfully withholding security deposits, threatening sudden evictions without notice, or arbitrarily cutting off electricity and water.
- **Consumer Grievances**: E-commerce platforms or local sellers refusing refunds for defective goods, delayed deliveries, or unfair trade practices.
- **Language Barrier**: Most official legal portals and statutes are written in dense, formal English, leaving regional language speakers (e.g., Bengali and Hindi) vulnerable and unaware of their statutory rights or remedies like the National Consumer Helpline (1915) or e-Daakhil.

## 👥 Target Users
- **Tenants & Students**: Renters who need quick clarity on notice periods, security deposits, and maintenance obligations.
- **Online & Retail Consumers**: Buyers who need a step-by-step roadmap to get refunds or file complaints against unfair sellers.
- **Everyday Citizens**: People looking for free legal aid (NALSA 15100), Zero FIR information, or RTI basics in their mother tongue without expensive advocate fees.

## 💡 Solution
**AdhikarSathi** acts as an empathetic, accessible legal buddy:
1. **Translates Complex Statutes into Plain Action**: Explains the Consumer Protection Act 2019 and Tenancy principles into simple **Do's and Don'ts**.
2. **Step-by-Step Action Roadmap**: Tells the user exactly where to start (customer care -> National Consumer Helpline 1915 -> e-Daakhil portal / Rent Authority).
3. **Formal Notice & Grievance Generator**: Generates customized legal notice templates ready to copy and send to landlords or sellers before taking formal legal steps.
4. **Verified Helplines & Portals**: Instant access to verified government helplines (1915, 15100, 1930, 112).

---

## ✨ Key Features
- **🌐 Multilingual Fluency & Instant Switch**:
  - **বাংলা (Bengali)**: Native, respectful, and simple Bengali terminology.
  - **हिन्दी (Hindi)**: Simple, conversational Hindi and Hinglish.
  - **English**: Clear, jargon-free plain English.
  - **1-Click Language Switch Bar**: Toggle between Bengali, Hindi, English, or Auto-detect in one click.
- **🏠 Comprehensive Tenant Rights**:
  - Security deposit deductions and recovery procedures.
  - Protections against unlawful lockouts, utility cuts, and eviction without 30-day notice.
  - Landlord entry privacy rules and repair responsibilities.
- **🛍️ Consumer Protection (Act 2019)**:
  - Defective goods, deficiency of service, dark patterns, and refund refusals.
  - Step-by-step reporting via National Consumer Helpline (NCH 1915 / consumerhelpline.gov.in).
  - Filing petitions on **e-Daakhil** (edaakhil.nic.in) across District, State, and National commissions.
- **📚 Citizen Legal Guide**:
  - Structured, ready-to-read statutory cheat sheets for Tenant Rights, Consumer Protection, Free Legal Aid (NALSA 15100), and Police Rights (Zero FIR, arrest safeguards).
- **⚖️ Built-in Ethical Disclaimer**:
  - Clearly explains that information provided is for legal awareness and education under Indian law.

---

## 🛠️ Technology Stack
- **Programming Language:** Python 3.14+
- **Package Manager:** [uv](https://docs.astral.sh/uv/)
- **AI Engine:** Google Gemini API (`google-genai` SDK, multi-model fallback architecture: `gemini-3.1-flash-lite`, `gemini-2.5-flash`, `gemini-3.6-flash`)
- **Web UI:** [Streamlit](https://streamlit.io/)
- **CLI Interface:** Interactive Terminal Assistant

---

## 🤖 How Gemini API is Used
- **Multi-Model Architecture:** Uses `gemini-3.1-flash-lite` for ultra-fast streaming responses (~1.5s) with automatic fallback to `gemini-2.5-flash` and `gemini-3.6-flash` to eliminate 429 rate-limit errors.
- **System Instructions:** Tailored prompt grounding Gemini with verified Indian legal frameworks (Consumer Protection Act 2019, Model Tenancy Act principles, NALSA statutory provisions, and penal/civil safeguards).
- **Multi-Turn Chat:** Stateful conversation with `client.chats.create()` enabling contextual follow-ups.
- **Streaming Tokens:** Real-time token streaming with `send_message_stream` for typewriter effect in Streamlit.

---

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd GDG_chatbot
```

### 2. Set up the environment using `uv`
```bash
# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate   # On macOS/Linux
# .venv\Scripts\activate    # On Windows

# Install all dependencies
uv sync
```

### 3. Configure environment variables
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the Project

#### Option A: Launch the Streamlit Web Application (Recommended)
```bash
uv run streamlit run app.py
```
*Or:*
```bash
uv run main.py --web
```
Open your browser at `http://localhost:8501`.

#### Option B: Run in Interactive Terminal (CLI Mode)
```bash
uv run main.py --cli
```

---

## 📸 Demo & Quick Questions to Try

1. **Bengali (Tenant Rights):**
   > *"বাড়িওয়ালা কোনো কারণ ছাড়া সিকিউরিটি ডিপোজিট ফেরত দিতে অস্বীকার করছে। আমি কী আইনি পদক্ষেপ নিতে পারি?"*

2. **Hindi (Consumer Complaint):**
   > *"ई-कॉमर्स साइट से डिफेक्टिव फोन मिला और वे रिफंड देने से मना कर रहे हैं। NCH 1915 पर कैसे शिकायत करूँ?"*

3. **English (e-Daakhil / Eviction):**
   > *"Can a landlord forcibly evict a tenant without notice or cut off electricity? What is the procedure to file on e-Daakhil?"*

4. **Notice Generator Tab**:
   > Input landlord/seller details, disputed amount, and generate a ready-to-send formal notice in 1 click!

---

## 📜 Disclaimer
*AdhikarSathi provides general legal awareness and information under Indian law. It does not constitute formal legal counsel or create an advocate-client relationship. For formal litigation or court representation, please consult an enrolled advocate or reach out to the National Legal Services Authority (NALSA) via toll-free 15100.*