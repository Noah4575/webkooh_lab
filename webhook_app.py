from flask import Flask, request
import subprocess
 
app = Flask(__name__)

@app.route('/staging', methods=['POST'])
def staging():
    payload = request.json
    ref = payload.get('ref', '')

    # Check if the push is to the desired branch, e.g., 'refs/heads/testing'
    if ref == 'refs/heads/staging':
        # this hook is coming from a push done to the "testing" branch
        # Add your code logic here
        subprocess.run(['cmd', '/c', 'staging_script.sh'], shell=True)
        print("Staging Hook Triggered")
        return 'OK', 200
    else:
        print("Staging Hook Skipped")
        return 'Skip',200
    
@app.route('/deploy', methods=['POST'])

def deploy():   
    payload = request.json
    ref = payload.get('ref', '')

    # Check if the push is to the desired branch, e.g., 'refs/heads/testing'
    if ref == 'refs/heads/deploy':
        # this hook is coming from a push done to the "testing" branch
        # Add your code logic here
        subprocess.run(['cmd', '/c', 'deploy_script.sh'], shell=True)
        print("Deploy Hook Triggered")
        return 'OK', 200
    else:
        print("Deploy Hook Skipped")
        return 'Skip',200
    
if __name__ == '__main__':
    app.run(debug=True,port=5000)