from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
class Interface():
    def __init__(self):
        self.window = Tk(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.window.title(text="Flashy")
        self.flash_card = Canvas(image="./images/card_front.png", width=800, height=526, bg=BACKGROUND_COLOR)
        self.card_image = PhotoImage(image="./images/card_front.png")
        self.flash_card.create_image(400, 268,image=self.card_image)
        self.french_text = self.flash_card.create_text(400, 150)