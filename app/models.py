from datetime import datetime
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    employees = db.relationship('Employee', backref='admin', lazy=True)
    customers = db.relationship('Customer', back_populates='admin', lazy=True)

    def __repr__(self):
        return f'<Admin {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Employee(UserMixin, db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(255), nullable=True)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)

    customers = db.relationship('Customer', back_populates='employee', lazy=True)

    def __repr__(self):
        return f'<Employee {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(150), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    email = db.Column(db.String(120), nullable=True)
    contact_no = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    
    marital_status = db.Column(db.String(20), nullable=True)

    interested_in_ielts = db.Column(db.Boolean, nullable=True, default=False)
    interested_in_pte = db.Column(db.Boolean, nullable=True, default=False)
    interested_in_toefl = db.Column(db.Boolean, nullable=True, default=False)
    interested_in_others = db.Column(db.String(100), nullable=True)

    study_visa = db.Column(db.Boolean, nullable=True, default=False)
    tourist_visa = db.Column(db.Boolean, nullable=True, default=False)
    pr = db.Column(db.Boolean, nullable=True, default=False)
    others_visa = db.Column(db.String(100), nullable=True) 

    course_preference_1 = db.Column(db.String(100), nullable=True)
    course_preference_2 = db.Column(db.String(100), nullable=True)
    course_preference_3 = db.Column(db.String(100), nullable=True)

    country_preference_1 = db.Column(db.String(100), nullable=True)
    country_preference_2 = db.Column(db.String(100), nullable=True)
    country_preference_3 = db.Column(db.String(100), nullable=True)

    city_preference_1 = db.Column(db.String(100), nullable=True)
    city_preference_2 = db.Column(db.String(100), nullable=True)
    city_preference_3 = db.Column(db.String(100), nullable=True)

    travel_history = db.relationship('TravelHistory', backref='customer', lazy=True)

    refusal_details = db.relationship('RefusalDetails', backref='customer', lazy=True)

    work_experience = db.relationship('WorkExperience', backref='customer', lazy=True)
    
    how_did_you_know_us = db.Column(db.String(255), nullable=True)

    other_information = db.Column(db.Text, nullable=True)

    sign_date = db.Column(db.DateTime, default=datetime.utcnow)

    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    admin = db.relationship('Admin', back_populates='customers')

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=True)
    employee = db.relationship('Employee', back_populates='customers')

    def __repr__(self):
        return f'<Customer {self.name}, {self.email}>'

class RefusalDetails(db.Model):
    __tablename__ = 'refusal_details'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    country = db.Column(db.String(100), nullable=True)
    refusal_date = db.Column(db.Date, nullable=True)
    reason = db.Column(db.Text, nullable=True)
    additional_info = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<RefusalDetails {self.country}, {self.refusal_date}>'

class WorkExperience(db.Model):
    __tablename__ = 'work_experience'

    id = db.Column(db.Integer, primary_key=True)
    organization_name = db.Column(db.String(150), nullable=True)
    designation = db.Column(db.String(150), nullable=True)
    joining_date = db.Column(db.Date, nullable=True)
    leaving_date = db.Column(db.Date, nullable=True)
    full_time_part_time = db.Column(db.String(20), nullable=True)
    job_duties = db.Column(db.Text, nullable=True)
    was_it_your_business = db.Column(db.String(20), nullable=True)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    def __repr__(self):
        return f'<WorkExperience {self.organization_name}, {self.designation}>'

class TravelHistory(db.Model):
    __tablename__ = 'travel_history'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), nullable=True)
    arrival_date = db.Column(db.Date, nullable=True)
    departure_date = db.Column(db.Date, nullable=True)
    details = db.Column(db.Text, nullable=True) 

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    def __repr__(self):
        return f'<TravelHistory {self.country}, {self.arrival_date}>'

class Education(db.Model):
    __tablename__ = 'education'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', backref='education')

    class_name = db.Column(db.String(100), nullable=True) 
    pass_out_year = db.Column(db.Integer, nullable=True)
    board_university_college = db.Column(db.String(255), nullable=True)
    percentage_or_grade_point = db.Column(db.Float,nullable=True)
    stream_subjects = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Education {self.degree}, {self.class_name}>'