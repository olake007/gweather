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
    weather_disc = response.get("list")[0].get("weather")[0].get('icon')

    print(weather_disc)



    if weather_disc == "04d":
        weather_icon = "04d.png"

    elif weather_disc == "01d":
        weather_icon = "01d.png"

    elif weather_disc == "02d":
        weather_icon = "02d.png"

    elif weather_disc == "03d":
        weather_icon = "03d.png"

    elif weather_disc == "09d":
        weather_icon = "09d.png"

    elif weather_disc == "10d":
        weather_icon = "10d.png"

    elif weather_disc == "11d":
        weather_icon = "11d.png"

    elif weather_disc == "13d":
        weather_icon = "13d.png"

    elif weather_disc == "50d":
        weather_icon = "50d.png"

    elif weather_disc == "01n":
        weather_icon = "01n.png"

    elif weather_disc == "02n":
        weather_icon = "02n.png"

    elif weather_disc == "03n":
        weather_icon = "03n.png"

    elif weather_disc == "04n":
        weather_icon = "04d.png"

    elif weather_disc == "09n":
        weather_icon = "09n.png"

    elif weather_disc == "10n":
        weather_icon = "10n.png"

    elif weather_disc == "11n":
        weather_icon = "11n.png"

    elif weather_disc == "13n":
        weather_icon = "13n.png"

    elif weather_disc == "50n":
        weather_icon = "50n.png"



    return render_template('result.html', weather_icon=weather_icon)


if __name__ == '__main__':
    app.run(debug=True)
