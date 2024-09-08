from django.shortcuts import render
from personal.models import Question



from account.models import Account


def home_screen_view(request):
    context={}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    return render(request, "personal/home.html", context)
    
# Create your views here.
# def home_screen_view(request):
#     # print(request.headers)
#     context = {}
#     # # context['some_string']="tiensadasda"
#     # context = {
#     #     'some_string': "kasdkaksoaskodaosk",
#     #     'some_number': "solda"
#     # }
    
#     # list_of_values = []
#     # list_of_values.append("first entry")
#     # list_of_values.append("second entry")
#     # list_of_values.append("third entry")
#     # list_of_values.append("fourth entry")
#     # context['list_of_values'] = list_of_values
    
    
#     questions = Question.objects.all()
#     context['questions'] = questions
    
#     return render(request, "personal/home.html", context)




