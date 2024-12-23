class Point:
    "Classe définissant un point caractérisé par ses coordonnées x, y et z."
    def __init__(self):
        "Constructeur de notre classe"
        self.x = 0
        self.y = 0
        self.z = 0
    def deplace(self, dx, dy, dz):
        "Méthode pour se déplacer"
        self.x += dx
        self.y += dy
        self.z += dz  

a = Point() # Création d'un objet Point
b = Point() # Création d'un objet Point
print("a : x =", a.x, "y =", a.y)
"""a.x = 1.0
a.y = 2.0
b.x = 3.0
b.y = 4.0

print("a : x =", a.x, "y =", a.y) # On affiche les attributs de a
print("b : x =", b.x, "y =", b.y) # On affiche les attributs de b"""
a.deplace(1, 2, 3) # On déplace le point a de 1 en x et 2 en y
print("a : x =", a.x, "y =", a.y) # On affiche les attributs de a
b.deplace(3, 4, 5) # On déplace le point b de 3 en x et 4 en y
print("b : x =", b.x, "y =", b.y) # On affiche les attributs de b
