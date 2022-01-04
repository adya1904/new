#base_file_name = "testALL"


codetop = """         #common in every file # in the top of every file
import requests \n
import restapicalls\n 
def main( ):\n
"""

codebot = """                     #common in every file     #bottom of every file
if __name__ == "__main__":\n
           main() """
           
testcucumber = """
 
from behave import *
import restapicalls
endpoint = None
request = None
headers=None
auth=None
response_code = None
name= None
#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl = 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
#baaseurl = 'https://petstore3.swagger.io/api/v3'
baseurl='{baseurl}'
@given( 'I set {method} {endpoint} API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = '{endpoint}'
@given('I have valid {parameter_value}')
def set_endpoint(context):
  global name
  name = '{parameter_value}'
@when('I send {method} HTTPS request {endpoint}')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= '{method}',url=baseurl+'/{endpoint}',load={parameter},headers={headers},auth={auth})
@then('I receive a valid HTTPS response code 200 from {endpoint} using {method}')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200
"""

addtestcucumber = """
endpoint = None
request = None
headers=None
auth=None
response_code = None
#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl = 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
#baseurl = 'https://petstore3.swagger.io/api/v3'
baseurl='{baseurl}'
@given( 'I set {method} {endpoint} API endpoint')
def set_endpoint(context):
  global endpoint
  endpoint = '{endpoint}'
@given('I have valid {parameter_value}')
def set_endpoint(context):
  global name
  name = '{parameter_value}'
@when('I send {method} HTTPS request {endpoint}')
def send_request(context):
  global request
  global baseurl
  request = restapicalls.api_call(method= '{method}',url=baseurl+'/{endpoint}',load={parameter},headers={headers},auth={auth})
@then('I receive a valid HTTPS response code 200 from {endpoint} using {method}')
def response(context):
  global response_code
  response_code = request[0] 
  assert response_code == 200
"""


def createfile(typefile,base_file_name):  #create a file
    
    if typefile == 'py':
        
        filename = base_file_name + 'auto' + ".py"#sting to store the name of the file
    if typefile == 'feature':
        filename = base_file_name + 'auto' + ".feature"    
    print(filename)    #printing file name
    try:
        

        file = open(filename, "w")   #if there is no file it will create a new file if file exixts then clear it
    except :
        print ("unable to create file")
        
    
    return file



def create_test_script(headers,auth,base_file_name,method, endpoint, parameter=None):     
       #calling the createfile func that returns a file
    method_check = {'get', 'post', 'put' , 'delete'}     #validation of methods
    if method.lower() not in  method_check :
        print ('this is not a correct method')
        return 
    print (type(parameter))                              #validate dictationary
    

    
    
    
    try:                                   #exception handeling
        print("Happy Holidays!")
        file = createfile(typefile = 'py',base_file_name = base_file_name) 
        print (file.name)   
        with open(file.name, 'w') as f:    #open(file.name, w) is for writing things into the file
            f.write(codetop)               #it will append all these into the new file
            f.write("    method ='" + method + "'\n")
            f.write("    endpoint='" + endpoint + "'\n")
            f.write("    parameter=" + str(parameter) + "\n")
            f.write("    headers=" + str(headers) + "\n")
            f.write("    auth=" + str(auth) + "\n")
            f.write("    resp=restapicalls.api_call(method,endpoint,parameter,headers=headers,auth=auth)\n")
            f.write("    print(resp)\n")
            f.write(codebot)
    except Exception as error:
        print (error)
        print ("file modification error")
        return
    
    return file                    # returning the newly created file


def create_cucumber_script(base_file_name,endpoints,methods,parameter_values,parameters,headers,auth):
    try:                                   #exception handeling
        file = createfile(typefile = 'py',base_file_name=base_file_name)
        txt = testcucumber.format(method=methods,endpoint = endpoints, parameter_value= parameter_values, parameter = parameters,headers=headers,auth=auth)  
        #print (testcucumber)  
        with open(file.name, 'w') as f:    #open(file.name, w) is for writing things into the file
            f.write (txt) 
            
                          
            
    except Exception as error:
        print (error)
        print ("file modification error")
        return
    
    return file   

