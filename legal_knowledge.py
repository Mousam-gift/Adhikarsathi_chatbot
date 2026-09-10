"""
legal_knowledge.py
Curated Indian Legal Reference Data & Helplines.
Specialized for Tenant Rights, Consumer Complaints, and Essential Citizen Rights.
"""

# Official Helplines & Portals
LEGAL_HELPLINES = {
    "consumer": {
        "title": "National Consumer Helpline (NCH)",
        "toll_free": "1915",
        "alt_number": "1800-11-4000",
        "sms": "8800001915",
        "website": "https://consumerhelpline.gov.in",
        "edaakhil": "https://edaakhil.nic.in",
        "desc_en": "Call 1915 or file on e-Daakhil for unfair trade, defective goods, and refund refusals.",
        "desc_hi": "दोषपूर्ण सामान, रिफंड न मिलने या धोखाधड़ी पर 1915 पर कॉल करें या e-Daakhil पर शिकायत दर्ज करें।",
        "desc_bn": "ত্রুটিপূর্ণ পণ্য, রিফান্ড না পাওয়ার বা প্রতারণার বিরুদ্ধে 1915 নম্বরে কল করুন বা e-Daakhil-এ অভিযোগ জানান।"
    },
    "legal_aid": {
        "title": "National Legal Services Authority (NALSA)",
        "toll_free": "15100",
        "website": "https://nalsa.gov.in",
        "desc_en": "Free legal representation and advice for marginalized citizens, women, children, and low-income individuals.",
        "desc_hi": "कम आय वाले नागरिकों, महिलाओं और जरूरतमंदों के लिए मुफ्त कानूनी सलाह व वकील (15100)।",
        "desc_bn": "স্বল্প আয়ের মানুষ, মহিলা ও দুঃস্থ নাগরিকদের জন্য সম্পূর্ণ বিনামূল্যে সরকারি আইনি সহায়তা (15100)।"
    },
    "cyber_crime": {
        "title": "National Cyber Crime Reporting Helpline",
        "toll_free": "1930",
        "website": "https://cybercrime.gov.in",
        "desc_en": "Report financial frauds, online scams, and unauthorized transactions immediately within golden hour.",
        "desc_hi": "ऑनलाइन वित्तीय धोखाधड़ी या साइबर अपराध की तत्काल सूचना 1930 पर दें।",
        "desc_bn": "অনলাইন আর্থিক প্রতারণা বা সাইবার ক্রাইমের অভিযোগ সঙ্গে সঙ্গে 1930 নম্বরে জানান।"
    },
    "emergency": {
        "title": "National Emergency Number",
        "toll_free": "112",
        "desc_en": "All-in-one emergency helpline for Police, Fire, and Ambulance.",
        "desc_hi": "पुलिस, आग या मेडिकल आपातकाल के लिए एकीकृत नंबर 112।",
        "desc_bn": "পুলিশ, দমকল ও চিকিৎসার জরুরি প্রয়োজনে অল-ইন-ওয়ান হেল্পলাইন 112।"
    }
}

# Core Law Summaries for System Grounding
CORE_LEGAL_GROUNDING = """
INDIAN LAW ESSENTIALS FOR CITIZENS:

1. TENANT RIGHTS (किरायेदार अधिकार / ভাড়াটিয়ার অধিকার):
   - Security Deposit: Landlords must return the security deposit after adjusting genuine dues/damages agreed in writing. Unreasonable forfeiture without itemized bills is unlawful. Under Model Tenancy Act principles, security deposit is capped (typically 1-2 months rent for residential).
   - Unlawful Eviction: Landlords CANNOT forcibly throw out a tenant, lock premises, cut off essential supplies (water, electricity), or withhold deposit without due legal process or written notice as per agreement (usually 30 days).
   - Right to Privacy & Entry: Landlord cannot enter rented premises without reasonable prior notice (usually 24 hours).
   - Written Agreement & Rent Receipts: Tenant is legally entitled to written receipts upon paying rent.
   - Repairs: Structural repairs are generally landlord's duty; minor day-to-day upkeep is tenant's.

2. CONSUMER COMPLAINTS (उपभोक्ता संरक्षण अधिनियम 2019 / ক্রেতা সুরক্ষা আইন ২০১৯):
   - Who is a Consumer: Anyone who buys goods or hires services for consideration (excluding resale/commercial). Covers online e-commerce transactions.
   - Key Rights: Right to safety, right to be informed, right to choose, right to be heard, right to seek redressal, right to consumer education.
   - Unfair Trade Practices: Misleading ads, refusing refunds for defective products/services, charging above MRP, unfair contract clauses.
   - Redressal Mechanism:
     * Tier 1: Approach seller/service provider customer care with written complaint.
     * Tier 2: National Consumer Helpline (NCH) via Toll-Free 1915, SMS, or consumerhelpline.gov.in.
     * Tier 3: e-Daakhil portal (edaakhil.nic.in) or filing in Consumer Commission:
       - District Commission: Claims up to ₹50 Lakhs (revised rules).
       - State Commission: Claims ₹50 Lakhs to ₹2 Crores.
       - National Commission (NCDRC): Claims above ₹2 Crores.

3. POLICE & GENERAL CITIZEN RIGHTS:
   - Zero FIR: Can register an FIR in ANY police station regardless of jurisdiction if a cognizable offense occurred.
   - Arrest/Detention safeguards: Right to know grounds of arrest, right to inform a family member/friend, right to free legal aid (NALSA 15100).
   - Right to Information (RTI Act 2005): File online at rtionline.gov.in for public authority accountability.
"""
