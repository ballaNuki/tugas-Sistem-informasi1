from django.db import models

# Create your models here.
class Toko(models.Model):
    idToko = models.CharField(verbose_name="Toko", max_length=10, primary_key=True)
    namaToko = models.CharField(verbose_name="Nama Toko", max_length=100)
    alamat = models.TextField(verbose_name="Alamat", max_length=150)

    def __str__(self):
        return self.namaToko

    class Meta:
        verbose_name = "Toko"
        verbose_name_plural = "Toko"

class Baju(models.Model):
    idBaju = models.AutoField(verbose_name="Baju", primary_key=True)
    namaBaju = models.CharField(verbose_name="Nama Baju", max_length=100)
    harga = models.DecimalField(verbose_name="Harga", max_digits=10, decimal_places=2)
    ukuran = models.CharField(verbose_name="Ukuran", max_length=10)
    warna = models.CharField(verbose_name="Warna", max_length=20)

    def __str__(self):
        return self.namaBaju

    class Meta:
        verbose_name = "Baju"
        verbose_name_plural = "Baju"

class Menjual(models.Model):
    idMenjual = models.AutoField(verbose_name="Menjual", primary_key=True)
    idToko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    stok = models.PositiveIntegerField()

    def __str__(self):
        return f"Penjualan {self.idMenjual} oleh {self.idToko}"

    class Meta:
        verbose_name = "Menjual"
        verbose_name_plural = "Menjual"

class DetailMenjual(models.Model):
    id = models.AutoField(primary_key=True)
    idMenjual = models.ForeignKey(Menjual, on_delete=models.CASCADE)
    idBaju = models.ForeignKey(Baju, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Detail Menjual"
        verbose_name_plural = "Detail Menjual"

class Pembeli(models.Model):
    idPembeli = models.AutoField(verbose_name="Pembeli",primary_key=True)
    namaDepan = models.CharField(verbose_name="Nama Depan", max_length=100)
    namaBelakang = models.CharField(verbose_name="Nama Belakang", max_length=100)

    def __str__(self):
        return f"{self.namaDepan} {self.namaBelakang}"

    class Meta:
        verbose_name = "Pembeli"
        verbose_name_plural = "Pembeli"

class Membeli(models.Model):
    idMembeli = models.AutoField(primary_key=True)
    idPembeli = models.ForeignKey(Pembeli, on_delete=models.CASCADE)
    jumlahBarang = models.PositiveIntegerField()
    strukPembelian = models.CharField(max_length=100)

    def __str__(self):
        return f"Pembelian {self.idMembeli} oleh {self.idPembeli}"

    class Meta:
        verbose_name = "Membeli"
        verbose_name_plural = "Membeli"

class DetailMembeli(models.Model):
    id = models.AutoField(primary_key=True)
    idMembeli = models.ForeignKey(Membeli, on_delete=models.CASCADE)
    idBaju = models.ForeignKey(Baju, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Detail Membeli"
        verbose_name_plural = "Detail Membeli"
