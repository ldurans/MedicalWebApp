import unittest

from django.test import TestCase

from healthnet.models import Hospital
from healthnet.models import Location
from healthnet.models import Profile, Admission, Account, User
from django.core.urlresolvers import resolve
from healthnet.views_home import *
from django.http import HttpRequest
from django.test.client import Client
from healthnet.forms import AdmissionForm, ProfileForm, LoginForm, validate_birthday, validate_username_available,validate_username_exists
from datetime import date
from datetime import datetime
from django import forms


class AppointmentMethodTests(TestCase):
    if __name__ == '__main__':
        unittest.main()

    def setUp(self):
        Location.objects.create(city='Rochester', zip="14623", state='NY,country = USA',
                                address="5353 Jefferon Rd")
        Location.objects.create(city='Buffalo', zip="14623", state='NY,country = USA',
                                address="5353 Jefferon Rd")

    def test_compare_locations(self):
        first_loc = Location.objects.get(city="Rochester")
        second_loc = Location.objects.get(city="Buffalo")
        self.assertEqual(first_loc == second_loc, False)


class HospitalTestCase(TestCase):
    def setUp(self):
        Location.objects.create(city="Brooklyn", zip="11210", state="New York", country="USA",
                                address="1000 Thousand Ave")
        Hospital.objects.create(name="NY Methodist Hospital", phone="347-743-1347",
                                location=Location.objects.get(city="Brooklyn"))

    def test_hospitals_can_get_location(self):
        methodistHospitalLocation = Location.objects.get(city="Brooklyn")
        methodistHospital = Hospital.objects.get(name="NY Methodist Hospital")
        self.assertEqual(methodistHospital.location, methodistHospitalLocation)


class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(firstname = "Kazusa", lastname = "Kitahara", insurance = "Excellus",)
        Profile.objects.create(firstname = "Kasumi", lastname = "Kitahara", insurance = "Excellus",)

    def test_profile(self):
        profile1 = Profile.objects.get(firstname = "Kazusa")
        profile2 = Profile.objects.get(firstname = "Kasumi")
        self.assertEqual(profile1 == profile2, False)


class TestHomeViews(TestCase):

    """
    Used to test the views for HealthNet's homepage
    """

    """Test to make sure the homepage renders the login view"""
    def test_login(self):
        found = resolve('/')
        self.assertEqual(found.func, login_view)

    """Test to make sure logout view resolves to the correct URL"""
    def test_logout(self):
        found = resolve('/logout/')
        self.assertEqual(found.func, logout_view)

    """Tests to make sure register view resolves to the correct URL"""
    def test_register(self):
        found = resolve('/register/')
        self.assertEqual(found.func, register_view)

    """Tests to make sure error denied view resolves to the correct URL"""
    def test_error_denied(self):
        found = resolve('/error/denied/')
        self.assertEqual(found.func, error_denied_view)


class TestMedtestViews(TestCase):

    """
    Used to test the views for the Medical Test module
    """

    """Test to make sure medical test upload view resolves to the correct URL"""
    def test_medtest_upload(self):
        from healthnet.views_medtest import create_view
        found = resolve('/medtest/upload/')
        self.assertEqual(found.func, create_view)

    """Test to make sure medical test list view resolves to the correct URL"""
    def test_medtest_list(self):
        from healthnet.views_medtest import list_view
        found = resolve('/medtest/list/')
        self.assertEqual(found.func, list_view)

    """Test to make sure medical test display view resolves to the correct URL"""
    def test_medtest_display(self):
        from healthnet.views_medtest import display_view
        found = resolve('/medtest/display/')
        self.assertEqual(found.func, display_view)

    """Test to make sure medical test update view resolves to the correct URL"""
    def test_medtest_update(self):
        from healthnet.views_medtest import update_view
        found = resolve('/medtest/update/')
        self.assertEqual(found.func, update_view)


class TestAdmissionViews(TestCase):

    """
    Used to test the views for the Admission module
    """

    """Test to make sure admission admit view resolves to the correct URL"""
    def test_admission_admit(self):
        from healthnet.views_admission import admit_view
        found = resolve('/admission/admit/')
        self.assertEqual(found.func, admit_view)

    """Test to make sure admission list view resolves to the correct URL"""
    def test_admission_list(self):
        from healthnet.views_admission import list_view
        found = resolve('/admission/list/')
        self.assertEqual(found.func, list_view)


class TestAppointmentViews(TestCase):

    """
    Used to test the views for the Appointment module
    """

    """Test to make sure appointment list view resolves to the correct URL"""
    def test_appointment_list(self):
        from healthnet.views_appointment import list_view
        found = resolve('/appointment/list/')
        self.assertEqual(found.func, list_view)

    """Test to make sure appointment calendar view resolves to the correct URL"""
    def test_appointment_calendar(self):
        from healthnet.views_appointment import calendar_view
        found = resolve('/appointment/calendar/')
        self.assertEqual(found.func, calendar_view)

    """Test to make sure appointment update view resolves to the correct URL"""
    def test_appointment_update(self):
        from healthnet.views_appointment import update_view
        found = resolve('/appointment/update/')
        self.assertEqual(found.func, update_view)

    """Test to make sure appointment create view resolves to the correct URL"""
    def test_appoinment_create(self):
        from healthnet.views_appointment import create_view
        found = resolve('/appointment/create/')
        self.assertEqual(found.func, create_view)


