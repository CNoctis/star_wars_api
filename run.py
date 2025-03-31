from app import app
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    app.run(
        host=os.getenv("FLASK_RUN_HOST", "0.0.0.0"), 
        port=int(os.getenv("FLASK_RUN_PORT", 5000)), 
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true"
    )
