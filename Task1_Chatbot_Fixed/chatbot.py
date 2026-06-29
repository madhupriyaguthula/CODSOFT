import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime


class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("AI ChatBot")
        self.root.geometry("600x700")
        self.root.configure(bg="#1e1e2f")

        title = tk.Label(
            root,
            text="🤖 Rule-Based ChatBot",
            font=("Arial", 18, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        title.pack(pady=10)

        self.chat_area = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Arial", 12),
            bg="#2d2d44",
            fg="white",
            insertbackground="white"
        )
        self.chat_area.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.config(state=tk.DISABLED)

        input_frame = tk.Frame(root, bg="#1e1e2f")
        input_frame.pack(fill=tk.X, padx=15, pady=10)

        self.user_input = tk.Entry(
            input_frame,
            font=("Arial", 12),
            bg="#2d2d44",
            fg="white",
            insertbackground="white"
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.send_message)

        send_btn = tk.Button(
            input_frame,
            text="Send",
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.send_message
        )
        send_btn.pack(side=tk.RIGHT)

        self.display_message(
            "Bot",
            "Hello! I'm your Rule-Based ChatBot. Type 'help' to see what I can do."
        )

    def display_message(self, sender, message):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

    def get_response(self, message):
        message = message.lower()

        if any(word in message for word in ["hello", "hi", "hey"]):
            return "Hello! How can I help you today?"

        elif "how are you" in message:
            return "I'm doing great! Thanks for asking."

        elif "your name" in message:
            return "I am a Rule-Based ChatBot created using Python."

        elif "time" in message:
            return f"Current Time: {datetime.now().strftime('%H:%M:%S')}"

        elif "date" in message:
            return f"Today's Date: {datetime.now().strftime('%d-%m-%Y')}"

        elif "joke" in message:
            return "Why do programmers hate nature? Because it has too many bugs!"

        elif "motivate" in message:
            return "Believe in yourself. Small progress every day leads to big success."

        elif "python" in message:
            return "Python is a powerful programming language used in AI, Web Development, and Data Science."

        elif "help" in message:
            return (
                "You can ask:\n"
                "• Hello\n"
                "• How are you\n"
                "• Time\n"
                "• Date\n"
                "• Joke\n"
                "• Motivation\n"
                "• Python\n"
                "• Your name"
            )

        elif any(word in message for word in ["bye", "exit", "quit"]):
            self.root.after(1000, self.root.destroy)
            return "Goodbye! Have a great day."

        else:
            return "Sorry, I don't understand that. Try typing 'help'."

    def send_message(self, event=None):
        message = self.user_input.get().strip()

        if message:
            self.display_message("You", message)

            response = self.get_response(message)
            self.display_message("Bot", response)

            self.user_input.delete(0, tk.END)


root = tk.Tk()
app = ChatBot(root)
root.mainloop()