from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import uuid
import time
from Powerpoint_explainer.Client.client import WebAPIClient  # Import the client you'll create later

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    uid = str(uuid.uuid4())
    timestamp = int(time.time())
    new_filename = f"{filename}_{timestamp}_{uid}.pptx"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
    file.save(file_path)

    # Assuming you have a WebAPIClient class defined in client/client.py
    client = WebAPIClient()
    uid_response = client.upload_file(file_path)

    return jsonify({'uid': uid_response}), 200


@app.route('/status/<string:uid>', methods=['GET'])
def get_status(uid):
    # Assuming you have a WebAPIClient class defined in client/client.py
    client = WebAPIClient()
    status_response = client.get_status(uid)

    return jsonify(status_response)


if __name__ == '__main__':
    app.run(debug=True)
