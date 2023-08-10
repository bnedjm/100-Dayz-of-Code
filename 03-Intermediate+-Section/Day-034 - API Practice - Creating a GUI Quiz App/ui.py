from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_TPL = ("Arial", 16, "italic")


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window

        self.window = Tk()
        self.window.title("Quiz Game!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label

        self.label_score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.label_score.grid(column=1, row=0)

        # Canvas

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.text_question = self.canvas.create_text(
            150,
            125,
            width=260,
            text="",
            fill=THEME_COLOR,
            font=FONT_TPL
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Button

        img_right = PhotoImage(file="./images/true.png")
        self.button_right = Button(
            image=img_right,
            width=100,
            height=100,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.true_clicked
        )
        self.button_right.grid(column=1, row=2)

        img_wrong = PhotoImage(file="./images/false.png")
        self.button_wrong = Button(
            image=img_wrong,
            width=100,
            height=100,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.false_clicked
        )
        self.button_wrong.grid(column=0, row=2)

        self.button_replay = Button(
            text="RePlay",
            width=20,
            highlightthickness=0,
            bg=THEME_COLOR,
            fg="white",
            state="disabled",
            command=self.replay
        )
        self.button_replay.grid(column=0, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.label_score.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_question, text=question_text)
        else:
            self.canvas.itemconfig(self.text_question,
                                   text=f"You've completed the quiz\n"
                                        f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.button_replay.config(state="active")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(500, self.get_next_question)

    def replay(self):
        self.quiz.reset()
        self.button_replay.config(state="disabled")
        self.button_right.config(state="normal")
        self.button_wrong.config(state="normal")
        self.get_next_question()
