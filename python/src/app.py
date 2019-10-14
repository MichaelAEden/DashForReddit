import os

from flask import Flask, send_from_directory

from route.subreddit import subreddit_blueprint

app = Flask(__name__, static_folder='../../react/build')

# Register API routes
app.register_blueprint(subreddit_blueprint, url_prefix="/api/subreddit")


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run()
