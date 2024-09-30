import tkinter as tk
from tkinter import scrolledtext
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon if not already done
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analyze_sentiment():
    user_input = input_text.get("1.0", tk.END).strip()
    if user_input:
        # Display user input in the chat
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"You: {user_input}\n")
        
        # Analyze sentiment
        sentiment_score = sia.polarity_scores(user_input)
        compound = sentiment_score['compound']

        if compound >= 0.05:
            sentiment = "Positive 😊"
        elif compound <= -0.05:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

        # Display the bot response in the chat
        chat_area.insert(tk.END, f"Bot: Your sentiment is {sentiment}\n")
        chat_area.config(state=tk.DISABLED)
        chat_area.yview(tk.END)  # Scroll to the bottom
        
        # Clear input text
        input_text.delete("1.0", tk.END)

def exit_chat():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Sentiment Analysis Chatbot")

# Set background color
root.configure(bg="#f0f0f0")

# Create a chat area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 14), bg="#ffffff", fg="#000000")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a text input box
input_text = tk.Text(root, height=3, font=("Arial", 14), bg="#ffffff", fg="#000000")
input_text.pack(padx=10, pady=10, fill=tk.X)

# Create a send button
send_button = tk.Button(root, text="Send", command=analyze_sentiment, font=("Arial", 12), bg="#4CAF50", fg="#ffffff")
send_button.pack(pady=5)

# Create an exit button
exit_button = tk.Button(root, text="Exit", command=exit_chat, font=("Arial", 12), bg="#f44336", fg="#ffffff")
exit_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
