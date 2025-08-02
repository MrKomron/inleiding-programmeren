from window import *

class game(window):  # overerving in Python; game erft over van window
    def __init__(self,n):
        super().__init__(n,n)
        self.n=n
        for r in range(n):
            for c in range(n):
                self.change_button_label(r,c," ")    # verander het label van de button op rij r en kolom c

    # Deze functie zal uitgevoerd worden telkens wanneer op een button geklikt wordt
    # De positie van die button is rij row en kolom col
    def button_clicked(self, row, col):
        display("Clicked "+str((row,col))+" current content of this tile: "+str(self.get_button_label(row,col)))

    # Deze functie wordt aangeroepen als in het menu "Validate" gekozen wordt
    def validate(self):
        display("validate")

    # Deze functie wordt aangeroepen als in het menu "Autofill" gekozen wordt
    def autofill(self):
        display("autofill")

    # Deze functie laad een bord in.
    # In opgave 2 moet je deze functie debuggen
    # De functie bevat een syntactische en een logische fout
    # Corrigeer beiden zodat het bestand correct wordt ingelezen
    def load_board(self,boardFile):

        # inlezen van het bestannd
        f=open(boardFile,"r")  # Open het bestand om te lezen
        board=[]  # we gaan eerst het bestand inlezen in de datastructuur board (een lijst van lijsten)
        rij=[]    # In deze lijst lezen we een voor een de rijen in
        for line in f:   # loop over alle lijnen in het bestand
            rij.clear()  # maak de rij eerst leeg (nodig voor alle rijen behalve de eerste)
            line=line.strip()   # Haal overtollige symbolen weg (bvb de newline "\n" op het einde van de lijn)
            for element in line:   # ga een voor een de symbolen in de lijn af
                rij.append(element)   # voeg het symbool toe aan de rij
            board.append(rij)   # voeg de rij toe aan het bord

        # Voorbereiden van het canvas
        self.newCanvas(len(board),len(board))  # resize het canvas; breedte en hoogte = aantal rijen in board
                                               # je mag ervan uitgaan dat het aantal rijen steeds gelijk is aan
                                               # het aantal kolommen; hier zit de fout NIET.
        self.n = len(board)  # bewaar de dimensies van het bord

        # Overbrengen van de inhoud van het bord op het canvas
        for i in range(len(board)): # loop de rijen van het bord af
            for j in board[i]:  # en de kolommen
                if board[i][j]==".":   # als er een punt in het bestand stond
                    self.change_button_label(i,j," ")  # dan is dit een nog niet ingevulde cel
                else:   # anders staat er 0 of 1 (mag je vanuit gaan; dit is NIET de fout)
                    self.change_button_label(i, j, (board[i][j]))   # verander het label van de button
                                                                       # naar de gegeven waarde
                    self.disable_button(i,j) # Zet de button op non-actief; deze waarde is gegeven, dus die kan niet
                                             # gewijzigd worden

    # Deze functie wordt aangeroepen als in het menu "Load" een van de opgaves geselecteerd wordt.
    # i is het nummer van die opgave
    def load(self,i):
        self.load_board("opgave"+str(i)+".txt")

    def getRow(self, rijnummer):
        rij=[]
        for kolom in range(self.n):
            waarde=self.get_button_label(rijnummer, kolom)
            rij.append(waarde)
        return rij

    def getColumn(self, kolomnummer):
        kolom=[]
        for rij in range(self.n):
            waarde=self.get_button_label(rij, kolomnummer)
            kolom.append(waarde)
        return kolom

    def setRow(self, rijnummer, nieuwe_rij):
        for c in range(self.n):
            self.change_button_label(rijnummer, c, nieuwe_rij[c])

    def setColumn(self, kolomnummer, nieuwe_kolom):
        for r in range(self.n):
            self.change_button_label(r, kolomnummer, nieuwe_kolom[r])


