import requests
from tkinter import *
import html
url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

headers = {
    'accept': "application/json",
    'x-rapidapi-key': "af97540220msh7ff7ff47eb8b851p1ca53djsnd66b8a103f8e",
    'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }
def quote():
    quiz =  html.unescape(requests.request("GET", url, headers=headers).json()["value"])
    cani.itemconfig(t, text=quiz)
window = Tk()
window.config(width=400, height=600, pady=20, padx=20, bg="#0F3057")
cani = Canvas(width=200, height=300, bg="#e7d9ea")
PIC = PhotoImage(file='chuck.png')
t = cani.create_text(100, 150, text="Chuck do karate", width=180, fill='#222831', font=("Arial", 14, "italic"))
cani.grid(column=0, row=0)
button = Button(image = PIC,
                    command = quote)
button.grid(column=0, row=1)
window.mainloop()