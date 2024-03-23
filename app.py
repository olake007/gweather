from flask import Flask, render_template, request
import requests
from datetime import datetime


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
    url1 = "https://api.openweathermap.org/data/2.5/forecast?q=" + form_city + "&appid=" + api_key
    url2 = "http://api.openweathermap.org/data/2.5/weather?q=" + form_city + "&APPID=" + api_key
    response_forecast = requests.get(url1).json()
    response_current = requests.get(url2).json()

    # gets weather icon information from the list and determines what icon needs to be displayed

    weather_disc1 = response_forecast.get("list")[0].get("weather")[0].get('icon')
    weather_disc2 = response_forecast.get("list")[8].get("weather")[0].get('icon')
    weather_disc3 = response_forecast.get("list")[16].get("weather")[0].get('icon')
    weather_disc4 = response_forecast.get("list")[24].get("weather")[0].get('icon')
    weather_disc5 = response_forecast.get("list")[32].get("weather")[0].get('icon')

    print(url1)

    print(weather_disc1)

    # determines what image to display depending on the weather - this is for the day that it is ordered on.
    if weather_disc1 == "04d":
        weather_icon1 = "04d.png"
    elif weather_disc1 == "04n":
        weather_icon1 = "04n.png"
    elif weather_disc1 == "01d":
        weather_icon1 = "01d.png"
    elif weather_disc1 == "02d":
        weather_icon1 = "02d.png"
    elif weather_disc1 == "10d":
        weather_icon1 = "10d.png"
    elif weather_disc1 == "01n":
        weather_icon1 = "01n.png"
    elif weather_disc1 == "02n":
        weather_icon1 = "02n.png"
    elif weather_disc1 == "03d":
        weather_icon1 = "03d.png"
    elif weather_disc1 == "03n":
        weather_icon1 = "03n.png"
    elif weather_disc1 == "09d":
        weather_icon1 = "09d.png"
    elif weather_disc1 == "09n":
        weather_icon1 = "09n.png"
    elif weather_disc1 == "10n":
        weather_icon1 = "10n.png"
    elif weather_disc1 == "11d":
        weather_icon1 = "11d.png"
    elif weather_disc1 == "11n":
        weather_icon1 = "11n.png"
    elif weather_disc1 == "13d":
        weather_icon1 = "13d.png"
    elif weather_disc1 == "13n":
        weather_icon1 = "13n.png"
    elif weather_disc1 == "50d":
        weather_icon1 = "50d.png"
    elif weather_disc1 == "50n":
        weather_icon1 = "50n.png"

    # day 2

    if weather_disc2 == "04d":
        weather_icon2 = "04d.png"
    elif weather_disc2 == "04n":
        weather_icon2 = "04n.png"
    elif weather_disc2 == "01d":
        weather_icon2 = "01d.png"
    elif weather_disc2 == "02d":
        weather_icon2 = "02d.png"
    elif weather_disc2 == "10d":
        weather_icon2 = "10d.png"
    elif weather_disc2 == "01n":
        weather_icon2 = "01n.png"
    elif weather_disc2 == "02n":
        weather_icon2 = "02n.png"
    elif weather_disc2 == "03d":
        weather_icon2 = "03d.png"
    elif weather_disc2 == "03n":
        weather_icon2 = "03n.png"
    elif weather_disc2 == "09d":
        weather_icon2 = "09d.png"
    elif weather_disc2 == "09n":
        weather_icon2 = "09n.png"
    elif weather_disc2 == "10n":
        weather_icon2 = "10n.png"
    elif weather_disc2 == "11d":
        weather_icon2 = "11d.png"
    elif weather_disc2 == "11n":
        weather_icon2 = "11n.png"
    elif weather_disc2 == "13d":
        weather_icon2 = "13d.png"
    elif weather_disc2 == "13n":
        weather_icon2 = "13n.png"
    elif weather_disc2 == "50d":
        weather_icon2 = "50d.png"
    elif weather_disc2 == "50n":
        weather_icon2 = "50n.png"

    # day 3

    if weather_disc3 == "04d":
        weather_icon3 = "04d.png"
    elif weather_disc3 == "04n":
        weather_icon3 = "04n.png"
    elif weather_disc3 == "01d":
        weather_icon3 = "01d.png"
    elif weather_disc3 == "02d":
        weather_icon3 = "02d.png"
    elif weather_disc3 == "10d":
        weather_icon3 = "10d.png"
    elif weather_disc3 == "01n":
        weather_icon3 = "01n.png"
    elif weather_disc3 == "02n":
        weather_icon3 = "02n.png"
    elif weather_disc3 == "03d":
        weather_icon3 = "03d.png"
    elif weather_disc3 == "03n":
        weather_icon3 = "03n.png"
    elif weather_disc3 == "09d":
        weather_icon3 = "09d.png"
    elif weather_disc3 == "09n":
        weather_icon3 = "09n.png"
    elif weather_disc3 == "10n":
        weather_icon3 = "10n.png"
    elif weather_disc3 == "11d":
        weather_icon3 = "11d.png"
    elif weather_disc3 == "11n":
        weather_icon3 = "11n.png"
    elif weather_disc3 == "13d":
        weather_icon3 = "13d.png"
    elif weather_disc3 == "13n":
        weather_icon3 = "13n.png"
    elif weather_disc3 == "50d":
        weather_icon3 = "50d.png"
    elif weather_disc3 == "50n":
        weather_icon3 = "50n.png"

    # day 4

    if weather_disc4 == "04d":
        weather_icon4 = "04d.png"
    elif weather_disc4 == "04n":
        weather_icon4 = "04n.png"
    elif weather_disc4 == "01d":
        weather_icon4 = "01d.png"
    elif weather_disc4 == "02d":
        weather_icon4 = "02d.png"
    elif weather_disc4 == "10d":
        weather_icon4 = "10d.png"
    elif weather_disc4 == "01n":
        weather_icon4 = "01n.png"
    elif weather_disc4 == "02n":
        weather_icon4 = "02n.png"
    elif weather_disc4 == "03d":
        weather_icon4 = "03d.png"
    elif weather_disc4 == "03n":
        weather_icon4 = "03n.png"
    elif weather_disc4 == "09d":
        weather_icon4 = "09d.png"
    elif weather_disc4 == "09n":
        weather_icon4 = "09n.png"
    elif weather_disc4 == "10n":
        weather_icon4 = "10n.png"
    elif weather_disc4 == "11d":
        weather_icon4 = "11d.png"
    elif weather_disc4 == "11n":
        weather_icon4 = "11n.png"
    elif weather_disc4 == "13d":
        weather_icon4 = "13d.png"
    elif weather_disc4 == "13n":
        weather_icon4 = "13n.png"
    elif weather_disc4 == "50d":
        weather_icon4 = "50d.png"
    elif weather_disc4 == "50n":
        weather_icon4 = "50n.png"

    # day 5

    if weather_disc5 == "04d":
        weather_icon5 = "04d.png"
    elif weather_disc5 == "04n":
        weather_icon5 = "04n.png"
    elif weather_disc5 == "01d":
        weather_icon5 = "01d.png"
    elif weather_disc5 == "02d":
        weather_icon5 = "02d.png"
    elif weather_disc5 == "10d":
        weather_icon5 = "10d.png"
    elif weather_disc5 == "01n":
        weather_icon5 = "01n.png"
    elif weather_disc5 == "02n":
        weather_icon5 = "02n.png"
    elif weather_disc5 == "03d":
        weather_icon5 = "03d.png"
    elif weather_disc5 == "03n":
        weather_icon5 = "03n.png"
    elif weather_disc5 == "09d":
        weather_icon5 = "09d.png"
    elif weather_disc5 == "09n":
        weather_icon5 = "09n.png"
    elif weather_disc5 == "10n":
        weather_icon5 = "10n.png"
    elif weather_disc5 == "11d":
        weather_icon5 = "11d.png"
    elif weather_disc5 == "11n":
        weather_icon5 = "11n.png"
    elif weather_disc5 == "13d":
        weather_icon5 = "13d.png"
    elif weather_disc5 == "13n":
        weather_icon5 = "13n.png"
    elif weather_disc5 == "50d":
        weather_icon5 = "50d.png"
    elif weather_disc5 == "50n":
        weather_icon5 = "50n.png"

    temp_k = response_current.get("main", {}).get("temp")
    temp_c = round(int(temp_k) - 273.15)
    timestamp = response_current.get("dt")
    dt = datetime.fromtimestamp(timestamp)

    print(temp_c)
    print(dt)

    weatherinfo_dict = {
        "temp_c": temp_c,
        "temp_k": temp_k,
        "dt": dt,
    }

    return render_template('result.html',
                           weather_icon1=weather_icon1, weather_icon2=weather_icon2,
                           weather_icon3=weather_icon3, weather_icon4=weather_icon4, weather_icon5=weather_icon5,
                           weatherinfo_dict=weatherinfo_dict)


if __name__ == '__main__':
    app.run(debug=True)
