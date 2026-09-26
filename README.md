# AI Auto Reply Chatbot

An AI-powered WhatsApp auto-reply chatbot built with Python that reads chat history, detects the latest sender, generates a natural reply using the Groq Llama 3.3 70B model, and automatically sends the response through the WhatsApp interface.

## Features

* 🤖 AI-generated replies using Groq API and Llama 3.3 70B
* 💬 Reads WhatsApp chat history automatically
* 👤 Detects whether the latest message was sent by the selected contact
* 🧠 Generates replies based on the complete chat history
* 🌐 Supports natural replies in Odia, Hindi, and English
* 🖱️ Automates WhatsApp interaction using PyAutoGUI
* 📋 Uses Pyperclip for copying and pasting chat data and replies
* ⚡ Continuously checks for new messages
* 🚫 Avoids processing the same chat repeatedly

## Technologies Used

* Python
* Groq API
* Llama 3.3 70B
* PyAutoGUI
* Pyperclip
* WhatsApp Web/Desktop

## How It Works

```text
WhatsApp Chat
      ↓
Copy Chat History
      ↓
Analyze Latest Message
      ↓
Check Sender
      ↓
If Selected Contact Sent Message
      ↓
Groq Llama 3.3 70B
      ↓
Generate Natural Reply
      ↓
Copy AI Response
      ↓
Paste into WhatsApp
      ↓
Send Message
```

## Project Workflow

1. The program opens and focuses on the target WhatsApp window.
2. It selects and copies the visible chat history.
3. The copied chat is retrieved using Pyperclip.
4. The program checks whether the latest message was sent by the selected contact.
5. If the selected contact sent the latest message, the complete chat history is sent to the Groq API.
6. The Llama 3.3 70B model generates a short and natural response.
7. The generated response is copied to the clipboard.
8. PyAutoGUI pastes the response into the WhatsApp chat box.
9. The message is automatically sent.
10. The program waits and checks for new messages again.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-auto-reply-chatbot.git
cd ai-auto-reply-chatbot
```

### 2. Install dependencies

```bash
pip install groq pyautogui pyperclip python-dotenv
```

### 3. Configure the Groq API

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Load the API key in Python:

```python
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
```

### 4. Protect your API key

Add `.env` to `.gitignore`:

```text
.env
```

**Never upload your actual API key to GitHub.**

## Running the Project

Start WhatsApp and open the target conversation before running:

```bash
python auto_reply.py
```

The program will wait for the target chat to be ready and then begin checking for new messages.

## Configuration

The default selected sender is:

```python
sender_name="Papali"
```

You can change it to another contact:

```python
is_last_message_from(chat_history, "ContactName")
```

The chatbot is configured to generate replies in:

* English
* Hindi
* Odia

## Important Notes

* This project uses screen coordinates through PyAutoGUI, so coordinates may need to be adjusted depending on your screen resolution and WhatsApp layout.
* The WhatsApp window must be positioned correctly for the automation to work.
* The chatbot should be tested carefully before enabling automatic message sending.
* Keep your API credentials private.

## Future Improvements

* Add a graphical user interface
* Add configurable screen coordinates
* Add better chat/message extraction
* Add customizable response styles
* Add pause/resume controls
* Add support for multiple contacts
* Improve message detection reliability
* Add conversation history management

## Author

**Sunit Swain**

B.Tech — Electronics and Communication Engineering
