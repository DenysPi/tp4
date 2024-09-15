import random



class Monde:

    def __init__(self, dimension, duree_repousse):
        self.dimension = dimension
        self.duree_repousse = duree_repousse
        self.carte = [[random.randint(0, 50) for i in range(dimension)] for j in range(dimension)]

    def herbePousse(self):        
        for i in range(len(self.carte)):
            for j in range(len(self.carte[i])):
                self.carte[i][j] += 1
    
    def herbeMangee(self, i, j):
        if self.carte[i][j] >= 30:
            self.carte[i][j] = 0
    
    def nbHerbe(self):
        nbHerbe = 0
        for i in range(len(self.carte)):
            for j in range(len(self.carte[i])):
                if self.carte[i][j] >= 30:
                    nbHerbe += 1
        return nbHerbe

    def getCoefCarte(self, i, j):
        return self.carte[i][j]
    
    


class Mouton:
    def __init__(self, gain_nourriture, position, taux_reproduction, monde):
        self.gain_nourriture = gain_nourriture
        self.position = (position[0], position[1]) 
        self.energie = random.randint(1, 2 * self.gain_nourriture)
        self.taux_reproduction = taux_reproduction
        self.monde = monde

    def variationEnergie(self):
        
        if self.monde.carte[self.position[0]][self.position[1]] >= self.monde.duree_repousse:
            self.energie += self.gain_nourriture
            self.monde.herbeMangee(self.position[0], self.position[1]) 
        else:
            self.energie -= 1

    def deplacement(self):
        
        binds = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        x, y = random.choice(binds)
        new_position = (self.position[0] + x, self.position[1] + y)
        
        
        new_position = (
            max(0, min(new_position[0], self.monde.dimension - 1)),
            max(0, min(new_position[1], self.monde.dimension - 1))
        )
        self.position = new_position

    def setPosition(self, pere):
   
        chance = random.randint(0, self.taux_reproduction)
        if chance == 4:  
        
            bebe = Mouton(4, pere.position, 50, pere.monde) 
        
      
            return bebe
        return None  

    def getPosition(self):
        return f'La position de mouton --> {self.position}'
    


class Simulation:
    def __init__(self, nombre_moutons, fin_du_monde):
        self.nombre_moutons = nombre_moutons
        self.horloge = 0
        self.monde = Monde(10, 30)  
        self.moutons = [Mouton(4, (random.randint(0, 4), random.randint(0, 4)), 4, monde=self.monde) for _ in range(self.nombre_moutons)]
        self.fin_du_monde = fin_du_monde
        self.resultats_moutons = len(self.moutons)

    def sim_mouton(self):
        
        while self.horloge < self.fin_du_monde and len(self.moutons) > 0:
            self.monde.herbePousse()
            
            new_moutons = []
            for mouton in self.moutons:
                mouton.variationEnergie()
                mouton.deplacement()

                
                new_mouton = mouton.setPosition(mouton)
                if new_mouton:
                    new_moutons.append(new_mouton)
            
                
            self.moutons = [m for m in self.moutons if m.energie > 0]
            self.moutons.extend(new_moutons)
            
            

            
            self.horloge += 1

        return f'Final ---> Carte = {self.monde.carte}, Moutons = {len(self.moutons)}'
        
        
simulation = Simulation(3, 10)

print(simulation.sim_mouton())




