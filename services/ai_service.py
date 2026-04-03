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
          "time": "XX min",
          "difficulty": "Easy/Medium/Hard",
          "type": "Healthy/Fast/Vegan/etc",
          "steps": ["Step 1...", "Step 2..."]
        }
      ],
      "recommended_recipe": 0,
      "total_calories": "XXXX kcal"
    }

    Rules:
    - Generate 2 to 3 different recipes
    - Include cooking time and difficulty
    - Classify recipe type (Healthy, Fast, etc.)
    - Mark ONE recommended recipe (index 0,1,2...)
    - Keep steps short and clear
    - Only JSON, no explanations
    """

    response = model.generate_content([prompt, img])

    try:
        clean_text = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_text)

        if not data.get("ingredients"):
            data["error"] = "⚠️ No food detected in the image. Try another one."
    except json.JSONDecodeError:
        data = {
          "ingredients": [],
          "recipes": [],
          "recommended_recipe": 0,
          "total_calories": "N/A",
          "error": "⚠️ Could not analyze image. Try another one."
        }

    return data