# # testcode voor vraag 1
spel=game(4)
spel.change_button_label(0, 0, "1")
spel.change_button_label(0, 2, "0")
spel.change_button_label(1, 1, "1")
spel.change_button_label(1, 2, "0")
spel.change_button_label(1, 3, "0")
spel.change_button_label(2, 3, "0")
spel.change_button_label(3, 2, "1")

for i in range(4):
    R=spel.getRow(i)
    R[i]="1"
    spel.setRow(i,R)

for i in range(4):
    R=spel.getColumn(i)
    print(R)

print(spel.getRow(1))
spel.setColumn(1,[" "," "," "," "])
print(spel.getRow(1))

# # Testcode voor vraag 2
# spel=game(4)
# spel.change_button_label(0, 0, "1")
# spel.change_button_label(0, 2, "0")
# spel.change_button_label(1, 1, "1")
# spel.change_button_label(1, 2, "0")
# spel.change_button_label(1, 3, "0")
# spel.change_button_label(2, 3, "0")
# spel.change_button_label(3, 2, "1")
# spel.mainloop()

# # Testcode voor vraag 3a
# spel=game(4)
# print(violation(["0","0","0","1"])) # drie maal 0 na elkaar
# print(violation(["0","0","1","1"])) # in orde
# print(violation(["0","0","1","0"])) # te veel nullen (3 > lengte van de lijst gedeeld door 2
# print(violation([" "," "," ","1"])) # in orde; spaties zijn nog niet ingevulde vakken
# print(violation(["0"," ","1","1"])) # in orde; spaties zijn nog niet ingevulde vakken
# print(violation(["1","1"," ","1"])) # niet in orde; te veel enen

# # testcode voor vraag 3b
# spel=game(4)
# spel.change_button_label(0, 0, "1")
# spel.change_button_label(0, 2, "0")
# spel.change_button_label(1, 1, "1")
# spel.change_button_label(1, 2, "0")
# spel.change_button_label(1, 3, "0")
# spel.change_button_label(2, 3, "0")
# spel.change_button_label(3, 2, "1")
# print(spel.violatingRows())
# print(spel.violatingColumns())
#
# spel.change_button_label(0, 3, "0")
# spel.change_button_label(2, 0, "1")
# spel.change_button_label(3, 0, "1")
# spel.change_button_label(3, 3, "1")
# print(spel.violatingRows())
# print(spel.violatingColumns())

# # testcode voor vraag 3c
# spel=game(4)
# spel.change_button_label(0, 0, "1")
# spel.change_button_label(0, 2, "0")
# spel.change_button_label(1, 1, "1")
# spel.change_button_label(1, 2, "0")
# spel.change_button_label(1, 3, "0")
# spel.change_button_label(2, 3, "0")
# spel.change_button_label(3, 2, "1")
# spel.mainloop()

# # Testcode voor 4a,b,c,d
# L=["0","0"," ", "1"," "," "]
# print(complete1(L))
# print(complete2(L))
# print(complete3(L))
# print(completeAll(L))
#
# L=["0"," "," ", "1"," "," "]
# print(complete1(L))
# print(complete2(L))
# print(complete3(L))
# print(completeAll(L))
#
# L=["0"," ","1", "1"," ","1"]
# print(complete1(L))
# print(complete2(L))
# print(complete3(L))
# print(completeAll(L))
#
# L=["0","0","0", "1"," "," "]
# print(complete1(L))
# print(complete2(L))
# print(complete3(L))
# print(completeAll(L))

# # testcode voor vraag 4e - het algoritme kan de puzzel helemaal oplossen
# spel=game(4)
# spel.change_button_label(0, 0, "1")
# spel.change_button_label(0, 2, "0")
# spel.change_button_label(1, 1, "1")
# spel.change_button_label(1, 2, "0")
# spel.change_button_label(1, 3, "0")
# spel.change_button_label(2, 3, "0")
# spel.change_button_label(3, 2, "1")
# spel.mainloop()