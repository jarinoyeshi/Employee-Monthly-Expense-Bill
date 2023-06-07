

# UNIT TEST FOR LOCATION ROUTES


try :
    import unittest
    import sys
    sys.path.append('.')
    from app import app


except Exception as e:
    print(" Error: {}".format(e))
    
    

class flasktest(unittest.TestCase):
           
    # TESTING 1 :  Statuscode for the route
    def test_index(self):
        tester = app.test_client(self) 
        resposne = tester.get("/expensehead/show")
        statuscode = resposne.status_code
        self.assertEqual(statuscode,200)
    
    
    
    # TESTING 2 :  returning application.json or not    
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/expensehead/show")
        self.assertEqual(response.content_type,"application/json")



if __name__ == "__main__":
    unittest.main()