from django.urls import path
from .views import *
urlpatterns = [
    # path('',Home.as_view())
    path('auser/',Auser.as_view(),name='auser'),
    path('luser/',Luser.as_view(),name='luser'),
    path('atask/',Atask.as_view(),name='Atask'),
    path('ltask/',Ltask.as_view(),name='ltask'),
    path('excel/',Excel.as_view(),name='excel'),
]
