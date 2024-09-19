class CRobot:
    def __init__(self, type_robot, sn) -> None:
        self.type_robot = type_robot
        self.sn = sn
        self.orientation = 1
        self.status = None
        
    def getType(self):
        return f'TYPE ROBOT ---> {self.type_robot}'
    
    def getSN(self):
        return f'Numéro de Série ---> {self.sn}'
    
    def getOrientation(self):
        orientations = {1: "NORD", 2: "EST", 3: "SUD", 4: "OUEST"}
        return orientations[self.orientation]
    
    def getStatus(self):
        return f'status ---> {self.status}'
    
    def setOrientation(self, new_orientation):
        if new_orientation in [1, 2, 3, 4]:
            self.orientation = new_orientation
    
    def setStatus(self, new_status):
        self.status = new_status
        
    def tourner(self, sens=1):
        if sens == 1:  
            if self.orientation == 1:
                self.orientation = 4 
            else: 
                self.orientation - 1
        elif sens == -1:  
            if self.orientation == 4: 
                self.orientation = 1 
            else: 
                self.orientation + 1
    
    def afficher(self):
        print(f"Robot Type: {self.type_robot}")
        print(f"Numéro de Série: {self.sn}")
        print(f"Orientation: {self.getOrientation()}")
        print(f"Statut: {self.status}")   


class CRobotMobile(CRobot):
    
    def __init__(self, type_robot, sn, abs=0, ord=0):
        super().__init__(type_robot, sn)
        self.abs = abs
        self.ord = ord 

    
    def avancer(self, x):
        if self.orientation == 1: 
            self.ord += x 
        elif self.orientation == 2:  
            self.abs += x  
        elif self.orientation == 3:  
            self.ord -= x 
        elif self.orientation == 4:  
            self.abs -= x  


    
    def affichePosition(self):
        print(f"Position actuelle -> Abscisse: {self.abs}, Ordonnée: {self.ord}")

    
    def afficher(self):
        super().afficher()
        self.affichePosition()



    

robot = CRobotMobile("Explorateur", "67890", 0, 0)

print("État initial:")
robot.afficher()

robot.setOrientation(2)
robot.afficher()

robot.setOrientation(4)  
robot.avancer(4)
robot.afficher()


robot.setOrientation(1)  
robot.avancer(6)
robot.afficher()

robot.setOrientation(2) 
robot.avancer(14)
robot.afficher()


robot.setOrientation(3)  
robot.avancer(8)
robot.afficher()

