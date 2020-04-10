import tkinter
import random

# function load_images
def load_images(card_images):
    suits=["heart","club","diamond","spade"]
    face_cards=["jack","queen","king"]
    extension='png'
    for suit in suits:
        for card in range(1,10):
            name= "BLACKJACK\cards\{}_{}.{}".format(str(card),suit,extension)
            image= tkinter.PhotoImage(file=name)
            card_images.append((card,image))

        for card in face_cards:
            name= "BLACKJACK\cards\{}_{}.{}".format(str(card),suit,extension)
            image= tkinter.PhotoImage(file=name)
            card_images.append((10,image))


def deal_cards(frame):
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    return next_card


def shuffle():
    random.shuffle(deck)

def score_hand(hand):
    score=0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value= 11
        score += card_value
        if score >21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_cards(dealer_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        res_text.set("Dealer wins")
    elif dealer_score >21 or dealer_score <player_score:
        res_text.set("Player wins")
    elif dealer_score > player_score:
        res_text.set("Dealer wins")
    else:
        res_text.set("Draw")


def deal_player():
    player_hand.append(deal_cards(player_frame))
    player_score = score_hand(player_hand)
    player_label.set(player_score)

    if player_score >21:
        res_text.set("Dealer wins ")

    # global player_score
    # global player_ace
    # card_value= deal_cards(player_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace= True
    #     card_value= 11
    # player_score += card_value
    # if player_score > 21 and player_ace:
    #     player_ace= False
    #     player_score -= 10
    # player_label.set(player_score)
    # if player_score >21:
    #     res_text.set("Dealer wins")
    print(locals()) 
def  new_game():
    global dealer_frame
    global player_frame
    global dealer_hand
    global player_hand

    dealer_frame.destroy()
    dealer_frame = tkinter.Frame(card_frame, background="green")
    dealer_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_frame = tkinter.Frame(card_frame, background="green")
    player_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    res_text.set("")

    dealer_hand=[]
    player_hand=[]

    deal_player()
    dealer_hand.append(deal_cards(dealer_frame))
    dealer_label.set(score_hand(dealer_hand))
    deal_player()



mainWindow = tkinter.Tk()
mainWindow.title("Black jack")
mainWindow.geometry("640x480")
mainWindow.configure(background="grey")

res_text= tkinter.StringVar()
res = tkinter.Label(mainWindow, textvariable= res_text)
res.grid(row=0, column=0, columnspan=3)

card_frame= tkinter.Frame(mainWindow, relief= "sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_label= tkinter.IntVar()
tkinter.Label(card_frame, text= "Dealer", background="green", fg="white",).grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_label, background="green", fg="white").grid(row=1,column=0)

dealer_frame= tkinter.Frame(card_frame, background="green")
dealer_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_label= tkinter.IntVar()
# player_score= 0
# player_ace= False

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_label, background="green", fg="white").grid(row=3, column=0)

player_frame= tkinter.Frame(card_frame, background="green")
player_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

but_frame= tkinter.Frame(mainWindow)
but_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_but= tkinter.Button(but_frame, text="Dealer", command=deal_dealer)
dealer_but.grid(row=0, column=0)

palyer_but= tkinter.Button(but_frame, text="Player", command=deal_player)
palyer_but.grid(row=0, column=1)

new_game_but= tkinter.Button(but_frame, text="New Game", command=new_game)
new_game_but.grid(row=0, column=2)

shuffle_but= tkinter.Button(but_frame, text= "Shuffle", command= shuffle)
shuffle_but.grid(row=0, column=3)

cards= []
load_images(cards)
print(cards)

deck = list(cards)
dealer_hand= []
player_hand= []

new_game()

mainWindow.mainloop()

