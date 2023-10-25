from flask import Flask, request

app = Flask(__name__)

@app.route('/meeting_transcript', methods=['POST'])
def meeting_transcript():
    data = request.get_json()
    print(data)
    if data and 'transcript' in data and data['transcript']['speaker'] is not None:
        speaker = data['transcript']['speaker']
        words = data['transcript']['words']
        msg = " ".join(word['text'] for word in words)
        print(f"{speaker}: {msg}")
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
