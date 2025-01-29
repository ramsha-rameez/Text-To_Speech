import pyttsx3
import tkinter as tk
from tkinter import scrolledtext

engine = pyttsx3.init()

root = tk.Tk()
root.title("Text-to-Speech App")

# Styling
root.configure(bg="#f0f0f0")
font = ("Arial", 12)

# Input Text Area
tk.Label(root, text="Enter text:", font=font, bg="#f0f0f0").pack(pady=(10, 0))

input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=font, bg="white", height=10)
input_text.pack(pady=(5, 10))

# Speak Button (Combined function)
def speak_and_exit():
    text = input_text.get("1.0", tk.END).strip()
    if text.lower() == 'exit':
        root.destroy()
    elif text:
        engine.say(text)
        engine.runAndWait()

tk.Button(root, text="Speak", command=speak_and_exit, font=font, bg="#4CAF50", fg="white").pack()

# Exit Label
tk.Label(root, text="Type 'exit' in the text box to quit.", font=font, bg="#f0f0f0").pack(pady=(10,10))

root.mainloop()