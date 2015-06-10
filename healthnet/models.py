from datetime import date

from django.db import models
from django.contrib.auth.models import User


INSURANCES = (
    (0, "N/A"),
    (1, "Aetna"),
    (2, "United HealthCare"),
    (3, "Humana"),
    (4, "Celtic Healthcare"),
    (5, "BlueCross BlueShield"),
    (6, "Cigna"),
    (7, "Emblem Healthcare"),
    (8, "Amerigroup"),
    (9, "Kaiser Permanente"),
    (10, "Wellpoint"),
)

US_STATES = (
    ("Alabama", "Alabama"), ("Alaska", "Alaska"), ("Arizona", "Arizona"), ("Arkansas", "Arkansas"), ("California", "California"),
    ("Colorado", "Colorado"), ("Connecticut", "Connecticut"), ("Delaware", "Delaware"), ("Florida", "Florida"), ("Georgia", "Georgia"),
    ("Hawaii", "Hawaii"), ("Idaho", "Idaho"), ("Illinois", "Illinois"), ("Indiana", "Indiana"), ("Iowa", "Iowa"),
    ("Kansas", "Kansas"), ("Kentucky", "Kentucky"), ("Louisiana", "Louisiana"), ("Maine", "Maine"), ("Maryland", "Maryland"),
    ("Massachusetts", "Massachusetts"), ("Michigan", "Michigan"), ("Minnesota", "Minnesota"), ("Mississippi", "Mississippi"), ("Missouri", "Missouri"),
    ("Montana", "Montana"), ("Nebraska", "Nebraska"), ("Nevada", "Nevada"), ("New Hampshire", "New Hampshire"), ("New Jersey", "New Jersey"),
    ("New Mexico", "New Mexico"), ("New York", "New York"), ("North Carolina", "North Carolina"), ("North Dakota", "North Dakota"), ("Ohio", "Ohio"),
    ("Oklahoma", "Oklahoma"), ("Oregon", "Oregon"), ("Pennsylvania", "Pennsylvania"), ("Rhode Island", "Rhode Island"), ("South Carolina", "South Carolina"),
    ("South Dakota", "South Dakota"), ("Tennessee", "Tennessee"), ("Texas", "Texas"), ("Utah", "Utah"), ("Vermont", "Vermont"),
    ("Virginia", "Virginia"), ("Washington", "Washington"), ("West Virginia", "West Virginia"), ("Wisconsin", "Wisconsin"), ("Wyoming", "Wyoming")
)


class Location(models.Model):
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50, default="United States")
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.address

    class Admin:
        list_display = ('city', 'country')


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    location = models.OneToOneField(Location)

    def __str__(self):
        return self.name

    class Admin:
        list_display = (
            'name',
            'phone',
            'location'
        )


