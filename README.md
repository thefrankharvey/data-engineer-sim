
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

If you encounter any issues, feel free to reach out for help!
