import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use the PORT environment variable from Cloud Run
    app.run(host="0.0.0.0", port=port)  # Bind to all interfaces