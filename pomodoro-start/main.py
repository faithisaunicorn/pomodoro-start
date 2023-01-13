from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text = "Timer")
    check_marks.config(text= "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
#display in minutes and seconds

def start_timer():
    global reps
    reps += 1
    if reps%8 == 0:
        countdown(LONG_BREAK_MIN*60)
        title.config(text = "Long Break", fg = RED)
    elif reps%2 == 0:
        countdown(SHORT_BREAK_MIN*60)
        title.config(text = "Short Break", fg = PINK)
    else:
        countdown(WORK_MIN*60)
        title.config(text = "Work", fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = round((math.floor(count%60)),2)

    if count_sec < 10: #troubleshooting for display xx:9 instead of xx:09
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>-1:
        global timer
        timer = window.after(1000, countdown, count-1)
        # 1000 milliseconds
        # accepts multiple args
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato Timer")
window.config(padx = 150, pady = 80, bg = YELLOW)

###Canvas is the tomato pic
canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness = 0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="yellow", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

#Title
title = Label(text="Timer", font=(FONT_NAME,50,"italic"), bg = YELLOW)
title.grid(column=2, row=1)

#Check marks
check_marks = Label(text="", font=(FONT_NAME,50,"italic"), fg = GREEN, bg = YELLOW)
check_marks.grid(column=2, row=4)

#Buttons
start_button = Button(text="Start", command=start_timer, highlightthickness = 0)
start_button.grid(column = 1, row = 3)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness = 0)
reset_button.grid(column = 3, row = 3)




window.mainloop()