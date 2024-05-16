from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database configuration
host = os.getenv("DB_HOST", "localhost")
database = os.getenv("DB_NAME", "TrabajoFinal2")
user = os.getenv("DB_USER", "Diplomado")
password = os.getenv("DB_PASSWORD", "diplomado")
port = os.getenv("DB_PORT", 5432)
