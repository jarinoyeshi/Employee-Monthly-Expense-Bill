

from .Iservice import IService
from Repositories.ExpenseDetailsRepository import ExpenseDetailsRepository
from Models.ExpenseDetails import ExpenseDetails

from Models.Context import Session
from typing import List


class ExpenseDetailsService(IService):
    
    
    def __init__(self,db:Session):
        self.db= db
        self.repo = ExpenseDetailsRepository(db)
        
    
    def GetAll(self)-> List[ExpenseDetails]:
        return self.repo.getAllData()
        
    
    
    def GetByIDOne(self, ID:str):
        return self.repo.getDataByIDOne(ID)
    
    
    
    def GetByID(self, ID:str):
        return self.repo.getDataByID(ID)
        
    
    
    def Add(self, newExpenseDetails: ExpenseDetails)->  ExpenseDetails:
        return self.repo.addData(newExpenseDetails)
        
    

    def Delete(self,ID:str):
        expenseDeatils = self.repo.getDataByID(ID)
        return self.repo.delete(expenseDeatils)
    
    
    def Delete(self, entity: ExpenseDetails):
        expenseDeatils = self.repo.getDataByID(entity)
        return self.repo.delete(expenseDeatils)
        
    
    def Update(self, newexpenseDeatilsUpdate: ExpenseDetails):
        newExpense = self.repo.getDataByID(newexpenseDeatilsUpdate.ID)
        newExpense.Distance = newexpenseDeatilsUpdate.Distance
        return self.repo.updateData(newExpense) 
       