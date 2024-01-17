from flask import Flask, request
import subprocess
import os
 
app = Flask(__name__)

@app.route('/staging', methods=['POST'])
def staging():
    payload = request.json
    ref = payload.get('ref', '')
    # Check if the push is to the desired branch, e.g., 'refs/heads/testing'
    if ref == 'refs/heads/staging':
        # this hook is coming from a push done to the "testing" branch
        # Add your code logic here
        os.system("git pull")
        os.system("pip install -r ./pull_app/requirements.txt")
        os.system("python ./pull_app/test-app.py")

        #subprocess.run(['cmd', '/c', 'staging_script.sh'], shell=True)
        print("Staging Hook Triggered")
        return 'OK', 200
    else:
        print("Staging Hook Skipped")
        return 'Skip',200
     
@app.route('/main', methods=['POST'])
def deploy():
    print("Deploy endpoint accessed")
    payload = request.json
    ref = payload.get('ref', '')
    print("THIS IS THE REF",ref)
    # Check if the push is to the desired branch, e.g., 'refs/heads/testing'
    if ref == 'refs/heads/main':
        # this hook is coming from a push done to the "testing" branch
        # Add your code logic here
        os.system("git pull")
        os.system("pip install -r ./pull_app/requirements.txt")
        print("Before running app.py")
        #os.system("python ./pull_app/app.py")
        subprocess.Popen(['python', './pull_app/app.py'])
        print("After running app.py")
        print("Deploy Hook Triggered")
        return 'OK', 400
    else:
        print("Deploy Hook Skipped") 
        return 'Skip',400

if __name__ == '__main__':
    app.run(port=5000)