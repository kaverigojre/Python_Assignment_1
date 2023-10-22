import configparser
import json
from flask import Flask, jsonify

# Create a Flask application
app = Flask(__name)

# Function to parse the configuration file and save it as JSON
def parse_config_and_save_to_json():
    config = configparser.ConfigParser()
    config.read('config.ini')  # Provide the path to your configuration file

    config_data = {}

    for section in config.sections():
        config_data[section] = {}
        for option in config.options(section):
            config_data[section][option] = config.get(section, option)

    with open('config.json', 'w') as json_file:
        json.dump(config_data, json_file, indent=4)

# Endpoint to fetch the configuration as JSON
@app.route('/get_config', methods=['GET'])
def get_config():
    with open('config.json', 'r') as json_file:
        config_data = json.load(json_file)
        return jsonify(config_data)

if __name__ == '__main__':
    try:
        parse_config_and_save_to_json()
        print("Configuration File Parser Results:")
        with open('config.json', 'r') as json_file:
            print(json_file.read())

        app.run()
    except FileNotFoundError:
        print("Error: Configuration file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
