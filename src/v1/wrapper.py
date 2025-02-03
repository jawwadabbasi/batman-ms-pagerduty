import concurrent.futures
import inspect
import json

from services.logger import Logger

class Wrapper:
	
	def ListRequest(x):
		
		try:
			return {
				'LastUpdated': str(x['lu_date']),
				'Date': str(x['date']),
			}
		
		except Exception as e:
			Logger.CreateExceptionLog(inspect.stack()[0][3],str(e),'ERROR - Could not wrap data')

			return False
		
	def Package(result,kind):

		data = []

		if type(result) != list:
			return data
		
		if kind not in [
			'list-requests'
		]:
			return data

		threads = []
		
		with concurrent.futures.ThreadPoolExecutor() as executor:
			for x in result:
				if kind == 'list-requests':
					threads.append(executor.submit(Wrapper.ListRequest,x))

		for x in threads:
			z = x.result()

			if z:
				data.append(z)

		return data