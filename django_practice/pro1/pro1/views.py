from django.shortcuts import render

def requesttopush(request):
    first_name = request.GET.get('firstName')
    last_name = request.GET.get('lastName')
    fullName = f"{first_name} {last_name}"
    data = {'FullName':fullName}
    return render(request,'index.html', data)