 
# Importation des modules nécessaires
import tkinter as tk

# Création de la fenêtre principale
fenetre = tk.Tk()

# Ajout d'un titre à la fenêtre
fenetre.title("Ma fenêtre")

# Définition de la taille de la fenêtre
fenetre.geometry("500x500")

# Ajout d'un label à la fenêtre
label = tk.Label(fenetre, text="Semabox", font=("Arial", 32))
label.pack()



 
# Création des 3 rectangles
rectangle1 = tk.Canvas(fenetre, width=250, height=500, bg="white", highlightthickness=2, highlightbackground="gray")
rectangle1.create_text(125, 20, text="Scan de port", font=("Arial", 16))

bouton1 = tk.Button(rectangle1, text="Scan de Machine")
bouton1.place(x=75, y=100)

bouton2 = tk.Button(rectangle1, text="Scan de port")
bouton2.place(x=75, y=150)

bouton3 = tk.Button(rectangle1, text="Effacer")
bouton3.place(x=75, y=200)

rectangle1.pack(side="left")



rectangle2 = tk.Canvas(fenetre, width=250, height=250, bg="white", highlightthickness=2, highlightbackground="gray")
rectangle2.pack(side="top", fill="x")
 
rectangle2.create_text(125, 20, text="Information", font=("Arial", 16))
 
rectangle2.create_text(125, 100, text="IP : \nDNS : 8.8.8.8\nHost name : mycomputer", font=("Arial", 12))





rectangle3 = tk.Canvas(fenetre, width=250, height=250, bg="white", highlightthickness=2, highlightbackground="gray")
rectangle3.pack(side="bottom", fill="x")

 
bouton4 = tk.Button(rectangle3, text="Speedtest")
bouton4.place(x=75, y=100)


 
rectangle3.create_text(125, 20, text="Speedtest", font=("Arial", 16))




# Boucle principale de la fenêtre
fenetre.mainloop()
 


