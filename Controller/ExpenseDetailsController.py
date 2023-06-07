
from Models.Context import Session,Blueprint,request,Schema
from Servises.ExpenseDetailsService import ExpenseDetailsService
from DTO.ExpenseDetailsDto import ExpenseDetailsDto,ExpenseDetailsUpdateDto,ValidationError
from Models.ExpenseDetails import ExpenseDetails


expenseDetails= Blueprint('expenseDetails',__name__)



# API CREATION




#  SHOW ALL DATA
@expenseDetails.route('/details/show',methods=['GET'])
def getexpenseDetails():
    return ExpenseDetailsService(Session()).GetAll()




#  SHOW DATA BY ID
@expenseDetails.route('/details/showbyID/<ExpenseDetailsID>',methods=['GET'])
def getexpenseDetailsByID(ExpenseDetailsID: str):
    return ExpenseDetailsService(Session()).GetByIDOne(ExpenseDetailsID)




#  ADD DATA
@expenseDetails.route('/details/add',methods=['POST'])
def addexpenseDetails():
    try:
        validationDTO = ExpenseDetailsDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    ExpenseDetailsService(Session()).Add(ExpenseDetails().getAnObject(dict(validationDTO)))
    return "SAVED"









# DELETE DATA
@expenseDetails.route('/details/delete/<ExpenseDetailsID>', methods=['DELETE'])
def deleteexpenseDetails(ExpenseDetailsID: str):
    ExpenseDetailsService(Session()).Delete(ExpenseDetailsID)
    return "Successfully deleted"







#UPDATE DATA
@expenseDetails.route('/details/update', methods=['PUT'])
def updateExpense():
    try:
        validationDTO = ExpenseDetailsUpdateDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    ExpenseDetailsService(Session()).Update(ExpenseDetails().getAnObject(dict(validationDTO)))
    return 'Updated Successfully'