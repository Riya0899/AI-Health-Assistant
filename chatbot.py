import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_ai_response(user_input):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        return response.text

    except Exception as e:
        return f"⚠️ Gemini Error: {str(e)}"

# from google import genai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# for m in client.models.list():
#     print(m.name)