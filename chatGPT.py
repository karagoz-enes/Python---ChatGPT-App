import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import openai

openai.api_key = "your api key"  # your openai API key here ex:"hasjgdjgu3y182182yda8731y387ds"
#how to get API key? goto this website:https://platform.openai.com/docs/overview
#click API keys from the left panel and create an api key :)
model_engine = "text-davinci-003"

class ChatGPTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatGPT APP")

        self.chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.chat_history.pack(pady=10)

        self.user_input = tk.Text(root, wrap=tk.WORD, width=50, height=5)
        self.user_input.pack(pady=10, fill=tk.X, expand=True)
        self.user_input_scrollbar = tk.Scrollbar(root, command=self.user_input.yview)
        self.user_input_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.user_input["yscrollcommand"] = self.user_input_scrollbar.set

        self.send_button = tk.Button(root, text="SEND", command=self.send_message)
        self.send_button.pack()
        self.exit_button = tk.Button(root, text="EXIT", command=root.destroy)
        self.exit_button.pack()

    def send_message(self):
        user_message = self.user_input.get("1.0", tk.END).strip()
        self.user_input.delete("1.0", tk.END)

        if user_message.lower() == 'exit':
            self.root.destroy()

        self.display_message("USER:", user_message, "blue")

        self.root.after(1000, self.process_chatgpt_response)

    def process_chatgpt_response(self):
        chatgpt_response = self.get_chatgpt_response("request")
        self.display_message("ChatGPT:", chatgpt_response, "red")

    def get_chatgpt_response(self, user_message):
        response = openai.Completion.create(
            engine=model_engine,
            prompt=user_message,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response["choices"][0]["text"]

    def display_message(self, sender, message, color):
        self.chat_history.tag_configure(sender, foreground=color, font=("Arial", 10, "italic"))
        self.chat_history.insert(tk.END, f"{sender} {message}\n", sender)
        self.chat_history.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatGPTApp(root)
    root.mainloop()
