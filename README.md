
# Streamlit Project Setup Guide

This guide will walk you through setting up and running a Streamlit project from scratch. No technical experience is required. Follow the steps below carefully, and you'll have your app up and running in no time!

---

## Prerequisites

### 1. Install Git
- Download and install Git from [git-scm.com](https://git-scm.com/).
- Follow the installation instructions for your operating system.

### 2. Install Python
- Download and install Python (version 3.8 or later) from [python.org](https://www.python.org/).
- Make sure to check the option to **Add Python to PATH** during installation.

---

## Step 1: Clone the Project Repository

1. Open your terminal (Command Prompt, PowerShell, or a terminal application).
2. Run the following command to clone the project:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
   Replace `https://github.com/your-username/your-repository.git` with the actual GitHub repository URL.

3. Navigate into the project directory:
   ```bash
   cd your-repository
   ```

---

## Step 2: Set Up a Virtual Environment

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

   You will see `(venv)` at the beginning of your terminal prompt if the virtual environment is activated.

---

## Step 3: Install Project Dependencies

1. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Step 4: Add Your `.env` File

1. Create a new file named `.env` in the project directory.
2. Open the `.env` file in a text editor and add the following lines:
   ```plaintext
   SUPABASE_URL=https://your-supabase-url.supabase.co
   SUPABASE_KEY=your-supabase-key
   ```
   - Replace `https://your-supabase-url.supabase.co` with your actual Supabase project URL.
   - Replace `your-supabase-key` with your actual Supabase API key (use the **Service Role Key** for full access).

3. Save the file.

---

## Step 5: Run the Streamlit App

1. Start the Streamlit development server:
   ```bash
   streamlit run app.py
   ```

2. Streamlit will open a new tab in your default web browser. If it doesn't open automatically, you will see a URL in your terminal (e.g., `http://localhost:8501`). Copy and paste it into your browser.

---

## Troubleshooting

### Common Issues
- **Virtual environment activation not working**:
  Ensure you have Python installed correctly and that you're running the appropriate activation command for your operating system.

- **ModuleNotFoundError**:
  Run `pip install -r requirements.txt` to ensure all dependencies are installed.

- **Supabase authentication errors**:
  Double-check the `SUPABASE_URL` and `SUPABASE_KEY` in your `.env` file.

---

## Next Steps
- Explore the app by selecting tables and viewing the data.
- Modify the app as needed for your use case.

---

## Tutorial Challenges

### EASY
1. Format the data and display it in the table in the following ways (may want/need to use pandas here):
   - Make the date values a human-readable and friendly format.
   - Remove special characters from the supplier name so that it is alphanumeric.
   - Clean campaign and placement names so they are consistent (the casing and breaks are different currently).
   - Exclude records with 0 impressions.

### MEDIUM
1. Write the clean data back to the database (i.e., clean alphanumeric names).
2. Group records by QUARTER.

### HARD/ADVANCED
1. Separate the data into dimensions and facts.
2. Write that data to the `placement_facts`, `placement_dimensions`, `campaign_facts`, and `campaign_dimensions` tables which are currently empty (exclude records with 0 impressions).
3. Remember the `created_date` here is NOT the `created_date` from the source data - the `created_date` should be the date that the record was inserted into YOUR database. Use Google/AI to add triggers to the 'created_date' columns so that it automatically updates when a record is inserted.
4. In SQL or Pandas or BOTH, sum the impressions of the placements associated with a single campaign and compare that with the campaign impressions in the campaign database to see if they align.
5. Isolate placements that have ZERO corresponding parent campaigns - start a new table to store these.
6. Generate and save a CSV report of these orphan placements to give to stakeholders for further investigation.

### EXTRA CREDIT
1. Ideally, ID columns should be integers only because the database can interact with integers quicker than text - currently, the IDs are a mix of integers and strings.
2. Find a good way to handle string-based IDs to map them to integers, then define the database table column data types as integers.
3. Right now, we are only inserting/writing a few records to a table but in the real world, we'll be inserting tens of thousands at a time.
4. Use SQLAlchemy to batch write operations.
5. For example, you get all the placements data and you change all the countries' values to random strings and write all new updated data to the `placements_dimensions` table - instead of SQLAlchemy running one line of insert statement per record, read the docs and batch the operations into chunks of data.
6. Refactor your code so that it adheres to 'clean code' and 'clean architecture' principles and patterns (i.e., functions should ideally have 0-2 arguments max, functions should be less than 10 lines long, code should read like English, don't store all your functions in one monolithic file, separate reusable and helper functions into separate files and import them in).

---

## Packages Used
This project uses the following Python packages:

- **Streamlit**: For building the web application interface. [Documentation](https://docs.streamlit.io/)
- **python-dotenv**: For managing environment variables securely. [Documentation](https://pypi.org/project/python-dotenv/)
- **Supabase**: For interacting with the Supabase database. [Documentation](https://supabase.com/docs/reference/python)
- **pandas**: For data manipulation and analysis. [Documentation](https://pandas.pydata.org/docs/)
- **SQLAlchemy**: For efficient database operations. [Documentation](https://docs.sqlalchemy.org/)

---

## Data and Table Structure

This project uses a relational database with the following hierarchy:

1. **Campaigns**:
   - Campaigns are the parent records.
   - Contain high-level details about campaigns such ass name, impressions, and clicks.

2. **Placements**:
   - Placements are child records related to specific campaigns.
   - Contain detailed information about individual ad placements.

### Source Tables
- **Source Data Tables**:
  These tables store the raw data fetched from external sources.

### Processed Tables (ETL Output)
- The data is processed via ETL (Extract, Transform, Load) pipelines and separated into:
  - **Fact Tables**:
    Quantitative data, such as impressions, clicks, and dates, that can be mathematically operated on.
  - **Dimension Tables**:
    Qualitative data, such as descriptions, names, and URLs.

By separating the data into facts and dimensions, we optimize for analytical queries and maintain a clean, structured database.
