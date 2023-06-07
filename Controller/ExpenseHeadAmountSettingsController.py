
from Models.Context import Schema,Session,Blueprint,request
from Models.ExpenseHeadAmountSettings import ExpenseHeadAmountSettings,ExpenseHeadAmountSettingsSchema
from Servises.ExpenseHeadAmountSettingsService import ExpenseHeadAmountSettingsService
from DTO.ExpenseHeadAmountSettingsDto import ExpenseHeadAmountSettingsDto,ValidationError,ExpenseHeadAmountSettingsUpdateDto


expenseHeadAmountSettings = Blueprint('expenseAmountSettings',__name__)



# API CREATION

# SHOW DATA
@expenseHeadAmountSettings.route('/amount/show',methods=['GET'])
def getexpenseHeadAmountSettings():
    return ExpenseHeadAmountSettingsService(Session()).GetAll()









#  SHOW DATA BY ID
@expenseHeadAmountSettings.route('/amount/showbyID/<ExpenseHeadAmountSettingsID>',methods=['GET'])
def getexpenseHeadAmountSettingsByID(ExpenseHeadAmountSettingsID: str):
    return ExpenseHeadAmountSettingsService(Session()).GetByIDOne(ExpenseHeadAmountSettingsID)









# ADD DATA
@expenseHeadAmountSettings.route('/amount/add',methods=['POST'])
def addExpenseHeadAmountSettings():
    try:
        validationDTO = ExpenseHeadAmountSettingsDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    ExpenseHeadAmountSettingsService(Session()).Add(ExpenseHeadAmountSettings().getAnObject(dict(validationDTO)))
    return "Amount Saved"



  
  
  
  

# DELETE DATA
@expenseHeadAmountSettings.route('/amount/delete/<ExpenseHeadAmountSettingsID>',methods=['DELETE'])
def deleteExpenseHeadAmountSettings(ExpenseHeadAmountSettingsID: str):
    ExpenseHeadAmountSettingsService(Session()).Delete(ExpenseHeadAmountSettingsID)
    return "Amount Deleted"













# UPDATE DATA
@expenseHeadAmountSettings.route('/amount/update',methods=['PUT'])
def updateExpenseHeadAmountSettings():
    try:
        validationDTO = ExpenseHeadAmountSettingsUpdateDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    ExpenseHeadAmountSettingsService(Session()).Update(ExpenseHeadAmountSettings().getAnObject(dict(validationDTO)))
    return "Amount Updated"


