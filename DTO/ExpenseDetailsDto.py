

from pydantic import BaseModel,Field, ValidationError,validator
from datetime import datetime,date


class ExpenseDetailsDto(BaseModel):
    ExpenseLocationID: str = Field(min_length=2,max_length=10)
    ExpenseDate: str
    LocationFrom: str = Field(min_length=3)
    LocationTo: str = Field(min_length=3)
    ExpenseHeadID: str
    ExpenseID: int
    ModeOfTransport: str = Field(default=None)
    Distance: str
    CreatedByID: str = Field(min_length=5)
    UpdatedByID: str  = Field(default=None)
    
    
    @validator('ExpenseDate')
    def parse_date(cls, value):
        if isinstance(value, date):
            value = value.strftime('%Y-%m-%d')
        return value
    
    
class ExpenseDetailsUpdateDto(BaseModel):
    ID: str = Field(min_length=2)
    Distance: str
