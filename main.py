from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/age-calculator", methods=["POST", "GET"])
def age_calculator():
    if request.method == 'POST':
        data = request.get_json()
        birthdate_str = data.get("birthdate")
        if not birthdate_str:
            return jsonify({"error": "No birthdate provided"}), 400
        try:
            birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
            today = datetime.today()
            years = today.year - birthdate.year
            months = today.month - birthdate.month
            if today.day < birthdate.day:
                months -= 1
            if months < 0:
                years -= 1
                months += 12
            age = f"{years} years {months} months"
            return jsonify({"age": age})
        except ValueError:
            return jsonify({"error": "Invalid date format"}), 400
    return render_template("age_calculator.html")

if __name__=="__main__":
    app.run()