class Profile(models.Model):
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
    )

    @staticmethod
    def to_gender(key):
        for item in Profile.GENDER:
            if item[0] == key:
                return item[1]
        return "None"

    firstname = models.CharField(blank=True, max_length=50)
    lastname = models.CharField(blank=True, max_length=50)
    insurance = models.CharField(blank=True, max_length=50)
    emergencyContactName = models.CharField(blank=True, max_length=50)
    emergencyContactNumber = models.CharField(blank=True, max_length=20)
    sex = models.CharField(blank=True, max_length=1, choices=GENDER)
    birthday = models.DateField(default=date(1000, 1, 1))
    phone = models.CharField(blank=True, max_length=20)
    allergies = models.CharField(blank=True, max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    prefHospital = models.ForeignKey(Hospital, null=True, related_name="profiles_prefhospital")
    linkedEmergencyContact = models.ForeignKey('Account', null=True, related_name="profiles_contact")
    primaryCareDoctor = models.ForeignKey('Account', null=True, related_name="profiles_primarycaredoctor")

    def get_populated_fields(self):
        """
        This is used by the form to collect the data.
        """
        fields = {}
        if self.firstname is not None:
            fields['firstname'] = self.firstname
        if self.lastname is not None:
            fields['lastname'] = self.lastname
        if self.sex is not None:
            fields['sex'] = self.sex
        if not self.birthday.year == 1000:
            fields['birthday'] = self.birthday
        if self.phone is not None:
            fields['phone'] = self.phone
        if self.allergies is not None:
            fields['allergies'] = self.allergies
        if self.insurance is not None:
            fields['insurance'] = self.insurance
        if self.emergencyContactName is not None:
            fields['emergencyContactName'] = self.emergencyContactName
        if self.emergencyContactNumber is not None:
            fields['emergencyContactNumber'] = self.emergencyContactNumber
        if self.prefHospital is not None:
            fields['prefHospital'] = self.prefHospital
        if self.linkedEmergencyContact is not None:
            fields['linkedEmergencyContact'] = self.linkedEmergencyContact
        if self.primaryCareDoctor is not None:
            fields['primaryCareDoctor'] = self.primaryCareDoctor
        return fields

    def __str__(self):
        return self.firstname + " " + self.lastname


class Account(models.Model):
    ACCOUNT_UNKNOWN = 0
    ACCOUNT_PATIENT = 10
    ACCOUNT_NURSE = 20
    ACCOUNT_DOCTOR = 30
    ACCOUNT_ADMIN = 40
    ACCOUNT_TYPES = (
        (ACCOUNT_UNKNOWN, "Unknown"),
        (ACCOUNT_PATIENT, "Patient"),
        (ACCOUNT_NURSE, "Nurse"),
        (ACCOUNT_DOCTOR, "Doctor"),
        (ACCOUNT_ADMIN, "Admin"),
    )
    EMPLOYEE_TYPES = (
        (ACCOUNT_NURSE, "Nurse"),
        (ACCOUNT_DOCTOR, "Doctor"),
        (ACCOUNT_ADMIN, "Admin"),
    )

    @staticmethod
    def to_name(key):
        """
        Parses an integer value to a string representing an account role.
        :param key: The account role as a int
        :return: The string representation of the name for the account role
        """
        for item in Account.ACCOUNT_TYPES:
            if item[0] == key:
                return item[1]
        return "None"

    @staticmethod
    def to_value(key):
        """
        Parses an string to a integer representing an account role.
        :param key: The account role as a string
        :return: The integer representation of the account role
        """
        key = key.lower()
        for item in Account.ACCOUNT_TYPES:
            if item[1].lower() == key:
                return item[0]
        return 0

    role = models.IntegerField(default=0, choices=ACCOUNT_TYPES)
    profile = models.OneToOneField(Profile)
    user = models.OneToOneField(User)

    def __str__(self):
        if self.role == 30:
            return "Dr. " + self.profile.__str__()
        elif self.role == 20:
            return "Nurse " + self.profile.__str__()
        else:
            return self.profile.__str__()

    class Admin:
        list_display = (
            'role',
            'profile',
            'user'
        )


class Action(models.Model):
    ACTION_NONE = 0
    ACTION_ACCOUNT = 1
    ACTION_PATIENT = 2
    ACTION_ADMIN = 3
    ACTION_APPOINTMENT = 4
    ACTION_MEDTEST = 5
    ACTION_PRESCRIPTION = 6
    ACTION_ADMISSION = 7
    ACTION_MEDICALINFO = 8
    ACTION_MESSAGE = 9
    ACTION_TYPES = (
        (ACTION_NONE, "None"),
        (ACTION_ACCOUNT, "Account"),
        (ACTION_PATIENT, "Patient"),
        (ACTION_ADMIN, "Admin"),
        (ACTION_APPOINTMENT, "Appointment"),
        (ACTION_MEDTEST, "Medical Test"),
        (ACTION_PRESCRIPTION, "Prescription"),
        (ACTION_ADMISSION, "Admission"),
        (ACTION_MEDICALINFO, "Medical Info"),
        (ACTION_MESSAGE, "Message"),
    )

    @staticmethod
    def to_name(key):
        """
        Parses an integer value to a string representing an action.
        :param key: The action number
        :return: The string representation of the name for action
        """
        for item in Action.ACTION_TYPES:
            if item[0] == key:
                return item[1]
        return "None"

    @staticmethod
    def to_value(key):
        """
        Parses an string to a integer representing an account role.
        :param key: The account role as a string
        :return: The integer representation of the account role
        """
        key = key.lower()
        for item in Action.ACTION_TYPES:
            if item[1].lower() == key:
                return item[0]
        return 0

    type = models.IntegerField(default=0, choices=ACTION_TYPES)
    timePerformed = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, related_name="actions_account")
    """
    Might have to add this field to specify:
    - where action was committed
    - exclude actions that are done at a hospital for which a specific
      admin is not in control of ?
    hospital = models.ForeignKey(Hospital)
    """


class Appointment(models.Model):
    doctor = models.ForeignKey(Account, related_name="appointments_doctor")
    patient = models.ForeignKey(Account, related_name="appointments_patient")
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default="Active")
    hospital = models.ForeignKey(Hospital)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    def get_populated_fields(self):
        """
        This is used by the form to collect the data.
        """
        fields = {
            'doctor': self.doctor,
            'patient': self.patient,
            'description': self.description,
            'hospital': self.hospital,
            'startTime': self.startTime,
            'endTime': self.endTime,
        }
        return fields


class Message(models.Model):
    target = models.ForeignKey(Account, related_name="messages_target")
    sender = models.ForeignKey(Account, related_name="messages_sender")
    header = models.CharField(max_length=300)
    body = models.CharField(max_length=1000)
    sender_deleted = models.BooleanField(default=False)
    target_deleted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    account = models.ForeignKey(Account, related_name="notifications_account")
    message = models.CharField(max_length=200)
    read = models.BooleanField(default=False)
    sent_timestamp = models.DateTimeField(auto_now_add=True)
    read_timestamp = models.DateTimeField(blank=True, null=True)


