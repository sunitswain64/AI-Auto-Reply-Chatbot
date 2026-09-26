import time
import pyautogui
import pyperclip
from groq import Groq

client = Groq(
    api_key=" "
)


def is_last_message_from(chat_log, sender_name="Papali"):
    """
    Returns True if the last message was sent by sender_name.
    """

    lines = [line.strip() for line in chat_log.splitlines() if line.strip()]

    if not lines:
        return False

    last_message = lines[-1]

    if not last_message.startswith("[") or "] " not in last_message:
        return False

    sender = last_message.split("] ", 1)[1].split(":", 1)[0].strip()

    return sender.lower() == sender_name.lower()


print("Switch to the target app...")
time.sleep(10)

# Focus WhatsApp
pyautogui.click(1343, 916)
time.sleep(1)

last_chat = ""

while True:

    # -----------------------------
    # Copy chat
    # -----------------------------
    pyautogui.moveTo(679, 100)
    pyautogui.dragTo(1236, 695, duration=1.5, button="left")

    time.sleep(0.5)

    pyautogui.hotkey("command", "c")

    time.sleep(1)

    chat_history = pyperclip.paste().strip()

    pyautogui.click(1236, 695)

    if not chat_history:
        print("Nothing copied.")
        time.sleep(2)
        continue

    # ------------------------------------
    # Ignore duplicate chats
    # ------------------------------------
    if chat_history == last_chat:
        time.sleep(2)
        continue

    last_chat = chat_history

    print("\n================ CHAT ================\n")
    print(chat_history)
    print("\n======================================\n")

    # ------------------------------------
    # Reply only if Papali sent last message
    # ------------------------------------
    if is_last_message_from(chat_history, "Papali"):

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are SUNIT SWAIN. "
                        "You speak Odia, Hindi and English naturally. "
                        "The user message contains the complete WhatsApp chat history. "
                        "Generate ONLY the next message that SUNIT SWAIN would send. "
                        "Keep the reply short, natural and human. "
                        "Do not explain your reasoning. "
                        "Do not summarize the conversation. "
                        "Output ONLY the reply text."
                    )
                },
                {
                    "role": "user",
                    "content": chat_history
                }
            ],
            temperature=0.7,
            max_tokens=150
        )

        response = completion.choices[0].message.content.strip()

        print("\n=========== AI REPLY ===========\n")
        print(response)
        print("\n================================\n")

        # Copy reply
        pyperclip.copy(response)

        time.sleep(0.5)

        # Click chat box
        pyautogui.click(734, 784)

        time.sleep(0.3)

        # Paste
        pyautogui.hotkey("command", "v")

        time.sleep(0.2)

        # Send
        pyautogui.press("enter")

        print("Reply Sent!")

    else:
        print("Last message is not from Papali.")

    # Check every 2 seconds
    time.sleep(2)