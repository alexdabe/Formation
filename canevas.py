import tkinter

t = 0
i = 0

def appuie(event):
    print("Appui sur la touche", event.char)
    global i, t
    i = i + 1
    t = t + 1
    print(i, t)
    graphique.create_line((t-1)*3, 120-(i-1)*(i-1), t*3, 120-i*i)
    # graphique.create_line((t-1)*3, (i-1)*(i-1), t*3, i*i)

fenetre = tkinter.Tk()

fenetre.geometry("300x300")
fenetre.title("Ma fenêtre")
fenetre.bind("<KeyPress-a>", appuie)
etiquette = tkinter.Label(fenetre, text= "Appuiez sur a") # création d'une étiquette
etiquette.grid(row=0, column = 0)
graphique = tkinter.Canvas(fenetre, width=150, height=120, background='yellow') # création d'un canevas
graphique.grid(row=1, column=0)
ligne1 = graphique.create_line(75, 0, 75, 120) # création d'une ligne verticale
ligne2 = graphique.create_line(0, 60, 150, 60) # création d'une ligne horizontale
# rectangle = graphique.create_rectangle(75, 60, 125, 110, fill='red') # création d'un rectangle
rectangle = graphique.create_rectangle(50, 35, 100, 85, fill='red')
base = 50
hauteur = 50
centre_x = 75
centre_y = 60
rectangle = graphique.create_rectangle(centre_x - base/2, centre_y - hauteur/2, centre_x + base/2, centre_y + hauteur/2, fill='red')
fenetre.mainloop()