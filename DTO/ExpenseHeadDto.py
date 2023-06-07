
from pydantic import BaseModel,Field,ValidationError


class ExpenseHeadDto(BaseModel):
    ID: str = Field(min_length=2)
    HeadName: str = Field(min_length=2, max_length=100)
    CreatedByID: str = Field(min_length=5)
    

class ExpenseHeadUpdateDto(BaseModel):
    ID: str = Field(min_length=2)
    HeadName: str = Field(min_length=4, max_length=50)

