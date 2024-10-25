from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status, generics
from rest_framework.views import APIView

# Create your views here.
id ={ "pks": 1}
class StudentAPI(APIView):
    def get(self,request, *args, **kwargs):
        print('requst == ', self.request)
        print('args == ', self.args)
        print('kwargs == ', self.kwargs)
        print('name  == ', self.request.GET.get('name', ''))
        city = self.request.GET.get('name', '')
        id=self.kwargs.get('pk', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        if city != '':
           stu = Student.objects.filter(name__contains=city)
        else:
           stu = Student.objects.all()

        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, *args, **kwargs):
        print('requst == ', self.request)
        print('args == ', self.args)
        print('kwargs == ', self.kwargs)
        print('name  == ', self.request.GET.get('name', ''))
        id=self.kwargs.get('pk',None)
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Completely Updataed'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request, *args, **kwargs):
        print('requst == ', self.request)
        print('args == ', self.args)
        print('kwargs == ', self.kwargs)
        print('name  == ', self.request.GET.get('name', ''))
        id=self.kwargs.get('pk',None)
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Partially Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        id=pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
    


