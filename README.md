# 🍽️ Restaurant Name Generator

This is a simple Streamlit web app that generates a catchy restaurant name and a suggested menu based on the type of cuisine your input. It uses a locally running LLM (LLaMA 2 via Ollama) and LangChain to generate creative outputs with natural language prompts.

------------

## 🧠 How It Works

1. The user enters a cuisine type (e.g., "Indian").
2. The app uses a predefined prompt to generate a unique restaurant name.
3. Another prompt generates a list of dishes for the named restaurant.
4. Results are displayed in the web interface.

------------

## 🛠️ Installation

1. **Install Ollama** (to run LLaMA 2 model locally):
   Follow instructions at: https://ollama.com

2. Run **ollama run llama2** in command prompt

3. Clone the repository

4. Install Dependencies:
   **pip install -r requirements.txt**
  
5. Run **streamlit run main.py** in terminal
