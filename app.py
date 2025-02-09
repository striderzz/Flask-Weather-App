from flask import Flask,render_template,request
import requests

app = Flask(__name__)

# OpenWeather API Configuration
API_KEY = "12f1d2c6894fa488bfe2354405ccab2b"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods = ['POST'])
def get_weather():
    city = request.form['city']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    response = requests.get(url).json()

    if response.get('cod') != 200:
     return render_template('index.html', error="City not found.")

    weather_data = {
          'city': city,
          'temperature': response['main']['temp'],
          'description': response['weather'][0]['description'],
          'humidity': response['main']['humidity'],
          'wind_speed': response['wind']['speed'],
          'icon': response['weather'][0]['icon'],
      }
    
    print(weather_data)
    return render_template('result.html', weather=weather_data)
 

    

if __name__ == "__main__":
    app.run(debug=True)
