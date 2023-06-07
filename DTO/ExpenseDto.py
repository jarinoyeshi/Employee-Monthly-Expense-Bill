
from pydantic import BaseModel,Field, ValidationError,validator
from datetime import datetime,date


class ExpenseDto(BaseModel):
    EmployeeID: str = Field(min_length=2)
    ExpenseMonth: str
    CheckedByID: str= Field(default=None)
    VerifiedByID: str= Field(default=None,)
    ForwardedByID: str= Field(default=None)
    RecommendedByID: str= Field(default=None)
    ApprovedByID: str= Field(default=None)
    FCAApprovedByID: str= Field(default=None)
    ManagementApprovedByID:  str= Field(default=None)
    Designation: str = Field(min_length=2)

    CreatedByID: str = Field(min_length=5)
    UpdatedByID: str  = Field(default=None)
    
    
    @validator('ExpenseMonth')
    def parse_date(cls, value):
        if isinstance(value, date):
            value = value.strftime('%Y-%m-%d')
        return value

class ExpenseUpdateDto(BaseModel):
    ID: int
    Designation: str