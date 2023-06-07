

# IMPORT MODULES
from Models.Context import Session
from Models.ExpenseHead import ExpenseHead,ExpenseHeadSchema
from .GenericRepository import GenericRepository


class ExpenseHeadRepository(GenericRepository):
    def __init__(self,db: Session):
        super().__init__(db,ExpenseHead,ExpenseHeadSchema())