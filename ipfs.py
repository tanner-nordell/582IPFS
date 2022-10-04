import requests
import json


def pin_to_ipfs(data):
	assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"
	# YOUR CODE HERE


	#with open('data.json', 'w') as f:
	#	json.dump(data,f)


	# infura_url = "https://api.pinata.cloud/ipfs/"

	project_id = '2FeGjmTGzI5aPZ1hqGGcmWbFbsU'
	project_secret = '1324c778cf5eb87efb37dca236472b1c'

	print(project_id)
	print(project_secret)

	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files = data,
							 auth=(project_id, project_secret))


	result = response.text
	cid = result
	print(result)
	return cid


def get_from_ipfs(cid, content_type="json"):
	assert isinstance(cid, str), f"get_from_ipfs accepts a cid in the form of a string"
	# YOUR CODE HERE

	# use cat

	assert isinstance(data, dict), f"get_from_ipfs should return a dict"
	return data
