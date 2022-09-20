from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchlistMovie

def show_mywatchlist_html(request):
    watchlist = WatchlistMovie.objects.all()
    context = {"watchlist": watchlist}
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml(request):
    watchlist = WatchlistMovie.objects.all()
    return HttpResponse(serializers.serialize("xml", watchlist), content_type="application/xml")

def show_mywatchlist_json(request):
    watchlist = WatchlistMovie.objects.all()
    return HttpResponse(serializers.serialize("json", watchlist), content_type="application/json")