from flask_restful import Resource
from flask import request
from app.response import response
from app import db
from app.models import Campus, Following, MajorCampus, CampusFaculty


class SearchCampus(Resource):    
    def get(self):
        """
        deskripsi: fungsi ini bertanggung jawab untuk melakukan pencarian data kampus
        parameter:  menerima data dari paramater GET dengan key 'param'
        return: mengembalikan list of dict dari data kampus
        """
        try:
            param = request.args.get('param')
            keyword = "%{}%".format(param)
            data_campus = Campus.query.filter(Campus.campus_name.like(keyword)).all()
            result = []
            for data in data_campus:
                item = {
                    'campus_name': data.campus_name,
                    'campus_address': data.campus_address,
                    'campus_logo': data.campus_logo,
                    'status': data.status,
                    'campus_accreditation': data.campus_accreditation,
                }

                result.append(item)

            return response.ok("success", result)
        except Exception as e:
                return response.bad_request("{}".format(e), '')


class FollowCampus(Resource):
    """
    deskripsi: fungsi ini bertanggung jawab untuk memfollow kampus yang di kalukan oleh user
    parameter:  menerima data dari body request yang berformat json, format json:
        {
            "campus_id": #,
            "user_id": #
        }

    return: mengembalikan nilai bolean
    """
    def get(self):
        try:
            request_json = request.get_json()
            campus_id = request_json.get('campus_id')
            user_id = request_json.get('user_id')
            following = Following(campus_id=campus_id, user_id=user_id)
            db.session.add(following)
            db.session.commit()        
            
            return response.ok("success", True)
        except Exception as e:
                return response.bad_request("{}".format(e), '')

    
class ListCampusMajor(Resource):
        """
        deskripsi: fungsi ini bertanggung jawab untuk menampilkan list fakultas yang berdasarkan id kampus
        parameter:  menerima data dari body request yang berformat json, format json:
            {
                "campus_id": #,
            }

        return: mengembalikan list of dict dari data kampus
        """
        def get(self):
            try:
                request_json = request.get_json()
                campus_id = request_json.get('campus_id')
                list_major = MajorCampus.query.join(CampusFaculty, MajorCampus.faculty_id==CampusFaculty.campus_faculty_id).filter_by(campus_id=campus_id).all()
                result = []
                for major in list_major:
                    item = {
                        'major_name':major.major_name,
                        'faculty_name':major.faculty.faculty_name
                    }
                    result.append(item)

                return response.ok("success", result)

            except Exception as e:
                return response.bad_request("{}".format(e), '')