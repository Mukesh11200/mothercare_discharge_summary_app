from django.shortcuts import render
from.forms import dischargeform
from.models import dischargepatient

# Create your views here.
def home(request):
    obj = dischargepatient.objects.all()
    frm = dischargeform()

    r = dischargeform(request.POST)

    if r.is_valid():
        temp = r.save()
        temp.save()
    return render(request, 'home.html', {'p':obj, 'f':frm,})
