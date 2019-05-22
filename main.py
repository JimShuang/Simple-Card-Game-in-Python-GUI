import tkinter as tk
from tkinter import messagebox
import os
import poker

image_path = r'****directory to where you save Card Image****'
balance = 1000
b = 0
w = 0

decks = poker.deck(4)
decks.shuffle_deck(3)

window = tk.Tk()
window.title('Card Game')
window.geometry('600x400')

canvas = tk.Canvas(window, height=200, width=600)

canvas.pack()

def play():
    global balance, b, w
    if b == 0:
        messagebox.showwarning("Warning", "Please make a bet.")
        return

    suit_dealer, value_dealer = decks.get_card().get_info()
    suit_player, value_player = decks.get_card().get_info()
    image_dealer_name = value_dealer + '_of_' + suit_dealer + '.png'
    image_player_name = value_player + '_of_' + suit_player + '.png'
    dealer_path = os.path.join(image_path, image_dealer_name)
    player_path = os.path.join(image_path, image_player_name)
    image_dealer = tk.PhotoImage(file=dealer_path).subsample(2, 2)
    image_player = tk.PhotoImage(file=player_path).subsample(2, 2)
    canvas.image = image_dealer, image_player
    image1 = canvas.create_image(160, 0, anchor='n', image=image_dealer)
    image2 = canvas.create_image(440, 0, anchor='n', image=image_player)

    values = {
        'ace': 14,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'jack': 11,
        'queen': 12,
        'king': 13
    }

    if values[value_player] > values[value_dealer]:
        w = 2 * b
        balance += w
        b = 0
        messagebox.showinfo("Results", "You win.")
    elif values[value_player] == values[value_dealer]:
        w = b
        balance += w
        b = 0
        messagebox.showinfo("Results", "Even.")
    else:
        w = 0
        b = 0
        messagebox.showinfo("Results", "You lose.")
    bet.set(str(b))
    bal.set(str(balance))
    win.set(str(w))

label_frm = tk.Frame(window)
label_frm.pack(side='top')
dealer_frm = tk.Frame(label_frm)
dealer_frm.pack(side='left', padx=100, pady=10)
tk.Label(dealer_frm, text = 'Dealer').pack()
player_frm = tk.Frame(label_frm)
player_frm.pack(side='left', padx=100, pady=10)
tk.Label(player_frm, text = 'Player').pack()

tk.Button(window, text='Play', command=play).pack(side='top', padx=10)



bottom_frm = tk.Frame(window)
bottom_frm.pack(side='bottom')
bet_frm = tk.Frame(bottom_frm)
bet_frm.pack(side='bottom')
balance_frm = tk.Frame(bet_frm)
balance_frm.pack(side='left', padx=50, pady=10)
totalbet_frm = tk.Frame(bet_frm)
totalbet_frm.pack(side='left', padx=50, pady=10)
win_frm = tk.Frame(bet_frm)
win_frm.pack(side='left', padx=50, pady=10)
wager_frm = tk.Frame(bottom_frm)
wager_frm.pack(side='top')

def make_bet(v):
    global b, balance
    b += v
    balance -= v
    bet.set(str(b))
    bal.set(str(balance))

def rebet():
    global b, balance
    balance += b
    b = 0
    bet.set(str(b))
    bal.set(str(balance))

tk.Button(wager_frm, text='1', command=lambda *args: make_bet(1)).pack(side='left', padx=10)
tk.Button(wager_frm, text='5', command=lambda *args: make_bet(5)).pack(side='left', padx=10)
tk.Button(wager_frm, text='10', command=lambda *args: make_bet(10)).pack(side='left', padx=10)
tk.Button(wager_frm, text='25', command=lambda *args: make_bet(25)).pack(side='left', padx=10)
tk.Button(wager_frm, text='50', command=lambda *args: make_bet(50)).pack(side='left', padx=10)
tk.Button(wager_frm, text='Rebet', command=rebet).pack(side='left', padx=30)

tk.Label(balance_frm, text = 'Balance', bg='orange').pack()
bal = tk.StringVar()
bal.set(str(balance))
tk.Label(balance_frm, textvariable=bal).pack()

tk.Label(totalbet_frm, text = 'Bet', bg='orange').pack()
bet = tk.StringVar()
bet.set(str(b))
tk.Label(totalbet_frm, textvariable=bet).pack()

tk.Label(win_frm, text = 'Win', bg='orange').pack()
win = tk.StringVar()
win.set(str(w))
tk.Label(win_frm, textvariable=win).pack()

window.mainloop()
