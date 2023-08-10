from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_reps():
    global reps
    reps = 0


def reset_timer():
    # Start timer to give var timer a value | Otherwise, pressing reset without starting generate an error
    # None instead of str
    start_timer()
    # resetting to initial state
    window.after_cancel(timer)
    reset_reps()
    canvas.itemconfig(text_timer, text=f"{0:02d}:{0:02d}")
    label_timer.config(text="TIMER", fg=GREEN)
    check_marks.set("")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps == 7:
        reset_timer()

    elif reps % 2 == 1 and reps < 6:
        count_down(60*WORK_MIN)
        label_timer.config(text="WORK", fg=GREEN)

    elif reps % 2 == 0 and reps < 6:
        count_down(60*SHORT_BREAK_MIN)
        label_timer.config(text="SHORT BREAK", fg=PINK)

    else:
        count_down(60*LONG_BREAK_MIN)
        label_timer.config(text="LONG BREAK", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer

    min_ = math.floor(count / 60)
    sec_ = count % 60

    canvas.itemconfig(text_timer, text=f"{min_:02d}:{sec_:02d}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0 and reps != 0:
            tmp = check_marks.get()
            tmp += "✅"
            check_marks.set(tmp)
            label_check_marks.config(textvariable=check_marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

img_png = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=img_png)
text_timer = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

# Label

label_timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label_timer.grid(column=1, row=0)

check_marks = StringVar()
check_marks.set("")

label_check_marks = Label(textvariable=check_marks, bg=YELLOW, fg=GREEN)
label_check_marks.grid(column=1, row=3)

# Button

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

window.mainloop()
