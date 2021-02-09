import requests
from flask import Flask, request
from config_weather import config

APPID = config()['appid'] # initialize weather api here

app = Flask(__name__)

@app.route('/')
def index():
    city=request.args.get("city", "")
    if city:
        weather_report=weather_data(city)
    else:
        weather_report='please indicate a correct city name'
    return ( 
        """<form action="" method="get">
                <h1>Welcome to my weather app</h1>
                city: <input type="text" name="city">
                <input type="submit" value="get weather report">
            </form>"""
            + "Weather Report: "
            + weather_report
        )

def weather_data(city):
    res=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={APPID}&units=metric")
    result = res.json()
    if result.get('cod') != 200:
        return f'Error getting temperature for {city}. Check the city name'
    else:
        return ("{}'s temperature: {}°C   ".format(city,result['main']['temp']) + 
            "Wind speed: {} m/s   ".format(result['wind']['speed']) + 
	        "Description: {}   ".format(result['weather'][0]['description']) +
	        "Weather: {}".format(result['weather'][0]['main']))

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)