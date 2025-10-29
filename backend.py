from flask import Flask
import json, datetime, os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow requests from your Flutter app

@app.route('/news.all.get')
def get_news_all_articles():
    data = []
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'news_data.json')
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return json.dumps(data)
    except Exception as e:
        return json.dumps({"error": str(e)}), 500

@app.route('/news.categories.get')
def get_news_categories():
    time_now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        'title': 'List of Categories',
        'time': time_now_str,
        'categories': [
            {'id': 1, 'name': 'Sports'},
            {'id': 2, 'name': 'Politics'},
            {'id': 3, 'name': 'Education'}
        ]
    }
    return json.dumps(data)

@app.route('/')
def index():
    return 'Welcome ENSIA Students from Flask!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
