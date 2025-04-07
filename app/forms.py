from flask_wtf import FlaskForm
from wtforms import (StringField, DateField, BooleanField, TextAreaField, IntegerField, SelectField, SubmitField, FieldList, FormField,FloatField,PasswordField)
from wtforms.validators import DataRequired, Optional, Length,EqualTo

class ChangePasswordForm(FlaskForm):
    current_password = PasswordField("Current Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm New Password", validators=[DataRequired()])
    submit = SubmitField("Change Password")

class TravelHistoryForm(FlaskForm):
    country = StringField('Country', validators=[Optional(), Length(max=100)])
    arrival_date = DateField('Arrival Date', validators=[Optional()])
    departure_date = DateField('Departure Date', validators=[Optional()])
    details = TextAreaField('Details', validators=[Optional()])


class EducationForm(FlaskForm):
    class_name = StringField('Class/Grade', validators=[Optional(), Length(max=100)])
    pass_out_year = IntegerField('Pass Out Year', validators=[Optional()])
    board_university_college = StringField('Board/University/College', validators=[Optional(), Length(max=255)])
    percentage_or_grade_point = FloatField('Percentage or Grade Point', validators=[Optional()])
    stream_subjects = StringField('Stream/Subjects', validators=[Optional(), Length(max=255)])


class WorkExperienceForm(FlaskForm):
    organization_name = StringField('Organization Name', validators=[Optional(), Length(max=150)])
    designation = StringField('Designation', validators=[Optional(), Length(max=150)])
    joining_date = DateField('Joining Date', validators=[Optional()])
    leaving_date = DateField('Leaving Date', validators=[Optional()])
    full_time_part_time = SelectField(
        'Full Time / Part Time', choices=[('', 'Select'), ('Full Time', 'Full Time'), ('Part Time', 'Part Time')], validators=[Optional()]
    )
    job_duties = TextAreaField('Job Duties', validators=[Optional()])
    was_it_your_business = StringField('Was it your business?', validators=[Optional()])

class RefusalDetailsForm(FlaskForm):
    country = StringField('Country', validators=[Optional(), Length(max=100)])
    refusal_date = DateField('Refusal Date', validators=[Optional()])
    reason = TextAreaField('Reason', validators=[Optional()])
    additional_info = TextAreaField('Additional Info', validators=[Optional()])

class CustomerForm(FlaskForm):
    name = StringField('Name', validators=[Optional(), Length(max=150)])
    dob = DateField('Date of Birth', validators=[Optional()])
    email = StringField('Email', validators=[Optional(), Length(max=120)])
    contact_no = StringField('Contact Number', validators=[Optional(), Length(max=20)])
    address = TextAreaField('Address', validators=[Optional(), Length(max=255)])

    marital_status = SelectField(
        'Marital Status', choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'),('Widower','Widower'),('Widow','Widow')], validators=[Optional()]
    )

    interested_in_ielts = BooleanField('Interested in IELTS')
    interested_in_pte = BooleanField('Interested in PTE')
    interested_in_toefl = BooleanField('Interested in TOEFL')
    interested_in_others = StringField('Other Interests', validators=[Optional(), Length(max=100)])

    study_visa = BooleanField('Study Visa')
    tourist_visa = BooleanField('Tourist Visa')
    pr = BooleanField('Permanent Residency')
    others_visa = StringField('Other types of Visa', validators=[Optional(), Length(max=100)])

    course_preference_1 = StringField('Course Preference 1', validators=[Optional(), Length(max=100)])
    course_preference_2 = StringField('Course Preference 2', validators=[Optional(), Length(max=100)])
    course_preference_3 = StringField('Course Preference 3', validators=[Optional(), Length(max=100)])

    country_preference_1 = StringField('Country Preference 1', validators=[Optional(), Length(max=100)])
    country_preference_2 = StringField('Country Preference 2', validators=[Optional(), Length(max=100)])
    country_preference_3 = StringField('Country Preference 3', validators=[Optional(), Length(max=100)])

    city_preference_1 = StringField('City Preference 1', validators=[Optional(), Length(max=100)])
    city_preference_2 = StringField('City Preference 2', validators=[Optional(), Length(max=100)])
    city_preference_3 = StringField('City Preference 3', validators=[Optional(), Length(max=100)])

    travel_history = FieldList(FormField(TravelHistoryForm), min_entries=1)
    refusal_details = FieldList(FormField(RefusalDetailsForm), min_entries=1)
    work_experience = FieldList(FormField(WorkExperienceForm), min_entries=1)
    education = FieldList(FormField(EducationForm), min_entries=1)

    how_did_you_know_us = StringField('How did you know us?', validators=[Optional(), Length(max=255)])
    other_information = TextAreaField('Other Information', validators=[Optional()])

    submit = SubmitField('Submit')