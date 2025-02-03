import requests

class Broadcast:

	api_endpoint = 'http://batman-ms-broadcast'

	def SendTeamsMessage(meta):

		data = {
			'Purpose': 'batman-incident',
			'Meta': meta
		}

		try:
			result = requests.post(f'{Broadcast.api_endpoint}/api/v1/Teams/Send',json = data,stream = True)

			return True if result.ok else False

		except:
			return False