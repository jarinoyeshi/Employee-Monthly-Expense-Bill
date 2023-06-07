
from Models.Context import Blueprint, request, Session
from Servises.ExpenseHeadService import ExpenseHeadService
from DTO.ExpenseHeadDto import ExpenseHeadDto,ValidationError,ExpenseHeadUpdateDto
from Models.ExpenseHead import ExpenseHead

# BLUEPRINT CREATION
expenseHead = Blueprint('expenseHead',__name__)


# API CREATION




#  SHOW ALL DATA
@expenseHead.route('/expensehead/show',methods=['GET'])
def getExpenseHead():
    return ExpenseHeadService(Session()).GetAll()




#  SHOW DATA BY ID
@expenseHead.route('/expensehead/showbyID/<ExpenseHeadID>',methods=['GET'])
def getExpenseHeadByID(ExpenseHeadID: str):
    return ExpenseHeadService(Session()).GetByIDOne(ExpenseHeadID)






#  ADD DATA
@expenseHead.route('/expensehead/add',methods=['POST'])
def addExpenseHead():
    try:
        validationDTO = ExpenseHeadDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    ExpenseHeadService(Session()).Add(ExpenseHead().getAnObject(dict(validationDTO)))
    return "SAVED"









# DELETE DATA
@expenseHead.route('/expensehead/delete/<ExpenseHeadID>', methods=['DELETE'])
def deleteExpenseHead(ExpenseHeadID: str):
    ExpenseHeadService(Session()).Delete(ExpenseHeadID)
    return "Successfully deleted"







#UPDATE DATA
@expenseHead.route('/expensehead/update', methods=['PUT'])
def updateExpense():
    try:
        validationDTO = ExpenseHeadUpdateDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    ExpenseHeadService(Session()).Update(ExpenseHead().getAnObject(dict(validationDTO)))
    return 'Updated Successfully'