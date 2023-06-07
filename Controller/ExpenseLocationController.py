

from Models.Context import Blueprint, request, Session
from Servises.ExpenseLocationService import ExpenseLocationService
from DTO.ExpenseLocationDto import ExpenseLocationDto,ValidationError,ExpenseLocationUpdateDto
from Models.ExpenseLocation import ExpenseLocation

# BLUEPRINT CREATION
expenseLocation = Blueprint('expenseLocation',__name__)







#  SHOW ALL DATA
@expenseLocation.route('/location/show',methods=['GET'])
def getExpenseLocation():
    return ExpenseLocationService(Session()).GetAll()








#  SHOW DATA BY ID
@expenseLocation.route('/location/showbyID/<ExpenseLocationID>',methods=['GET'])
def getExpenseLocationByID(ExpenseLocationID: str):
    return ExpenseLocationService(Session()).GetByIDOne(ExpenseLocationID)








# ADD DATA
@expenseLocation.route('/location/add',methods=['POST'])
def addExpenseLocation():
    try:
        validationDTO = ExpenseLocationDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    ExpenseLocationService(Session()).Add(ExpenseLocation().getAnObject(dict(validationDTO)))
    return 'Location Saved'







# DELETE DATA
@expenseLocation.route('/location/delete/<ExpenseLocationID>',methods=['delete'])
def deleteLocation(ExpenseLocationID: str):
    ExpenseLocationService(Session()).Delete(ExpenseLocationID)
    return 'Deleted Successfully'








# UPDATE DATA
@expenseLocation.route('/location/update',methods=['PUT'])
def updateLocation():
    try:
        validationDTO = ExpenseLocationUpdateDto(**request.json)
    except ValidationError as e:
        return e.json()
    
    ExpenseLocationService(Session()).Update(ExpenseLocation().getAnObject(dict(validationDTO)))  
    return "Location Updated"  