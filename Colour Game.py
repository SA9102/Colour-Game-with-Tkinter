from tkinter import *
import time
import threading
import random
from playsound import playsound

root = Tk()

BUTTON_BG = "#383838"
BUTTON_TEXT_STYLE = "Calibri 11 bold"
BUTTON_WIDTH = 7
r_c = 0

colour_texts = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink"]
colours = ["#ff3d3d", "#ff7b1c", "#fff04f", "#43d948", "#30f8ff", "#4058de", "#875ad1", "#e048d4"]
seconds = 30

def playSound():
    playsound('Incorrect.wav')

# a procedure that changes the text and its colour, if a button is pressed
def displayText(button_id):
    global seconds
    print(seconds)
    if seconds >= 1:
        global colour_texts
        global colours
        global r_c
        global score
        # if the button id (the colour of the button in hex) does not match the colour of the text
        if button_id != colours[r_c]:
            # if the game is not yet over
            if seconds != 30:
                sound = threading.Thread(target=playSound)
                sound.start()
        else:
            global score_text
            score += 1
            score_text['text'] = 'Score: ' + str(score)
            
        # (r_ct: random colour text) choose a random word from the list to be displayed
        r_ct = random.randint(0, len(colour_texts)-1)
        # (r_c: random colour) choose a random colour from the list to colour the text
        r_c = random.randint(0, len(colours)-1)
        display_text.config(text=colour_texts[r_ct], fg=colours[r_c])

# a procedure that handles the timer
def changeTime():
    global timer
    global seconds
    global game_end_text
    while seconds > -1:
        timer['text'] = 'Timer: ' + str(seconds)
        seconds -= 1
        time.sleep(1)
    game_end_text.pack(side=LEFT)

display_frame = Frame(root, width=350, height=200, bg="#4a4a4a", pady=50)
display_frame.pack(fill=X)

buttons_frame = Frame(root,width=350,height=100, bg="#4a4a4a", padx=100)
buttons_frame.pack(fill=X)

timer_frame = Frame(root, width=100,height=20, bg="red")
timer_frame.pack(side=LEFT, fill=X)



# defining and adding buttons
red = Button(buttons_frame, text="Red", fg="white", bg=BUTTON_BG, font=BUTTON_TEXT_STYLE, width=BUTTON_WIDTH, command=lambda: displayText("#ff3d3d"))
red.grid(row=0)
orange = Button(buttons_frame, text="Orange", fg="white", bg=BUTTON_BG, font=BUTTON_TEXT_STYLE, width=BUTTON_WIDTH, command=lambda: displayText("#ff7b1c"))
orange.grid(row=1)
yellow = Button(buttons_frame, text="Yellow", fg="white", bg=BUTTON_BG, font=BUTTON_TEXT_STYLE, width=BUTTON_WIDTH, command=lambda: displayText("#fff04f"))
yellow.grid(row=2)
green = Button(buttons_frame, text="Green", fg="white", bg=BUTTON_BG, font=BUTTON_TEXT_STYLE, width=BUTTON_WIDTH, command=lambda: displayText("#43d948"))
green.grid(row=3)
cyan = Button(buttons_frame, text="Cyan", fg="white", bg=BUTTON_BG, font=BUTTON_TEXT_STYLE, width=BUTTON_WIDTH, command=lambda: displayText("#30f8ff"))
cyan.grid(row=0, column=1)
blue = Button(buttons_frame, text="Blue", fg="white", bg=BUTTON_BG, font=BUTTON_TEXT_STYLE, width=BUTTON_WIDTH, command=lambda: displayText("#4058de"))
blue.grid(row=1, column=1)
purple = Button(buttons_frame, text="Purple", fg="white", bg=BUTTON_BG, font=BUTTON_TEXT_STYLE, width=BUTTON_WIDTH, command=lambda: displayText("#875ad1"))
purple.grid(row=2, column=1)
pink = Button(buttons_frame, text="Pink", fg="white", bg=BUTTON_BG, font=BUTTON_TEXT_STYLE, width=BUTTON_WIDTH, command=lambda: displayText("#e048d4"))
pink.grid(row=3, column=1)


display_text = Label(display_frame, text="", bg="#4a4a4a", fg="black", font="Calibri 50 bold")
display_text.pack()

# timer
timer = Label(timer_frame, text="Timer: ")
timer.pack(side=LEFT)

# score
score_text = Label(timer_frame, text="Score: 0", padx=20)
score_text.pack(side=LEFT)

# message that the game as ended
game_end_text = Label(timer_frame, text="GAME ENDED", padx=20)

score = 0

# call subroutine, passing in an empty string as an argument
displayText("")

# we include threading so that we can still interact with the program while the timer is on
t = threading.Thread(target=changeTime)
t.start()

    

root.mainloop()
