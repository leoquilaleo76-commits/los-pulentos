class Paciente:
    def __init__(self,rut:str, nombre:str, edad:int,previson:str):
        self.rut=rut
        self.nombre=nombre
        self.edad=edad
        self.previson=previson
    @property
    def rut(self)-> str:
        return self.__rut
    
    
    
    @rut.setter
    def rut(self,rut:str)-> None:
        self.__rut=rut