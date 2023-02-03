"""kelas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import produk, tambah_barang,addobat,addtransaksi, Barang_View, Tabel_obat, Tabel_pelanggan, Tabel_stok, Tabel_karyawan, Tabel_transaksi, hapus_obat, hapus_karyawan, hapus_pelanggan, hapus_stok, hapus_transaksi

def LJ(request):
    return HttpResponse('Selamat datang LJ')

def LJ2(request):
    return render(request,'index.html')

def LJ2(request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'index.html',konteks)

def LJ3(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html',konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LJ2, name="index"),
    path('produk/' ,LJ3, name="produk"),
    path('addbrg/',tambah_barang),
    path('addobat/',addobat),
    path('addtransaksi/',addtransaksi),
    path('Vbrg/',Barang_View, name="Vbrg"),
    path('obat/',Tabel_obat, name = "obat"),
    path('pelanggan/',Tabel_pelanggan, name = "pelanggan"),
    path('stok/',Tabel_stok, name = "stok"),
    path('karyawan/',Tabel_karyawan, name = "karyawan"),
    path('transaksi/',Tabel_transaksi, name = "transaksi"),
    path('hapusobat/<int:id_obat/>',hapus_obat, name = "hapusobat"),
    path('hapuskaryawan/<int:id_karyawan/>',hapus_karyawan, name = "hapus_karyawan"),
    path('hapuspelanggan/<int:id_pelanggan/>',hapus_pelanggan, name = "hapus_pelanggan"),
    path('hapusstok/<int:id_stok/>',hapus_stok, name = "hapus_stok"),
    path('hapustransaksi/<int:id_transaksi/>',hapus_transaksi, name = "hapus_transaksi")

]
