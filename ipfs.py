import requests
import json


def pin_to_ipfs(data):
	assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"
	# YOUR CODE HERE
	#print(data)

	with open('data.json', 'w') as f:
		json.dump(data,f)


	project_id = '2FeGjmTGzI5aPZ1hqGGcmWbFbsU'
	project_secret = '1324c778cf5eb87efb37dca236472b1c'

	#print(project_id)
	#print(project_secret)

	response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files = {'file': json.dumps(data)},
							 auth=(project_id, project_secret))


	result = response.json()
	cid = result.get("Hash")
	#print(cid)
	return cid


def get_from_ipfs(cid, content_type="json"):
	assert isinstance(cid, str), f"get_from_ipfs accepts a cid in the form of a string"
	# YOUR CODE HERE
	project_id = '2FeGjmTGzI5aPZ1hqGGcmWbFbsU'
	project_secret = '1324c778cf5eb87efb37dca236472b1c'
	response = requests.post(f'https://ipfs.infura.io:5001/api/v0/cat?arg={cid}', auth=(project_id, project_secret))
	print(response.text)
	data = response.json()

	assert isinstance(data, dict), f"get_from_ipfs should return a dict"
	return data
