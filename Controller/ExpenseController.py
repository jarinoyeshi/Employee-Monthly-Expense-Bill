

from Models.Context import Session,Blueprint,request,Schema,jsonify
from Servises.ExpenseService import ExpenseService
from DTO.ExpenseDto import ExpenseDto,ExpenseUpdateDto,ValidationError
from Models.Expense import Expense


expenseBill= Blueprint('expenseBill',__name__)







#  SHOW ALL DATA
@expenseBill.route('/expense/show',methods=['GET'])
def getExpense():
     return ExpenseService(Session()).GetAll()



#  SHOW DATA BY ID
@expenseBill.route('/expense/showbyID/<ExpenseID>',methods=['GET'])
def getExpenseByID(ExpenseID: str):
    return ExpenseService(Session()).GetByIDOne(ExpenseID)


    


#  ADD DATA
@expenseBill.route('/expense/add',methods=['POST'])
def addExpenses():
    try:
        validationDTO = ExpenseDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    ExpenseService(Session()).Add(Expense().getAnObject(dict(validationDTO)))
    return "Expense SAVED"









# DELETE DATA
@expenseBill.route('/expense/delete/<ExpenseID>', methods=['DELETE'])
def deleteExpense(ExpenseID: str):
    ExpenseService(Session()).Delete(ExpenseID)
    return "Expense deleted"







#UPDATE DATA
@expenseBill.route('/expense/update', methods=['PUT'])
def updateExpense():
    try:
        validationDTO = ExpenseUpdateDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    ExpenseService(Session()).Update(Expense().getAnObject(dict(validationDTO)))
    return 'Expense Updated Successfully'