class TestPrescriptionViews(TestCase):

    """
    Used to test the views for the Prescription module
    """

    """Test to make sure prescription create view resolves to the correct URL"""
    def test_prescription_create(self):
        from healthnet.views_prescription import create_view
        found = resolve('/prescription/create/')
        self.assertEqual(found.func, create_view)

    """Test to make sure prescription list view resolves to the correct URL"""
    def test_prescription_list(self):
        from healthnet.views_prescription import list_view
        found = resolve('/prescription/list/')
        self.assertEqual(found.func, list_view)


class TestMessageViews(TestCase):

    """
    Used to test the views for the Message module
    """

    """Test to make sure message list view resolves to the correct URL"""
    def test_message_list(self):
        from healthnet.views_message import list_view
        found = resolve('/message/list/')
        self.assertEqual(found.func, list_view)

    """Test to make sure message new view resolves to the correct URL"""
    def test_message_new(self):
        from healthnet.views_message import new_view
        found = resolve('/message/new/')
        self.assertEqual(found.func, new_view)


class TestMedicalInfoViews(TestCase):

    """
    Used to test the views for the Medical Info module
    """
    """Test to make sure medical info list view resolves to the correct URL"""
    def test_medinfo_list(self):
        from healthnet.views_medicalInfo import list_view
        found = resolve('/medicalinfo/list/')
        self.assertEqual(found.func, list_view)

    """Test to make sure medical info update view resolves to the correct URL"""
    def test_medinfo_update(self):
        from healthnet.views_medicalInfo import update_view
        found = resolve('/medicalinfo/update/')
        self.assertEqual(found.func, update_view)

class TestAdminViews(TestCase):

    """
    Used to test the views for administrator accounts in HealthNet
    """
    def test_admin_users(self):
        from healthnet.views_admin import users_view
        found = resolve('/admin/users/')
        self.assertEqual(found.func, users_view)

    def test_admin_activity(self):
        from healthnet.views_admin import activity_view
        found = resolve('/admin/activity/')
        self.assertEqual(found.func, activity_view)

    def test_admin_add_hospital(self):
        from healthnet.views_admin import add_hospital_view
        found = resolve('/admin/add_hospital/')
        self.assertEqual(found.func, add_hospital_view)

    def test_admin_create_employee(self):
        from healthnet.views_admin import createemployee_view
        found = resolve('/admin/createemployee/')
        self.assertEqual(found.func, createemployee_view)

    def test_admin_statistic(self):
        from healthnet.views_admin import statistic_view
        found = resolve('/admin/statistics/')
        self.assertEqual(found.func, statistic_view)

    def test_admin_csv_import(self):
        from healthnet.views_admin import csv_import_view
        found = resolve('/admin/import/')
        self.assertEqual(found.func, csv_import_view)


class TestProfileViews(TestCase):
    """
    Used to test the views for the Profile module
    """
    def test_profile_profile(self):
        from healthnet.views_profile import profile_view
        found = resolve('/profile/')
        self.assertEqual(found.func, profile_view)

    def test_profile_password(self):
        from healthnet.views_profile import password_view
        found = resolve('/profile/password/')
        self.assertEqual(found.func, password_view)

    def test_profile_update(self):
        from healthnet.views_profile import update_view
        found = resolve('/profile/update/')
        self.assertEqual(found.func, update_view)


class InvalidUser(TestCase):
    def setUp(self):
        self.client = Client()

    "Test to make sure that when an invalid user logs in page does not crash"
    def test_invalidUser(self):
        response = self.client.post('/', {'username': 'patienta@test.com', 'password': 'a'})
        self.assertRedirects(response, '/setup/', status_code=302, target_status_code=200, msg_prefix='')


class TestAdmission(TestCase):
    "Test to make sure the admission page is not available to users that are not logged in"
    def test_NoLogin_NoView(self):
        url = '/admission/admit/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class TestProfileForm(TestCase):

    def setUp(self):
        bday = datetime.now()
        location_data = Location.objects.create(
            city="Rochester",
            zip="14623",
            state="New York",
            country="United States",
            address="None"
        )
        test_hospital = Hospital.objects.create(location=location_data)

        self.form_data = {
            'firstname': "Test",
            'lastname': "User",
            'insurance': "5854-5854-5868",
            'emergencyContactName': "Bobby",
            'emergencyContactNumber': "Buschay",
            'sex': 'M',
            'birthday': bday,
            'phone': "585-555-5555",
            'allergies': "I aint got none",
            'created': datetime.now(),
            'prefHospital': test_hospital.id,
        }

    "Test valid data in profile form"
    def test_valid_profile_form(self):
        form = ProfileForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    "Test insurance missing causes profile form to not be valid"
    def test_inurance_missing(self):
        self.form_data['insurance'] = ''
        form = ProfileForm(data=self.form_data)
        self.assertFalse(form.is_valid())


class TestFormValidators(TestCase):

    def setUp(self):
        self.birthday = date(1000, 1, 1)

    "Test validator to make sure birthdays more than 200 years ago raise error"
    def test_validate_lower_bound_birthday(self):
        self.assertRaises(forms.ValidationError, validate_birthday, self.birthday)

    def test_validate_upper_bound_birthday(self):
        self.birthday = date(2015, 12, 12)
        self.assertRaises(forms.ValidationError, validate_birthday, self.birthday)

    def test_validate_correct_birthday(self):
        self.birthday = date(1994, 12, 12)
        self.assertIsNone(validate_birthday(self.birthday))

    def test_validate_username_exists(self):
        User.objects.create(username="test@test.com", password="password")
        self.assertRaises(forms.ValidationError, validate_username_exists, 'test@doesntexist.com')

    def test_validate_username_available(self):
        User.objects.create(username="test@test.com", password="password")
        self.assertRaises(forms.ValidationError, validate_username_available, 'test@test.com')


























