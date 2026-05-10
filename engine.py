import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Add servings=None as an optional parameter
def find_recipe(available_ingredients, servings=None):
    ingredients_string = ', '.join(available_ingredients)
    
    # Dynamically adjust the prompt based on whether they provided a serving size
    if servings:
        servings_prompt = f"Please scale this recipe specifically to serve {servings} people."
    else:
        servings_prompt = "Assume a standard serving size (about 2 to 4 people)."
    
    prompt = f"""
    You are an expert chef. I have the following ingredients: {ingredients_string}. 
    {servings_prompt}
    
    Suggest a recipe using these. Format with:
    - Recipe Name
    - Description
    - Ingredients List (with exact quantities needed for the serving size)
    - Instructions
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    
    return response.text