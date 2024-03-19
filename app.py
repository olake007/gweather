from flask import Flask, render_template, request
import requests

app = Flask(__name__)
template_folder = 'template'


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    api_key = "aa9496e9adb3bf2f85fa97e59f3b278a"
    form_city = request.form.get('city')
    form_city = form_city.replace(" ", "")
    url = ("https://api.openweathermap.org/data/2.5/forecast?q=" + form_city + "&appid=" + api_key)
    response = requests.get(url).json()
    weather_disc = response.get("list")[0].get("weather")[0].get('description')

    if weather_disc == "broken clouds":
        weather_icon = "brokenclouds.png"

    elif weather_disc == "clear sky":
        weather_icon = "clearsky.png"

    elif weather_disc == "few clouds":
        weather_icon = "fewclouds.png"

    elif weather_disc == "scattered clouds":
        weather_icon = "scatteredclouds.png"

    elif weather_disc == "shower rain":
        weather_icon = ""

    elif weather_disc == "rain":
        weather_icon = ""

    elif weather_disc == "thunderstorm":
        weather_icon = ""

    elif weather_disc == "snow":
        weather_icon = ""

    elif weather_disc == "mist":
        weather_icon = ""

    return render_template('result.html', weather_icon=weather_icon)


if __name__ == '__main__':
    app.run(debug=True)
