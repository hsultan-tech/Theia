from flask import Flask, render_template, send_from_directory
import os

# Create Flask app with correct paths for Vercel
app = Flask(__name__, 
           template_folder='../templates',
           static_folder='../static',
           static_url_path='/static')

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/Identify")
def identify():
    return render_template("identify.html")

# Explicit static file handler for Vercel
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('../static', filename)

# Export app for Vercel
if __name__ == "__main__":
    app.run(debug=True)
