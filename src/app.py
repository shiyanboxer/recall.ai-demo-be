import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Custom Axios Instance
recall = requests.Session()
recall.headers.update({
    'authorization': f'token {os.environ["RECALL_API_KEY"]}',
    'content-type': 'application/json'
})
recall.timeout = 10

# Gets the bot name and meeting link from the request body
# Connects the bot to the meeting


@app.route('/', methods=['POST'])
def connect_bot():
    my_request = request.json
    bot_name = my_request.get('bot_name')
    meeting_url = my_request.get('meeting_url')

    if not bot_name or not meeting_url:
        return jsonify({'error': 'Bot name and meeting URL are required'}), 400
    try:
        payload = {
            'meeting_url': meeting_url,
            'bot_name': bot_name,
            'transcription_options': {'provider': 'assembly_ai'},
            'real_time_transcription': {'destination_url': f'{os.environ["WEBHOOK_URL"]}/meeting_transcript'}
        }
        response = recall.post(
            'https://api.recall.ai/api/v1/bot', json=payload)
        data = response.json()
        print(data)
        return jsonify({'id': data['id']}), 200
    except Exception as err:
        return jsonify({'error': str(err)}), 500


def leave_meeting(meeting_id):
    try:
        recall.post(
            f'https://api.recall.ai/api/v1/bot/{meeting_id}/leave_call')
    except Exception as err:
        print(err)


if __name__ == '__main__':
    app.run(port=5000)
