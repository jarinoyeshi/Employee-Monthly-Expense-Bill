from Models.Context import BaseModel, Base,Column,String,Schema,fields



class ExpenseHead(Base,BaseModel):
    __tablename__ = 'ExpenseHead'
    ID= Column(String(10),primary_key=True)
    HeadName= Column(String(100),unique=True)
    
class ExpenseHeadSchema(Schema):
    ID= fields.Str()
    HeadName= fields.Str()
    IsActive = fields.Boolean()
    CreatedByID= fields.Str()
    CreatedOn = fields.DateTime()
    
