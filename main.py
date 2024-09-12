import time
import random
class Monde:
    def __init__(self,  dimension, duree_repousse):
        self.dimension =dimension
        self.duree_repousse = duree_repousse
        self.carte = [[random.randint(0,40) for j in range(dimension)]for i in range(dimension)]
    def herbePousse(self):
        for col in range(self.dimension):
            for item in range(self.dimension):
                self.carte[col][item] += 1
            
        print(self.carte)   
    
    def herbeMangee(self, i, j):
        if self.carte[i][j]> self.duree_repousse:
            self.carte[i][j] = 0
    def nbHerbe(self):
        count = 0
        for col in range(self.dimension):
            for item in range(self.dimension):
                if self.carte[col][item] > self.duree_repousse:
                    count +=1
        return count
    def get_coef_carte(self, i, j):
        return self.carte[i][j]
    
    def get_carte(self):
        return self.carte

    


class Mouton:
    def __init__(self,  gain_nourriture, position:tuple, taux_reproduction):
        self.gain_nourriture =gain_nourriture
        self.position = position
        self.energie =random.randint(1, self.gain_nourriture*2)
        self.monde = Monde()

    def variationEnergie(self):
        if self.monde.get_coef_carte(self.position[0],self.position[1]) > 30:
            self.energie += gain_nourriture
            self.monde.herbeMangee(self.position[0],self.position[1])
        else:
            self.energie -= 1

    def deplacement   
# m = Monde(2, 30)
# m.herbePousse()
# m.herbePousse()
# m.get_carte()
