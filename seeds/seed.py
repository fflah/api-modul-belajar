from flask_seeder import Seeder
from app.models import CampusFaculty, Users, Campus, MajorCampusCost, MajorCampus

class UserSeeder(Seeder):
  def run(self):
    list_user = [
         {'username':'yoga.rap','password': 'akupintar', 'gender':'laki-laki', 'asal_sekolah':'SMA 10 Surabaya', 'jenjang':'SMA', 'home_address':'Jln surabaya no 129'},
         {'username':'yogi.rip','password': 'akupintar', 'gender':'laki-laki', 'asal_sekolah':'SMA 10 Surabaya', 'jenjang':'SMA', 'home_address':'Jln surabaya no 129'},
    ]
    for user_data in list_user:
        user = Users(
            username=user_data['username'],
            gender=user_data['gender'],
            asal_sekolah=user_data['asal_sekolah'],
            jenjang=user_data['jenjang'],
            home_address=user_data['home_address'],
        )
        user.setPassword(user_data['password'])
        self.db.session.add(user)

class CampusSeeder(Seeder):
  def run(self):
    list_campus = [
        {
            'campus_id': 1, 
            'campus_name':'Institud Teknologi Sepuluh November (ITS)',
            'campus_type': 'Negri', 
            'status':'PTN-BH', 
            'campus_accreditation':'A',
            'no_phone':'031-3729129', 
            'fax':'031-4729230238', 
            'campus_address':'Jl. Raya keputih sokulila surabaya',
            'campus_logo':'logo.png'
        },
        {
            'campus_id': 2, 
            'campus_name':'Universitas Gajah Mada (UGM)',
            'campus_type': 'Negri', 
            'status':'PTN-BH', 
            'campus_accreditation':'A', 
            'no_phone':'031-37292121', 
            'fax':'031-2135365', 
            'campus_address':'Jl. Raya jogja raya 89',
            'campus_logo':'logo.png'
        },
        {
            'campus_id': 3, 
            'campus_name':'Universitas Indonesia (UI)',
            'campus_type': 'Negri', 
            'status':'PTN-BH', 
            'campus_accreditation':'A', 
            'no_phone':'031-37292121', 
            'fax':'031-2135365', 
            'campus_address':'Jl. Raya Jakarta raya 89',
            'campus_logo':'logo.png'
        },
    ]
    for campus_data in list_campus:
        campus = Campus(
            campus_name=campus_data['campus_name'],
            campus_type=campus_data['campus_type'],
            status=campus_data['status'],
            campus_accreditation=campus_data['campus_accreditation'],
            no_phone=campus_data['no_phone'],
            fax=campus_data['fax'],
            campus_address=campus_data['campus_address'],
            campus_logo=campus_data['campus_logo'],
        )        
        self.db.session.add(campus)
  

class CampusFacultySeeder(Seeder):
  def run(self):
    list_faculty = [
        {'campus_faculty_id':1, 'faculty_name':'Fakultas Teknik', 'campus_id':1}, 
        {'campus_faculty_id':2, 'faculty_name':'Sains dan Matematika', 'campus_id':1}, 
        {'campus_faculty_id':3, 'faculty_name':'Fakultas Bisnis', 'campus_id':1}, 
        {'campus_faculty_id':4, 'faculty_name':'Fakultas Teknik', 'campus_id':2}, 
        {'campus_faculty_id':5, 'faculty_name':'Fakultas Komunikasi dan Informatika', 'campus_id':2}, 
        {'campus_faculty_id':6, 'faculty_name':'Fakultas Kesehatan', 'campus_id':2}, 
        {'campus_faculty_id':7, 'faculty_name':'Fakultas Kesehatan', 'campus_id':3}, 
        {'campus_faculty_id':8, 'faculty_name':'Fakultas Kedokteran', 'campus_id':3}, 
        {'campus_faculty_id':9, 'faculty_name':'Fakultas Teknik', 'campus_id':3}, 
    ]
    for data_faculty in list_faculty:
        cost_type = CampusFaculty(
            campus_faculty_id=data_faculty['campus_faculty_id'], 
            faculty_name=data_faculty['faculty_name'],
            campus_id=data_faculty['campus_id'])

        self.db.session.add(cost_type)


