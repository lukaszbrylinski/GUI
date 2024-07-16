import pandas
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
timer = None
current_card = {}


def next_word_correct():
    global timer, current_card
    if timer is not None:
        window.after_cancel(timer)
    # cur_index = random.randint(0,len(df)-1)
    # cur_word = df[cur_index]["French"]
    current_card = random.choice(words_to_learn)
    flash_card.itemconfig(language_name,text="French", fill="black")
    flash_card.itemconfig(language_word, text=current_card["French"], fill="black")
    flash_card.itemconfig(flashy,image=card_front_image)
    # window.after(3000,     change_card(cur_index))

    timer = window.after(3000, lambda:change_card(current_card))
    # window.after_cancel(timer)
    words_to_learn.remove(current_card)
    new_words = pandas.DataFrame(words_to_learn)
    new_words.to_csv("./data/words_to_learn.csv", index=False)


def next_word_incorrect():
    global timer, current_card
    if timer is not None:
        window.after_cancel(timer)
    # cur_index = random.randint(0,len(df)-1)
    # cur_word = df[cur_index]["French"]
    current_card = random.choice(words_to_learn)
    flash_card.itemconfig(language_name,text="French", fill="black")
    flash_card.itemconfig(language_word, text=current_card["French"], fill="black")
    flash_card.itemconfig(flashy,image=card_front_image)
    # window.after(3000,     change_card(cur_index))

    timer = window.after(3000, lambda:change_card(current_card))
    # window.after_cancel(timer)


def change_card(chosen_card):
    flash_card.itemconfig(language_name, text="English", fill="white")
    flash_card.itemconfig(flashy, image=card_back_image)
    flash_card.itemconfig(language_word, text=chosen_card["English"], fill="white")


try:
    data = pandas.read_csv("./data/words_to_learn.csv")

except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    dataf = pandas.DataFrame(data)
else:
    dataf = pandas.DataFrame(data)
# print(random.choice(df))
finally:
    words_to_learn = dataf.to_dict(orient="records")


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
flashy = flash_card.create_image(400, 268, image=card_front_image)
flash_card.grid(column=0, row=0, columnspan=2)

language_name = flash_card.create_text(400, 150, text="French", font=("Ariel",40, "italic"))
language_word = flash_card.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

incorrect_image = PhotoImage(file="./images/wrong.png")
incorrect_button = Button(image=incorrect_image, highlightthickness=0, command=next_word_incorrect)
incorrect_button.grid(column=0, row=1)

correct_image = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0,command=next_word_correct)
correct_button.grid(column=1, row=1)


next_word_incorrect()


window.mainloop()