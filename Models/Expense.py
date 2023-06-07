from Models.Context import BaseModel, Base,Column,DateTime,Integer,String,Schema,fields,Session
from datetime import datetime


class Expense(Base,BaseModel):
    __tablename__ = 'Expense'
    ID=  Column(Integer,primary_key=True,autoincrement=True)
    EmployeeID = Column(String(10),nullable= False)
    ExpenseMonth= Column(DateTime,nullable= False)
    CheckedByID= Column(String(10))
    CheckedOn= Column(DateTime,onupdate=datetime.now)
    VerifiedByID= Column(String(10))
    VerifiedOn= Column(DateTime,onupdate=datetime.now)
    ForwardedByID= Column(String(10))
    ForwardedOn= Column(DateTime,default=None)
    RecommendedByID= Column(String(10))
    RecommendedOn= Column(DateTime,onupdate=datetime.now)
    ApprovedByID= Column(String(10))
    ApprovedOn= Column(DateTime,onupdate=datetime.now)
    FCAApprovedByID= Column(String(10))
    FCAApprovedOn= Column(DateTime,default=None)
    ManagementApprovedByID= Column(String(10))
    ManagementApprovedOn= Column(DateTime,onupdate=datetime.now)
    Designation = Column(String(50),nullable= False)
    



class ExpenseSchema(Schema):
    ID=  fields.Str()
    EmployeeID = fields.Str()
    ExpenseMonth= fields.DateTime()
