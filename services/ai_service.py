import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv
import json

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-2.5-flash')


def analyze_image(image_path):
    img = Image.open(image_path)

    prompt = """
    Analyze the food items in this image and return ONLY valid JSON.

    Format:

    {
      "ingredients": [
        {"name": "item1", "calories": "XX kcal"}
      ],
      "recipes": [
        {
          "title": "Recipe name",
          "description": "Short description of the dish",
          "steps": ["Step 1...", "Step 2..."]
        }
      ],
      "total_calories": "XXXX kcal"
    }

    Rules:
    - Generate 2 to 3 different recipes using the ingredients
    - Each recipe must have a title and description
    - Each step should be clear and short
    - Each ingredient must have calories
    - Also calculate total calories
    - No explanations
    - Only JSON
    """

    response = model.generate_content([prompt, img])

    try:
        clean_text = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_text)
    except:
        data = {
            "ingredients": [],
            "recipes": [
                {
                    "title": "Error",
                    "description": "",
                    "steps": ["Error parsing AI response"]
                }
            ],
            "total_calories": "N/A"
        }

    return data