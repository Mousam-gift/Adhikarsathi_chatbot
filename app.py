"""
app.py
AdhikarSathi (অধিকারসাথী / अधिकारसाथी)
Interactive Multilingual Legal Rights Assistant for Indian Citizens (Bengali, Hindi, English)
Powered by Google Gemini (gemini-3.6-flash)
"""

import os
import streamlit as st
from dotenv import load_dotenv

from legal_engine import LegalRightsBot
from legal_knowledge import LEGAL_HELPLINES

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AdhikarSathi ⚖️ Legal Rights Bot",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ──────────────────────────────────────────────
# MASSIVE CSS OVERHAUL — Premium UI with animations
# ──────────────────────────────────────────────
st.markdown("""
<style>
    /* ═══════ GLOBAL ═══════ */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* ═══════ ANIMATED HERO ═══════ */
    @keyframes shimmer {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulse-glow {
        0%, 100% { box-shadow: 0 0 15px rgba(99, 102, 241, 0.3); }
        50% { box-shadow: 0 0 30px rgba(99, 102, 241, 0.6); }
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-6px); }
    }
    @keyframes typing-dot {
        0%, 80%, 100% { opacity: 0; transform: scale(0.6); }
        40% { opacity: 1; transform: scale(1); }
    }

    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 40%, #1e40af 100%);
        border-radius: 16px;
        padding: 32px 36px;
        margin-bottom: 24px;
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.6s ease-out;
    }
    .hero-container::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.04), transparent);
        animation: shimmer 3s infinite;
    }
    .hero-container::after {
        content: '⚖️';
        position: absolute;
        right: 30px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 5rem;
        opacity: 0.12;
        animation: float 4s ease-in-out infinite;
    }
    .hero-title {
        font-size: 2.4rem;
        font-weight: 900;
        color: white;
        margin: 0;
        letter-spacing: -1px;
        position: relative;
        z-index: 1;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: rgba(255,255,255,0.82);
        margin-top: 8px;
        position: relative;
        z-index: 1;
        line-height: 1.6;
    }
    .hero-badges {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 18px;
        position: relative;
        z-index: 1;
    }
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        padding: 6px 14px;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255,255,255,0.15);
        color: #fff;
        transition: all 0.25s ease;
    }
    .hero-badge:hover {
        background: rgba(255,255,255,0.18);
        transform: translateY(-2px);
    }
    .badge-tenant { background: rgba(34, 197, 94, 0.2); }
    .badge-consumer { background: rgba(59, 130, 246, 0.2); }
    .badge-helpline { background: rgba(239, 68, 68, 0.2); }
    .badge-lang { background: rgba(168, 85, 247, 0.2); }

    /* ═══════ STAT CARDS ═══════ */
    .stats-row {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-bottom: 20px;
        animation: fadeInUp 0.7s ease-out 0.1s both;
    }
    .stat-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        transition: all 0.25s ease;
        position: relative;
        overflow: hidden;
    }
    .stat-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        border-color: #6366f1;
    }
    .stat-card::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, #6366f1, #a855f7);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    .stat-card:hover::after { transform: scaleX(1); }
    .stat-icon { font-size: 1.8rem; margin-bottom: 4px; }
    .stat-value {
        font-size: 1.6rem;
        font-weight: 800;
        color: #1e293b;
        line-height: 1.2;
    }
    .stat-label {
        font-size: 0.78rem;
        color: #64748b;
        font-weight: 500;
        margin-top: 2px;
    }

    /* ═══════ SCENARIO CARDS ═══════ */
    .scenario-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
        margin-bottom: 16px;
    }
    .scenario-tile {
        background: linear-gradient(135deg, #f8fafc, #f1f5f9);
        border: 1.5px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px 18px;
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    .scenario-tile:hover {
        background: linear-gradient(135deg, #eff6ff, #e0f2fe);
        border-color: #3b82f6;
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.12);
    }
    .scenario-tile::before {
        content: '';
        position: absolute;
        top: -50%; right: -50%;
        width: 100%; height: 100%;
        background: radial-gradient(circle, rgba(99,102,241,0.06) 0%, transparent 70%);
        transition: all 0.4s ease;
    }
    .scenario-tile:hover::before { top: -20%; right: -20%; }
    .scenario-emoji { font-size: 1.6rem; }
    .scenario-title {
        font-weight: 700;
        font-size: 0.9rem;
        color: #1e293b;
        margin-top: 6px;
    }
    .scenario-desc {
        font-size: 0.78rem;
        color: #64748b;
        margin-top: 3px;
        line-height: 1.4;
    }
    .scenario-lang {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 0.7rem;
        font-weight: 600;
        margin-top: 6px;
    }
    .lang-bn { background: #fef3c7; color: #92400e; }
    .lang-hi { background: #fee2e2; color: #991b1b; }
    .lang-en { background: #dbeafe; color: #1e40af; }
    .lang-mix { background: #ede9fe; color: #5b21b6; }

    /* ═══════ SIDEBAR HELPLINE CARDS ═══════ */
    .sidebar-card {
        background: linear-gradient(135deg, #ffffff, #f8fafc);
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 12px;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    .sidebar-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.06);
    }
    .sidebar-card-accent {
        position: absolute;
        left: 0; top: 0; bottom: 0;
        width: 4px;
        border-radius: 4px 0 0 4px;
    }
    .accent-blue { background: linear-gradient(to bottom, #3b82f6, #6366f1); }
    .accent-green { background: linear-gradient(to bottom, #22c55e, #16a34a); }
    .accent-red { background: linear-gradient(to bottom, #ef4444, #dc2626); }
    .sidebar-card-title {
        font-weight: 700;
        font-size: 0.85rem;
        color: #334155;
        margin-left: 8px;
    }
    .sidebar-card-num {
        font-size: 1.5rem;
        font-weight: 900;
        color: #0f172a;
        margin: 4px 0 2px 8px;
        letter-spacing: 1px;
    }
    .sidebar-card-links {
        margin-left: 8px;
        font-size: 0.75rem;
    }
    .sidebar-card-links a {
        color: #6366f1;
        text-decoration: none;
        font-weight: 500;
    }
    .sidebar-card-links a:hover { text-decoration: underline; }

    /* ═══════ DISCLAIMER ═══════ */
    .disclaimer-modern {
        background: linear-gradient(135deg, #fffbeb, #fef3c7);
        border: 1px solid #fde68a;
        border-radius: 12px;
        padding: 14px 18px;
        margin-top: 24px;
        font-size: 0.83rem;
        color: #92400e;
        display: flex;
        align-items: flex-start;
        gap: 10px;
    }
    .disclaimer-modern-icon { font-size: 1.2rem; }
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# BOT INIT
# ──────────────────────────────────────────────
@st.cache_resource
def get_bot():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None
    try:
        return LegalRightsBot(api_key=api_key)
    except Exception as e:
        st.error(f"Error initializing Gemini Legal Engine: {e}")
        return None

bot = get_bot()

# ──────────────────────────────────────────────
# STATE MANAGEMENT
# ──────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "🙏 **নমস্কার! / नमस्ते! / Welcome!**\n\n"
                "I am **AdhikarSathi** (অধিকারসাথী) ⚖️, your AI Legal Rights Companion. I help everyday Indian citizens understand their rights in simple words:\n\n"
                "| Topic | What I Cover |\n"
                "|---|---|\n"
                "| 🏠 **Tenant Rights** | Security deposits, notice periods, unlawful lockout, repair duties |\n"
                "| 🛍️ **Consumer Protection** | Defective items, refund refusals, e-commerce disputes, NCH 1915 |\n"
                "| 🛡️ **Citizen Safeguards** | Zero FIR, NALSA 15100 free legal aid, cyber fraud 1930 |\n\n"
                "💬 **Ask me in বাংলা, हिन्दी, English, or Hinglish/Banglish!**\n\n"
                "📖 Switch to the **📚 Legal Guide** tab to view statutory rights, helplines, and FAQs!"
            )
        }
    ]

if "chat_session" not in st.session_state or st.session_state.chat_session is None:
    if bot:
        st.session_state.chat_session = bot.create_chat()

# ──────────────────────────────────────────────
# SIDEBAR
# ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚖️ AdhikarSathi")
    st.caption("অধিকারসাথী • अधिकारसाथी • Your Rights Companion")

    st.divider()

    # ──────────────────────────────────────────────
    # LANGUAGE SWITCHER (INTERACTIVE)
    # ──────────────────────────────────────────────
    st.markdown("##### 🌐 Change Language / ভাষা পরিবর্তন / भाषा बदलें")

    def switch_language(target_lang_name):
        code_map = {
            "Auto-detect (সব ভাষা / सभी भाषाएँ)": None,
            "English": "en",
            "हिन्दी (Hindi)": "hi",
            "বাংলা (Bengali)": "bn"
        }
        lang_code = code_map.get(target_lang_name)
        st.session_state.active_language = target_lang_name
        st.session_state.selected_lang_code = lang_code
        if bot:
            st.session_state.chat_session = bot.create_chat(preferred_language=lang_code)

        if lang_code == "bn":
            greeting = "🌐 **ভাষা পরিবর্তন করা হয়েছে: বাংলা (Bengali)**\n\nনমস্কার! আমি **অধিকারসাথী**। এখন থেকে আমি সম্পূর্ণ বাংলায় আপনার সাথে কথা বলব। ভাড়াটিয়া অধিকার বা ক্রেতা সুরক্ষা নিয়ে আপনার কী প্রশ্ন আছে বলুন।"
            st.toast("ভাষা পরিবর্তন হয়েছে: বাংলা", icon="🇧🇩")
        elif lang_code == "hi":
            greeting = "🌐 **भाषा बदल दी गई है: हिन्दी (Hindi)**\n\nनमस्ते! मैं **अधिकारसाथी** हूँ। अब से मैं आपसे पूरी तरह हिन्दी में बात करूँगा। किरायेदार अधिकार या उपभोक्ता शिकायत के संबंध में आपका क्या प्रश्न है?"
            st.toast("भाषा बदल दी गई: हिन्दी", icon="🇮🇳")
        elif lang_code == "en":
            greeting = "🌐 **Language Changed: English**\n\nHello! I am **AdhikarSathi**. I will now assist you in English. What legal question or grievance can I help you with?"
            st.toast("Language changed: English", icon="🇬🇧")
        else:
            greeting = "🌐 **Language Set: Auto-detect**\n\nYou can ask in Bengali, Hindi, or English, and I will reply in your language!"
            st.toast("Auto-detect enabled", icon="🌐")

        st.session_state.messages.append({"role": "assistant", "content": greeting})

    lang_options = [
        "Auto-detect (সব ভাষা / सभी भाषाएँ)",
        "English",
        "हिन्दी (Hindi)",
        "বাংলা (Bengali)"
    ]
    current_active = st.session_state.get("active_language", "Auto-detect (সব ভাষা / सभी भाषाएँ)")
    current_idx = lang_options.index(current_active) if current_active in lang_options else 0

    selected_choice = st.selectbox(
        "Select Language / ভাষা নির্বাচন করুন:",
        options=lang_options,
        index=current_idx,
        key="sidebar_lang_selector"
    )

    if selected_choice != current_active:
        switch_language(selected_choice)
        st.rerun()

    selected_lang_code = st.session_state.get("selected_lang_code", None)

    st.divider()
    st.markdown("##### 📞 Emergency Helplines")

    # NCH
    nch = LEGAL_HELPLINES["consumer"]
    st.markdown(f"""
    <div class="sidebar-card">
        <div class="sidebar-card-accent accent-blue"></div>
        <div class="sidebar-card-title">🛒 {nch['title']}</div>
        <div class="sidebar-card-num">📞 {nch['toll_free']}</div>
        <div class="sidebar-card-links">
            <a href="{nch['website']}" target="_blank">consumerhelpline.gov.in</a> ·
            <a href="{nch['edaakhil']}" target="_blank">e-Daakhil</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # NALSA
    nalsa = LEGAL_HELPLINES["legal_aid"]
    st.markdown(f"""
    <div class="sidebar-card">
        <div class="sidebar-card-accent accent-green"></div>
        <div class="sidebar-card-title">⚖️ {nalsa['title']}</div>
        <div class="sidebar-card-num">📞 {nalsa['toll_free']}</div>
        <div class="sidebar-card-links">
            Free legal aid · <a href="{nalsa['website']}" target="_blank">nalsa.gov.in</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Cybercrime
    cyber = LEGAL_HELPLINES["cyber_crime"]
    st.markdown(f"""
    <div class="sidebar-card">
        <div class="sidebar-card-accent accent-red"></div>
        <div class="sidebar-card-title">🛡️ Cyber Crime Helpline</div>
        <div class="sidebar-card-num">📞 {cyber['toll_free']}</div>
        <div class="sidebar-card-links">
            Financial fraud · <a href="{cyber['website']}" target="_blank">cybercrime.gov.in</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔄 New Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.chat_session = bot.create_chat(preferred_language=selected_lang_code) if bot else None
            st.rerun()
    with c2:
        if st.button("ℹ️ About", use_container_width=True):
            st.toast("AdhikarSathi • GDG Hackathon • Gemini 3.6 Flash", icon="⚖️")

# ──────────────────────────────────────────────
# API KEY GUARD
# ──────────────────────────────────────────────
if not bot:
    st.error("⚠️ `GEMINI_API_KEY` is not configured! Add your API key to `.env` to continue.")
    st.stop()

# ──────────────────────────────────────────────
# HERO BANNER
# ──────────────────────────────────────────────
st.markdown("""
<div class="hero-container">
    <div class="hero-title">AdhikarSathi • অধিকারসাথী</div>
    <div class="hero-subtitle">
        Empowering Indian citizens with simple, actionable legal knowledge for
        <strong>Tenant Rights</strong> & <strong>Consumer Complaints</strong>
        in Bengali, Hindi, and English.
    </div>
    <div class="hero-badges">
        <span class="hero-badge badge-tenant">🏠 Tenant Protections</span>
        <span class="hero-badge badge-consumer">🛍️ Consumer Act 2019</span>
        <span class="hero-badge badge-helpline">📞 NCH 1915 · e-Daakhil</span>
        <span class="hero-badge badge-lang">🗣️ বাংলা · हिन्दी · English</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# STAT COUNTERS
# ──────────────────────────────────────────────
st.markdown("""
<div class="stats-row">
    <div class="stat-card">
        <div class="stat-icon">🏠</div>
        <div class="stat-value">6+</div>
        <div class="stat-label">Tenant Rights Covered</div>
    </div>
    <div class="stat-card">
        <div class="stat-icon">🛍️</div>
        <div class="stat-value">5+</div>
        <div class="stat-label">Consumer Protections</div>
    </div>
    <div class="stat-card">
        <div class="stat-icon">📞</div>
        <div class="stat-value">4</div>
        <div class="stat-label">Official Helplines</div>
    </div>
    <div class="stat-card">
        <div class="stat-icon">🗣️</div>
        <div class="stat-value">3</div>
        <div class="stat-label">Languages Supported</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────
# MAIN TABS (AI Chat & Legal Guide)
# ──────────────────────────────────────────────
tab_chat, tab_guide = st.tabs([
    "💬 AI Legal Chat",
    "📚 Legal Guide"
])

# ══════════════════════════════════════════════
# TAB 1: INTERACTIVE CHAT
# ══════════════════════════════════════════════
with tab_chat:

    # Scenario Prompt Cards (rendered as styled buttons)
    st.markdown("##### 💡 Quick Legal Scenarios — click to ask instantly:")

    scenario_data = [
        {
            "emoji": "🏠",
            "title": "Deposit Not Returned",
            "desc": "বাড়িওয়ালা ₹35,000 সিকিউরিটি ডিপোজিট ফেরত দিচ্ছে না",
            "lang": "বাংলা",
            "lang_class": "lang-bn",
            "prompt": "বাড়িওয়ালা কোনো রসিদ বা কারণ ছাড়া আমার ₹৩৫,০০০ সিকিউরিটি ডিপোজিট ফেরত দিতে অস্বীকার করছে। বাড়ি ছেড়ে দিয়েছি, চাবি দিয়ে দিয়েছি। আমার আইনি অধিকার কী এবং কী পদক্ষেপ নেওয়া উচিত?"
        },
        {
            "emoji": "🛍️",
            "title": "Defective Product Refund",
            "desc": "ऑनलाइन खरीदा ₹18,000 का फोन खराब, रिफंड नहीं मिला",
            "lang": "हिन्दी",
            "lang_class": "lang-hi",
            "prompt": "ऑनलाइन खरीदा ₹18,000 का फोन खराब निकला और सेलर रिफंड देने से मना कर रहा है। मैं NCH 1915 पर शिकायत कैसे करूँ और e-Daakhil पर कैसे केस फाइल करूँ?"
        },
        {
            "emoji": "⚡",
            "title": "Illegal Power/Water Cut",
            "desc": "Landlord disconnected electricity and water illegally",
            "lang": "English",
            "lang_class": "lang-en",
            "prompt": "My landlord illegally disconnected my electricity and water supply after a minor argument. Can I file a police complaint or approach Rent Authority? What are my immediate legal remedies?"
        },
        {
            "emoji": "🍽️",
            "title": "Overcharging Above MRP",
            "desc": "Restaurant MRP se jyada charge kar raha hai",
            "lang": "Hinglish",
            "lang_class": "lang-mix",
            "prompt": "Restaurant and airport stall MRP se jyada charge kar rahe hain packed items par. Kya ye Consumer Protection Act 2019 ke under unfair trade practice hai? Main kaise complaint kar sakta hun?"
        }
    ]

    # ──────────────────────────────────────────────
    # 1-CLICK QUICK LANGUAGE SWITCH BUTTONS
    # ──────────────────────────────────────────────
    st.markdown("##### 🌐 Change Language / ভাষা পরিবর্তন / भाषा बदलें:")
    l_c1, l_c2, l_c3, l_c4 = st.columns(4)
    with l_c1:
        if st.button("🌐 Auto-detect", key="btn_lang_auto", use_container_width=True):
            switch_language("Auto-detect (সব ভাষা / सभी भाषाएँ)")
            st.rerun()
    with l_c2:
        if st.button("🇧🇩 বাংলা (Bengali)", key="btn_lang_bn", use_container_width=True):
            switch_language("বাংলা (Bengali)")
            st.rerun()
    with l_c3:
        if st.button("🇮🇳 हिन्दी (Hindi)", key="btn_lang_hi", use_container_width=True):
            switch_language("हिन्दी (Hindi)")
            st.rerun()
    with l_c4:
        if st.button("🇬🇧 English", key="btn_lang_en", use_container_width=True):
            switch_language("English")
            st.rerun()

    st.markdown("---")

    # Scenario Prompt Cards (rendered as styled buttons)
    st.markdown("##### 💡 Quick Legal Scenarios — click to ask instantly:")

    scenario_data = [
        {
            "emoji": "🏠",
            "title": "Deposit Not Returned",
            "desc": "বাড়িওয়ালা ₹35,000 সিকিউরিটি ডিপোজিট ফেরত দিচ্ছে না",
            "lang": "বাংলা",
            "lang_class": "lang-bn",
            "prompt": "বাড়িওয়ালা কোনো রসিদ বা কারণ ছাড়া আমার ₹৩৫,০০০ সিকিউরিটি ডিপোজিট ফেরত দিতে অস্বীকার করছে। বাড়ি ছেড়ে দিয়েছি, চাবি দিয়ে দিয়েছি। আমার আইনি অধিকার কী এবং কী পদক্ষেপ নেওয়া উচিত?"
        },
        {
            "emoji": "🛍️",
            "title": "Defective Product Refund",
            "desc": "ऑनलाइन खरीदा ₹18,000 का फोन खराब, रिफंड नहीं मिला",
            "lang": "हिन्दी",
            "lang_class": "lang-hi",
            "prompt": "ऑनलाइन खरीदा ₹18,000 का फोन खराब निकला और सेलर रिफंड देने से मना कर रहा है। मैं NCH 1915 पर शिकायत कैसे करूँ और e-Daakhil पर कैसे केस फाइल करूँ?"
        },
        {
            "emoji": "⚡",
            "title": "Illegal Power/Water Cut",
            "desc": "Landlord disconnected electricity and water illegally",
            "lang": "English",
            "lang_class": "lang-en",
            "prompt": "My landlord illegally disconnected my electricity and water supply after a minor argument. Can I file a police complaint or approach Rent Authority? What are my immediate legal remedies?"
        },
        {
            "emoji": "🍽️",
            "title": "Overcharging Above MRP",
            "desc": "Restaurant MRP se jyada charge kar raha hai",
            "lang": "Hinglish",
            "lang_class": "lang-mix",
            "prompt": "Restaurant and airport stall MRP se jyada charge kar rahe hain packed items par. Kya ye Consumer Protection Act 2019 ke under unfair trade practice hai? Main kaise complaint kar sakta hun?"
        }
    ]

    cols = st.columns(4)
    for idx, s in enumerate(scenario_data):
        with cols[idx]:
            if st.button(f"{s['emoji']} {s['title']}", key=f"sq_{idx}", use_container_width=True, help=s['desc']):
                st.session_state.pending_prompt = s['prompt']

    st.markdown("---")

    # Chat history
    for message in st.session_state.messages:
        avatar = "⚖️" if message["role"] == "assistant" else "👤"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # User input
    user_prompt = st.chat_input("Ask a legal question in Bengali, Hindi, English, or Hinglish...")
    if "pending_prompt" in st.session_state and st.session_state.pending_prompt:
        user_prompt = st.session_state.pending_prompt
        st.session_state.pending_prompt = None

    if user_prompt:
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_prompt)

        with st.chat_message("assistant", avatar="⚖️"):
            lang_code = st.session_state.get("selected_lang_code")
            if lang_code == "bn":
                prompt_to_send = f"[CRITICAL INSTRUCTION: YOU MUST RESPOND STRICTLY AND ENTIRELY IN BENGALI (বাংলা). DO NOT USE ENGLISH.]\n\n{user_prompt}"
            elif lang_code == "hi":
                prompt_to_send = f"[CRITICAL INSTRUCTION: YOU MUST RESPOND STRICTLY AND ENTIRELY IN HINDI (हिन्दी). DO NOT USE ENGLISH.]\n\n{user_prompt}"
            elif lang_code == "en":
                prompt_to_send = f"[CRITICAL INSTRUCTION: YOU MUST RESPOND STRICTLY IN ENGLISH.]\n\n{user_prompt}"
            else:
                prompt_to_send = user_prompt

            def stream_gen():
                try:
                    stream = st.session_state.chat_session.send_message_stream(prompt_to_send)
                    for chunk in stream:
                        if chunk.text:
                            yield chunk.text
                except Exception as e:
                    # Automatic fallback to bot.ask which tries gemini-3.6 -> gemini-2.5 -> gemini-3.1
                    fallback_reply = bot.ask(prompt_to_send, preferred_language=lang_code)
                    yield fallback_reply

            full_response = st.write_stream(stream_gen())
            st.session_state.messages.append({"role": "assistant", "content": full_response})

            # Feedback row
            fc1, fc2, fc3 = st.columns([1, 1, 6])
            with fc1:
                if st.button("👍 Helpful", key=f"fb_y_{len(st.session_state.messages)}"):
                    st.toast("Thank you! Glad it helped.", icon="✨")
            with fc2:
                if st.button("👎 More detail", key=f"fb_n_{len(st.session_state.messages)}"):
                    st.toast("Got it — try asking a follow-up!", icon="💡")

    # Disclaimer
    st.markdown("""
    <div class="disclaimer-modern">
        <span class="disclaimer-modern-icon">⚠️</span>
        <span><strong>Legal Disclaimer:</strong> AdhikarSathi provides general legal awareness under Indian law. It does not replace formal legal advice from an enrolled advocate. For representation, contact NALSA at <strong>15100</strong>.</span>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
# TAB 2: LEGAL GUIDE
# ══════════════════════════════════════════════
with tab_guide:
    st.markdown("### 📚 Citizen Legal Rights Cheat Sheet")

    with st.expander("🏠 **Tenant Rights** (किरायेदार अधिकार / ভাড়াটিয়ার অধিকার)", expanded=True):
        st.markdown("""
| Right | Details |
|---|---|
| **Security Deposit** | Capped at 1–2 months rent. Landlord must return with itemized deductions. Normal wear ≠ damage. |
| **Eviction Protection** | Cannot forcibly lock out, throw belongings, or cut utilities. Minimum 30-day written notice required. |
| **Privacy** | Landlord must give 24-hour prior notice before entering premises. |
| **Rent Receipts** | Tenant is legally entitled to written rent receipts for every payment. |
| **Structural Repairs** | Major/structural repairs are landlord's duty; minor upkeep is tenant's. |
        """)

    with st.expander("🛍️ **Consumer Protection Act, 2019** (উপভোক্তা সুরক্ষা / उपभोक्ता संरक्षण)"):
        st.markdown("""
| Right | Details |
|---|---|
| **Refund & Replacement** | Refusing refund for defective goods = Unfair Trade Practice |
| **NCH Helpline** | Call **1915** (toll-free) or SMS **8800001915** |
| **e-Daakhil** | File complaint online at [edaakhil.nic.in](https://edaakhil.nic.in) — no lawyer needed |
| **Jurisdiction** | District Commission: up to ₹50L · State: ₹50L–₹2Cr · National: above ₹2Cr |
| **MRP Protection** | Charging above MRP on any packaged product is illegal and punishable |
        """)

    with st.expander("⚖️ **Free Legal Aid (NALSA)** (বিনামূল্যে আইনি সহায়তা / मुफ्त कानूनी सहायता)"):
        st.markdown("""
| Eligibility | Details |
|---|---|
| **Who Qualifies** | Women, children, SC/ST, persons with disabilities, low-income citizens |
| **How to Access** | Call **15100** or visit District Legal Services Authority (DLSA) |
| **Legal Basis** | Article 39A of Indian Constitution + Legal Services Authorities Act, 1987 |
| **What You Get** | Free advocate representation, court fee waiver, legal counseling |
        """)

    with st.expander("🚔 **Police & Emergency Rights**"):
        st.markdown("""
| Right | Details |
|---|---|
| **Zero FIR** | Register FIR in ANY police station regardless of jurisdiction |
| **Grounds of Arrest** | Police must inform you why you are being arrested |
| **Inform Family** | You have the right to inform a family member or friend |
| **Free Legal Aid** | Right to free advocate during detention (NALSA 15100) |
| **Cyber Fraud** | Report immediately on **1930** or [cybercrime.gov.in](https://cybercrime.gov.in) |
| **Emergency** | All-in-one: **112** (Police + Fire + Ambulance) |
        """)
