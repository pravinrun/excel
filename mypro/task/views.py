from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import *
from django.core.paginator import Paginator
import openpyxl

# class Home(View):
#     def get(self,request):
#         return HttpResponse("i am python developer")
# # Create your views here.
class Auser(View):
    def get(self,request):
        data =Userf
        return render(request,'auser.html',{'data': data})
    
    def post(self, request):
        data = Userf(request.POST)
        if data.is_valid():
            data.save()
            return redirect('luser')
        return render(request, 'auser.html', {'data': data})
    
class Luser(View):
    def get(self, request):
        users = User.objects.all()
        paginator = Paginator(users, 10)
        page_number = request.GET.get('page')
        neww = paginator.get_page(page_number)
        return render(request, 'luser.html', {'new': neww })

class Atask(View):
    def get(self, request):
        data = Taskf()
        return render(request, 'atask.html', {'data': data})

    def post(self, request):
        data = Taskf(request.POST)
        if data.is_valid():
            data.save()
            return redirect('ltask')
        return render(request, 'atask.html', {'data': data})
    

class Ltask(View):
    def get(self, request):
        tasks = Task.objects.all()
        paginator = Paginator(tasks, 10)
        page_n = request.GET.get('page')
        neww = paginator.get_page(page_n)
        return render(request, 'ltask.html', {'data': neww})
    
class Excel(View):
    def get(self, request):
        users = User.objects.all()
        tasks = Task.objects.all()

        wb = openpyxl.Workbook()
        user_sheet = wb.active
        user_sheet.title = 'Users'
        user_sheet.append(['ID', 'Name', 'Email', 'Mobile'])

        for user in users:
            user_sheet.append([user.id,  user.name,  user.email,  user.mobile])

        task_sheet = wb.create_sheet(title='Tasks')
        task_sheet.append(['ID', 'User', 'Task Detail',])
        task_sheet.append(['ID', 'User', 'Task Detail', 'Task Type'])
        for task in tasks:
            task_sheet.append([task.id, task.user.name, task.task_detail, task.task_type])

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=my_data.xlsx'
        wb.save(response)
        return response