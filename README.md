#  AI Kitchen Assistant

##  Author  
Enis Beysim  
Plovdiv University – Software Technologies and Design  

---

##  Overview
AI Kitchen Assistant is a web-based application that uses artificial intelligence to analyze food images and generate cooking recipes automatically.

The system uses a AI model (Google Gemini API) to:
- Detect ingredients from an uploaded image  
- Estimate calories for each ingredient  
- Generate multiple recipe suggestions  
- Provide step-by-step cooking instructions  

---

##  Features

-  Image upload and processing  
-  Ingredient detection with calorie estimation  
-  Generation of 2–3 different recipes  
-  Total calorie calculation    
-  Clean and responsive UI  

---

##  Project Structure

| Directory / File        | Purpose |
|------------------------|--------|
| `app.py`               | Main Flask application (routing & logic) |
| `services/ai_service.py` | AI integration and prompt handling |
| `templates/`           | HTML templates (UI) |
| `static/`              | CSS and uploaded images |
| `static/uploads/`      | Saved user-uploaded images |
| `.env`                 | API key configuration |
| `requirements.txt`     | Python dependencies |

---

##  Technologies Used

### Backend
- Python  
- Flask  

### AI Integration
- Google Gemini API

### Frontend
- HTML5  
- CSS3  
- Bootstrap  
- Font Awesome  

---

##  How It Works

1. User uploads an image  
2. Image is sent to the AI model  
3. AI extracts:
   - Ingredients  
   - Calories  
   - Recipes  
4. AI returns structured JSON  
5. Data is displayed in the UI  

---

##  Prompt Engineering

The application uses structured prompts to ensure:
- JSON-only responses  
- Multiple recipe generation  
- Step-by-step instructions  
- Calorie estimation

---

##  Requirements
- Google Gemini API Key
- Python 3.10+
  
### Libraries
- flask
- google-generativeai
- pillow
- python-dotenv

## Start Instructions

Follow these steps to run the project locally:

### 1) Clone the repository
```bash
git clone https://github.com/iEosiX/AI-Kitchen-Assistant.git
cd AI-Kitchen-Assistant
```
### 2) Create a virtual environment
```bash
python -m venv .venv
```
### 3) Activate the virtual environment
```bash
Windows: .venv\Scripts\activate

Mac/Linux: source .venv/bin/activate
```
### 4) Install dependencies
```bash
pip install -r requirements.txt
```
### 5) Create a .env file in the root directory and add your API key:
```bash
GOOGLE_API_KEY=your_api_key_here
```
### 6) Run the application
```bash
python app.py
```
### 7) Open in browser
```bash
Go to: http://127.0.0.1:5000/
```
---

## Testing

### Functional Tests
- Upload food image → ingredients and recipes are generated

### Example Inputs
- Food images (pizza, salad, fruits, inside of a fridge)

---
