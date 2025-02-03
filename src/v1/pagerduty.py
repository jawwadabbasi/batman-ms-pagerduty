import settings
import json

from includes.common import Common
from v1.handler import Handler

class Pagerduty:

    def Get(purpose,meta={}):

        api_data = {}
        api_data['ApiHttpResponse'] = 500
        api_data['ApiMessages'] = []
        api_data['ApiResult'] = []

        try:
            purpose = str(purpose).strip().lower()
            meta = Common.ParseDataToDict(meta)
        
        except:
            api_data['ApiHttpResponse'] = 400
            api_data['ApiMessages'] += ['INFO - Invalid arguments']

            return api_data
        
        pd = Pagerduty.Compose(purpose,meta if meta else {})

        if not pd:
            api_data['ApiHttpResponse'] = 400
            api_data['ApiMessages'] += ['ERROR - Unsupported purpose']

            return api_data
        
        result = Handler.InvokeApi(
            pd['Method'],
            pd['Service'],
            pd['Endpoint'],
            pd['RequestBody']
        )

        if not result:
            api_data['ApiHttpResponse'] = 400
            api_data['ApiMessages'] += ['ERROR - Request to PagerDuty failed']

            return api_data

        api_data['ApiHttpResponse'] = 200
        api_data['ApiMessages'] += ['INFO - Request processed successfully']
        api_data['ApiResult'] = result

        return api_data
    
    def Request(endpoint,payload={}):

        pd = Pagerduty.Compose(endpoint,payload)

        if not pd:
            return False
        
        return Handler.InvokeApi(
            pd['Method'],
            pd['Service'],
            pd['Endpoint'],
            pd['RequestBody']
        )

    def Compose(purpose,meta={}):

        if purpose == 'oncallinfo':
            return Pagerduty.ComposeGetOnCall(meta)
        
        if purpose == 'teaminfo':
            return Pagerduty.ComposeGetTeam(meta)
        
        if purpose == 'teammembers':
            return Pagerduty.ComposeGetTeamMembers(meta)
        
        if purpose == 'userinfo':
            return Pagerduty.ComposeGetUser(meta)
        
        if purpose == 'usercontact':
            return Pagerduty.ComposeGetUserContactMethod(meta)
        
        if purpose == 'scheduleinfo':
            return Pagerduty.ComposeGetSchedule(meta)
        
        if purpose == 'incidentinfo':
            return Pagerduty.ComposeGetIncident(meta)
        
        if purpose == 'schedules':
            return Pagerduty.ComposeListSchedule(meta)
        
        if purpose == 'incidents':
            return Pagerduty.ComposeListIncident(meta)
        
    def ComposeGetOnCall(meta):

        return {
            "Service": settings.PAGERDUTY_API,
            "Endpoint": "/oncalls",
            "Method": "GET",
            "RequestBody": {
                "team_ids[]": meta.get("TeamId", settings.PAGERDUTY_BATMAN_TEAMID),
                "schedule_ids[]": meta.get("ScheduleId", settings.PAGERDUTY_BATMAN_SCHEDULEID),
                "limit": meta.get("Limit", 25),
                "offset": meta.get("Offset", 0),
                "total": True,
                "time_zone": "UTC",
                "since": meta.get("StartDate", ""),
                "until": meta.get("EndDate", "")
            }
        }
    
    def ComposeGetTeam(meta):

        return {
            "Service": settings.PAGERDUTY_API,
            "Endpoint": f"/teams/{meta.get('TeamId', settings.PAGERDUTY_BATMAN_TEAMID)}",
            "Method": "GET",
            "RequestBody": {
                "time_zone": "UTC"
            }
        }
    
    def ComposeGetTeamMembers(meta):

        return {
            "Service": settings.PAGERDUTY_API,
            "Endpoint": f"/teams/{meta.get('TeamId', settings.PAGERDUTY_BATMAN_TEAMID)}/members",
            "Method": "GET",
            "RequestBody": {
                "time_zone": "UTC"
            }
        }
    
    def ComposeGetUser(meta):

        return {
            "Service": settings.PAGERDUTY_API,
            "Endpoint": f"/users/{meta.get('UserId')}",
            "Method": "GET",
            "RequestBody": {
                "time_zone": "UTC"
            }
        }
    
    def ComposeGetUserContactMethod(meta):

        return {
            "Service": settings.PAGERDUTY_API,
            "Endpoint": f"/users/{meta.get('UserId')}/contact_methods/{meta.get('ContactMethodId')}",
            "Method": "GET",
            "RequestBody": {
                "time_zone": "UTC"
            }
        }
    
    def ComposeGetSchedule(meta):

        return {
            "Service": settings.PAGERDUTY_API,
            "Endpoint": f"/schedules/{meta.get('ScheduleId', settings.PAGERDUTY_BATMAN_SCHEDULEID)}",
            "Method": "GET",
            "RequestBody": {
                "time_zone": "UTC"
            }
        }
    
    def ComposeGetIncident(meta):

        return {
            "Service": settings.PAGERDUTY_API,
            "Endpoint": f"/incidents/{meta.get('IncidentNumber')}",
            "Method": "GET",
            "RequestBody": {
                "time_zone": "UTC"
            }
        }
    
    def ComposeListSchedule(meta):

        return {
            "Service": settings.PAGERDUTY_API,
            "Endpoint": "/schedules",
            "Method": "GET",
            "RequestBody": {
                "total": True,
                "limit": meta.get('Limit', 25),
                "Offset": meta.get('Offset'),
                "time_zone": "UTC"
            }
        }
    
    def ComposeListIncident(meta):

        return {
            "Service": settings.PAGERDUTY_API,
            "Endpoint": "/incidents",
            "Method": "GET",
            "RequestBody": {
                "total": True,
                "limit": meta.get('Limit', 25),
                "Offset": meta.get('Offset'),
                "team_ids[]" : meta.get('TeamId', settings.PAGERDUTY_BATMAN_TEAMID),
                "statuses[]" : meta.get('Status', 'triggered'),
                "time_zone": "UTC"
            }
        }