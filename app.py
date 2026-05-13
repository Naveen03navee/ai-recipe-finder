import streamlit as st
import requests

st.set_page_config(page_title="AI Recipe Finder", page_icon="🍳", layout="centered")

st.title("🍳 AI Recipe Finder")
st.write("Tell me what's in your fridge, and I'll whip up a recipe!")
st.divider()

# Upgraded to a text_area for more space, and updated placeholder to show quantities
ingredients_input = st.text_area(
    "What ingredients do you have? (You can include quantities!)", 
    placeholder="e.g., 500g chicken, 2 cups rice, garlic, heavy cream"
)

# Added an optional number input for servings
servings_input = st.number_input(
    "For how many people? (Optional)", 
    min_value=1, 
    max_value=20, 
    value=None, 
    step=1, 
    placeholder="Leave blank for standard (2-4 people)"
)

if st.button("Generate Recipe", type="primary"):
    if not ingredients_input:
        st.warning("Please enter at least one ingredient!")
    else:
        ingredients_list = [i.strip() for i in ingredients_input.split(",") if i.strip()]
        
        # Build the payload dynamically
        payload = {"ingredients": ingredients_list}
        if servings_input:
            payload["servings"] = servings_input
            
        with st.spinner("Chef AI is thinking..."):
            try:
                api_url = "https://ai-recipe-finder-et10.onrender.com"
                response = requests.post(api_url, json=payload)
                
                if response.status_code == 200:
                    recipe_text = response.json().get("recipe", "No recipe found.")
                    st.success("Recipe generated successfully!")
                    st.markdown(recipe_text)
                else:
                    st.error(f"Backend Error {response.status_code}: {response.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error("🚨 Could not connect to the API. Make sure your Docker container is running on port 8000!")