import streamlit as st
from github_client import GitHubClient
from ai_engine import AIEngine
from prompts import SYSTEM_PROMPT

st.set_page_config(page_title="GitHub AI Bot")
st.title("🚀 GitHub Code Assistant")

repo_name = st.text_input("Enter Repo Name (e.g., owner/repo):")
user_query = st.chat_input("Ask about the code...")

if repo_name and user_query:
    gh = GitHubClient()
    ai = AIEngine()
    
    repo_data = gh.get_repo_details(repo_name)
    context = f"{SYSTEM_PROMPT}\nRepo Info: {repo_data}"
    
    response = ai.get_response(user_query, context)
    st.write(response)
