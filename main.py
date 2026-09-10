"""
main.py
Entry point for AdhikarSathi - Local Language Legal Rights Assistant.
Supports both interactive Terminal CLI mode and Streamlit Web dashboard launch.
"""

import sys
import subprocess
from legal_engine import LegalRightsBot

def launch_web():
    """Launches the Streamlit Web Application."""
    print("\n🚀 Launching AdhikarSathi Streamlit Web Dashboard...")
    cmd = [sys.executable, "-m", "streamlit", "run", "app.py"]
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n👋 Web server stopped.")

def run_cli():
    """Runs an interactive Terminal conversation."""
    print("=" * 65)
    print("⚖️  AdhikarSathi (नागरिक अधिकार ও আইনি সহায়িকা)")
    print("   Local Language Legal Rights Assistant (Bengali / Hindi / English)")
    print("=" * 65)
    print("\nSelect your preferred language / ভাষা নির্বাচন করুন / भाषा चुनें:")
    print("1. Auto-detect (মেশানো / जैसा पूछेंगे वैसा)")
    print("2. বাংলা (Bengali)")
    print("3. हिन्दी (Hindi)")
    print("4. English")
    print("5. 🌐 Launch Streamlit Web UI instead")
    
    choice = input("\nEnter choice [1-5, default=1]: ").strip()
    
    if choice == "5":
        launch_web()
        return

    lang_map = {
        "1": None,
        "2": "bn",
        "3": "hi",
        "4": "en"
    }
    preferred_lang = lang_map.get(choice, None)

    try:
        bot = LegalRightsBot()
    except Exception as e:
        print(f"\n❌ Error initializing Legal Rights Bot: {e}")
        print("Please verify that GEMINI_API_KEY is configured in your .env file.")
        return

    chat = bot.create_chat(preferred_language=preferred_lang)

    print("\n" + "-" * 65)
    print("Ask any question about Tenant Rights, Consumer Complaints, or basic law.")
    print("Example queries:")
    print(" - 'বাড়িওয়ালা সিকিউরিটি ডিপোজিট ফেরত দিতে অস্বীকার করছে, কী করব?'")
    print(" - 'ऑनलाइन मंगाया सामान टूटा निकला, रिफंड कैसे लें?'")
    print(" - 'How do I file a consumer complaint on e-Daakhil without a lawyer?'")
    print("Type 'exit' or 'quit' to end session.")
    print("-" * 65 + "\n")

    while True:
        try:
            query = input("\n👤 You: ").strip()
            if not query:
                continue
            if query.lower() in ["exit", "quit", "q"]:
                print("\n🙏 Thank you for using AdhikarSathi. Take care!")
                break
            
            print("\n⚖️ AdhikarSathi is analyzing Indian statutes...")
            response = chat.send_message(query)
            print("\n" + response.text + "\n")
            print("-" * 65)
        except KeyboardInterrupt:
            print("\n\nSession terminated. Goodbye!")
            break
        except Exception as e:
            print(f"\n⚠️ Error: {e}")

def main():
    if "--web" in sys.argv:
        launch_web()
    elif "--cli" in sys.argv:
        run_cli()
    else:
        # If run directly without flags, provide easy access
        if len(sys.argv) > 1 and sys.argv[1] not in ["--help", "-h"]:
            run_cli()
        else:
            print("=" * 65)
            print("⚖️  AdhikarSathi - Local Language Legal Rights Bot")
            print("=" * 65)
            print("Choose how you would like to run:")
            print("  1) Web UI (Streamlit - Recommended)")
            print("  2) Terminal CLI")
            user_in = input("Enter choice [1 or 2, default=1]: ").strip()
            if user_in == "2":
                run_cli()
            else:
                launch_web()

if __name__ == "__main__":
    main()
