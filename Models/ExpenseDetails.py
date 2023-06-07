from Models.Context import BaseModel, Base,Column,Boolean,DateTime,Integer,String,datetime,ForeignKey,Schema,fields


class ExpenseDetails(Base,BaseModel):
    __tablename__ = 'ExpenseDetails'
    ID= Column(Integer,primary_key=True,autoincrement=True)
    ExpenseLocationID=Column(String(10),ForeignKey('ExpenseLocation.ID')) 
    ExpenseDate= Column(DateTime(),nullable= False)
    LocationFrom = Column(String(50),nullable= False)
    LocationTo= Column(String(50),nullable= False)
    ExpenseHeadID= Column(String(10),ForeignKey('ExpenseHead.ID')) 
    ExpenseID= Column(Integer,ForeignKey('Expense.ID')) 
    ModeOfTransport= Column(String(10))
    Distance= Column(String(10))


class ExpenseDetailsSchema(Schema):
    ID= fields.Integer()
    ExpenseLocationID= fields.Str()
    CreatedByID= fields.Str()

