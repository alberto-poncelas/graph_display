from flask import Flask
from flask_cors import CORS
import json
import sys



filename=sys.argv[1]


app = Flask(__name__)
CORS(app)





flatten = lambda list: [item for sublist in list for item in sublist]

node2json = lambda node: json.loads('{ "id": "'+node+'" }')
pair2json = lambda pair: json.loads('{ "source": "'+pair[0]+'", "target": "'+pair[1]+'" }')


def load_data():
	with open(filename,"r") as f:
		data_raw = f.readlines()
	#Formal data
	data=[x.strip().split("\t") for x in data_raw]
	#Obtain nodes
	nodes = set(flatten(data))
	#to json format
	nodesjson=[node2json(x) for x in nodes]
	linksjson=[pair2json(x) for x in data]
	#Convert json to string
	json_out={"nodes" : nodesjson , "links" : linksjson }
	return json.dumps(json_out)




@app.route('/')
def show_json():
    #return '{ "nodes": [ { "id": " node 1" }, { "id": "node 2" } ], "links": [ { "source": " node 1", "target": "node 2" } ] } '
    out = load_data()
    return out

if __name__ == '__main__':
    app.run()