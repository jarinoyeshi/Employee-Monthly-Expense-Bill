from Models.Context import BaseModel, Base,Column,String,Schema,fields

class ExpenseLocation(Base,BaseModel):
    __tablename__= "ExpenseLocation"
    ID= Column(String(10),primary_key=True)
    LocationName= Column(String(50),unique=True)
    ShortName= Column(String(50),nullable=False)
    


class ExpenseLocationSchema(Schema):
    ID= fields.Str()
    LocationName= fields.Str()
    ShortName= fields.Str()
    #UpdatedByID= fields.Str()