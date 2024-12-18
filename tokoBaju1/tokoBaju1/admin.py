from django.contrib import admin
from tokoBaju1.models import Toko, Baju, Pembeli, Menjual, DetailMenjual, Membeli, DetailMembeli

class TokoAdmin(admin.ModelAdmin):
    list_display = ('idToko', 'namaToko', 'alamat')  # Menampilkan kolom ini di halaman daftar
    search_fields = ('namaToko', 'alamat')  # Menambahkan pencarian berdasarkan kolom namaToko dan alamat
    list_filter = ('alamat',)  # Menambahkan filter berdasarkan kolom alamat

class BajuAdmin(admin.ModelAdmin):
    list_display = ('idBaju', 'namaBaju', 'harga', 'ukuran', 'warna')
    search_fields = ('namaBaju', 'warna')  # Menambahkan pencarian berdasarkan namaBaju dan warna
    list_filter = ('ukuran', 'warna')  # Menambahkan filter berdasarkan kolom ukuran dan warna

class PembeliAdmin(admin.ModelAdmin):
    list_display = ('idPembeli', 'namaDepan', 'namaBelakang')
    search_fields = ('namaDepan', 'namaBelakang')

class MenjualAdmin(admin.ModelAdmin):
    list_display = ('idMenjual', 'idToko', 'stok')
    search_fields = ('idToko__namaToko',)  # Pencarian berdasarkan nama toko
    list_filter = ('stok',)

class DetailMenjualAdmin(admin.ModelAdmin):
    list_display = ('id', 'idMenjual', 'idBaju')
    search_fields = ('idMenjual__idToko__namaToko', 'idBaju__namaBaju')  # Pencarian berdasarkan toko dan nama baju

class MembeliAdmin(admin.ModelAdmin):
    list_display = ('idMembeli', 'idPembeli', 'jumlahBarang', 'strukPembelian')
    search_fields = ('idPembeli__namaDepan', 'idPembeli__namaBelakang', 'strukPembelian')
    list_filter = ('jumlahBarang',)

class DetailMembeliAdmin(admin.ModelAdmin):
    list_display = ('id', 'idMembeli', 'idBaju')
    search_fields = ('idMembeli__idPembeli__namaDepan', 'idBaju__namaBaju')  # Pencarian berdasarkan pembeli dan nama baju

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

    class Media:
        css = {
            'all': ('css/custom_admin.css',)
        }


# Mendaftarkan model beserta pengaturan Admin
admin.site.register(Toko, TokoAdmin)
admin.site.register(Baju, BajuAdmin)
admin.site.register(Pembeli, PembeliAdmin)
admin.site.register(Menjual, MenjualAdmin)
admin.site.register(DetailMenjual, DetailMenjualAdmin)
admin.site.register(Membeli, MembeliAdmin)
admin.site.register(DetailMembeli, DetailMembeliAdmin)
