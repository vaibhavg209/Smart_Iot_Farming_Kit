import sys
import os

# Add the parent directory to the Python path so we can import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from app import app
    
    # For Vercel serverless deployment
    # The app instance is already configured and ready to use
    
except ImportError as e:
    print(f"Error importing app: {e}")
    raise
except Exception as e:
    print(f"Error initializing app: {e}")
    raise

# Test endpoint to verify deployment
@app.route('/health')
def health():
    """Health check endpoint"""
    return {
        'status': 'healthy',
        'message': 'Flask app is running on Vercel'
    }, 200

# Export the Flask app for Vercel
# Vercel automatically wraps this with serverless function handler
