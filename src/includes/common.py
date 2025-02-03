import inspect
import json

from datetime import datetime, timezone
from services.logger import Logger

class Common:

	def Date():

		return datetime.now(timezone.utc).strftime('%Y-%m-%d')

	def Datetime():

		return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

	def DateObject():

		return datetime.strptime(Common.Date(), '%Y-%m-%d')

	def DatetimeObject():

		return datetime.strptime(Common.Datetime(), '%Y-%m-%d %H:%M:%S')

	def MonthDatetime():

		return datetime.now(timezone.utc).strftime('%B %d, %Y')
	
	def Timestamp():

		timestamp = Common.Datetime()
		timestamp = timestamp.replace('-', '').replace(' ', '').replace(':', '')

		return timestamp
	
	def ParseDataToDict(data):

		if not data or data is None or (isinstance(data, str) and data.strip() == ''):
			return {}

		if isinstance(data, str):
			try:
				data = json.loads(data)

			except Exception as e:
				Logger.CreateExceptionLog(inspect.stack()[0][3], str(e), data)

				raise ValueError('Invalid JSON format')
		
		return data