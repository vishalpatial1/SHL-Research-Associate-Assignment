"""
Setup script to configure Gemini API key for Jay Tiwari's submission
"""

import os

# API Key for Jay Tiwari's submission
GEMINI_API_KEY = "AIzaSyCJEMsVZYajgZslvgCbLOPKXz00RZ-jebU"

def setup_env_file():
    """Create .env file with API key"""
    env_content = f"""# Google Gemini API Key
# Submission by: Jay Tiwari
# Position: AI Reach Intern
# Company: SHL Company
GEMINI_API_KEY={GEMINI_API_KEY}

# Server Port (Optional - defaults to 8000)
PORT=8000
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("[OK] Created .env file with Gemini API key")
    print(f"[OK] API Key configured: {GEMINI_API_KEY[:20]}...")

def test_api_key():
    """Test if the API key works"""
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        
        # Try different model names
        models_to_try = ['gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-pro']
        for model_name in models_to_try:
            try:
                test_model = genai.GenerativeModel(model_name)
                response = test_model.generate_content("Say 'API key is working' if you can read this.")
                print(f"\n[OK] API Key test successful with model: {model_name}!")
                print(f"Response: {response.text[:100]}")
                return True
            except Exception as e:
                continue
        raise Exception("None of the models worked")
    except Exception as e:
        print(f"\n[ERROR] API Key test failed: {e}")
        return False

if __name__ == '__main__':
    print("="*60)
    print("Setting up API Key for Jay Tiwari's Submission")
    print("Position: AI Reach Intern")
    print("Company: SHL Company")
    print("="*60)
    
    setup_env_file()
    
    print("\nTesting API key...")
    if test_api_key():
        print("\n" + "="*60)
        print("[SUCCESS] API key is configured and working!")
        print("="*60)
        print("\nNext steps:")
        print("1. Run: python create_sample_data.py (if not done)")
        print("2. Run: python run_server.py (to start API)")
        print("3. Test: python test_api.py")
    else:
        print("\n[WARNING] API key test failed. Please verify the key.")

