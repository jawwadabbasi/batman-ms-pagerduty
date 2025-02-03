import settings
import requests
import inspect
import json

from services.logger import Logger

class Handler:

	def InvokeApi(method,service,endpoint,request_body):

		headers = {
			'Authorization': f'Token token={settings.PAGERDUTY_TOKEN}'
		}

		if method == 'GET':

			try:
				result = requests.get(f"{service}{endpoint}",params=request_body,stream=False,headers=headers,timeout=30)

				return result.json() if result.ok else False

			except Exception as e:
				Logger.CreateExceptionLog(inspect.stack()[0][3], str(e), f"ERROR - {method} request to application {service} failed with payload: " + json.dumps(request_body))

				return False
		
		if method == 'POST':

			try:
				result = requests.post(f"{service}{endpoint}",json=request_body,stream=False,headers=headers,timeout=30)

				return result.json() if result.ok else False
			
			except Exception as e:
				Logger.CreateExceptionLog(inspect.stack()[0][3], str(e), f"ERROR - {method} request to application {service} failed with payload: " + json.dumps(request_body))

				return False
		
		Logger.CreateExceptionLog(inspect.stack()[0][3], f"ERROR - {method} request to application {service} failed", json.dumps(request_body))

		return False