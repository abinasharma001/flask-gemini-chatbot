import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key loaded: {api_key[:10]}...{api_key[-5:] if api_key else 'NONE'}\n")

genai.configure(api_key=api_key)

print("🔍 Checking available models for your API key...\n")

try:
    models = genai.list_models()
    
    available_generate_models = []
    
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            available_generate_models.append(m.name)
            print(f"✅ {m.name}")
            print(f"   Display Name: {m.display_name}")
            print(f"   Description: {m.description[:100]}...")
            print(f"   Methods: {m.supported_generation_methods}\n")
    
    if not available_generate_models:
        print("❌ No models with generateContent support found!")
        print("\n📋 All available models:")
        for m in models:
            print(f"   - {m.name} (Methods: {m.supported_generation_methods})")
    else:
        print(f"\n✅ Total models available: {len(available_generate_models)}")
        print(f"\n💡 Use this in your code:")
        print(f"   model = genai.GenerativeModel('{available_generate_models[0]}')")
        
except Exception as e:
    print(f"❌ Error accessing API: {e}")
    print("\n🔧 Possible issues:")
    print("   1. API key is invalid or expired")
    print("   2. Gemini API is not enabled for your account")
    print("   3. You need to create a new API key")