import random
import tkinter as tk
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from tkinter import messagebox

def gamewin(comp, you):
    if comp == you:
        return "It's a tie!"
    elif comp == 'rock':
        return "You win!" if you == 'paper' else "You lose!"
    elif comp == 'paper':
        return "You win!" if you == 'scissors' else "You lose!"
    elif comp == 'scissors':
        return "You win!" if you == 'rock' else "You lose!"
    

def play_game():
    you = choice_var.get()
    if not you:
        result_label.config(text="Please select an option", font=20)
        return

    randno = random.choice(['rock', 'paper', 'scissors'])
    you_label.config(text=f"You chose: {you}")
    comp_label.config(text=f"Computer chose: {randno}")
    result = gamewin(randno, you)
    Result_Message=messagebox.showinfo(" Result ",result, )
        
    result_label.config(text=result, font=20)
    choice_var.set("")

# Create the main window
root = tk.Tk()
ttk.Style(theme="superhero")
root.geometry("500x400")
root.resizable(width=False, height=False)
root.title("Rock-Paper-Scissors Game")

# Load images
rock_img = Image.open("Images/Rock.jpg").resize((100, 100))
paper_img = Image.open("Images/Paper.jpg").resize((100, 100))
scissors_img = Image.open("Images/Scissors.jpg").resize((100, 100))

# Convert PIL Images to PhotoImage
rock_img = ImageTk.PhotoImage(rock_img)
paper_img = ImageTk.PhotoImage(paper_img)
scissors_img = ImageTk.PhotoImage(scissors_img)

# Create and configure widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(ttk.W, ttk.E, ttk.N, ttk.S))

choice_var = tk.StringVar()
choices = ['rock', 'paper', 'scissors']

# Radio buttons with images for user choice
for choice in choices:
    img = rock_img if choice == 'rock' else paper_img if choice == 'paper' else scissors_img
    ttk.Radiobutton(frame, image=img, variable=choice_var, value=choice).pack(side=tk.LEFT, padx=10,pady=20)

# Play button
play_button = ttk.Button(frame, text="Play", command=play_game)
play_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Labels to display results
you_label = ttk.Label(root, text="You have chosen: ",font=("calibri",16))
you_label.grid(row=3, column=0, pady=20)
comp_label = ttk.Label(root, text="Computer chose: ",font=("calibri",16))
comp_label.grid(row=2, column=0, pady=20)
result_label = ttk.Label(root, text="",font=("NewTimesRoman"))
result_label.grid(row=4, column=0, pady=20)

# Run the main loop
root.mainloop()