def add_cucumber_script(base_file_name,endpoints,methods,parameter_values,parameters,headers,auth):
    try:                                   #exception handeling
        
        txt = addtestcucumber.format(method=methods,endpoint = endpoints, parameter_value= parameter_values, parameter = parameters,headers=headers,auth=auth)  
        #print (testcucumber)                 #print 
        with open(base_file_name, 'a') as f:    #a is for adding/appending new texts into the file
            f.write (txt) 
            
                          
            
    except Exception as error:
        print (error)
        print ("file modification error")
        return
    
    return f  



def add_feature_script(file,featurename, scenarioname, endpoint, pointingattribute, methods):    
    
    try:                                   #exception handeling
            
        with open(file, 'a') as f:    #open(file.name, w) is for writing things into the file #it will append all these into the new file
            print(f.name)
            f.write (" "   +"\n")    #appending strings into the file

            f.write("Scenario: " + scenarioname +"\n")

            f.write("\t"+"Given I set " + methods +' ' + endpoint + " API endpoint" +"\n")

            f.write("\t"+"And I have valid " + pointingattribute +"\n")

            f.write("\t"+"When I send "+ methods +" HTTPS request "+endpoint+"\n")

            f.write("\t"+"Then I receive a valid HTTPS response code 200 from "+endpoint+" using " + methods+"\n")  

    except Exception as error:
        print (error)
        print ("file modification error")
        return
    
    return file                    # returning the newly created file


def create_feature_script(file,featurename, scenarioname, endpoint, pointingattribute, methods):    
    
    try:                                   #exception handeling
            
        with open(file.name, 'a') as f:    #open(file.name, w) is for writing things into the file
                                             #it will append all these into the new file
            f.write ("Feature: " + featurename +"\n")    #appending strings into the file

            f.write("Scenario: " + scenarioname +"\n")

            f.write("\t"+"Given I set " + methods +' ' + endpoint + " API endpoint" +"\n")

            f.write("\t"+"And I have valid " + pointingattribute +"\n")

            f.write("\t"+"When I send "+ methods +" HTTPS request "+endpoint+"\n")

            f.write("\t"+"Then I receive a valid HTTPS response code 200 from "+endpoint+" using " + methods+"\n")  

            f.close()
    except Exception as error:
        print (error)
        print ("file modification error")
        return
    
    return file                    # returning the newly created file



#def create_file(typescript=None,projectid= "1234",userstoryid=None,method=None,endpoint=None,parameter=None,parameter_values=None,featurename=None,scenarioname=None,pointingattribute=None):
def create_file(typescript='testscript',projectid= "1111",userstoryid="2222",method=None,endpoint=None,parameter=None,consumes=None, authorization=None, parameter_values=None,featurename=None,scenarioname=None,pointingattribute=None,headers=None,auth=None,featuresdir='features/'):
    if typescript == 'testscript':           
        base_file_name = "testAPI"+str(projectid)+str(userstoryid)
        create_test_script(headers=headers,auth=auth,base_file_name=base_file_name,method=method, endpoint= endpoint, parameter=parameter)
    if typescript == 'stepsscript':
        base_file_name =featuresdir+"steps/"+"testcucumber"+str(projectid)+str(userstoryid)
        create_cucumber_script(base_file_name= base_file_name,endpoints=endpoint,methods=method,parameter_values=parameter_values,parameters=parameter,headers=headers,auth=auth)
    
    if typescript == 'createfeature':                            #conditionals
        base_file_name = featuresdir+"testfeature"+str(projectid)+str(userstoryid)                          #base file name
        newfile = createfile(typefile = 'feature',base_file_name = base_file_name) 
        create_feature_script(file=newfile,featurename=featurename, scenarioname=scenarioname, endpoint=endpoint, pointingattribute=pointingattribute, methods=method)
    if typescript == 'addtofeature':                            #conditionals
        base_file_name =featuresdir+"testfeature"+str(projectid)+str(userstoryid)+'auto.feature'                          #base file name
        #exsistingfile=open(base_file_name,'a')
        add_feature_script(file=base_file_name,featurename=featurename, scenarioname=scenarioname, endpoint=endpoint, pointingattribute=pointingattribute, methods=method)  
    if typescript=='addtostepsscript':
        base_file_name =featuresdir+"steps/"+"testcucumber"+str(projectid)+str(userstoryid)+'auto.py'
        add_cucumber_script(base_file_name= base_file_name,endpoints=endpoint,methods=method,parameter_values=parameter_values,parameters=parameter,headers=headers,auth=auth)
       
           
