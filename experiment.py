import requests
import json

test_prompts = ["Hi!" , 
                "Explain complex numbers.", 
                "What is 20/4?",
                "Write function for finding a local minimum of a given function on an interval in Python.",
                "Write function for finding a local minimum of a given function on an interval in Java.",
                "Write a query in SQL for finding the biggest value in the column 'cost' of table 'spendings'."]

models = ["deepseek-coder:latest",
          "dolphin-phi:latest", 
          "orca-mini:latest", 
          "phi:latest", 
          "stablelm-zephyr:latest", 
          "starcoder:latest", 
          "tinyllama:latest"]
          

model = models[0]
prompt = test_prompts[0]


for prompt in test_prompts:
    for model in models:

        request = {"model": model, "prompt": prompt, "stream": False}

        response = requests.post("http://localhost:11434/api/generate", json=request)

        
        print("\n\n", model, "--> ", response.status_code, "--> \"", response.json()["response"], "\"")

        log = {"model":model, "prompt": prompt, "response": response.json()["response"], "exit_code": response.status_code, "full_response": response.json()}

        f = open("test_log.txt", "a")
        f.write(json.dumps(log))
        f.close()
