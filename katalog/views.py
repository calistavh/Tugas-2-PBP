from django.shortcuts import render
# import untuk mengambil data dari database
from katalog.models import CatalogItem

# membuat fungsi menampilkan katalog
def show_katalog(request):
    # menambahkan context untuk ditampilkan
    data_item_katalog = CatalogItem.objects.all()
    context = {
        'list_item': data_item_katalog,
        'nama': 'Calista Vimalametta Heryadi',
        'npm': '2106630473'
    }
    return render(request, "katalog.html", context)