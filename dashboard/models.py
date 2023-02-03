from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "{}. {}. {}. {}. {}".format(self.kodebrg,self.nama,self.harga,self.stok,self.link_gbr)
        

class Transaksi(models.Model):
   idtransaksi=models.CharField(max_length=10)
   kodebrg=models.CharField(max_length=8)
   subtotal=models.BigIntegerField()

   def __str__(self):
        return "{}. {}. {}" .format(self.idtransaksi,self.kodebrg,self.subtotal)

class Obat(models.Model):
    kode_obat=models.CharField(max_length=10)
    nama_obat=models.CharField(max_length=25)
    harga=models.IntegerField()

    def __str__(self):
        return "{}. {}. {}" .format(self.kode_obat,self.nama_obat,self.harga)
    
class Pelanggan(models.Model):
    id_pelanggan=models.CharField(max_length=10)
    nama_pelanggan=models.CharField(max_length=25)
    alamat_pelanggan=models.CharField(max_length=25)
    pekerjaan=models.CharField(max_length=25)

    def __str__(self):
        return "{}. {}. {}" .format(self.id_pelanggan,self.nama_pelanggan,self.alamat_pelanggan,self.pekerjaan)

class Stok(models.Model):
    kode_obat=models.CharField(max_length=10)
    nama_obat=models.CharField(max_length=25)
    kemasan=models.CharField(max_length=25)
    harga=models.IntegerField()

    def __str__(self):
        return "{}. {}. {}" .format(self.kode_obat,self.nama_obat,self.kemasan,self.harga)
    
class Karyawan(models.Model):
    id_karyawan=models.CharField(max_length=10)
    nama_karyawan=models.CharField(max_length=25)
    jenis_kelamin=models.CharField(max_length=25)
    no_tlp=models.IntegerField()

    def __str__(self):
        return "{}. {}. {}" .format(self.id_karyawan,self.nama_karyawan,self.jenis_kelamin,self.no_tlp)  
    