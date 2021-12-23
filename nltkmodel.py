import nltk
import json
from nltk import tag
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
​
#import sys
#sys.path.append('../')
#export PYTHONPATH=$PATH=/root/ml-powered-test-fw/api
#export PYTHONPATH=$PATH=/root/ml-powered-test-fw/api/models/NLTKModel
​
​
from testcase_generator.createallscript import create_test_script
baseurl = 'https://virtserver.swaggerhub.com/imadyasha.padhee/MusicAPIZooniverese/1.0.0'
p_baseurl = "https://petstore.swagger.io/v2"
from synonyms import synonym
from parse_yaml_file import parse_yaml
from input_body import get_in_body
​
ps = PorterStemmer()
​
def get_endpoint(user_story, yaml_file, project_id, github_link, base_url):
    stopWords = set(stopwords.words('english'))
    words = word_tokenize(user_story)
    wordsFiltered = []
​
    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)
    tagged = nltk.pos_tag(wordsFiltered)
​
    parse_yaml_response, schema = parse_yaml(yaml_file)
    #print(json.dumps(schema, sort_keys=False, indent=2))
​
    get = ["see","search","observe","get","identify","detect","view","informed"]
    post = ["add","include","upload","annotate"]
    put = ["update","change","edit","filter"]
    delete = ["remove", "delete"]
    req_action=[]
​
    for i in range(len(tagged)):
        if tagged[i][0] in (set(synonym(get))):
            req_action.append(tagged[i])
            req_action.append("get")
​
        elif tagged[i][0] in (set(synonym(post))):
            req_action.append(tagged[i])
            req_action.append("post")
        
        elif tagged[i][0] in (set(synonym(put))):
            req_action.append(tagged[i])
            req_action.append("put")
            
        elif tagged[i][0] in (set(synonym(delete))):
            req_action.append(tagged[i])
            req_action.append("delete")
    
    common_endpoint_tokens = [] 
    for endpoint in parse_yaml_response:
        splitted_endpoint = endpoint.split("/")
        del splitted_endpoint[0]
        lem_endpoint = []
        lem_common_words = []
        for j in range(len(tagged)):
            lem_common_words.append(ps.stem(tagged[j][0]))
        for k in splitted_endpoint:
            lem_endpoint.append(ps.stem(k))
        for i in lem_common_words:
            if i in lem_endpoint:
                common_endpoint_tokens.append(i)
    filtered_common_endpoint_tokens = list(set(common_endpoint_tokens))
​
    for endpoint in parse_yaml_response:
        splitted_endpoint = endpoint.split("/")
        del splitted_endpoint[0]
        lem_endpoint = []
        for k in splitted_endpoint:
            if k.startswith("{"):
                pass
            else:
                lem_endpoint.append(ps.stem(k))
        set_difference=set(lem_endpoint).symmetric_difference(set(filtered_common_endpoint_tokens))
        for method in parse_yaml_response[endpoint]:
            if not set_difference:
                if method==req_action[1]:
                    final_endpoint(endpoint,method,parse_yaml_response,schema,project_id)
            # else:
            #     set_intersection= set(lem_endpoint).intersection(set(filtered_common_endpoint_tokens))
            #     if not set_intersection.symmetric_difference(set(lem_endpoint)):
            #         if method==req_action[1]:
            #             final_endpoint(endpoint,method,parse_yaml_response,schema,project_id)
​
def final_endpoint(endpoint,method,parse_yaml_response,schema,project_id):
    load = {'id': "1"}
    req_endpoint = ""
    #print(endpoint)
    req_endpoint_lst= endpoint.split("{")
    for i in range(len(req_endpoint_lst)):
        if req_endpoint_lst[i].endswith("}"):
            req_endpoint_lst[i]=load["id"]
        req_endpoint = req_endpoint+req_endpoint_lst[i]
    
    endpoint1 = p_baseurl + req_endpoint
    if method=="post" or method=="put":
        if "schema" in parse_yaml_response[endpoint][method]:
            vch_schema = parse_yaml_response[endpoint][method]["schema"]["$ref"].split("/")
            prmtr = get_in_body(vch_schema[-1],schema)
        # if prmtr:
            # p=json.dumps(prmtr, sort_keys=False, indent=2)
            # print(p)
            create_test_script('testscript',project_id, None, method,endpoint1,prmtr)
        else:
            create_test_script('testscript',project_id, None, method,endpoint1 )
    else:
    # print(endpoint1)
        create_test_script('testscript',project_id, None, method,endpoint1 )
    
​
data = "I want to add pet."
get_endpoint(data,"petstore.yaml")
​
# data = "As a user, I want to add info about perceptually similar video items."
# get_endpoint(data,"zooniverse.yaml")
