import os
import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Streamlit app
st.title("Supabase Data Viewer")

# Select table to view
table = st.selectbox("Select a table to view", ["source_placements", "source_campaigns"])

if table:
    # Fetch data from Supabase
    data = supabase.table(table).select("*").execute()

    if data.data:  # Access the `data` attribute of the response object
        st.write(f"Displaying data for `{table}` table:")
        st.dataframe(data.data)  # Use the `data` attribute to access the table data
    else:
        st.write(f"No data found for `{table}` table.")
