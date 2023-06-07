

from .Iservice import IService
from Repositories.ExpenseHeadRepository import ExpenseHeadRepository
from Models.ExpenseHead import ExpenseHead

from Models.Context import Session
from typing import List


class ExpenseHeadService(IService):
    
    
    def __init__(self,db:Session):
        self.db= db
        self.repo = ExpenseHeadRepository(db)
        
    
    
    
    def GetAll(self)-> List[ExpenseHead]:
        return self.repo.getAllData()
        
    
    
    
    def GetByIDOne(self, ID:str):
        return self.repo.getDataByIDOne(ID)    
    

 
 
    def GetByID(self, ID:str):
        return self.repo.getDataByID(ID)       
    
    
    
    
    
    def Add(self, newExpenseHead: ExpenseHead)->  ExpenseHead:
        if(len(newExpenseHead.ID)==0 or newExpenseHead.ID == " "):
            raise ValueError('Invalid Value')
        return self.repo.addData(newExpenseHead)
        
    
    
    
    

    def Delete(self,ID:str):
        expeseHead = self.repo.getDataByID(ID)
        if(expeseHead == None):
             raise ValueError(f'Expense Head not found with ID:{ID}')
        return self.repo.delete(expeseHead)
    
    
    
    
    
    def Delete(self, entity: ExpenseHead):
         expeseHead = self.repo.getDataByID(entity)
         return self.repo.delete(expeseHead)
        
    
    
    
    
    
    
    def Update(self, newExpenseHeadUpdate: ExpenseHead):
        expenseHead = self.repo.getDataByID(newExpenseHeadUpdate.ID)
        expenseHead.HeadName = newExpenseHeadUpdate.HeadName
        return self.repo.updateData(expenseHead) 
       