import random

class Monde:

    def __init__(self, dimension, duree_repousse, carte):
        self.dimension = dimension
        self.duree_repousse = 30
        self.carte = [[random.randint(0,50) for i in range(dimension)] for j in range(dimension)]

    def herbePousse(self):
        for i,j in range(len(self.carte)):
            self.carte[i][j] += 1
    
    def herbeMangee(self, i, j):
        for i,j in range(len(self.carte)):
            self.carte[i][j] = 0 if self.carte[i][j] >= 30
    
    def nbHerbe(self, nbHerbe):
        nbHerbe = 0
        for i,j in range(len(self.carte)):
            if self.carte[i][j] >= 30:
                nbHerbe += 1

    def getCoefCarte(self, i, j):
        return self.carte[i][j]

class Mouton:
    def __init__(self, gain_nourriture, position, taux_reproduction, monde)
    self.gain_nourriture = 4
    self.position = (i,j)
    self.energie = random.randint(1, 2*self.gain_nourriture)
    self.taux_reproduction = 4
    self.monde = monde

    def variationEnergie(self):
        if self.monde.carte[self.position[0]][self.position[1]] >= self.monde.duree_repousse:
            self.energie += self.gain_nourriture
            self.monde.carte[self.position[0]][self.position[1]] = 0
        else:
            self.energie = self.energie - 1

    def deplacement(self):
        deplace = random.randint(0,8)
        position = list(self.position)
        binds = {
            1: (position[0]-1, position[1]-1),
            2: position[1] -1,
            3: (position[0]+1, position[1]-1),
            4: position[0] + 1,
            5: (position[0]+1, position[1]+1),
            6: position[1] + 1,
            7: (position[0]-1, position[1]+1),
            8: position[0] - 1
        }
        position = binds[deplace]
        self.position = tuple(position)
        return self.position
    
    def setPosition(self, pere):
        chance = randint(0, self.taux_reproduction)
        if chance == 4:
            bebe = Mouton(4, pere.position, 50, 4, pere.monde)
            bebe.position[0], bebe.position[1] = self.position[0], self.position[1]
        
    def getPosition(self):
        return f'La position de mouton --> {self.position}'

class Simulation:
    def __init__(self, nombre_moutons, fin_du_monde, monde):
        self.nombre_moutons = nombre_moutons
        self.horloge = 0
        self.monde = Monde()
        self.moutons = [Mouton(4, (random.randint(for i in range(2))), 4, Monde()) for mouton in range(self.nombre_moutons)]




