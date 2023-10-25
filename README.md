<!-- ABOUT THE PROJECT -->
*View the frontend repository [here](https://github.com/shiyanboxer/recall.ai-demo-fe)*

# About The Project
This is a simple web application that showcases the [Recall.ai](https://www.recall.ai) in action. The project was developed using Python, Flask, React, Typescript, and the Recall.ai API. Users can input a bot name and a Google or Zoom meeting link, enabling the Recall.ai bot to join the meeting. Additionally, users have the capability to disconnect the meeting bot and pause and resume recordings.

![Backend Server](https://github.com/shiyanboxer/recall.ai-demo-be/blob/main/img/BackendServer.png)

<!-- FEATURES -->
## Features
- **Create Bot**: The bot is generated when a valid meeting link and bot name are provided. This feature utilizes the [Create Bot endpoint](https://recallai.readme.io/reference/bot_create).
- **Transcribe Meeting**: Recall.ai transcribes meeting dialogues, making them visible on the screen. This feature utilizes the  [Bot Transcript List](https://recallai.readme.io/reference/bot_transcript_list)
- **Pause Bot**: This feature instructs the bot to pause a recording. This feature utilizes the [Pause Recording Create endpoint](https://recallai.readme.io/reference/bot_pause_recording_create).
- **Resume Bot**: This feature allows the bot to continue recording, by utilizing the [Bot Resume Recording Create endpoint](https://recallai.readme.io/reference/bot_resume_recording_create).
- **Leave Meeting**: This feature allows the bot to leave the meeting, by utilizing the [Bot Leave Call Create endpoin](https://recallai.readme.io/reference/bot_leave_call_create)

<!-- TECHNOLOGIES -->
### Built With
- Recall.ai API
- Python 3.10.5
- Flask
- Requests
- Request
- Jsonify
- os
- CORS

<!-- PROJECT STRUCTURE -->
## Project Structure

Below is an overview of the project structure.

- **app.py**: This is the main application file containing the Flask app and the defined routes.

- **transcript.py**: This script defines a Flask application that listens for POST requests at the /meeting_transcript endpoint. It processes incoming JSON data, extracts speaker-transcript pairs, and prints them to the console. It is typically used for handling real-time meeting transcription data.

- **requirements.txt**: This file lists the Python packages required for this project. You can generate this file using `pip freeze > requirements.txt` to capture the dependencies.

- **.env**: You can store your environment variables here, including `RECALL_API_KEY` and `WEBHOOK_URL`. Make sure to add this file to your `.gitignore` to keep sensitive data secure.

- **README.md**: This file provides documentation and instructions for running the application. You can include descriptions of the endpoints, how to set up environment variables, and how to run the application.

- **.gitignore**: This file is used to specify which files or directories should be ignored by version control. You should include `.env` and `venv/` in the `.gitignore` file to prevent sensitive data and virtual environments from being committed to your repository.

- **LICENSE**: If you want to specify the licensing terms for your project, you can include a LICENSE file with the chosen license's text.


<!-- API DOCUMENTATION -->
## API Documentation

This API provides endpoints for interacting with the Recall.ai service. Before using these endpoints, ensure that you have set the necessary environment variables (`RECALL_API_KEY` and `WEBHOOK_URL`).

### 1. Connect Bot

- **Endpoint**: `/`
- **Method**: POST
- **Description**: Connects a bot to a meeting, enabling real-time transcription.
- **Request JSON Parameters**:
  - `bot_name`: (string) The name of the bot.
  - `meeting_url`: (string) The URL of the meeting.
- **Response**:
  - `id`: (int) The ID of the created bot.
- **Status Codes**:
  - 200: Success.
  - 400: Bad Request - Missing `bot_name` or `meeting_url`.
  - 500: Internal Server Error.

### 2. Disconnect from Meeting

- **Endpoint**: `/disconnect`
- **Method**: POST
- **Description**: Disconnects the bot from a meeting.
- **Request JSON Parameters**:
  - `meeting_id`: (int) The ID of the meeting to disconnect from.
- **Status Codes**:
  - 200: Success.
  - 500: Internal Server Error (if an error occurs).

### 3. Pause Recording

- **Endpoint**: `/pause`
- **Method**: POST
- **Description**: Pauses the recording of a meeting.
- **Request JSON Parameters**:
  - `meeting_id`: (int) The ID of the meeting to pause recording for.
- **Status Codes**:
  - 200: Success.
  - 500: Internal Server Error (if an error occurs).

### 4. Resume Recording

- **Endpoint**: `/resume`
- **Method**: POST
- **Description**: Resumes the recording of a meeting.
- **Request JSON Parameters**:
  - `meeting_id`: (int) The ID of the meeting to resume recording for.
- **Status Codes**:
  - 200: Success.
  - 500: Internal Server Error (if an error occurs).

### 5. Meeting Transcript Webhook

- **Endpoint**: `/meeting_transcript`
- **Method**: POST
- **Description**: Receives and processes real-time meeting transcription data. It extracts and prints speaker-transcript pairs.
- **Request JSON Parameters**:
  - `transcript`: (object) The transcription data.
- **Status Codes**:
  - 200: Success.


<!-- PREREQUISITES -->
## Prerequisites
* **Python 3.10** - Installation guide found [here](https://www.python.org/downloads/).
* **pip** - Installation guide found [here](https://pip.pypa.io/en/stable/installation/).
* **ngrok** - Installation guide found [here](https://ngrok.com/).

<!-- QUICKSTART -->
## Quickstart

To get your project running locally, follow these steps.

1. **Generate an API Key**

   Go to the Recall dashboard and generate an [API Key](https://www.recall.ai/).

2. **Clone the Repository**

   ```sh
   git clone https://github.com/shiyanboxer/recall.ai-demo-be.git
   ```

3. **Install the Project Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Generate a Webhook with ngrok**

   Run the following command in your terminal and copy the webhook URL

   ```bash
      ngrok http 8000
   ```

4. **Update the `.env` File**

   Enter your API Key and Webhook URL in the `.env` file

   ```bash
      RECALL_API_KEY=YOUR_API_KEY
      WEBHOOK_URL=YOUR_WEBHOOK_URL
   ```

5. **Run the Server**

   Now you’re ready to run the server, run the following command in your terminal

   ```bash
      cd src
      python app.py
   ```

<!-- USAGE -->
## Usage
1. Generate a URL for your webhook using ngrok on our specified port (8000).

   ```sh
   ngrok http 8000
   ```

2. Add your webhook URL to the `.env` file.

   ```txt
   WEBHOOK_URL=YOUR URL HERE
   ```

3. Start your backend server

   ```bash
   cd src
   python app.py
   ```

4. Once the service is running, start your client server. (You will need to follow the steps on the [Recall.ai Demo Frontend respoitory](https://github.com/shiyanboxer/recall.ai-demo-fe) to set this up)

   ```bash
   npm run dev
   ```

5. Open http://localhost:3000/ to see the project

6. Create a Zoom or Google Meets meeting and copy the meeting URL

7. Paste the meeting URL into the meeting link field and assign a name to the meeting bot in the name field. Afterward, click on "Connect."

8. Admit the meeting bot in your meeting.

![Admit bot](https://github.com/shiyanboxer/recall.ai-demo-be/blob/main/img/MeetingAdmit.png)

9. After clicking "Connect," you'll be directed to the Connected meeting page. Here, you can manage the bot and view the real-time meeting transcript.


## References
Recall documentation: https://recallai.readme.io/reference/recall-overview

## Contact
If you have any questions, please reach out to shiyanboxer@gmail.com. 
