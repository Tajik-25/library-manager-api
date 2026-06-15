from dotenv import load_dotenv
import os
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
DATA_BASE_URL = os.getenv("DATA_BASE_URL")