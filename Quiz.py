import tkinter as tk
from tkinter import messagebox

# Quizvragen en antwoorden
quiz_questions = [
    {"question": "Is Python een programmeertaal?", "answer": "ja", "type": "yesno"},
    {"question": "Wat is 2 + 2?", "answer": "4", "type": "open"},
    {"question": "Welke taal wordt gebruikt voor webontwikkeling?", "answer": "HTML", "type": "multiple", "options": ["Python", "HTML", "Java"]},
    {"question": "Wat is de hoofdstad van Frankrijk?", "answer": "Parijs", "type": "open"},
    {"question": "Is 10 groter dan 5?", "answer": "ja", "type": "yesno"},
    {"question": "Welke planeet staat het dichtst bij de zon?", "answer": "Mercurius", "type": "open"},
    {"question": "Hoeveel benen heeft een spin?", "answer": "8", "type": "open"},
    {"question": "Wat is de binaire representatie van 2?", "answer": "10", "type": "open"}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        
        self.question_index = 0
        self.score = 0
        
        self.label = tk.Label(root, text="", font=("Arial", 14))
        self.label.pack(pady=20)
        
        self.answer_entry = tk.Entry(root, font=("Arial", 14))
        self.yes_button = tk.Button(root, text="Ja", command=lambda: self.check_answer("ja"))
        self.no_button = tk.Button(root, text="Nee", command=lambda: self.check_answer("nee"))
        self.option_buttons = []
        
        self.submit_button = tk.Button(root, text="Antwoord verzenden", command=lambda: self.check_answer(self.answer_entry.get().strip()))
        
        self.show_question()
        
    def show_question(self):
        for btn in self.option_buttons:
            btn.pack_forget()
        self.answer_entry.pack_forget()
        self.yes_button.pack_forget()
        self.no_button.pack_forget()
        self.submit_button.pack_forget()
        
        question = quiz_questions[self.question_index]
        self.label.config(text=question["question"])
        
        if question["type"] == "yesno":
            self.yes_button.pack()
            self.no_button.pack()
        elif question["type"] == "multiple":
            self.option_buttons = []
            for option in question["options"]:
                btn = tk.Button(self.root, text=option, command=lambda opt=option: self.check_answer(opt))
                btn.pack()
                self.option_buttons.append(btn)
        else:
            self.answer_entry.pack()
            self.submit_button.pack()
        
    def check_answer(self, answer):
        correct_answer = quiz_questions[self.question_index]["answer"].lower()
        
        if answer.lower() == correct_answer:
            self.score += 1
            messagebox.showinfo("Resultaat", "Correct!")
        else:
            messagebox.showinfo("Resultaat", f"Fout! Het juiste antwoord is: {correct_answer}")
        
        self.question_index += 1
        if self.question_index < len(quiz_questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz voltooid", f"Je eindscore is: {self.score}/{len(quiz_questions)}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
