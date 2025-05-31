# Clarity

Clarity is a desktop personal journal application that allows users to maintain entries, analyze them for mood patterns, and share results with specialists. The application supports the diagnostic process for mood disorders such as depression, mania, and others.

This project was developed as part of my bachelor's thesis titled **"A mood disorder diagnosis support system based on text analysis"** at Maria Curie-Skłodowska University.  
Thesis available at: [Placeholder](https://www.linkedin.com/in/nazar-kuziv/)

## Prerequisites

- Python 3.10
- Google account (for email configuration)
- Supabase account (for database hosting)
- Git (for downloading the project)

## Installation and Configuration

1. **Download the Project**
   - Clone the repository from GitHub:
     ```bash
     git clone [repository-url]
     ```

2. **Download and Extract Model Files**
   - Download the model archive from:
     ```
     https://mega.nz/file/ZxkRGTrR#6WB7t7i8FqyN1aKjA6hb7sX2-0_Qzdtr-oB1gAclUXg
     ```
   - Extract the contents of the archive into the `static` directory of the project

3. **Create a Supabase Database**
   - Create a new database in Supabase
   - Using the console, the `db_backup.sql` file (located in the `otherFiles` directory), and the command:
     ```bash
     psql -d "Your session pooler connection string" -f .\db_backup.sql
     ```
     create all necessary tables and populate them with sample data.
   - The **session pooler connection string** can be found under the "Connect" button in your Supabase project. Remember to replace `[YOUR-PASSWORD]` with your database password in the URL.

4. **Generate Gmail App Password**
   - Enable two-factor authentication on your Google account
   - Go to your Google account management page
   - Search for "App passwords"
   - Generate a password for our application

5. **Environment Setup**
   - In the project directory, create a Python 3.10 virtual environment:
     ```bash
     python3.10 -m venv .venv
     ```
   - Activate the virtual environment:
     ```bash
     .venv\Scripts\activate
     ```
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

6. **Configure .env File**
   - Paste the generated password in the `.env` file under the `EMAIL_APP_PASSWORD` variable
   - Paste the email address used to generate the password under the `EMAIL_APP_PASSWORD` variable (remove all spaces from the password)
   - In the `.env` file, paste your Supabase Project URL under the `SUPABASE_URL` variable
   - Paste your API Key (received when creating the Supabase database) under the `SUPABASE_KEY` variable

## Running the Application

After completing all the above steps, run the application with:

```bash
python main.py