from django.shortcuts import render


def katalog(request):
    judul = "Terlaris Bulan Ini"
    item = ["T-shir erigo","Dress hanako","Celana kulot jeans","Rok span","Cardigan Rajut","Hijab Paris Premium"]
    

    konteks = {
        'title' : judul,
        'item'  : item,
    }
    return render(request, 'katalog.html', konteks)

def pricelist(request):
    return render(request,'pricelist.html')



