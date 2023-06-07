

from .Iservice import IService
from Repositories.ExpenseRepository import ExpenseRepository
from Models.Expense import Expense

from Models.Context import Session
from typing import List


class ExpenseService(IService):
    
    
    def __init__(self,db:Session):
        self.db= db
        self.repo = ExpenseRepository(db)
        
    
    def GetAll(self)-> List[Expense]:
        return self.repo.getAllData()
        
    
    
    def GetByIDOne(self, ID:str):
        return self.repo.getDataByIDOne(ID)
    
    
    
    def GetByID(self, ID:str):
        return self.repo.getDataByID(ID)
        
    
    
    def Add(self, newExpense: Expense)->  Expense:
        return self.repo.addData(newExpense)
        
    

    def Delete(self,ID:str):
        expense = self.repo.getDataByID(ID)
        return self.repo.delete(expense)
    
    def Delete(self, entity: Expense):
        expense = self.repo.getDataByID(entity)
        return self.repo.delete(expense)
        
    
    def Update(self, newExpenseUpdate: Expense):
        newExpense = self.repo.getDataByID(newExpenseUpdate.ID)
        newExpense.Designation = newExpenseUpdate.Designation        
        return self.repo.updateData(newExpense) 
       