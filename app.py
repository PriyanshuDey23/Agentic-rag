import streamlit as st
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2
from phi.embedder.google import GeminiEmbedder
import os
from typing import Optional, List
from phi.model.google import Gemini
from phi.vectordb.pgvector import PgVector, SearchType
from dotenv import load_dotenv
from phi.agent import Agent

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY is None:
    st.error("Google API Key is missing. Please check your .env file.")
    st.stop()  # Stop execution if the API key is missing

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url, search_type=SearchType.hybrid, embedder=GeminiEmbedder(api_key=GOOGLE_API_KEY)),
)

# Load the knowledge base: Comment out after first run
knowledge_base.load(recreate=True, upsert=True)

# Using @st.experimental_memo instead of @st.cache_resource for caching agent initialization

def initialize_agents():
    return Agent(
        model=Gemini(id="gemini-2.0-flash-exp"),
        knowledge=knowledge_base,
        read_chat_history=True,
        show_tool_calls=True,
        markdown=True,
    )

# Initialize agent
multimodal_Agent = initialize_agents()

# Launch CLI app for the agent
multimodal_Agent.cli_app(markdown=True)
