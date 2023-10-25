import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Create a single 'recall' session with common headers
recall = requests.Session()
recall.headers.update({
    'authorization': f'token {os.environ["RECALL_API_KEY"]}',
    'content-type': 'application/json'
})
recall.timeout = 10


# Function to make a generic API call
def make_recall_api_call(endpoint, method='POST', data=None):
    try:
        response = recall.request(
            method,
            f'https://api.recall.ai/api/v1/bot/{endpoint}',
            json=data,
        )
        response.raise_for_status()
        return response.json()
    except Exception as err:
        return str(err), 500


# Establish connection with meeting and bot
@app.route('/', methods=['POST'])
def connect_bot():
    data = request.json
    bot_name = data.get('bot_name')
    meeting_url = data.get('meeting_url')

    if not bot_name or not meeting_url:
        return jsonify({'error': 'Bot name and meeting URL are required'}), 400

    payload = {
        'meeting_url': meeting_url,
        'bot_name': bot_name,
        'transcription_options': {'provider': 'assembly_ai'},
        'real_time_transcription': {'destination_url': f'{os.environ["WEBHOOK_URL"]}/meeting_transcript'}
    }
    result = make_recall_api_call('bot', 'POST', payload)
    return jsonify(result), 200


# Disconnect bot from meeting
@app.route('/disconnect', methods=['POST'])
def leave_meeting():
    data = request.json
    meeting_id = data.get('meetingId')

    if not meeting_id:
        return jsonify({'error': 'Meeting ID is required'}), 400

    result = make_recall_api_call(f'bot/{meeting_id}/leave_call')
    return jsonify(result), 200

# Pause meeting recording


@app.route('/pause', methods=['POST'])
def pause_recording():
    data = request.json
    meeting_id = data.get('meetingId')
    if not meeting_id:
        return jsonify({'error': 'Meeting ID is required'}), 400

    result = make_recall_api_call(f'bot/{meeting_id}/pause_recording')
    return jsonify(result), 200


# Resume meeting recording
@app.route('/resume', methods=['POST'])
def resume_recording():
    data = request.json
    meeting_id = data.get('meetingId')
    if not meeting_id:
        return jsonify({'error': 'Meeting ID is required'}), 400

    result = make_recall_api_call(f'bot/{meeting_id}/resume_recording')
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(port=5000)