class MajorCampusSeeder(Seeder):
  def run(self):
    list_major_campus = [
         {
            'major_campus_id':1,
            'major_name':'Teknik Mesin',
            'faculty_id': 1, 
            'major_description':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nulla non ab voluptatum! Tempore nam quasi quo temporibus, unde, fuga impedit excepturi labore fugiat distinctio accusamus quisquam. Aspernatur praesentium minima voluptate saepe necessitatibus, eos recusandae sapiente temporibus fugit mollitia magnam animi provident dolores quos rem soluta dicta sit aperiam quam quasi quisquam qui! Ab nisi animi modi harum, tempore voluptatum beatae tenetur illo reiciendis iste vero deleniti alias, nesciunt veniam eveniet accusantium natus? Sit ab numquam illo dolores? Magni vel voluptate repudiandae possimus odit qui nesciunt nulla itaque, ad, architecto veritatis blanditiis repellat sequi laboriosam. Culpa est modi quod animi ducimus?', 
            'work_prospect':'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Velit esse praesentium culpa voluptatum reprehenderit, nisi libero tempore voluptatem laborum. Illum deserunt aliquam blanditiis dolor incidunt consequuntur quis beatae quibusdam exercitationem praesentium possimus quam, sed facilis expedita ex sequi modi provident distinctio molestias, obcaecati neque? Ea perferendis assumenda deserunt esse nemo.', 
            'jenjang': 'Sarjana',
            'campus_id':1, 
            'tingkat_keketatan':1, 
            'major_accreditation':'A',
            'kuota_mahasiswa_baru':90,
            'jumlah_pendaftaran':80
         },
         {
            'major_campus_id':2,
            'major_name':'Biologi',
            'faculty_id': 2, 
            'major_description':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nulla non ab voluptatum! Tempore nam quasi quo temporibus, unde, fuga impedit excepturi labore fugiat distinctio accusamus quisquam. Aspernatur praesentium minima voluptate saepe necessitatibus, eos recusandae sapiente temporibus fugit mollitia magnam animi provident dolores quos rem soluta dicta sit aperiam quam quasi quisquam qui! Ab nisi animi modi harum, tempore voluptatum beatae tenetur illo reiciendis iste vero deleniti alias, nesciunt veniam eveniet accusantium natus? Sit ab numquam illo dolores? Magni vel voluptate repudiandae possimus odit qui nesciunt nulla itaque, ad, architecto veritatis blanditiis repellat sequi laboriosam. Culpa est modi quod animi ducimus?', 
            'work_prospect':'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Velit esse praesentium culpa voluptatum reprehenderit, nisi libero tempore voluptatem laborum. Illum deserunt aliquam blanditiis dolor incidunt consequuntur quis beatae quibusdam exercitationem praesentium possimus quam, sed facilis expedita ex sequi modi provident distinctio molestias, obcaecati neque? Ea perferendis assumenda deserunt esse nemo.', 
            'jenjang': 'Sarjana',
            'campus_id':1, 
            'tingkat_keketatan':1, 
            'major_accreditation':'A',
            'kuota_mahasiswa_baru':120,
            'jumlah_pendaftaran':110
         },
         {
            'major_campus_id':3,
            'major_name':'Ekonomi',
            'faculty_id': 3, 
            'major_description':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nulla non ab voluptatum! Tempore nam quasi quo temporibus, unde, fuga impedit excepturi labore fugiat distinctio accusamus quisquam. Aspernatur praesentium minima voluptate saepe necessitatibus, eos recusandae sapiente temporibus fugit mollitia magnam animi provident dolores quos rem soluta dicta sit aperiam quam quasi quisquam qui! Ab nisi animi modi harum, tempore voluptatum beatae tenetur illo reiciendis iste vero deleniti alias, nesciunt veniam eveniet accusantium natus? Sit ab numquam illo dolores? Magni vel voluptate repudiandae possimus odit qui nesciunt nulla itaque, ad, architecto veritatis blanditiis repellat sequi laboriosam. Culpa est modi quod animi ducimus?', 
            'work_prospect':'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Velit esse praesentium culpa voluptatum reprehenderit, nisi libero tempore voluptatem laborum. Illum deserunt aliquam blanditiis dolor incidunt consequuntur quis beatae quibusdam exercitationem praesentium possimus quam, sed facilis expedita ex sequi modi provident distinctio molestias, obcaecati neque? Ea perferendis assumenda deserunt esse nemo.', 
            'jenjang': 'Sarjana',
            'campus_id':1, 
            'tingkat_keketatan':3, 
            'major_accreditation':'B',
            'kuota_mahasiswa_baru':120,
            'jumlah_pendaftaran':110
         },
         {
            'major_campus_id':4,
            'major_name':'Teknik Elektro',
            'faculty_id': 4, 
            'major_description':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nulla non ab voluptatum! Tempore nam quasi quo temporibus, unde, fuga impedit excepturi labore fugiat distinctio accusamus quisquam. Aspernatur praesentium minima voluptate saepe necessitatibus, eos recusandae sapiente temporibus fugit mollitia magnam animi provident dolores quos rem soluta dicta sit aperiam quam quasi quisquam qui! Ab nisi animi modi harum, tempore voluptatum beatae tenetur illo reiciendis iste vero deleniti alias, nesciunt veniam eveniet accusantium natus? Sit ab numquam illo dolores? Magni vel voluptate repudiandae possimus odit qui nesciunt nulla itaque, ad, architecto veritatis blanditiis repellat sequi laboriosam. Culpa est modi quod animi ducimus?', 
            'work_prospect':'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Velit esse praesentium culpa voluptatum reprehenderit, nisi libero tempore voluptatem laborum. Illum deserunt aliquam blanditiis dolor incidunt consequuntur quis beatae quibusdam exercitationem praesentium possimus quam, sed facilis expedita ex sequi modi provident distinctio molestias, obcaecati neque? Ea perferendis assumenda deserunt esse nemo.', 
            'jenjang': 'Sarjana',
            'campus_id':2, 
            'tingkat_keketatan':5, 
            'major_accreditation':'AB',
            'kuota_mahasiswa_baru':120,
            'jumlah_pendaftaran':80
         },
         {
            'major_campus_id':5,
            'major_name':'Teknik Kimia',
            'faculty_id': 4, 
            'major_description':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nulla non ab voluptatum! Tempore nam quasi quo temporibus, unde, fuga impedit excepturi labore fugiat distinctio accusamus quisquam. Aspernatur praesentium minima voluptate saepe necessitatibus, eos recusandae sapiente temporibus fugit mollitia magnam animi provident dolores quos rem soluta dicta sit aperiam quam quasi quisquam qui! Ab nisi animi modi harum, tempore voluptatum beatae tenetur illo reiciendis iste vero deleniti alias, nesciunt veniam eveniet accusantium natus? Sit ab numquam illo dolores? Magni vel voluptate repudiandae possimus odit qui nesciunt nulla itaque, ad, architecto veritatis blanditiis repellat sequi laboriosam. Culpa est modi quod animi ducimus?', 
            'work_prospect':'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Velit esse praesentium culpa voluptatum reprehenderit, nisi libero tempore voluptatem laborum. Illum deserunt aliquam blanditiis dolor incidunt consequuntur quis beatae quibusdam exercitationem praesentium possimus quam, sed facilis expedita ex sequi modi provident distinctio molestias, obcaecati neque? Ea perferendis assumenda deserunt esse nemo.', 
            'jenjang': 'Sarjana',
            'campus_id':2, 
            'tingkat_keketatan':2, 
            'major_accreditation':'AB',
            'kuota_mahasiswa_baru':120,
            'jumlah_pendaftaran':80
         },
         {
            'major_campus_id':6,
            'major_name':'Ilmu Komunikasi',
            'faculty_id': 5, 
            'major_description':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nulla non ab voluptatum! Tempore nam quasi quo temporibus, unde, fuga impedit excepturi labore fugiat distinctio accusamus quisquam. Aspernatur praesentium minima voluptate saepe necessitatibus, eos recusandae sapiente temporibus fugit mollitia magnam animi provident dolores quos rem soluta dicta sit aperiam quam quasi quisquam qui! Ab nisi animi modi harum, tempore voluptatum beatae tenetur illo reiciendis iste vero deleniti alias, nesciunt veniam eveniet accusantium natus? Sit ab numquam illo dolores? Magni vel voluptate repudiandae possimus odit qui nesciunt nulla itaque, ad, architecto veritatis blanditiis repellat sequi laboriosam. Culpa est modi quod animi ducimus?', 
            'work_prospect':'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Velit esse praesentium culpa voluptatum reprehenderit, nisi libero tempore voluptatem laborum. Illum deserunt aliquam blanditiis dolor incidunt consequuntur quis beatae quibusdam exercitationem praesentium possimus quam, sed facilis expedita ex sequi modi provident distinctio molestias, obcaecati neque? Ea perferendis assumenda deserunt esse nemo.', 
            'jenjang': 'Sarjana',
            'campus_id':2, 
            'tingkat_keketatan':2, 
            'major_accreditation':'AB',
            'kuota_mahasiswa_baru':120,
            'jumlah_pendaftaran':80
         },
         {
            'major_campus_id':7,
            'major_name':'Teknik Industri',
            'faculty_id': 1, 
            'major_description':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nulla non ab voluptatum! Tempore nam quasi quo temporibus, unde, fuga impedit excepturi labore fugiat distinctio accusamus quisquam. Aspernatur praesentium minima voluptate saepe necessitatibus, eos recusandae sapiente temporibus fugit mollitia magnam animi provident dolores quos rem soluta dicta sit aperiam quam quasi quisquam qui! Ab nisi animi modi harum, tempore voluptatum beatae tenetur illo reiciendis iste vero deleniti alias, nesciunt veniam eveniet accusantium natus? Sit ab numquam illo dolores? Magni vel voluptate repudiandae possimus odit qui nesciunt nulla itaque, ad, architecto veritatis blanditiis repellat sequi laboriosam. Culpa est modi quod animi ducimus?', 
            'work_prospect':'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Velit esse praesentium culpa voluptatum reprehenderit, nisi libero tempore voluptatem laborum. Illum deserunt aliquam blanditiis dolor incidunt consequuntur quis beatae quibusdam exercitationem praesentium possimus quam, sed facilis expedita ex sequi modi provident distinctio molestias, obcaecati neque? Ea perferendis assumenda deserunt esse nemo.', 
            'jenjang': 'Sarjana',
            'campus_id':3, 
            'tingkat_keketatan':2, 
            'major_accreditation':'AB',
            'kuota_mahasiswa_baru':120,
            'jumlah_pendaftaran':80
         },
         {
            'major_campus_id':8,
            'major_name':'Fisioterapi',
            'faculty_id': 7, 
            'major_description':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nulla non ab voluptatum! Tempore nam quasi quo temporibus, unde, fuga impedit excepturi labore fugiat distinctio accusamus quisquam. Aspernatur praesentium minima voluptate saepe necessitatibus, eos recusandae sapiente temporibus fugit mollitia magnam animi provident dolores quos rem soluta dicta sit aperiam quam quasi quisquam qui! Ab nisi animi modi harum, tempore voluptatum beatae tenetur illo reiciendis iste vero deleniti alias, nesciunt veniam eveniet accusantium natus? Sit ab numquam illo dolores? Magni vel voluptate repudiandae possimus odit qui nesciunt nulla itaque, ad, architecto veritatis blanditiis repellat sequi laboriosam. Culpa est modi quod animi ducimus?', 
            'work_prospect':'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Velit esse praesentium culpa voluptatum reprehenderit, nisi libero tempore voluptatem laborum. Illum deserunt aliquam blanditiis dolor incidunt consequuntur quis beatae quibusdam exercitationem praesentium possimus quam, sed facilis expedita ex sequi modi provident distinctio molestias, obcaecati neque? Ea perferendis assumenda deserunt esse nemo.', 
            'jenjang': 'Sarjana',
            'campus_id':3,
            'tingkat_keketatan':2, 
            'major_accreditation':'AB',
            'kuota_mahasiswa_baru':50,
            'jumlah_pendaftaran':30
         },
         {
            'major_campus_id':9,
            'major_name':'Dokter Gigi',
            'faculty_id': 8, 
            'major_description':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nulla non ab voluptatum! Tempore nam quasi quo temporibus, unde, fuga impedit excepturi labore fugiat distinctio accusamus quisquam. Aspernatur praesentium minima voluptate saepe necessitatibus, eos recusandae sapiente temporibus fugit mollitia magnam animi provident dolores quos rem soluta dicta sit aperiam quam quasi quisquam qui! Ab nisi animi modi harum, tempore voluptatum beatae tenetur illo reiciendis iste vero deleniti alias, nesciunt veniam eveniet accusantium natus? Sit ab numquam illo dolores? Magni vel voluptate repudiandae possimus odit qui nesciunt nulla itaque, ad, architecto veritatis blanditiis repellat sequi laboriosam. Culpa est modi quod animi ducimus?', 
            'work_prospect':'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Velit esse praesentium culpa voluptatum reprehenderit, nisi libero tempore voluptatem laborum. Illum deserunt aliquam blanditiis dolor incidunt consequuntur quis beatae quibusdam exercitationem praesentium possimus quam, sed facilis expedita ex sequi modi provident distinctio molestias, obcaecati neque? Ea perferendis assumenda deserunt esse nemo.', 
            'jenjang': 'Sarjana',
            'campus_id':3,
            'tingkat_keketatan':0, 
            'major_accreditation':'AB',
            'kuota_mahasiswa_baru':50,
            'jumlah_pendaftaran':0
         },
         {
            'major_campus_id':10,
            'major_name':'Farmasi',
            'faculty_id': 7, 
            'major_description':'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nulla non ab voluptatum! Tempore nam quasi quo temporibus, unde, fuga impedit excepturi labore fugiat distinctio accusamus quisquam. Aspernatur praesentium minima voluptate saepe necessitatibus, eos recusandae sapiente temporibus fugit mollitia magnam animi provident dolores quos rem soluta dicta sit aperiam quam quasi quisquam qui! Ab nisi animi modi harum, tempore voluptatum beatae tenetur illo reiciendis iste vero deleniti alias, nesciunt veniam eveniet accusantium natus? Sit ab numquam illo dolores? Magni vel voluptate repudiandae possimus odit qui nesciunt nulla itaque, ad, architecto veritatis blanditiis repellat sequi laboriosam. Culpa est modi quod animi ducimus?', 
            'work_prospect':'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Velit esse praesentium culpa voluptatum reprehenderit, nisi libero tempore voluptatem laborum. Illum deserunt aliquam blanditiis dolor incidunt consequuntur quis beatae quibusdam exercitationem praesentium possimus quam, sed facilis expedita ex sequi modi provident distinctio molestias, obcaecati neque? Ea perferendis assumenda deserunt esse nemo.', 
            'jenjang': 'Sarjana',
            'campus_id':3,
            'tingkat_keketatan':2, 
            'major_accreditation':'AB',
            'kuota_mahasiswa_baru':50,
            'jumlah_pendaftaran':30
         },
    ]
    for data_major in list_major_campus:
        major_campus = MajorCampus(
            major_campus_id=data_major['major_campus_id'],
            major_name=data_major['major_name'],
            faculty_id=data_major['faculty_id'],
            major_description=data_major['major_description'],
            work_prospect=data_major['work_prospect'],
            jenjang=data_major['jenjang'],
            campus_id=data_major['campus_id'],
            tingkat_keketatan=data_major['tingkat_keketatan'],
            major_accreditation=data_major['major_accreditation'],
            kuota_mahasiswa_baru=data_major['kuota_mahasiswa_baru'],
            jumlah_pendaftaran=data_major['jumlah_pendaftaran'],
        )

        self.db.session.add(major_campus)

        

