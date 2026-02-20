# IntelliSQL 🔮


https://github.com/user-attachments/assets/c1235590-e869-47c3-a993-937eab5ccdd8


<div align="center">
  <h3>Watch the Demo</h3>
  <video src="./Demo/demo_video.mp4" width="100%" controls></video>
  <p>
    <em>(If the video doesn't play, <a href="./Demo/demo_video.mp4">click here to watch it</a>)</em>
  </p>
</div>

---

## 📖 About Project

**IntelliSQL** is an innovative AI-powered application designed to revolutionize how users interact with databases. By leveraging the advanced capabilities of **Google Gemini**, this tool allows users to query SQL databases using natural language (plain English) instead of writing complex SQL code manually.

Whether you are a novice user or an experienced developer, IntelliSQL bridges the gap between human language and database logic.

**Key Features:**
*   **Natural Language Processing:** Converts English questions (e.g., *"How many students are in the Data Science class?"*) into valid SQL queries.
*   **Intelligent Execution:** Automatically executes the generated SQL query against the database and retrieves the results.
*   **Data Visualization:** Presents the retrieved data in a clean, tabular format using Pandas.

---

## 🛠️ Requirements

To run this project locally, you need the following Python libraries installed:

*   `streamlit` (For the web interface)
*   `google-generativeai` (For accessing Gemini models)
*   `python-dotenv` (For managing API keys securely)
*   `pandas` (For data handling and display)

---

## 📸 Sample Screenshots

### 1. Home Page
![Home Page](./Demo/home_page.png)

### 2. About Page
![About Page](./Demo/about_page.png)

### 3. Output Page
![Output Page](./Demo/output_page.png)

---

## 🚀 How to Run It

Follow these simple steps to set up and run the project on your local machine:

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Configure Environment Variables
Create a `.env` file in the root directory and add your Google Gemini API key:
```env
API_KEY="your_google_api_key_here"
```

### Step 3: Initialize the Database
Run the `sql.py` script to create the `data.db` database and populate it with sample student records:
```bash
python sql.py
```

### Step 4: Run the Application
Launch the Streamlit app:
```bash
streamlit run app.py
```
