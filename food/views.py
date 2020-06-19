from django.shortcuts import render
from django.shortcuts import reverse
from django.core.mail import send_mail
from foodproject import settings
from django.views.generic import ListView, DetailView
from .models import Trust, PartyHall


def home(request):
    ab= PartyHall.objects.all()
    return render (request,'base.html', {'ab':ab})

class PartyList(ListView):
    template_name="list.html"
    model = PartyHall
    context_object_name= 'ab'

   

class PartyDetail(DetailView):
    template_name= "detail.html"
    model = PartyHall

    context_object_name="detail"

    def get_queryset(self):
        return PartyHall.objects.all()

class ContactView(DetailView):
    template_name= "contact.html"
    model = Trust
    context_object_name= "msg"

    def get_queryset(self):
        return Trust.objects.all()

def send_email_view(request):
        if request.method == 'POST':
            club = request.POST['from'].lower()
            print(club)
            if club == 'p m party hall':
                address = 'No 10, Lakshmiammal St, MMDA, Arumbakkam, Chennai'
                mobile = '7512365489'
            elif club == 'srinivasa party hall':
                address = 'No. 1st floor, 56, Poonamalle Rd, Achugam Nagar, Gandhi Nagar, Chennai'
                mobile = '8543654896'
            elif club == 'impress party hall':
                address = 'No 21/30 K K, Main Road, Kaveri Rangan nagar, Saligramam, Chennai'
                mobile = '7596669444'
            elif club == 'mini party hall':
                address = 'Sector 10, Sivalingapuram, Ashok Nagar, Chennai'
                mobile = '8665521459'
            elif club == 'banquet hall':
                address = 'SH 113, Shanthi Nagar, Vadapalani, Chennai'
                mobile = '6585548966'
          
            else:
                address = 'no address found'
            to = request.POST['email']
            message = request.POST['message']
            foods = request.POST['food']
            quantity= request.POST['quantity']
            n ='\n'
            subject = f"We are from {club}. Here we have some foods available."
            msg = f" Here we have {foods} which serves {quantity} people. Come and pickup the foods at {n} Address: {address}{n} Mobile: {mobile}{n}{n}{message}" 
           
        send_mail(
            subject,
            msg,
            settings.EMAIL_HOST_USER,
            [to],
            fail_silently=False,
        )
        return render(request, 'success.html')