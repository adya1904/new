import json
#base_file_name = "testALL"
codetop = """            #common in everyfile into the top
import requests \n
import testcase_generator.urlresponse \n
def main(): \n
"""
    
codebot = """              #common in everyfile into the bottom
if __name__ == "__main__":\n
          main() """
          
testcucumber = """
from os import name
from behave import *
import restapicalls
endpoint = None
request = None
response_code = None
baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
@given('I set {method} {endpoint} API endpoint')
def set_endpoint(context):
    global endpoint
    endpoint = '{endpoint}'
@given('I have a valid {parameter_value}')
def set_endpoint(context):
    global name
    name = '{parameter_value}'
@when('I send {method}HTTPS request')
def send_request(context):
    global request
    global baseurl
    request = restapicalls.api_call(method='{method}',url=baseurl+'/song/{endpoint}',load={parameter})
@then('I receive a valid HTTPS response code 200')
def response(context):
    global response_code
    response_code = request[0]
    assert response_code == 200
"""
def createfile(typefile,base_file_name):  #function to create a new file
    if typefile == 'py':
        filename = base_file_name + 'auto' + ".py"        #to store the file name
    if typefile == 'feature':
        filename = base_file_name + 'auto' + ".feature" 
    print(filename)
    try:
        file = open(filename, "w")  #open is a function with stingparameter a to create a file
    except:
        print("unable to create file")
    return file
def create_test_script(typescript,projectid, userstoryid, method,endpoint,parameter=None,parameter_values=None,featurename=None,scenarioname=None,pointingattribute=None):    #validation of method
    method_check = {'get','post','put','delete'}      #method_check is a set
    if method.lower() not in method_check:
        print('this is not the correct method')
        return
    arg_data = dict()
    arg_data.update({"method":method})
    arg_data.update({"endpoint":endpoint})
    arg_data.update({"parameter":parameter})
    
    try:
        file = createfile(typefile = 'py',base_file_name=projectid)         #calling createfile function that will return the new file
        with open(file.name, 'w') as f:   # w string for writing contents into the new file
            f.write(codetop)
            f.write("    data = ")
            f.write(json.dumps(arg_data))
            f.write('\n')
            f.write("    resp=testcase_generator.urlresponse.api_call(method,endpoint,parameter)\n")
            f.write("    print(resp)\n")
            f.write(codebot)
    except Exception as error:
        print(error)
        print("file modification error")
        return
    if typescript == 'testscript':             #conditionals
        base_file_name = "testAPI"+ projectid + userstoryid              #basefile name
        create_test_script(base_file_name,method, endpoint, parameter)
    if typescript == 'stepsscript':
        base_file_name = "testcucumber"+projectid + userstoryid
        create_cucumber_script(base_file_name=base_file_name,endpoints=endpoint,methods=method,parameters=parameter,parameter_values=parameter_values)
    if typescript == 'createfeature':
        base_file_name = "testfeature"+projectid+userstoryid
        newfile = createfile(typefile = 'feature',base_file_name = base_file_name)
        create_feature_script(file=newfile,featurename=featurename,scenarioname=scenarioname,endpoint=endpoint,pointingattribute=pointingattribute,methods=method)
    return file           #returns the newly created file
def create_cucumber_script(base_file_name,endpoints, methods, parameters, parameter_values):
    try:
        file = createfile(typefile = 'py',base_file_name=base_file_name)
        txt = testcucumber.format(method=methods,endpoint=endpoints,parameter=parameters,parameter_value=parameter_values)
        print(testcucumber)
        with open(file.name, 'w') as f:
            f.write (txt)
            
    except Exception as error:
        print(error)
        print("file modification error")
        return
    return file
def create_feature_script(file,featurename,scenarioname,endpoint,pointingattribute,methods):    #validation of method
    
    
    try:
                #calling createfile function that will return the new file
        with open(file.name, 'a') as f:   # a stringparameter for appending into the new file
            
            f.write("Feature: " + featurename + "\n") #appending strings to new file
            f.write("Scenario: " + scenarioname + "\n")
            f.write("Given I set " + methods+ ' '+ endpoint + "API endpoint" + "\n")
            f.write("And I have valid" + pointingattribute + "\n")
            f.write("When I send" + methods + "HTTPS request\n")
            f.write("Then I receive a valid HTTPS response code 200\n")
            f.write("Examples:\n")
            
    except Exception as error:
        print(error)
        print("file modification error")
        return
    return file        #returns the newly created file
# def create_file(typescript=None,projectid= None,userstoryid=None,method=None,endpoint=None,parameter=None,parameter_values=None,featurename=None,scenarioname=None,pointingattribute=None):
#     if typescript == 'testscript':             #conditionals
#         base_file_name = "testAPI"+ projectid + userstoryid              #basefile name
#         create_test_script(base_file_name=base_file_name,method = method,endpoint = endpoint,parameter = parameter)
#     if typescript == 'stepsscript':
#         base_file_name = "testcucumber"+projectid + userstoryid
#         create_cucumber_script(base_file_name=base_file_name,endpoints=endpoint,methods=method,parameters=parameter,parameter_values=parameter_values)
#     if typescript == 'createfeature':
#         base_file_name = "testfeature"+projectid+userstoryid
#         newfile = createfile(typefile = 'feature',base_file_name = base_file_name)
#         create_feature_script(file=newfile,featurename=featurename,scenarioname=scenarioname,endpoint=endpoint,pointingattribute=pointingattribute,methods=method)
# parameter2 = {"id": "4214","additionalMetadata":"Date22/11/19","file":"songfile.mp4"}
# baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
# endpoint2 = baseurl + '/song/' + parameter2['id'] + '/uploadImage'
# method2 = 'post'
#create_file(typescript='testscript',projectid='hello',userstoryid='folks',method=method2,endpoint=endpoint2,parameter=parameter2)
#create_file (typescript='stepsscript',projectid='hey',userstoryid='world',endpoint='findByName', method='post',parameter= 'None',parameter_values='adyasha') 
#create_file(typescript='createfeature',projectid='hi',userstoryid='you',featurename =' Uploading images or songs using ID in POST API', scenarioname ='Upload songs or images', endpoint = 'song/songID/uploadimage', pointingattribute = 'songID', method='POST')