#parameter2 = {"id": "4214","additionalMetadata":"Date22/11/19","file" : "songfile.mp4"}
#baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
#baseurl= 'https://virtserver.swaggerhub.com/zooniverse/petstoredummy/1.0.0'
#baseurl = 'https://petstore3.swagger.io/api/v3'
baseurl='http://httpbin.org'                    #new base url cuz xml didn't worked on petstore

#endpoint =  'pet/' + '10'

#create_file(baseurl=baseurl,parameter_values='id',typescript = 'stepsscript',projectid='hello',userstoryid='world', method = 'GET',endpoint = endpoint,parameter = None) 
#create_file(typescript='stepsscript',projectid='hii',userstoryid='folks',endpoint = 'findByName', method = 'get', parameter_values = 'adyasha', parameter = 'None')   
#create_file(typescript='createfeature',projectid='hey',userstoryid='you',featurename = 'Finding the songs using singer name using GET API', scenarioname ='Get song by singer name' ,endpoint ='findByname' , pointingattribute = ' Singername', method='GET')
#create_file(baseurl=baseurl,typescript = 'testscript',method='get',endpoint=endpoint,projectid='hello',userstoryid='world')
#create_file(typescript='createfeature',projectid='peet',userstoryid='storee',featurename = 'Finding the pets using pet id using GET API', scenarioname ='Get pet by pet id' ,endpoint =endpoint , pointingattribute = 'petid', method='GET',parameter_values='petid')
#create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename = 'Finding the order using order id using GET API', scenarioname ='Get order by order id' ,endpoint ='store/order/2' , pointingattribute = 'orderid', method='GET',parameter_values='orderid')
#create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename = 'log users using userid using GET API', scenarioname ='log user using user id' ,endpoint ='user/login' , pointingattribute = 'userid', method='GET',parameter_values='userid',parameter={'username':'addy','password':'paddy'})
#create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename='get user by user name using GET API',scenarioname='get user by user name',endpoint = 'user/user1',pointingattribute='username', method = 'GET', parameter_values = 'username')
#create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename='placing order for pet',scenarioname='place order',endpoint = 'store/order',pointingattribute='ordername', method = 'POST', parameter_values = 'ordername',parameter={"id": 2,  "petId": 4,"quantity": 2,"shipDate": "2021-12-22T04:03:05.280Z","status": "available","complete": 'false'},baseurl=baseurl)
#create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename='add a new pet to the store',scenarioname='adding pet',endpoint='pet',pointingattribute='petnumber',method='POST',parameter_values='petnumber',parameter={"id": 0,"category": {"id": 0,"name": "string"},"name": "doggie","photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"})
#create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename='place an order of pet to the store',scenarioname='ordering pet',endpoint='store/order',pointingattribute='petorder',method='POST',parameter_values='petorder',parameter={"id": 10,"petId": 198772,"quantity": 7,"shipDate": "2021-12-24T03:36:33.067Z","status": "approved","complete": 'true'})
#create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename='update an exsisting pet in the store',scenarioname='update pet',endpoint='pet',pointingattribute='existingpetid',method='PUT',parameter_values='existingpetid',parameter={"id": 10,"name": "doggie","category": {"id": 1,"name": "Dogs"  },"photoUrls": ["string"  ],"tags": [{"id": 0,"name": "string"    }],"status": "available"})
#create_file(typescript='addtofeature',projectid='peet',userstoryid='storee',featurename = 'delete the order using order id using delete method', scenarioname ='delete order by order id' ,endpoint ='store/order/1' , pointingattribute = 'deleteorderid', method='DELETE',parameter_values='deleteorderid')
create_file(baseurl=baseurl,typescript='createfeature',projectid='peet',userstoryid='storee',featurename = 'pssing xml as parameters', scenarioname ='xml parameters' ,endpoint ='post' , pointingattribute = 'postxml', method='POST',parameter="\"<?xml version='1.0' encoding='utf-8'?><a>adyasha</a>\"",parameter_values='postxml',headers={'Content-Type': 'application/xml'})


