from flask import Flask, render_template

# Create Flask app with correct paths for Vercel
app = Flask(__name__, 
           template_folder='../templates',
           static_folder='../static')

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/Identify")
def identify():
    return render_template("identify.html")

# Export app for Vercel
if __name__ == "__main__":
    app.run(debug=True)
