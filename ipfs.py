import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_string = json.dumps(data)
	# infura_url = "https://api.pinata.cloud/ipfs/"

	project_id = 'test1'
	project_secret = '582e947d3d224196bb08eb926aa5eda2'

	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', json=json_string, auth=(project_id, project_secret))
	result = response.text
	cid = result
	print(result)
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE

	#use cat

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
