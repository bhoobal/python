import os
import json
import xmltodict

propfname="run.properties"
testresultfname= "junitResult.xml"

logresult = {
   "job_number": "integer",
   "brand":  "string ",
   "revision":  "integer ",
   "runtype":  "string ",
   "category":  "string ",
   "job_name":  "string ",
   "file":  "string ",
   "name":  "string ",
   "timestamp":  "timestamp ",
   "classname":  "string ",
   "testname":  "string ",
   "duration":  "numeric ",
   "skipped":  "boolean ",
   "passed":  "boolean ",
   "starttime":  "timestamp ",
   "stdout":  "string ",
   "stderr":  "string ",
   "id":  "string "
}


def pushtoesindes(path):
    print("Inside es index",path)
    if not os.path.exists(path):
        print("ERROR! Invalid location")
        return

    files = os.listdir(path)
    runprop = {}

    
    for file in files:
        testfiles= os.listdir(path+'/'+ file)
        for testfile in testfiles:        
            logresult["job_number"]=file
            # run properties we need the following information: brand, revision, runtype, category, job_name
            if (testfile == propfname):
                filepath= path+'/'+ file+'/'+testfile
                with open(filepath) as fh:
                    for line in fh:
                        command, description = line.strip().split("=",1)
                        
                        runprop[command] = description.strip()
                        logresult[command] = description.strip()
            elif (testfile == testresultfname):
                xmlfilepath= path+'/'+ file+'/'+testfile
                with open(xmlfilepath) as xml_file:
                    data_dict = xmltodict.parse(xml_file.read())
                    xml_file.close()
                    json_data = json.dumps(data_dict)   
                    d=json.loads(json_data)                                
                    logresult["file"]=d["result"]["suites"]["suite"][0]["file"]
                    logresult["name"]=d['result']['suites']['suite'][0]['name']
                    logresult["stdout"]=d['result']['suites']['suite'][0]['stdout']
                    logresult["stdout"]=d['result']['suites']['suite'][0]['stderr']                                   

        print ("Job -", file, logresult, "\n")

if __name__ == "__main__":
    try:        
        pushtoesindes(r"./dataset1")

    except Exception as e:
        print(f"Error: {e}")        
