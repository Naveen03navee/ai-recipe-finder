from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from engine import find_recipe

app = FastAPI(title="AI Recipe Finder API")

# Update the request model to include optional servings
class IngredientRequest(BaseModel):
    ingredients: List[str]
    servings: Optional[int] = None

@app.get("/")
def home():
    return {"message": "Welcome to the AI Recipe Finder API!"}

@app.post("/recommend")
def get_recipe(request: IngredientRequest):
    if not request.ingredients:
        raise HTTPException(status_code=400, detail="Please provide at least one ingredient.")
    
    try:
        # Pass the servings data to the engine
        recipe_text = find_recipe(request.ingredients, request.servings)
        return {"recipe": recipe_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)