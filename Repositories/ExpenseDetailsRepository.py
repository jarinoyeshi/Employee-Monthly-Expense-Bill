


# IMPORT MODULES
from Models.Context import Session
from Models.ExpenseDetails import ExpenseDetails,ExpenseDetailsSchema
from .GenericRepository import GenericRepository


class ExpenseDetailsRepository(GenericRepository):
        def __init__(self,db:Session):
            super().__init__(db,ExpenseDetails,ExpenseDetailsSchema())
    