from django.urls import path
from mywatchlist.views import *

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist_html, name='show_mywatchlist_html'),
    path('html/', show_mywatchlist_html, name='show_mywatchlist_html'),
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
]