import sys
# sys.path.append("/usr/local/lib/python3.9/dist-packages/")
# sys.path.append("/usr/lib/python3/dist-packages/")
# sys.path.append("/home/vish182/.local/lib/python3.9/site-packages")
from flask import Flask
from flask import jsonify, request
import json
from flask_cors import CORS
import autochord

app = Flask(__name__)
CORS(app)


@app.route('/getChords', methods=["POST"])
def addUser():
    print(request.json['path'])
    path = request.json['path']
    op = autochord.recognize('../tab-backend/handlers/audio/music/'+str(path), lab_fn='chords.lab')
    print(op)
    res = []

    for i in op:
        res.append(i[2])
        
    return jsonify(res)



if __name__ == "__main__":
    print("hello world")
    app.run(host='0.0.0.0', port=6000,debug=True)
    

