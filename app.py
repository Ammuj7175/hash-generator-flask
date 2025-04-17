from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hash_result = ""
    selected_algo = "md5"

    if request.method == "POST":
        text = request.form.get("text", "")
        selected_algo = request.form.get("algorithm", "md5")

        if selected_algo == "md5":
            hash_result = hashlib.md5(text.encode()).hexdigest()
        elif selected_algo == "sha256":
            hash_result = hashlib.sha256(text.encode()).hexdigest()

    return render_template("index.html", hash_result=hash_result, algorithm=selected_algo)

if __name__ == "__main__":
    app.run(debug=True)
