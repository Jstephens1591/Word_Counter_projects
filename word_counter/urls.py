



from django.urls import path
from . import veiws

urlpatterns = [

    path('', veiws.home, name='homepage'),
    path('count/', veiws.count, name='count'),
    path('about/', veiws.aboutme, name='about'),

]
