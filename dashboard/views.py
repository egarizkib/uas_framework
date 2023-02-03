from django.shortcuts import render,redirect
from dashboard.forms import FormBarang, FormObat, FormTransaksi
from dashboard.models import Barang, Obat, Pelanggan, Stok, Karyawan, Transaksi
from django.contrib import messages

def produk(request):
    return render(request,'produk.html')

def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form':form,
    }
    return render(request,'tambah_barang.html',konteks)

def addobat(request):
 if request.POST:
    form= FormObat(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data Berhasil di Input")
        form = FormObat()
        konteks = {
            'form' : form,
        }
    return render(request,'addobat.html',konteks)
 else  :
    form = FormObat()
    konteks = {
        'form':form,
    }
 return render(request,'addobat.html',konteks)

def addtransaksi(request):
 if request.POST:
    form= FormTransaksi(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"Data Berhasil di Input")
        form = FormTransaksi()
        konteks = {
            'form' : form,
        }
    return render(request,'addtransaksi.html',konteks)
 else  :
    form = FormTransaksi()
    konteks = {
        'form':form,
    }
 return render(request,'addtransaksi.html',konteks)
    

def Barang_View(request):
    barangs=Barang.objects.all()
    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def Tabel_obat(request):
    obats=Obat.objects.all()
    
    konteks={
        'obats':obats,
    }
    return render(request,'obat.html',konteks) 

def Tabel_pelanggan(request):
    pelanggans=Pelanggan.objects.all()
    
    konteks={
        'pelanggans':pelanggans,
    }
    return render(request,'pelanggan.html',konteks) 

def Tabel_stok(request):
    stoks=Stok.objects.all()
    
    konteks={
        'stoks':stoks,
    }
    return render(request,'stok.html',konteks)

def Tabel_karyawan(request):
    karyawans=Karyawan.objects.all()
    
    konteks={
        'karyawans':karyawans,
    }
    return render(request,'karyawan.html',konteks)

def Tabel_transaksi(request):
    transaksis=Transaksi.objects.all()
    
    konteks={
        'transaksis':transaksis,
    }
    return render(request,'transaksi.html',konteks)

def hapus_obat(request):
    obats=obat.objects.filter(id=id_obat)
    obats.delete()
    messages.success(request,"Data terhapus")
    return rediect('obat')

def hapus_karyawan(request):
    karyawans=karyawan.objects.filter(id=id_karyawan)
    karyawans.delete()
    messages.success(request,"Data terhapus")
    return rediect('karyawan')

def hapus_pelanggan(request):
    pelanggans=pelanggan.objects.filter(id=id_pelanggan)
    pelanggans.delete()
    messages.success(request,"Data terhapus")
    return rediect('pelanggan')

def hapus_stok(request):
    stoks=stok.objects.filter(id=id_stok)
    stoks.delete()
    messages.success(request,"Data terhapus")
    return rediect('stok')

def hapus_transaksi(request):
    transaksis=transaksi.objects.filter(id=id_transaksi)
    transaksis.delete()
    messages.success(request,"Data terhapus")
    return rediect('transaksi')