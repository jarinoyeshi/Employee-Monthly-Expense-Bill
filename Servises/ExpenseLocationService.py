

from .Iservice import IService
from Repositories.ExpenseLocationRepository import ExpenseLocationRepository
from Models.ExpenseLocation import ExpenseLocation

from Models.Context import Session
from typing import List


class ExpenseLocationService(IService):
    
    
    def __init__(self,db:Session):
        self.db= db
        self.repo = ExpenseLocationRepository(db)
        
    
    def GetAll(self)-> List[ExpenseLocation]:
        return self.repo.getAllData()
    
    
    
    
    def GetByIDOne(self, ID:str):
        return self.repo.getDataByIDOne(ID)
        
    
    
    def GetByID(self, ID:str):
        return self.repo.getDataByID(ID)
        
    
    
    def Add(self, newExpenseLocation: ExpenseLocation)->  ExpenseLocation:
        return self.repo.addData(newExpenseLocation)
        
    

    def Delete(self,ID:str):
        expenseLocation = self.repo.getDataByID(ID)
        return self.repo.delete(expenseLocation)
    
    def Delete(self, entity: ExpenseLocation):
        expenseLocation = self.repo.getDataByID(entity)
        return self.repo.delete(expenseLocation)
        
    
    def Update(self, newExpenseLocationUpdate: ExpenseLocation):
        newExpenseLocation = self.repo.getDataByID(newExpenseLocationUpdate.ID)
        newExpenseLocation.LocationName = newExpenseLocationUpdate.LocationName
        return self.repo.updateData(newExpenseLocation) 
       