

# IMPORTATION

from abc import ABC, abstractmethod

class IService(ABC):
    
    @abstractmethod
    def GetAll(self):
        pass
    

    
    
    @abstractmethod
    def GetByID(self):
        pass
    
    
    @abstractmethod
    def GetByIDOne(self):
        pass
    
    @abstractmethod
    def GetByID(self):
        pass
    
    @abstractmethod
    def Add(self):
        pass
    
    @abstractmethod
    def Delete(self):
        pass
    
    @abstractmethod
    def Update(self):
        pass
    
