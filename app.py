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

    print(url)

    response = requests.get(url).json()

    data = response['list']

    weather_disc = response.get("list")[0].get("weather")[0].get('description')

    print(weather_disc)

    if weather_disc == "overcast clouds":
        weather_icon =

    print(response)

    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
