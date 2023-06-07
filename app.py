
# Author: Jarin Tasnim Oyeshi
# Date: 11 April 2023
# Version: 2.0.0


from flask import Flask,jsonify
from Models.Context import Session



# IMPORTING REPOSITORIES TO TEST
from Repositories.ExpenseLocationRepository import ExpenseLocationRepository
from Repositories.ExpenseDetailsRepository import ExpenseDetailsRepository
from Repositories.ExpenseHeadAmountSettingsRepository import ExpenseHeadAmountSettingsRepository
from Repositories.ExpenseHeadRepository import ExpenseHeadRepository
from Repositories.ExpenseRepository import ExpenseRepository



# IMPORTING MODELS TO TEST 
from Servises.ExpenseLocationService import ExpenseLocationService
from Servises.ExpenseDetailsService import ExpenseDetailsService
from Servises.ExpenseHeadAmountSettingsService import ExpenseHeadAmountSettingsService
from Servises.ExpenseHeadService import ExpenseHeadService
from Servises.ExpenseService import ExpenseService
 


# importing models
from Models.Expense import Expense
from Models.ExpenseDetails import ExpenseDetails
from Models.ExpenseHead import ExpenseHead
from Models.ExpenseHeadAmountSettings import ExpenseHeadAmountSettings
from Models.ExpenseLocation import ExpenseLocation


from Models.Context import Session



#  ADDING SESSION TO EXPENSE HEAD
session = Session()

#__________________________  Expense Head _____________________________


# data = expp.GetAll()
# for x in data:
#     print('{:>3}'.format(x.ID))
    

# data = expp.GetByID('CA')
# print(data.ID,data.HeadName)


#  Update 1 
# expense = expp.GetByID('CA')
# expense.HeadName = "City Allowence"
# data = expp.Update(expense)


# Update 2
# data = ExpenseHead(ID='RJ',HeadName='Rajbari')
# expp.Update(data)

# DELETE 
# data = expp.Delete('RJ')


#  ADD DATA
# data = ExpenseHead(ID='RJ',HeadName='Rajbari',CreatedByID='LPL08431')
# expp.Add(data)





#__________________________  Expense Details _____________________________


# ADD DATA
# data = ExpenseDetails(ExpenseLocationID='H.Q.',ExpenseHeadID='MP',CreatedByID='LPL08431')
# expD.Add(data)

# GET ALL
# data = expD.GetAll()
# for x in data:
#     print('{:>3}'.format(x.ID))
    
    
    

#__________________________  Expense Location Details _____________________________

# GET ALL
# data = expL.GetAll()
# for x in data:
#     print('{:>3}'.format(x.ID))
    
    
    


#__________________________  Expense Head Details _____________________________


# GET ALL
# data = expH.GetAll()
# for x in data:
#     print('{:>3}'.format(x.ID))
    

#__________________________  Expense Head Amount settings Details _____________________________

# GET ALL
# data = expHA.GetAll()
# for x in data:
#     print('{:>3}'.format(x.ID))
     


#__________________________  Expense s _____________________________

# GET ALL
# data = exp.GetAll()
# for x in data:
#     print('{:>3}'.format(x.ID))












#________  Validation check ____________
from DTO.ExpenseHeadDto import ExpenseHeadDto,ValidationError
from DTO.ExpenseDetailsDto import ExpenseDetailsDto,ValidationError
from DTO.ExpenseDto import ExpenseDto
from DTO.ExpenseHeadAmountSettingsDto import ExpenseHeadAmountSettingsDto
from DTO.ExpenseLocationDto import ExpenseLocationDto

# Expense Head Check
# data = ExpenseHeadDto(**{'ID':'DA','HeadName':'Daily Allowence','CreatedByID':'LPL08431'})
# newData = ExpenseHead().getAnObject(dict(data))
# expH.Add(newData)


# Expense Details Checks
# data= ExpenseDetailsDto(**{'ExpenseLocationID':'MP','ExpenseDate':'2022-04-11','LocationFrom':'Faridpur','LocationTo':'Rajbari','ExpenseID':'3','Distance':'100km','CreatedByID':'LPL08431'})
# newData = ExpenseDetails().getAnObject(dict(data))
# expD.Add(newData)


# Expense DTO CHECK
# data= ExpenseDto(**{'EmployeeID':'LPL000','ExpenseMonth':'2022/2/12','Designation':'SMPO','CreatedByID':'LPL08431'})
# newData = Expense().getAnObject(dict(data))
# exp.Add(newData)


# EXPENSE HEAD AMOUNT SETTINGS CHECK
# data= ExpenseHeadAmountSettingsDto(**{'ID':'LPL000','ExpenseHeadID':'DA','ExpenseLocationID':'DC','Designation':'SMPO','Amount':400,'CreatedByID':'LPL08431'})
# newData = ExpenseHeadAmountSettings().getAnObject(dict(data))
# exp.Add(newData)



# EXPENSE LOCATION CHECK
# try:
#     data= ExpenseLocationDto(**{'ID':'NEW','LocationName':'Newww','ShortName':'new','CreatedByID':'LPL08431'})
#     newData = ExpenseLocation().getAnObject(dict(data))
#     expL.Add(newData)
# except ValidationError as e:
#     print(e.json)







#________________  Making blue print____

from Controller.ExpenseHeadController import expenseHead
from Controller.ExpenseLocationController import expenseLocation
from Controller.ExpenseHeadAmountSettingsController import expenseHeadAmountSettings
from Controller.ExpenseDetailsController import expenseDetails
from Controller.ExpenseController import expenseBill



from Models.Expense import ExpenseSchema
app= Flask(__name__)
app.register_blueprint(expenseHead)
app.register_blueprint(expenseLocation)
app.register_blueprint(expenseHeadAmountSettings)
app.register_blueprint(expenseDetails)
app.register_blueprint(expenseBill)


### SWAGGER TEST


# from apispec import APISpec
# from apispec.ext.marshmallow import MarshmallowPlugin
# from apispec_webframeworks.flask import FlaskPlugin
# app = Flask(__name__, template_folder='./swagger/templates')
# @app.route('/')
# def hello_world():
#     return 'Hello, World'
# spec = APISpec(
#     title='flask-api-swagger-doc',
#     version='1.0.0',
#     openapi_version='3.0.2',
#     plugins=[FlaskPlugin(), MarshmallowPlugin()]
# )
# @app.route('/api/swagger.json')
# def create_swagger_spec():
#     return jsonify(spec.to_dict())






###------------------------  Swagger api documentation setup -------------------###

from flask_swagger_ui import get_swaggerui_blueprint

# swagger configs
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name' : "REST API"
    } 
)

app.register_blueprint(SWAGGER_BLUEPRINT,url_prefix = SWAGGER_URL)



# SWAGGER_URL = '/swagger'
# API_URL = '/static/swagger1.json'
# SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config = {
#         'app_name' : "REST API"
#     } 
# )

# app.register_blueprint(SWAGGER_BLUEPRINT,url_prefix = SWAGGER_URL)































if __name__ == '__main__':
    app.run(debug=True,port=3500)