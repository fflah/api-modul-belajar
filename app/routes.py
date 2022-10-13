from app import api
from app.controllers import Campus

api.add_resource(Campus.SearchCampus, '/search-campus')
api.add_resource(Campus.FollowCampus, '/follow-campus')
api.add_resource(Campus.ListCampusMajor, '/list-major-campus')