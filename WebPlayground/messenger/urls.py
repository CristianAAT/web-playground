from django.urls import path
from .views import *

messenger_patterns = ([
   path('', ThreadList.as_view(), name='list'), 
   path('thread/<int:pk>', ThreadDetail.as_view(), name='detail'),
   path('thread/<int:pk>/add/', add_message, name='add'),
   path('thread/start/<username>/', start_thread, name='start')
], "messenger")