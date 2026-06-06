# CodeAlpha__task__3
# Simple Rule-Based Chatbot

A lightweight, console-based intelligent chatbot implemented in Python. This project demonstrates basic Natural Language Processing (NLP) concepts using standard string normalization and a rule-based conditional response system.

## 🚀 Features

* **String Normalization:** Automatically converts user input to lowercase and strips trailing spaces to ensure robust input matching.
* **Instant Rule-Based Responses:** Provides contextual responses for common greetings and inquiries.
* **Continuous Loop Execution:** Runs endlessly in the terminal until the user explicitly signals to exit.
* **Graceful Exit Handler:** Safely breaks the execution loop when the user says "bye".

---

## 🛠️ How It Works

The core logic maps cleaned user inputs to predefined static responses using a standard conditional decision structure:

| User Input (Case-Insensitive) | Chatbot Response |
| :--- | :--- |
| `hello` | "Hi!" |
| `how are you` | "I'm fine, thanks!" |
| `what is your name` | "I am a simple chatbot." |
| `bye` | "Goodbye!" |
| *Anything else* | "Sorry, I don't understand that." |

---

## 💻 Getting Started

### Prerequisites
Make sure you have Python installed on your local machine. This project works natively on **Python 3.x** and requires no external third-party libraries.

### Installation & Execution

1. Clone or download this repository to your computer.
2. Open your terminal or command prompt inside the project folder.
3. Run the script using the following command:

```bash
python chatbot.py
