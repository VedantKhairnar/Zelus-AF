web: gunicorn app:app --timeout 120
worker: python main.py
heroku ps:scale worker=1
