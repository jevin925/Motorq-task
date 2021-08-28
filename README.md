# MOTORQ Task

## STEP-1 : Clone this repository

## STEP-2 : Creating Virtual environment
##### Use following command to set up virtual environment
py -m venv <env-name>
##### Activate environment
<env-name>\Scripts\activate.bat

## STEP-3 Install requirements.txt
pip install -r requirements.txt

## STEP-4 : Run following commands

python manage.py runserver

#### The website should be up and running




#### API Documentation 
## Google Doc Link to API Documentation : https://docs.google.com/document/d/1umjxS8Iizqnk2DVH-BGEtkKPiWEAckSsY8myfEoEhuU/edit?usp=sharing


API Documentation:

Add Student:

Method: POST
Endpoint: https://motorq-task.herokuapp.com/api/user/add-student
Description: API to add a student in the “student” table

JSON data to be posted to add a student :

{
	“name”:”Jevin”,
         “email “: “jevin925@gmail.com”
}

---------------------------------------------------------------------------------------------------------------------
Get Student Details:

Method: GET
Endpoint: https://motorq-task.herokuapp.com/api/user/get-students
Description: API  for fetching student details from the “student” table

---------------------------------------------------------------------------------------------------------------------
Add Subject:

Method: POST
Endpoint: https://motorq-task.herokuapp.com/api/user/add-subject
Description: API to add a subject in the “subjects” table

JSON data to be posted to add a student :

{
	“name”:”DSA”,
        “available_seats” : 60,
        “sub_day” : “Tuesday”,
        “start_time” : “17:30:00”,
        “end_time” : “18:30:00”,
}
---------------------------------------------------------------------------------------------------------------------

Get Subject Details:

Method: GET
Endpoint: https://motorq-task.herokuapp.com/api/user/get-subjects
Description:  API to fetch subject details from the “subjects” table

---------------------------------------------------------------------------------------------------------------------

Register Subject:

Method: POST
Endpoint: https://motorq-task.herokuapp.com/api/user/register-subject

Description: API for a student to register a subject. Upon calling this API, it will first check if there is a seat available for the course. If available, then it will check for the time slot clashing with the time slots of already registered subjects.

If seats are not available, then a response is generated stating: “No seats available”.
If seats are available but the time slot clashes, a response stating: “Time slot clashed” will be generated.

JSON data to be posted to register a subject:

{
	“sub_id” : “1”,
	“user_id” : “1”
}

---------------------------------------------------------------------------------------------------------------------

Unregister Subject:

Method: POST
Endpoint: https://motorq-task.herokuapp.com/api/user/unregister-subject

Description: API to unregister the subject. Upon calling this API, it will unregister the already registered subject for a particular student and if there exists any student in the “waiting_list”, the first student in the list will be assigned this unregistered subject.

JSON data to be posted to unregister a subject:

{
	“sub_id” : “1”,
	“user_id” : “1”
}

## Thank you
