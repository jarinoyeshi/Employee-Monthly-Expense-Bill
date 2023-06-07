from Models.Context import BaseModel, Base,ForeignKey,Column,Integer,String,Schema,fields

class ExpenseHeadAmountSettings(Base,BaseModel):
    __tablename__ = 'ExpenseHeadAmountSettings'
    ID= Column(String(10),primary_key=True)
    ExpenseHeadID= Column(String(10),ForeignKey('ExpenseHead.ID'))
    ExpenseLocationID= Column(String(10),ForeignKey('ExpenseLocation.ID'))
    Designation= Column(String(100),nullable= False)
    Amount= Column(Integer,nullable= False)


class ExpenseHeadAmountSettingsSchema(Schema):
    ID= fields.Str()
    ExpenseHeadID= fields.Str()
    ExpenseLocationID= fields.Str()
    Designation= fields.Str()
    Amount= fields.Integer()