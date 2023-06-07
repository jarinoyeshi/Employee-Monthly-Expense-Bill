

from .Iservice import IService
from Repositories.ExpenseHeadAmountSettingsRepository import ExpenseHeadAmountSettingsRepository
from Models.ExpenseHeadAmountSettings import ExpenseHeadAmountSettings

from Models.Context import Session
from typing import List


class ExpenseHeadAmountSettingsService(IService):
    
    
    def __init__(self,db:Session):
        self.db= db
        self.repo = ExpenseHeadAmountSettingsRepository(db)
        
    
    def GetAll(self)-> List[ExpenseHeadAmountSettings]:
        return self.repo.getAllData()
        
    
    
    
    def GetByIDOne(self, ID:str):
        return self.repo.getDataByIDOne(ID)
    
    
    
    
    def GetByID(self, ID:str):
        return self.repo.getDataByID(ID)
    
    
    
        
    
    
    def Add(self, newExpenseHeadAmount: ExpenseHeadAmountSettings)->  ExpenseHeadAmountSettings:
        return self.repo.addData(newExpenseHeadAmount)
        
    


    def Delete(self,ID:str):
        expeseHeadAmount = self.repo.getDataByID(ID)
        return self.repo.delete(expeseHeadAmount)
    
    
    
    
    def Delete(self, entity: ExpenseHeadAmountSettings):
        expeseHeadAmount = self.repo.getDataByID(entity)
        return self.repo.delete(expeseHeadAmount)
        
    
    
    
    
    def Update(self, newExpenseHeadAmountUpdate: ExpenseHeadAmountSettings):
        newExpenseHeadAmount = self.repo.getDataByID(newExpenseHeadAmountUpdate.ID)
        newExpenseHeadAmount.Amount = newExpenseHeadAmountUpdate.Amount
        print(newExpenseHeadAmount.Amount)
        return self.repo.updateData(newExpenseHeadAmount) 