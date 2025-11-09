import tkinter as tk
import random

root = tk.Tk()
root.title("Magic 8 Ball")
root.geometry("400x300")

title_label = tk.Label(root, text="Magic 8 Ball", font=("Arial", 20))
title_label.pack(pady=10)

question_label = tk.Label(root, text="Ask a yes/no question")
question_label.pack(pady=5)

question_entry = tk.Entry(root, width=30, justify="center")
question_entry.pack(pady=5)

answer_label = tk.Label(root, text="", font=("Arial", 16))
answer_label.pack(pady=20)

answers = ["Yes!", "No!", "Maybe...", "Ask again later", "Definitely", "I dont't think so", "Try again", "Absolutely"]

def give_answer():
    question = question_entry.get().strip()
    if question == "":
        answer_label.config(text="Please type a question.")
        return
    reply = random.choice(answers)
    answer_label.config(text=reply)

ask_btn = tk.Button(root, text="Ask", width=12)
ask_btn.pack(pady=5)

def ask_pressed():
    give_answer()

ask_btn.config(command=ask_pressed)

root.mainloop()