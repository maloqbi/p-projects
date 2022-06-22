from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .models import Student
from .serializers import StudentSerializer


class StudentItemViews(APIView):
    
    serializer_calss = StudentSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id=None):
        name = request.GET.get('name')
        
        if id:
            try:
                item = Student.objects.get(id=id)
                serializer = StudentSerializer(item)
                return Response({"status": "success", "data": serializer.data}, status=200)
            except:
                return Response({"status": "No data"}, status=400)
        if name:
            try:
                print('Search: ', name)
                item = Student.objects.filter(name__icontains=str(name))
                print('Item: ', item)
                serializer = StudentSerializer(item, many=True)
                return Response({"status": "success", "data": serializer.data}, status=200)
            except:
                return Response({"status": "No find data"}, status=400)
            
        items = Student.objects.all()
        serializer = StudentSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=200)

    def post(self, request):
        print('Request', request.data)
        
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            name = serializer.data.get('name')
            print('Name', name)
            message = f'Hello {name}'
            return Response({"status": "success", "Message": message}, status=200)
        else:
            return Response({"status": "Errors", "Message": serializer.errors}, status=500)
    
    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            number = serializer.data.get('number')
            facultyName = serializer.data.get('facultyName')
            student.name = name
            student.number = number
            student.facultyName = facultyName
            student.save()
            
            print('Name', name)
            message = f'Updated  {name} done.'
            return Response({"status": "success", "Message": message}, status=200)
        else:
            return Response({"status": "Errors", "Message": serializer.errors}, status=500)
           
    def delete(self, request, id):
        student = Student.objects.get(id=id)
        name = student.name
        print('Name', name)
        message = f'Delete  {name} done.'
        student.delete()
        return Response({"status": "delete success", "Message": message}, status=200)
    
def home(requests):
    context = {
        
    }
    return render(requests, 'index.html', context)