import os
import sys
from app import create_app

# Add this to ensure proper module resolution
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)