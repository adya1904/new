import json
import random
​
def get_in_body(req_schema,definition):
  pet=("caty", "doggie", "ruby","chimpu", "zoozy", "jimmy", "puppy", "rocky")
  category=("dogs","cats","birds")
  tags=("pet1","pet2","pet3")
  status = ("pending","available","sold")
  body = dict()
  for schema in definition:
    if schema==req_schema:
      for atrbt in definition[schema]["properties"]:
        for a in definition[schema]["properties"][atrbt]:
          if a=="$ref":
            A=definition[schema]["properties"][atrbt][a].split("/")
            body.update({atrbt:get_in_body(A[-1],definition)})
          elif a=="type":
            if definition[schema]["properties"][atrbt][a]=="array":
              for i in definition[schema]["properties"][atrbt]:
                if i=="items":
                  for j in definition[schema]["properties"][atrbt][i]:
                    x= definition[schema]["properties"][atrbt][i][j].split("/")
                    some_var=definition[schema]["properties"][atrbt]
                    definition[schema]["properties"][atrbt] = []
                    if len(x)==1:
                      definition[schema]["properties"][atrbt].append(some_var[i][j])
                      definition[schema]["properties"][atrbt][0] = "photo.png"
                      y= {atrbt:definition[schema]["properties"][atrbt]}
                      body.update(y)
                    else:
                      definition[schema]["properties"][atrbt].append(get_in_body(x[-1],definition))
                      z= {atrbt:definition[schema]["properties"][atrbt]}
                      body.update(z)
            elif definition[schema]["properties"][atrbt][a]=="integer":
              definition[schema]["properties"][atrbt]["type"]=random.randint(0,10)
              body.update({atrbt:definition[schema]["properties"][atrbt]["type"]})
            else:
              if atrbt == "status":
                definition[schema]["properties"][atrbt]["type"]=random.choice(status)
              elif schema == 'Category':
                definition[schema]["properties"][atrbt]["type"]=random.choice(category)
              elif schema == "Tag":
                definition[schema]["properties"][atrbt]["type"]=random.choice(tags)
              else:
                definition[schema]["properties"][atrbt]["type"]=random.choice(pet)
              body.update({atrbt:definition[schema]["properties"][atrbt]["type"]})
  return(body)
  
# xxx=get_in_body("Order",definition1)
# p=json.dumps(xxx, sort_keys=False, indent=2)
# print(p)
