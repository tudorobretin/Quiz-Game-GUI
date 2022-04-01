import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUi():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quizzler")
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white", highlightthickness=False)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=250,
            text=f" ",
            fill="black",
            font=("Arial", 16, "italic")
        )

#Score-------------------------------------------------

        self.score_label = tkinter.Label(text=f"Score: 0",
                                         bg=THEME_COLOR,
                                         fg="white",
                                         font=("Arial", 14, "bold")
                                         )
        self.score_label.grid(row=0, column=1)

#Buttons--------------------------------------------------
        correct = tkinter.PhotoImage(file="images/true.png")
        self.correct_button = tkinter.Button(image=correct, highlightthickness=False, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)

        incorrect = tkinter.PhotoImage(file="images/false.png")
        self.incorrect_button = tkinter.Button(image=incorrect, highlightthickness=False, command=self.false_pressed)
        self.incorrect_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.configure(bg="white")
            self.canvas.itemconfig(self.question_text, text= q_text)

        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz!\n\n{self.quiz.score}/10")
            self.correct_button.config(state="disabled")
            self.incorrect_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            print("right")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(600, self.get_next_question)









