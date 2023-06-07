

from pydantic import BaseModel,Field, ValidationError,validator
from datetime import datetime,date


class ExpenseHeadAmountSettingsDto(BaseModel):
    ID: str = Field(min_length=2)
    ExpenseHeadID: str = Field(min_length=2)
    ExpenseLocationID: str = Field(min_length=2)
    Designation: str = Field(min_length=2)
    Amount: int
    CreatedByID: str = Field(min_length=5)
    UpdatedByID: str  = Field(default=None)
    
    

class ExpenseHeadAmountSettingsUpdateDto(BaseModel):
    ID: str = Field(min_length=2)
    Amount: int 