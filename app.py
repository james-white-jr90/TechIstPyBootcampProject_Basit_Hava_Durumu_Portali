import os
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city")
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric&lang=tr"
        )
        try:
            response = requests.get(url)
            if response.status_code != 200:
                return render_template("result.html", error=True)
            data = response.json()
            weather = {
                "city": city,
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"],
            }
            return render_template("result.html", weather=weather)
        except requests.exceptions.RequestException:
            return render_template("result.html", error=True)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
