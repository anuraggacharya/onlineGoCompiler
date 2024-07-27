from fastapi import FastAPI
import subprocess

app=FastAPI()

def executeGo(filename):
    try:
        command=f"go run {filename}"
        result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Command returned non-zero exit status {e.returncode}")
        return e.stderr
    else:
        #print("Command executed successfully")
        #print(f"Output:\n{result.stdout}")
        return result.stdout
        

@app.get("/")
def executeCode():
    result=executeGo("hello.go")
    return {"output":result}