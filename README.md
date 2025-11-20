🌍 Agentic AI Trip Planner

A smart, AI-powered agentic travel planning system that generates complete trip itineraries using LLM-based reasoning, tool-calling, real-time APIs, and multi-step planning.
Built using FastAPI, Streamlit, and uv for fast Python environment management.

✨ Project Overview

This Trip Planner takes user inputs such as destination, budget, travel days, preferences, and special requirements — and uses an agent-style workflow to generate:

Daily itineraries

Hotel suggestions

Places to visit

Food recommendations

Budget breakdown

Travel tips

It combines LLM reasoning, external API calls, and smart planning logic to build highly personalized travel plans.

🧠 Key Features

🗺️ AI-generated day-wise itinerary

🧮 Budget estimation and cost planning

🍽️ Food + local experience suggestions

🏨 Stay recommendations

🚖 Commute suggestions (local transport, optimal routes)

⚡ Built using agents / tool-calling logic

🌐 FastAPI backend

🖥️ Streamlit frontend UI

🚀 Works with any LLM provider (OpenAI, Groq, etc.)

🛠️ Tech Stack

Languages: Python 3.10
Frameworks: FastAPI, Streamlit
Tools: uv (package + environment manager), Uvicorn
AI Models: OpenAI GPT
Other: REST APIs for city / places data/ weather/ currency etc

⚙️ Setup & Installation

1️⃣ clone project and create project using uv
git clone https://github.com/abhinav7876/Agentic-Trip-Planner.git
pip install uv
uv init AI_Travel_Planner

2️⃣ Check installed packages
uv pip list
uv python list

3️⃣ Create virtual environment
uv venv env --python cpython-3.10.18-windows-x86_64-none

4️⃣ Activate the virtual environment (Windows)
env\Scripts\activate.bat

🚀 Running the Project
1️⃣ Start FastAPI backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000

2️⃣ Start the Streamlit UI
streamlit run streamlit_app.py


After this, the UI opens in your browser and interacts with your FastAPI server.

![alt text](<Screenshot 2025-11-12 042320.png>) ![alt text](<Screenshot 2025-11-12 042542.png>)