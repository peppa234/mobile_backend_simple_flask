# Flask Backend for Mobile App

This is a simple Flask backend API for serving news data to a Flutter mobile application.

## Endpoints

- `GET /` - Welcome message
- `GET /news.all.get` - Get all news articles
- `GET /news.categories.get` - Get news categories

## Local Development

1. Create virtual environment:
```bash
python -m venv venv
```

2. Activate virtual environment:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
python backend.py
```

The server will run on `http://localhost:8080`

## Deployment on Render

This app is configured to deploy on Render. The app automatically uses the PORT environment variable provided by Render.

