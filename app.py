import streamlit as st
import os
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd


# Load environment variables
load_dotenv()


# Configure GenAI Key
api_key = os.getenv("API_KEY")
if api_key:
    # Using the flash model to avoid quota errors and ensure speed
    genai.configure(api_key=api_key)
else:
    st.error("API_KEY not found. Please check your .env file.")


# Function to Load Google Gemini Model
def get_gemini_response(question, prompt):
    # Use flash model for better rate limits
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([prompt[0], question])
    return response.text


# Function to retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    column_names = [description[0] for description in cur.description]
    conn.commit()
    conn.close()
    return rows, column_names


# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENTS and has the following columns - NAME, CLASS, MARKS, COMPANY.
    \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this: SELECT COUNT(*) FROM STUDENTS;
    \nExample 2 - Tell me all the students studying in MCom class?, 
    the SQL command will be something like this: SELECT * FROM STUDENTS WHERE CLASS="MCom"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]


# --- UI Functions ---


def page_home():
    st.markdown("""
    <style>
    .main-title {font-size: 3rem; color: #4CAF50; text-align: center;}
    .sub-title {font-size: 1.5rem; color: #4CAF50; text-align: center; margin-bottom: 2rem;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='main-title' style='color: #4CAF50;'>Welcome to IntelliSQL!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='sub-title' style='color: #4CAF50;'>Revolutionizing Database Querying with Advanced LLM Capabilities</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # Displaying logo.png (The blue gear/network icon)
        if os.path.exists("./logo.png"):
            st.image("./logo.png", width=700)
        else:
            st.write("📂 (Image 'logo.png' not found)")

    with col2:
        st.markdown("<h3 style='color: #4CAF50;'>Wide Range of Offerings</h3>", unsafe_allow_html=True)
        st.markdown("""
        <ul style="font-size: 1.1rem; list-style-type: none;">
            <li>💡 Intelligent Query Assistance</li>
            <li>🔍 Data Exploration and Insights</li>
            <li>📊 Efficient Data Retrieval</li>
            <li>🚀 Performance Optimization</li>
            <li>🛠️ Syntax Suggestions</li>
            <li>📈 Trend Analysis</li>
        </ul>
        """, unsafe_allow_html=True)



def page_about():
    st.markdown("<h1 style='color: #4CAF50;'>About IntelliSQL</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background-color: transparent; padding: 0px; border-radius: 10px;'>
        <p style='color: black; font-size: 1.2rem;'>
        IntelliSQL is an innovative project aimed at revolutionizing database querying using advanced Language Model 
        capabilities. Powered by cutting-edge LLM (Large Language Model) architecture, this system offers users an 
        intelligent platform for interacting with SQL databases effortlessly and intuitively.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Displaying database.png (The database cylinder)
    st.write("") # Spacer
    if os.path.exists("./database.png"):
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.image("database.png", use_container_width=True)
    else:
        st.write("💾 (Image 'database.png' not found)")



def page_intelligent_query_assistance():
    st.markdown("<h1 style='color: #4CAF50;'>Intelligent Query Assistance</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color: black;'>
    IntelliSQL enhances the querying process by providing intelligent assistance to users. Whether they are novice or 
    experienced SQL users, IntelliSQL guides them through crafting complex queries with ease. By understanding natural 
    language queries, IntelliSQL suggests relevant SQL statements, offers syntax suggestions, and assists in optimizing 
    query performance, thereby streamlining the database interaction experience.
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([5,4])

    with col1:
        st.markdown("### Enter Your Query:")
        question = st.text_input("Input:", key="input", label_visibility="collapsed")
        st.write("")
        submit = st.button("Get Answer")

        if submit:
            if question:
                try:
                    response = get_gemini_response(question, prompt)
                    st.success(f"Generated SQL Query: {response}")

                    data, columns = read_sql_query(response, "data.db")
                    st.subheader("The Result is:")

                    # Convert to pandas DataFrame for table display
                    df = pd.DataFrame(data, columns=columns)
                    st.dataframe(df, use_container_width=True)

                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("Please enter a question.")

    with col2:
        # Displaying output.png (The magnifying glass/search icon)
        if os.path.exists("./output.png"):
            st.image("output.png", width=600)
        else:
            st.write("🤖 (Image 'output.png' not found)")



# --- Main App Structure ---


def main():
    st.set_page_config(page_title="IntelliSQL", page_icon="🔮", layout="wide")

    st.sidebar.markdown("""
    <style>
    .sidebar-text {color: black; font-size: 1.2rem;}
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "About", "Intelligent Query Assistance"])

    if selection == "Home":
        page_home()
    elif selection == "About":
        page_about()
    elif selection == "Intelligent Query Assistance":
        page_intelligent_query_assistance()



if __name__ == "__main__":
    main()
    