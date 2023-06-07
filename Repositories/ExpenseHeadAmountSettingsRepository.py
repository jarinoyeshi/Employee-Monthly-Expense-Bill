

# IMPORT MODULES
from Models.Context import Session
from Models.ExpenseHeadAmountSettings import ExpenseHeadAmountSettings,ExpenseHeadAmountSettingsSchema
from .GenericRepository import GenericRepository


class ExpenseHeadAmountSettingsRepository(GenericRepository):
    def __init__(self,db: Session):
        super().__init__(db,ExpenseHeadAmountSettings,ExpenseHeadAmountSettingsSchema())