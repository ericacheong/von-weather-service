#!venv/bin/python
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

weather = [
    {
        'id': 1,
        'city': 'paris',
        'temp_celsius': 15, 
        'humidity_percent': 82,
        'wind_kmh': 10,
        'status': 'Partly cloudy',
        'atmospheric_pressure_mb': 1009
    },
    {
        'id': 2,
        'city': 'hongkong',
        'temp_celsius': 24,
        'humidity_percent': 67,
        'wind_kmh': 12,
        'status': 'Sunny',
        'atmospheric_pressure_mb': 1013
    },
    {
        'id': 3,
        'city': 'shanghai',
        'temp_celsius': 19,
        'humidity_percent': 75,
        'wind_kmh': 9,
        'status': 'Clear',
        'atmospheric_pressure_mb': 1013
    },

    ]




@app.route('/api/v1.0/<city>/temp', methods=['GET'])
def get_temp(city):
    city_weather = [city_weather for city_weather in weather if city_weather['city'] == city]
    if len(city_weather) == 0:
        abort(404)
    return jsonify({
        'city': city,
        'temperture': city_weather[0]['temp_celsius']
        })

@app.route('/api/v1.0/<city>/humidity', methods=['GET'])
def get_humidity(city):
    city_weather = [city_weather for city_weather in weather if city_weather['city'] == city]
    if len(city_weather) == 0:
        abort(404)
    return jsonify({
        'city': city,
        'humidity': city_weather[0]['humidity_percent']
        })

@app.route('/api/v1.0/<city>/wind', methods=['GET'])
def get_wind(city):
    city_weather = [city_weather for city_weather in weather if city_weather['city'] == city]
    if len(city_weather) == 0:
        abort(404)
    return jsonify({
        'city': city,
        'wind': city_weather[0]['wind_kmh']
        })

@app.route('/api/v1.0/<city>/status', methods=['GET'])
def get_status(city):
    city_weather = [city_weather for city_weather in weather if city_weather['city'] == city]
    if len(city_weather) == 0:
        abort(404)
    return jsonify({
        'city': city,
        'status': city_weather[0]['status']
        })

@app.route('/api/v1.0/<city>/atmospres', methods=['GET'])
def get_atmospres(city):
    city_weather = [city_weather for city_weather in weather if city_weather['city'] == city]
    if len(city_weather) == 0:
        abort(404)
    return jsonify({
        'city': city,
        'atmospheric pressure': city_weather[0]['atmospheric_pressure_mb']
        })

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)