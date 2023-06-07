

# IMPORTED MODULES
from Models.Context import Base
from abc import ABC, abstractmethod
from typing import TypeVar,List







# DEFINING A GENERIC TYPE VARIABLE 'ENTITY'
Entity= TypeVar('Entity',bound= Base)





# DECLARING ABSTRACT METHODS
class IGenericRepository(ABC):
    @abstractmethod
    def getAllData(self)->List[Entity]:
        pass
    
    
    
    
    
    @abstractmethod
    def getDataByID(self, ID:int) ->Entity:
        pass
    
    
    
    
    
    @abstractmethod
    def getDataByID(self, ID:str) ->Entity:
        pass
    
    
    
    
    @abstractmethod
    def getDataByIDOne(self, ID:str) ->Entity:
        pass  
    
    
    
    
    @abstractmethod
    def addData(self,entity:Entity)->Entity:
        pass
    
    
    
    
    
    
    @abstractmethod
    def updateData(self, entity:Entity)->Entity:
        pass
    
    
    
    
    
    @abstractmethod
    def delete(self, ID:str)-> None:
        pass
    
    
    
    
    
    @abstractmethod
    def delete(self, ID:int)-> None:
        pass
    
    
    
    
    
    @abstractmethod
    def delete(self, entity:Entity)->None:
        pass