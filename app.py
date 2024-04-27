import subprocess
import os
from pathlib import Path

from flask import Flask, request
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

FILE_INPUT_LOCATION = os.getenv("FILE_INPUT_LOCATION", "/var/lib/telegram-bot/input/")
FILE_OUTPUT_LOCATION = os.getenv("FILE_OUTPUT_LOCATION", "/var/lib/telegram-bot/output/")
FILE_SIZE_LIMIT = int(os.getenv("FILE_SIZE_LIMIT", 20))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FILE_INPUT_LOCATION
app.config['MAX_CONTENT_LENGTH'] = FILE_SIZE_LIMIT * 1000 * 1000


@app.route("/health", methods=['GET'])
async def get_health():
    return {"message": "ok"}, 200


@app.route("/", methods=['GET'])
async def get_index():
    return {"message": "welcome"}, 200


@app.route("/forms/libreoffice/converttopdf", methods=['POST'])
async def post_pdfConversion():
    input_filename = request.form.get("filename")

    if not input_filename:
        return {"error": "filename is missing"}, 422
    
    input_filepath = os.path.join(FILE_INPUT_LOCATION, input_filename)

    if os.path.exists(input_filepath):
        exit_code = subprocess.call(['libreoffice', '--headless', '--convert-to', 'pdf', "--outdir", FILE_OUTPUT_LOCATION, input_filepath])
        if exit_code == 0:
            return{"message": "done"}, 200
        else:
            return{"error": "converter exit code is " + exit_code}, 500
    else:
        return {"error": "non-existent filename - " + input_filepath}, 422
    

if __name__ == '__main__':
    app.run()