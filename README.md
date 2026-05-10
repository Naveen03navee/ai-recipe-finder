# AI Recipe Finder (Dockerized Microservice)

A full-stack, containerized AI application that generates custom recipes based on available ingredients, powered by Google's Gemini 2.5 Flash model. 

## Architecture & Tech Stack
* **AI Engine:** Google GenAI SDK (Gemini 2.5 Flash)
* **Backend:** FastAPI, Pydantic (Data Validation)
* **Frontend:** Streamlit 
* **DevOps:** Docker, multi-tier microservice architecture

## How to Run Locally

### Prerequisites
* Docker Desktop
* A Google Gemini API Key

### Installation
1. Clone the repository.
2. Create a `.env` file in the root directory and add your API key:
   `GEMINI_API_KEY=your_key_here`
3. Build and run the Docker container:
   ```bash
   docker build --network=host -t ai-recipe-api .
   docker run -p 8000:8000 --env-file .env ai-recipe-api