class Admission(models.Model):

    ADMISSIONREASON = (
        ('Pneumonia', "Pneumonia"),
        ('Congestive Heart Failure', "Congestive Heart Failure"),
        ('Hardening of the arteries', "Hardening of the arteries"),
        ('Heart Attack', "Heart Attack"),
        ('Chronic Obstruction Lung Disease', "Chronic Obstruction Lung Disease"),
        ('Stroke', "Stroke"),
        ('Irregular Heartbeat', "Irregular Heartbeat"),
        ('Congestive Heart Failure', "Congestive Heart Failure"),
        ('Complications of procedures, devices, implants and grafts', "Complications of procedures, devices, implants and grafts"),
        ('Mood Disorders', "Mood Disorders"),
        ('Fluid and Electrolyte Disorders', "Fluid and Electrolyte Disorders"),
        ('Urinary Infections', "Urinary Infections"),
        ('Asthma', "Asthma"),
        ('Diabetes mellitus with and without complications', "Diabetes mellitus with and without complications"),
        ('Skin Infections', "Skin Infections"),
        ('Gallbladder Disease', "Gallbladder Disease"),
        ('Gastrointestinal Bleeding', "Gastrointestinal Bleeding"),
        ('Hip Fracture', "Hip Fracture"),
        ('Appendicitis', "Appendicitis"),
        ('Other', "Other")
    )

    account = models.ForeignKey(Account, related_name="admissions_account")
    timestamp = models.DateTimeField(auto_now_add=True)
    discharged_timestamp = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=20, choices=ADMISSIONREASON)
    description = models.CharField(blank=True, max_length=1000)
    hospital = models.ForeignKey(Hospital)
    active = models.BooleanField(default=True)


class Prescription(models.Model):
    patient = models.ForeignKey(Account, related_name="prescriptions_patient")
    doctor = models.ForeignKey(Account, related_name="prescriptions_doctor")
    date = models.DateField()
    medication = models.CharField(max_length=100)
    strength = models.CharField(max_length=30)
    instruction = models.CharField(max_length=200)
    refill = models.IntegerField()
    active = models.BooleanField(default=True)

    
class MedicalInfo(models.Model):
    BLOOD = (
        ('A+', 'A+ Type'),
        ('B+', 'B+ Type'),
        ('AB+', 'AB+ Type'),
        ('O+', 'O+ Type'),
        ('A-', 'A- Type'),
        ('B-', 'B- Type'),
        ('AB-', 'AB- Type'),
        ('O-', 'O- Type'),
    )

    @staticmethod
    def to_blood(key):
        for item in MedicalInfo.BLOOD:
            if item[0] == key:
                return item[1]
        return "None"

    account = models.ForeignKey(Account, related_name="medicalinfo_account")
    bloodType = models.CharField(max_length=10, choices=BLOOD)
    allergy = models.CharField(max_length=100)
    alzheimer = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    stroke = models.BooleanField(default=False)
    comments = models.CharField(max_length=700)

    def get_populated_fields(self):
        fields = {
            'account': self.account.pk,
            'bloodType': self.bloodType,
            'allergy': self.allergy,
            'alzheimer': self.alzheimer,
            'asthma': self.asthma,
            'diabetes': self.diabetes,
            'stroke': self.stroke,
            'comments': self.comments,
        }
        return fields


class MedicalTest(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    hospital = models.ForeignKey(Hospital)
    description = models.CharField(max_length=200)
    doctor = models.ForeignKey(Account, related_name="medicaltests_doctor")
    patient = models.ForeignKey(Account, related_name="medicaltests_patient")
    private = models.BooleanField(default=True)
    completed = models.BooleanField()
    image1 = models.FileField(blank=True, null=True, upload_to='medtests/%Y/%m/%d')
    image2 = models.FileField(blank=True, null=True, upload_to='medtests/%Y/%m/%d')
    image3 = models.FileField(blank=True, null=True, upload_to='medtests/%Y/%m/%d')
    image4 = models.FileField(blank=True, null=True, upload_to='medtests/%Y/%m/%d')
    image5 = models.FileField(blank=True, null=True, upload_to='medtests/%Y/%m/%d')

    def get_populated_fields(self):
        """
        This is used by the form to collect the data.
        """
        fields = {
            'name': self.name,
            'date': self.date,
            'hospital': self.hospital,
            'description': self.description,
            'doctor': self.doctor,
            'patient': self.patient,
            'private': self.private,
            'completed': self.completed,
            'image1': self.image1,
            'image2': self.image2,
            'image3': self.image3,
            'image4': self.image4,
            'image5': self.image5,
        }
        return fields

class Statistics(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()

    def get_populated_fields(self):
        """
        This is used by the form to collect the data.
        """
        fields = {
            'startDate': self.startDate,
            'endDate': self.endDate,
        }
        return fields