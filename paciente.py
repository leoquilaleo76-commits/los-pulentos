class Paciente:
    PREVIONES_VALIDAS:set[str]={"Fonasa","Isapre","Particular","Otro"}  
   
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
        @property
        def nombre(self)-> str:
            return self.__nombre

        @nombre.setter
        def nombre(self,nombre:str)-> None:
            self.__nombre=nombre
            @property
            def edad(self)-> int:
                return self.__edad
            
            
            @edad.setter
            def edad(self,edad:int)-> None:
                self.__edad=edad
                
                @property
                def previson(self)-> str:
                    return self.__previson
                
                
                @previson.setter
                def previson(self,previson:str)-> None:
                    self.__previson=previson
                    
                    def __str__(self)-> str:
                        return f"información del paciente: {self.rut} - {self.nombre} - {self.edad} - {self.previson}"
                    
                    def __repr__(self)-> str:
                        return f"Paciente({self.rut},{self.nombre},{self.edad},previson='{self.previson}')"
                    
                    