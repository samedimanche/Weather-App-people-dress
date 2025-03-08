# Flask-Based Weather Forecasting Service

This project is a **weather forecasting service** built using **Flask**, a lightweight Python web framework. The service not only provides weather forecasts but also displays photos of how people typically dress for the current weather conditions, based on the temperature. This unique feature makes it a practical and visually engaging tool for users to plan their outfits according to the weather.

## Overview

The service integrates with the [weatherapi.com](https://www.weatherapi.com/) API to fetch real-time weather data. Users can input their location, and the service will display the current temperature along with a corresponding photo of how people dress in such weather. The photos are sourced from the Internet and are used solely for **educational purposes**, with no commercial intent.

### Key Features

- **Weather Forecast**: Fetches real-time weather data using the **weatherapi.com** API.
- **Outfit Suggestions**: Displays photos of how people dress for the current temperature.
- **User-Friendly Interface**: Simple and intuitive design for easy navigation.
- **API Key Integration**: Users can insert their own API key from **weatherapi.com** to access the service.

## Technologies Used

- **Flask**: The core framework used to build the web application.
- **weatherapi.com**: Provides accurate and real-time weather data.
- **HTML/CSS**: Used for structuring and styling the front-end interface.
- **Python**: The primary programming language for backend logic and API integration.
- **Jinja2**: Templating engine for rendering dynamic content in Flask.

## How It Works

1. **API Integration**: The service connects to **weatherapi.com** to fetch weather data based on the user's location.
2. **Temperature Analysis**: The current temperature is analyzed to determine the appropriate clothing style.
3. **Photo Display**: A photo corresponding to the temperature is displayed, showing how people typically dress in such weather.
4. **User Interaction**: Users can input their location and view the weather forecast along with outfit suggestions.

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Key**:
   - Obtain an API key from [weatherapi.com](https://www.weatherapi.com/).
   - Insert the API key in the designated configuration file or environment variable.

4. **Run the Application**:
   ```bash
   flask run
   ```

5. **Access the Service**:
   - Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

- Enter your location in the provided input field.
- View the current weather forecast and corresponding outfit suggestions.

## Disclaimer

All photos used in this service are sourced from the Internet and are intended solely for **educational purposes**. They are not used for any commercial purposes.

## Contribution

Contributions to the project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Thank you for your interest in this project! For more details, feel free to explore the repository and reach out with any questions.
