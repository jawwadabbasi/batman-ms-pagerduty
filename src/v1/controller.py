import inspect

from services.logger import Logger
from v1.pagerduty import Pagerduty

class Ctrl_v1:

    def Response(endpoint, request_data=None, api_data=None, log=True):

        if log is True:
            Logger.CreateServiceLog(endpoint, request_data, api_data)

        return api_data

    def BadRequest(endpoint, request_data=None):

        api_data = {}
        api_data['ApiHttpResponse'] = 400
        api_data['ApiMessages'] = ['ERROR - Missing required parameters']
        api_data['ApiResult'] = []

        Logger.CreateServiceLog(endpoint, request_data, api_data)

        return api_data

    def Get(request_data):

        if (not request_data.get('Purpose')):
            return Ctrl_v1.BadRequest(inspect.stack()[0][3], request_data)

        api_data = Pagerduty.Get(
            request_data.get('Purpose'),
            request_data.get('Meta', None)
        )

        return Ctrl_v1.Response(inspect.stack()[0][3], request_data, api_data)