#create_file(typescript='stepsscript',projectid='peet',userstoryid='storee',featurename = 'Finding the pets using pet id using GET API', scenarioname ='Get pet by pet id' ,endpoint =endpoint , pointingattribute = 'petid', method='GET',parameter_values='petid',headers = {'Content-type': 'application/json'})
#create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename = 'Finding the order using order id using GET API', scenarioname ='Get order by order id' ,endpoint ='store/order/2' , pointingattribute = 'orderid', method='GET',parameter_values='orderid',headers = {'Content-type': 'application/json'})
#create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename = 'log users using userid using GET API', scenarioname ='log user using user id' ,endpoint ='user/login' , pointingattribute = 'userid', method='GET',parameter_values='userid',parameter={'username':'addy','password':'paddy'},headers = {'Content-type': 'application/json'})
#create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename='get user by user name using GET API',scenarioname='get user by user name',endpoint = 'user/user1',pointingattribute='username', method = 'GET', parameter_values = 'username',headers = {'Content-type': 'application/json'})
#create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename='placing order for pet',scenarioname='place order',endpoint = 'store/order',pointingattribute='ordername', method = 'POST', parameter_values = 'ordername',parameter={"id": 2,  "petId": 4,"quantity": 2,"shipDate": "2021-12-22T04:03:05.280Z","status": "available","complete": 'false'},baseurl=baseurl)
#create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename='add a new pet to the store',scenarioname='adding pet',endpoint='pet',pointingattribute='petnumber',method='POST',parameter_values='petnumber',parameter={"id": 0,"category": {"id": 0,"name": "string"},"name": "doggie","photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"})#,headers = {'Content-type': 'application/text'})
#create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename='place an order of pet to the store',scenarioname='ordering pet',endpoint='store/order',pointingattribute='petorder',method='POST',parameter_values='petorder',parameter={"id": 10,"petId": 198772,"quantity": 7,"shipDate": "2021-12-24T03:36:33.067Z","status": "approved","complete": 'true'})#,headers = {'Content-type': 'application/json'})
#create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename='update an exsisting pet in the store',scenarioname='update pet',endpoint='pet',pointingattribute='existingpetid',method='PUT',parameter_values='existingpetid',parameter={"id": 10,"name": "doggie","category": {"id": 1,"name": "Dogs"  },"photoUrls": ["string"  ],"tags": [{"id": 0,"name": "string"    }],"status": "available"})#,headers = {'Content-type': 'application/json'}) 
#create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename = 'create a list of users with given input array', scenarioname ='create user order' ,endpoint ='createWithList' , pointingattribute = 'orderlist', method='POST',parameter=[{"id": 10,"username": "theUser","firstName": "John","lastName": "James","email": "john@email.com","password": "12345","phone": "12345","userStatus": 1  }],parameter_values='orderlist')  
#create_file(typescript='addtostepsscript',projectid='peet',userstoryid='storee',featurename = 'delete the order using order id using delete method', scenarioname ='delete order by order id' ,endpoint ='store/order/1' , pointingattribute = 'deleteorderid', method='DELETE',parameter_values='deleteorderid',headers = {'Content-type': 'application/json'})
create_file(baseurl=baseurl,typescript='stepsscript',projectid='peet',userstoryid='storee',featurename = 'passing xml as parameters', scenarioname ='xml parameters' ,endpoint ='post' , pointingattribute = 'postxml', method='POST',parameter="\"<?xml version='1.0' encoding='utf-8'?><a>adyasha</a>\"",parameter_values='postxml',headers={'Content-Type': 'application/xml'})
create_file(baseurl=baseurl,typescript='testscript',projectid='peet',userstoryid='storee',featurename = 'passing xml as parameters', scenarioname ='xml parameters' ,endpoint ='post' , pointingattribute = 'postxml', method='POST',parameter="\"<?xml version='1.0' encoding='utf-8'?><a>adyasha</a>\"",parameter_values='postxml',headers={'Content-Type': 'application/xml'})