class MajorCampusCostSeeder(Seeder):
  def run(self):
    
    list_major_campus_cost = [
        {
            'major_campus_cost_id': 1, 
            'major_campus_id': 1,
            'major_cost_name':'UKT',
            'cost_value': 10000, 
        },
        {
            'major_campus_cost_id': 2, 
            'major_campus_id': 2,
            'major_cost_name':'UKT',
            'cost_value': 10000, 
        },
        {
            'major_campus_cost_id': 4, 
            'major_campus_id': 4,
            'major_cost_name':'UKT',
            'cost_value': 10000, 
        },
        {
            'major_campus_cost_id': 5, 
            'major_campus_id': 5,
            'major_cost_name':'UKT',
            'cost_value': 10000, 
        },
        {
            'major_campus_cost_id': 6, 
            'major_campus_id': 6,
            'major_cost_name':'UKT',
            'cost_value': 10000, 
        },
        {
            'major_campus_cost_id': 7, 
            'major_campus_id': 7,
            'major_cost_name':'UKT',
            'cost_value': 10000, 
        },
        {
            'major_campus_cost_id': 8, 
            'major_campus_id': 8,
            'major_cost_name':'UKT',
            'cost_value': 10000, 
        },
        {
            'major_campus_cost_id': 9, 
            'major_campus_id': 9,
            'major_cost_name':'UPP',
            'cost_value': 10000, 
        },
        {
            'major_campus_cost_id': 10, 
            'major_campus_id': 9,
            'major_cost_name':'UPS',
            'cost_value': 10000, 
        },
        ]
    for major_cost in list_major_campus_cost:
        cost = MajorCampusCost(
            major_campus_cost_id=int(major_cost['major_campus_cost_id']),
            major_campus_id=int(major_cost['major_campus_id']),
            major_cost_name=major_cost['major_cost_name'],
            cost_value=int(major_cost['cost_value']),
        )        
        self.db.session.add(cost)
