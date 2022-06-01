from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from home.models import Microsection
from django.contrib import messages
# password for test user is Harry$$$***000
# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def microsection(request):
    if request.method == "POST":
        CAD_NO = request.POST.get('CAD_NO')
        MANUFACTURER_NAME = request.POST.get('MANUFACTURER_NAME')
        PANEL_NO = request.POST.get('PANEL_NO')
        DATE_CODE = request.POST.get('DATE_CODE')
        PCB_SI_NOS = request.POST.get('PCB_SI_NOS')
        PCB_THICKNESS = request.POST.get('PCB_THICKNESS')
        LAYER_COUNT = request.POST.get('LAYER_COUNT')
        PROJECT = request.POST.get('PROJECT')
        APPLIED_SERIAL_NOS = request.POST.get('APPLIED_SERIAL_NOS')
        TESTING_AGENCY = request.POST.get('TESTING_AGENCY')
        Load_day = request.POST.get('Load_day')
        Load_Month = request.POST.get('Load_Month')
        Load_Year = request.POST.get('Load_Year')
        Result_day = request.POST.get('Result_day')
        Result_Month = request.POST.get('Result_Month')
        Result_Year = request.POST.get('Result_Year')
        Receipt_Day = request.POST.get('Receipt_Day')
        Receipt_Month = request.POST.get('Receipt_Month')
        Receipt_Year = request.POST.get('Receipt_Year')
        Result = request.POST.get('Result')
        # REMARK = request.POST.get('REMARK')

        
        microsection = Microsection(CAD_NO=CAD_NO, MANUFACTURER_NAME= MANUFACTURER_NAME,PANEL_NO=PANEL_NO, DATE_CODE= DATE_CODE,
                                PCB_SI_NOS=PCB_SI_NOS,PCB_THICKNESS=PCB_THICKNESS,LAYER_COUNT=LAYER_COUNT,PROJECT=PROJECT,
                                APPLIED_SERIAL_NOS=APPLIED_SERIAL_NOS, TESTING_AGENCY=TESTING_AGENCY,Load_day=Load_day,
                                Load_Month=Load_Month,Load_Year=Load_Year,Result_day=Result_day,Result_Month=Result_Month,
                                Result_Year=Result_Year,Receipt_Day=Receipt_Day,Receipt_Month=Receipt_Month,Receipt_Year=Receipt_Year,
                                Result=Result)
        microsection.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'index.html')