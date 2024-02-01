import requests
import json

''' Fill in the following information '''
# General information
YOUR_EMAIL = "hailind2@illinois.edu" # <put your coursera account email>,
YOUR_SECRET = "1buXHrdLncAaSJna" # <put your secret token from coursera>

# Section 1s
IP_ADDRESS1 = "54.145.174.142:5000" # <put your first EC2 instance's IP address>
IP_ADDRESS2 = "54.175.137.124:5000" # <put your second instance's IP address>
YOUR_LOAD_BALANCER1 = "MP2UIUC-1561337335.us-east-1.elb.amazonaws.com" # <put your load_balancer address for section 1>
# Section 2
YOUR_LOAD_BALANCER2 = "MP23A-4-1406014663.us-east-1.elb.amazonaws.com" # <put your load_balancer address for section 2>, 

''' Don't change the following '''
url = "https://ekwygde36j.execute-api.us-east-1.amazonaws.com/alpha/execution"
input = {
            'ip_address1': IP_ADDRESS1,
            'ip_address2': IP_ADDRESS2,
			'load_balancer1': YOUR_LOAD_BALANCER1, 
            'load_balancer2': YOUR_LOAD_BALANCER2,
			'submitterEmail': YOUR_EMAIL, 
			'secret': YOUR_SECRET, 
		}
payload = { "input": json.dumps(input),
    		"stateMachineArn": "arn:aws:states:us-east-1:913708708374:stateMachine:mp2grader"
        }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)