from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    user_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), index=True, unique=True, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    asal_sekolah = db.Column(db.String(255), nullable=False)
    jenjang = db.Column(db.String(100), nullable=False)
    photo_profile = db.Column(db.String(255), nullable=True)
    home_address = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Users {}>'.format(self.username)
    
    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)


class Campus(db.Model):
    campus_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    campus_name = db.Column(db.String(255), nullable=False)
    campus_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    campus_accreditation = db.Column(db.String(50), nullable=False)
    no_phone = db.Column(db.String(50), nullable=False)
    fax = db.Column(db.String(100), nullable=False)
    campus_address = db.Column(db.Text(), nullable=False)
    hero_image = db.Column(db.String(255), nullable=True)
    campus_logo = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Campus {}>'.format(self.campus_name)

        
class Following(db.Model):
    following_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    campus_id = db.Column(db.BigInteger, db.ForeignKey(Campus.campus_id))
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.user_id))

    def __repr__(self):
        return '<Following {}>'.format(self.following_id)

        
class CampusFaculty(db.Model):
    campus_faculty_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    faculty_name = db.Column(db.String(255), nullable=False)
    campus_id = db.Column(db.BigInteger, db.ForeignKey(Campus.campus_id))

    def __repr__(self):
        return '<CostType {}>'.format(self.faculty_name)


class MajorCampus(db.Model):
    major_campus_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    major_name = db.Column(db.String(255), nullable=False)
    faculty_id = db.Column(db.BigInteger, db.ForeignKey(CampusFaculty.campus_faculty_id))
    major_description = db.Column(db.Text(), nullable=True)
    work_prospect = db.Column(db.Text(), nullable=True)
    jenjang = db.Column(db.String(255), nullable=True)
    campus_id = db.Column(db.BigInteger, db.ForeignKey(Campus.campus_id))
    tingkat_keketatan = db.Column(db.Integer, nullable=True)
    major_accreditation = db.Column(db.String(50), nullable=False)
    kuota_mahasiswa_baru = db.Column(db.Integer, nullable=True)
    jumlah_pendaftaran = db.Column(db.Integer, nullable=True)
    campus_cost = db.relationship('MajorCampusCost', backref='major_campus')
    faculty = db.relationship('CampusFaculty', backref='major_campus')

    def __repr__(self):
        return '<MajorCampus {}>'.format(self.major_name)


class MajorCampusCost(db.Model):
    major_campus_cost_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    major_cost_name = db.Column(db.String(255), nullable=False)
    cost_value = db.Column(db.Integer, nullable=False)
    major_campus_id = db.Column(db.BigInteger, db.ForeignKey("major_campus.major_campus_id"))


    def __repr__(self):
        return '<MajorCampusCost {}>'.format(self.major_cost_name)

