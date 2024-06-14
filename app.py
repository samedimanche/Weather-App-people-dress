from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Set the path to the img folder
img_folder = 'static/img'

# Set the API key for the weather service (replace with your own API key)
api_key = '7efa370fe14e4c0db2575239241406'


@app.route('/', methods=['GET', 'POST'])
def index():
    location = None
    temperature = None
    image_files = []

    if request.method == 'POST':
        # Get the user's entered location from the form
        location = request.form['location']

        # Make an API request to get the weather data for the location
        weather_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        # Extract the temperature from the weather data
        temperature = weather_data['current']['temp_c']

        # Determine the appropriate image range based on the temperature
        if -30 <= temperature < 0:
            image_range = range(1, 3)
        elif 0 <= temperature < 15:
            image_range = range(4, 6)
        elif 15 <= temperature < 20:
            image_range = range(7, 9)
        else:
            image_range = range(10, 12)

        # Generate the image file names based on the range
        image_files = [f'{i}.jpg' for i in image_range]

    return render_template('index.html', location=location, temperature=temperature, image_files=image_files)

if __name__ == '__main__':
    app.run(debug=True)