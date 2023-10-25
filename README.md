<!-- ABOUT THE PROJECT -->
*View the frontend repository [here](https://github.com/shiyanboxer/recall.ai-demo-fe)*

# About The Project
This is a simple web application that showcases the [Recall.ai](https://www.recall.ai) in action. The project was developed using Python, Flask, React, Typescript, and the Recall.ai API. Users can input a bot name and a Google or Zoom meeting link, enabling the Recall.ai bot to join the meeting. Additionally, users have the capability to disconnect the meeting bot and pause and resume recordings.

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

<!-- PROJECT -->
## Project Structure
The project is divided into two separate repositories: the frontend repository and the backend repository.

<!-- PREREQUISITES -->
### Prerequisites
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

6. **Create a Meeting**

   Create a meeting with Zoom or Google Meets. After creating the meeting, make sure to stay in the meeting and save the meeting URL.

7. **Run the Frontend Server**

   To connect your server to the client, you will need to follow the steps on the [Recall.ai Demo Frontend respoitory](https://github.com/shiyanboxer/recall.ai-demo-fe)


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

4. Once the service is running open start your client server

   ```bash
   npm run dev
   ```

5. Open http://localhost:3000/ to see the project

## References
- Recall documentation: https://recallai.readme.io/reference/recall-overview

## Contact
If you have any questions, please reach out to shiyanboxer@gmail.com. 
