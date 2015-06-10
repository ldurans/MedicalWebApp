 _   _                  _   _     _       _   _          _                    |
| | | |   ___    __ _  | | | |_  | |__   | \ | |   ___  | |_                  |
| |_| |  / _ \  / _` | | | | __| | '_ \  |  \| |  / _ \ | __|                 |
|  _  | |  __/ | (_| | | | | |_  | | | | | |\  | |  __/ | |_                  |
|_| |_|  \___|  \__,_| |_|  \__| |_| |_| |_| \_|  \___|  \__|                 |
                                                                              |
                                       HealthNet by Project Curry             |
                                                                              |
------------------------------------------------------------------------------+
    INSTALLATION                                                              |
------------------------------------------------------------------------------+

1. Make sure that the target environment for HealthNet has Python 3.2.2 and
   Django 1.6.5 installed and running correctly.

2. Unzip the compressed folder containing the HealthNet application into a
   suitable directory of your choice.

3. Once that is done, open a command prompt window (Windows) or a Terminal
   window (Mac OS).

4. In your terminal or command prompt window, navigate to the directory that
   the file 'quickstart.py' is located in.

5. Type in the command "python quickstart.py" on your command prompt or
   Terminal window and run it.

6. Take the HTTP address from the line beginning with "Starting development
   server at...". Put that web address into a web browser of your choice and go
   to it. The URL you enter should look something like this:
   http://localhost:8000    OR      http://127.0.0.1:8000

7. If this is the first time running HealthNet, when you visit the web address,
   you will be prompted to setup an Administrator account through which the
   rest of the system can be configured.

------------------------------------------------------------------------------+
    LOGINS AND PASSWORDS                                                      |
------------------------------------------------------------------------------+

We have setup a number of accounts on the system that have been pre populated
with data to fully show off our interface. The login credentials for them are:

    Username: admina@test.com
    Password: a

    Username: doctora@test.com
    Password: a

    Username: nursea@test.com
    Password: a

    Username: patienta@test.com
    Password: a

------------------------------------------------------------------------------+
    DISCLAIMERS                                                               |
------------------------------------------------------------------------------+

The HealthNet application provides the following functionality

- Patient Registration
- Administrator Registration
- Update Patient Profile Information
- Update Patient Medical Information
- Create or Update Patient Appointment
- Cancel Patient Appointment
- Appointment Calendar
- Add/Remove Prescriptions
- Viewing Patient Medical Information, Prescriptions and Tests and Results
- Release Test Results
- Logging System Activity
- Admission and Discharge to/from Hospital
- Viewing Activity Log
- Viewing System Statistics
- Patient Transfer
- Upload Patient Information
- Send Private Message
- Importing / Exporting Information Through .csv Files

Unfortunately, things don't always work how we want them to. Here is a list of
known bugs currently in the HealthNet system:

- Patients cannot export information.
- Administrator is able to change its role to any of the other roles
  (Patient, Nurse, Doctor)
- We do not have a unified view of patient medical information, prescriptions,
  tests, and results.
- We keep track of admitted and discharged patients in the same list.

------------------------------------------------------------------------------+
    BASIC USAGE INSTRUCTIONS                                                  |
------------------------------------------------------------------------------+

1.  Patient Registration - patients only

    a) When first starting HealthNet, you will be greeted by HealthNet's login
       page.

    b) Once there, press one of the 'Register' buttons located either in the
       upper right corner of the page or in the middle of the page.

    c) HealthNet will take you to a registration form for patients. Once there,
       fill in the form with the information asked for by the form.

    d) Once done, press the 'Register' button.

    e) You should now be logged in and taken to the dashboard page with a green
       alert message telling you that you have successfully been registered
       with HealthNet. If you do not see this, the registration form may not
       have been filled out correctly. HealthNet will tell you what part(s) of
       the form must be done. Retry steps c and d.

2.  Doctor, Nurse, and/or Administrator Registration - administrators only

    a) Doctors, Nurses, and Administrators must be registered by an already
       existing HealthNet administrator. To do this, an administrator must
       first be logged in.

    b) Once the administrator is logged in, move the mouse pointer over to the
       left side of the page to reveal a side bar - if it is hidden - and
	     click 'Manage Users'.

    c) You will be directed to a page displaying all of the users registered
       to HealthNet. In the upper left of the page, next to the side bar,
       press the green 'Add Employee' button.

    d) Now you should see the 'Add an Employee' form. Fill in the form,
       entering the information for your new employee's account.

    e) Once done, press the 'Register' button.

    f) You should now see a green alert message telling you that the new
       doctor, nurse, or administrator account was successfully registered.
       If you do not see one, the form may not have been filled in correctly.
       HealthNet will tell you what part(s) of the form must be done.
       Retry steps d and e.

3.  Logging On to HealthNet - any user type

    a) When first starting HealthNet, you will be greeted by HealthNet's login
       page.

    b) If you have not already created an account, you cannot login and must
       first register. If you have, simply type in the email address you used
       to register into the 'Email' field and the password you chose into the
       'Password' field and then press enter or click on the dark blue 'Login'
       button

    c) If you provided the same credentials you used to register, you shall be
       logged in to HealthNet and be taken to the dashboard page. Otherwise,
       you shall remain on the login page because your credentials were not
       right. Retype your credentials and try again.

4.  Logging Out of HealthNet - any user type

    a) While you are logged into your account, navigate over to
       'Account Management' located on the upper right of the page.

    b) Press it once and a pop-down menu will be displayed.

    c) Now press the 'Logout' button on the bottom of the menu.

    d) HealthNet will log you out of the system and return you back to the
       login page telling you that you have successfully logged out.

5.  Changing Your Password - any user type

    a) While you are logged into your account, navigate over to
       'Account Management' located on the upper right of the page.

    b) Press it once and a pop-down menu will be displayed.

    c) Now press the 'Change Password' option near the bottom of the menu.

    d) Once you are taken to the 'Password Reset' page, type in your current
       password into the 'Current' field.

    e) Now type in the password you would like to change to twice: once into
       the 'New' field and once more into the field right below it.

    f) Press the 'Change Password' button.

    g) You should now see a green alert message telling you that your
       password has been successfully changed. If you do not see one, your
       password has not been changed. HealthNet will tell you what password
       did not match. Retry steps d through f.

6.  Viewing Your Profile - any user type

    a) While you are logged into your account, navigate over to
       'Account Management' located on the upper right of the page. Press
       'View Profile' to go to your dashboard page.

7.  Updating Your Profile - any user type

    a) While you are logged into your account, navigate over to
       'Account Management' located on the upper right of the page.

    b) Press it once and a pop-down menu will be displayed.

    c) Now press the 'Update Profile' option in the middle of the menu.

    d) You will be taken to the 'Update Profile' form. From there, you may fill
       out or alter any of the information in the form.

    e) Once done, press the 'Update Profile' button on the bottom of the page.

    f) You should now see a green alert message telling you that your profile
       has been updated. If you do not see one, your profile has not been
       updated. HealthNet will tell you what part(s) of the form must be done.
       Retry steps d through e.

8.  Viewing Your Messages - any user type

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Messages'.

    b) HealthNet will take you to your Messages page.

    c) To view the messages you have received, press the 'Received messages'
       tab.

    d) To view the messages you have sent, press the 'Sent messages' tab.

9.  Reading A Message - any user type

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Messages'.

    b) HealthNet will take you to your Messages page.

    c) To read to a message, press the 'Read' button located under the
       'Options' column.

    d) A modal view will fall down from the top of the screen displaying the
       message's subject, sender, receiver, and contents.

    e) Click on the green 'Reply' button to reply to the sender or click on the
       dark blue 'Return to list' button to go back to the Messages page.

10. Replying to A Message - any user type

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Messages'.

    b) HealthNet will take you to your Messages page.

    c) To reply to a message, you can either first read it and then press the
       'Reply' button on the modal view or press the 'Reply' button located
       under the 'Options' column.

    d) You will be taken to the 'New Message' form. Fill out the header and
       body of the message.

    e) Once done, press the 'Send Message' button in the middle of the page.

    f) You should now be taken back to your Messages page. You should see a
       green alert message telling you that your message was successfully sent.
       If you do not see this, the message was not sent. HealthNet will tell
       you what part(s) of the form must be done. Retry steps d and e.

11. Sending A Message - any user type

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Messages'.

    b) HealthNet will take you to your Messages page.

    c) Press the green 'New message' button near the top of the screen.

    d) You will be taken to the 'New Message' form. Choose who you would like
       to send this message to and then fill out the header and body of the
       message.

    e) Once done, press the 'Send Message' button in the middle of the page.

    f) You should now be taken back to your Messages page. You should see a
       green alert message telling you that your message was successfully sent.
       If you do not see this, the message was not sent. HealthNet will tell
       you what part(s) of the form must be done. Retry steps d and e.

12. Archiving A Message - any user type

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Messages'.

    b) HealthNet will take you to your Messages page.

    c) To archive a message, press the 'Archive' button under the 'Options'
       column.

    d) You should now be taken back to your Messages page. You should see a
       green alert message telling you that the mesage was archived.

13. Viewing Appointments - patients, nurses, and doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Appointments'.

    b) HealthNet will take you to your Appointments page.

    c) To view all the appointments that are currently active, press the
       'Active appointments' tab.

    d) To view all the appointments that have been cancelled, press the
       'Cancelled appointments' tab.


14. Creating An Appointment - patients, nurses, and doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Appointments'.

    b) HealthNet will take you to your Appointments page.

    c) Press the green 'New Appointment' button near the top of the page

    d) You will be taken to the 'Create Appoinment' page.

    e) Once there, fill out the necessary information and then press 'Create'
       when you are done.

    f) You should be taken back to your Appointments page. You should see a
       green alert message telling you that the appointment was successfully
       created. If you do not see this, the appointment was not created.
       HealthNet will tell you what part(s) of the form must be done.
       Retry step e.

15. Canceling An Appointment - patients and doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Appointments'.

    b) HealthNet will take you to your Appointments page.

    c) To cancel an appointment, press the 'Cancel' button under the 'Options'
       column.

    d) HealthNet will ask for confirmation of intent. Press 'Cancel the
       appointment' and the appointment will be canceled.

16. Viewing Medical Tests - patients, nurses, and doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Medical Tests'.

    b) HealthNet will take you to your Medical Tests page.

    c) From there, you will see all of the medical tests uploaded to the
       HealthNet system. You can go them by sorting through it, going through
       each set of data manually, or searching for a particular item using the
       search bar in the upper right of the page.

    d) To view one particular medical test, press the 'Display' button under
       the 'Options' column in the table of medical tests.

17. Creating A Medical Test - doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Medical Tests'.

    b) HealthNet will take you to your Medical Tests page.

    c) Press the green 'Upload Medical Test' button near the top of the page.

    d) You will be taken to the 'Upload Test Result' page.

    e) Once there, fill out the information asked for and then press 'Upload'.

    f) You should see a green alert message telling you that the medical test
       was successfully uploaded. If you do not see this, the medical test was
       not uploaded. HealthNet will tell you what part(s) of the form must be
       done. Retry step e.

18. Updating A Medical Test - doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Medical Tests'.

    b) HealthNet will take you to your Medical Tests page.

    c) To update a medical test, press the 'Update' button under the 'Options'
       column.

    d) You will be taken to the 'Update Medical Test' page.

    e) Once there, you may fill out or alter the information currently in the
       form.

    e) You should see a green alert message telling you that the medical test
       was successfully uploaded. If you do not see this, the medical test was
       not uploaded. HealthNet will tell you what part(s) of the form must be
       done. Retry step e.

19. Viewing Prescriptions - patients, nurses, and doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Prescriptions'.

    b) HealthNet will take you to your Prescriptions page.

    c) From there, you will see all of the prescriptions filled by the
       HealthNet system. You can go them by sorting through it, going through
       each set of data manually, or searching for a particular item using the
       search bar in the upper right of the page.

20. Filling A Prescription - doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Prescriptions'.

    b) HealthNet will take you to your Prescriptions page.

    c) Press the green 'Add Prescription' button near the top of the page.

    d) HealthNet will take you to the 'Add Prescriptions' form. Fill out the
       information asked for by the form.

    e) Once done, press the 'Add Prescription' button.

    f) You should see a green alert message telling you that the prescription
       was successfully filled out. If you do not see this, the prescription
       was not filled out. HealthNet will tell you what part(s) of the form
       must be done. Retry step d.

21. Canceling A Prescription - doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Prescriptions'.

    b) HealthNet will take you to your Prescriptions page.

    c) To cancel a prescription, press the 'Delete' button under the 'Options'
       column.

    d) Click the red 'Delete' button to confirm the deletion of the
       prescription or click the dark blue 'Return to list' button or the
       'x' on the upper right of the pop up window to not delete the
       prescription.

    e) You should see a green alert message telling you that the prescription
       was successfully deleted if the red 'Delete' button was pressed.
       Otherise the prescription was not deleted and the user will be taken
       back to the prescription display.

22. Viewing Admissions - administrators only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Admitted Patients'.

    b) HealthNet will take you to your Admissions page.

    c) From there, you will see the record of admissions filled by the
       HealthNet system. You can go them by sorting through it, going through
       each set of data manually, or searching for a particular item using the
       search bar in the upper right of the page.

23. Admitting A Patient - nurses and doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Admitted Patients'.

    b) HealthNet will take you to your Admissions page.

    c) Press the green 'Admit Patient' button located near the top of the page.

    d) You will be taken to the 'Admit Patient' form. Fill out the information
       required by the form.

    e) Once done, press the 'Admit' button near the bottom of the page.

    f) You should be taken back to your Admissions page. You should see a green
       alert message telling you that the patient was successfully admiited.
       If you do not see this, the patient was not admitted. HealthNet will
       tell you what part(s) of the form must be done. Retry steps d and e.

24. Discharging A Patient - doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Admitted Patients'.

    b) HealthNet will take you to your Admissions page.

    c) To discharge a patient, press the 'Discharge' button under the 'Options'
       button.

    d) HealthNet will ask you for confirmation of intent. Press 'Discharge'
       again and the patient will now be discharged.

25. Importing / Exporting A .csv File - administrators only

    a) Keep in mind that only HealthNet administrators can view HealthNet
       activity.

    b) While you are logged into your account (as an administrator), go to the
       sidebar menu to the left of the page and press 'CSV Management'.

    c) HealthNet will take you to the CSV Management page.

    d) By default, the first option that'll be shown to you is to import
       information through a .csv file.

    e) To import through a .csv file, press the 'Choose file' button and
       select the .csv file that you would like to upload. Then, press
       'Submit'. You should see an green alert message telling you that
       information was imported into HealthNet.

    f) To export to a .csv file, press the 'Export Information' button and then
       select what information you would like to export. Once you have
       selected, then press 'Submit'. A .csv file will be downloaded by your
       web browswer containing the specified information.

26. Viewing the Activity on HealthNet - administrators only

    a) Keep in mind that only HealthNet administrators can view HealthNet
       activity.

    b) While you are logged into your account (as an administrator), go to the
       sidebar menu to the left of the page and press 'Viewing Activity'.

    c) HealthNet will take you to the HealthNet activity page.

    d) From there, you can go through the logged activity by clicking on the
       table headers 'Type', 'Description', 'User', and 'Time' to sort by that
       parameter or search for a particular item using the search bar in the
       upper right of the page.

27. Viewing System Statistics - administrators only

    a) Keep in mind that only HealthNet administrators can view statistics
       found from HealthNet.

    b) While you are logged into your account (as an administrator), go to the
       sidebar menu to the left of the page and press 'View Statistics'.

    c) HealthNet will take you to the HealthNet statistics page.

    d) From there, you can see different statistics such as the number of
       patients admitted and the number of users registered. To narrow down
       statistics found between two points in time, type in a start time and an
       end time and then press 'Get Statistics'.

28. Managing HealthNet Users - administrators only

    a) Keep in mind that only HealthNet administrators can manage the users
       registered in HealthNet.

    b) While you are logged into your account (as an administrator), go to the
       sidebar menu to the left of the page and press 'Manage Users'.

    c) HealthNet will take you to the HealthNet user management page.

    d) From there, you can go through the users created in HealthNet by
       sorting by clicking the table headers 'Username','First name', 'Last
       name', and 'Role', going through each set of data manually, or
       searching for a particular item using the search bar in the upper right
       of the page.

    e) From here, you can also press the green 'Add Employee' button to
       register a new employee.

29. Viewing Patient Medical Information
         - patients(their own only), nurses, and doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Medical Info'.

    If user is patient:
    b) If user is a patient then their medical profile is displayed.

    If user is nurse or doctor:
    b) Healthnet will take you to the Healthnet Patients List page that
       displays the patient's name, blood type, and allergy as well as an
       option column in a table.

    c) From there, you will see a table of patients, their blood type,
       allergy, and options available for the doctor and nurse. You can go
       through them by sorting by clicking any one of the table headers
       'Patient', 'Blood', 'Type' and 'Allergy', or searching for a particular
       item using the searchbar in the upper right of the page.

30. Update Patient Medical Information - nurses and doctors only

    a) While you are logged into your account, go to the sidebar menu to the
       left of the page and press 'Medical Info'.

    b) Healthnet will take you to the Healthnet Patients List page. that
       displays the patient's name, blood type, and allergy as well as an
       options column in a table.

    c) From there, you will see a table of patients, their blood type, allergy,
       and option available for the doctor and nurse. You can go through them
       by sorting by clicking any one of the table headers 'Patient', 'Blood',
       'Type' and 'Allergy', or searching for a particular item using the
       search bar in the upper right of the page.

    d) Locate the desired user by searching manually or using he search bar.
       Under the 'options' column to the farthest right of the table, click on
       the orange 'Update' button corresponding to the desired patient.

    e) HealthNet will take you to the 'Update Medical Info' form. Fill out the
       information asked for by the form.

    e) Once done, press the dark blue 'Update Medical Info' button located at
       the bottom of the page.

    f) You should see a green alert message telling you that the medical info
       was successfully updated. If you do not see this, the form was not
       properly filled out. HealthNet will tell you what part(s) of the form
       must one. Retry step e.

------------------------------------------------------------------------------+
    CREDITS                                                                   |
------------------------------------------------------------------------------+

HealthNet was brought to you by:

    Kaiwen Zheng      -   kxz6582@rit.edu
    Daniel Roach      -   dxr5716@rit.edu
    Arshdeep Khalsa   -   ask7708@rit.edu
    Joseph Cumbo      -   jwc6999@rit.edu
    David Lor         -   dsl4458@rit.edu


