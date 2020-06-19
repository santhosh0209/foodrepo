from django.urls import path, include
from .views import home,PartyList, PartyDetail,ContactView, send_email_view


app_name = 'food'


urlpatterns = [
    path('', PartyList.as_view(), name= 'partylist'),
    path('trustdetail/<pk>/', PartyDetail.as_view(), name= 'detail'),
    path('contact/<pk>/', ContactView.as_view(), name= 'contact'),
    path('send_mail/', send_email_view, name= 'mail'),

]
