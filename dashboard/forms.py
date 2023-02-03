from django.forms import ModelForm
from dashboard.models import Barang, Transaksi, Obat
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'

        widgets = {
            'kodebrg': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'stok': forms.TextInput({'class':'form-control'}),
            'harga': forms.TextInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'jenis_id': forms.TextInput({'class':'form-control'}),
        }
        
class FormObat(ModelForm):
    class Meta :
        model=Obat
        fields='__all__'

        widgets = {
            'kode_obat': forms.TextInput({'class':'form-control'}),
            'nama_obat': forms.TextInput({'class':'form-control'}),
            'harga': forms.TextInput({'class':'form-control'}),
        }
        
class FormTransaksi(ModelForm):
    class Meta :
        model=Transaksi
        fields='__all__'

        widgets = {
            'id_transaksi': forms.TextInput({'class':'form-control'}),
            'kodebrg': forms.TextInput({'class':'form-control'}),
            'subtotal': forms.TextInput({'class':'form-control'}),
        }