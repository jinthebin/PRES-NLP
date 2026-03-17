import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Google Sheets Configuration
GS_CONFIG = {
    "service_account": os.getenv("GS_SERVICE_ACCOUNT_JSON"),
    "spreadsheet_id": os.getenv("GS_SPREADSHEET_ID"),
    "sheet_name": os.getenv("GS_SHEET_NAME")
}