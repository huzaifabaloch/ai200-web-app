from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }

            .card {
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                text-align: center;
            }

            h1 {
                color: #333;
            }

            p {
                color: #666;
            }

            .status {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>🚀 Hello Tuna!</h1>
            <p>This is a test FastAPI web page.</p>
            <p class="status">● Server is running</p>
        </div>
    </body>
    </html>
    """