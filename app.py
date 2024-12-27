import streamlit as st
from pymongo import MongoClient

# Streamlit App Title
st.title("MongoDB Streamlit App")

# Display Hello World message
st.write("Hello World")

# MongoDB Connection
try:
    # MongoDB URI
    client = MongoClient("mongodb+srv://ingolealessa:mREYsWLYMzGgmyV8@streamlit-app-db.issod.mongodb.net/?retryWrites=true&w=majority&appName=streamlit-app-db")
    
    db = client["streamlit-app-db"]
    collection = db["users"]

    # Test the connection
    st.success("Connected to MongoDB!")

except Exception as e:
    st.error(f"Error: {e}")
