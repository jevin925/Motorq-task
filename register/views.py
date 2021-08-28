from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, user_subject, waiting_list, subjects
from django.http import JsonResponse
from django.http.response import HttpResponse
from .serializers import StudentSerializer, SubjectSerializer, UserSubjectSerializer, WaitingListSerializer
# Create your views here.


# API For Adding Student
# request : POST
# endpoint : add-student
class RegisterStudent(APIView):
    
    
        def post(self, request):
            
            serializer = StudentSerializer(data = request.data)
            if not serializer.is_valid():
               
                return Response({
                "success":False,
                "message": serializer.errors,
            
                })

            serializer.save()

            return Response({
                "success":True,
                "message":"Student added successfully",
                "data":serializer.data
                })

# API For Getting Student
# request : GET
# endpoint : get-all-students
class GetStudent(APIView):
    
        def get(self, request):
            student_instance = User.objects.all()
            serializer = StudentSerializer(student_instance, many=True)

            return Response({
                "success":True,
                "message":"",
                "data":serializer.data
                })  


# API For Adding Subject
# request : POST
# endpoint : add-subject
class AddSubject(APIView):
    
        def post(self, request):
            
            serializer = SubjectSerializer(data = request.data)
            if not serializer.is_valid():
               
                return Response({
                "success":False,
                "message": serializer.errors,
            
                })

            serializer.save()

            return Response({
                "success":True,
                "message":"Subject added successfully",
                "data":serializer.data
                })


# API For Getting Subject
# request : GET
# endpoint : get-all-subject
class GetSubject(APIView):
    
        # permission
        def get(self, request):
            subject_instance = subjects.objects.all()
            serializer = SubjectSerializer(subject_instance, many=True)

            return Response({
                "success":True,
                "message":"",
                "data":serializer.data
                })  


# API For Registering subject
# request : POST
# endpoint : register-subject
class RegisterSubject(APIView):
    

        def post(self, request):
            
            serializer = UserSubjectSerializer(data = request.data)
            subject_instance = subjects.objects.get(id=request.data['sub_id'])
            user_instance = user_subject.objects.filter(user_id=request.data['user_id'])
            for i in user_instance:
              
               if (i.sub_id.sub_day == subject_instance.sub_day) and ((i.sub_id.start_time <= subject_instance.start_time and i.sub_id.end_time >= subject_instance.start_time) or (i.sub_id.start_time <= subject_instance.end_time and i.sub_id.end_time >= subject_instance.end_time) or (i.sub_id.start_time >= subject_instance.start_time and i.sub_id.end_time <= subject_instance.end_time)):
                  
                    return Response({
                    "success":False,
                    "message": "Subject slot is clashing with " + i.sub_id.name + "."
                    })
            
            if subject_instance.available_seats == 0:
                wait_serializer =  WaitingListSerializer(data=request.data)
                if not wait_serializer.is_valid():
               
                    return Response({
                    "success":False,
                    "message": serializer.errors,
                
                    })
                wait_serializer.save()

                return Response({
                "success":False,
                "message": "No Seat available so you are put in waiting list",
            
                })
           

            if not serializer.is_valid():
               
                return Response({
                "success":False,
                "message": serializer.errors,
            
                })
            
            subject_instance.available_seats -=  1
            subject_instance.save()
            serializer.save()

            return Response({
                "success":True,
                "message":"Subject added successfully",
                "data":serializer.data
                })



# API For Cancelling Subject
# request : Post
# endpoint : unregister-subject
class UnregisterSubject(APIView):
    
        def post(self, request):
            
            user_subject_instance = user_subject.objects.get(sub_id=request.data['sub_id'], user_id=request.data['user_id'])
            if not user_subject_instance:
                 return Response({
                    "success":False,
                    "message":"Subject not registered",
                
                    })
            user_subject_instance.delete()
            waiting_list_instance = waiting_list.objects.filter(sub_id = request.data['sub_id'])
            
            for i in waiting_list_instance:
                user_subject_ins  =  user_subject(sub_id = i.sub_id, user_id = i.user_id)
                user_subject_ins.save()
                i.delete()
                break
            
            return Response({
                "success":True,
                "message":"Subject Unregistered successfully",
          
                })