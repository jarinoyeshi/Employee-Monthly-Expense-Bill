


from pydantic import BaseModel,Field, ValidationError



class ExpenseLocationDto(BaseModel):
    ID: str = Field(min_length=2)
    LocationName: str
    ShortName: str = Field(min_length=2)
    CreatedByID: str = Field(min_length=5)
    UpdatedByID: str  = Field(default=None)
    
class ExpenseLocationUpdateDto(BaseModel):
    ID: str = Field(min_length=2)
    LocationName: str = Field(min_length=4, max_length=50)
    UpdatedByID: str  = Field(min_length=2)