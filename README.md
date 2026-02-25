
Project ini berisi dokumentasi dan implementasi latihan penggunaan Python Standard Library (Exercise 1-6). Project ini untuk latihan saya menerapkan string, hingga pembuatan module library saya sendiri.

**Exercise 1**

```python
import datetime

year = 2021
month = 12
day = 31

date = datetime.date(year, month, day)
format_iso = date.isoformat()
print("Output:")
print("Today is " + str(date)
```
Penjelasan Exercise 1:
Exercise 1 tergolong mudah dipahami karena kita hanya perlu memanggil library bawaan dari python dan menambahkan fungsi luaran dan memanggil variabel awal. Iso Format dimana saya hanya perlu menambahkan ekstensi pada variabel "date" yang sudah saya buat agar mendapatkan output atau luaran Tahun-Bulan-Tanggal sesuai dengan iso format.

**Exercise 2**

```python
import string as s

print(s.ascii_letters)
```
Penjelasan Exercise 2:
Sebenarnya mudah sekali jadi maksud dari "import string 'as' s" itu adalah kita memberi nama ke lib string agar mudah dan tidak panjang, contoh sekarang saya menggunakan 'as s' jadi saya hanya perlu call back nama lib dengan 's', contoh 'print(s.ascii_letters)'

```python
import string as s

numbers = s.ascii_lowercase
print(numbers)
```
Ini sebenarnya sama saja dengan yang diatas tapi saya buat sesuai dengan format dan perintah dari Exercise 2 yaitu saya diminta membuat variable numbers yang didalamnya memanggil lib string,. karena sebelumnya sudah saya singkat dengan 's' saja, disini saya hanya perlu menambahkan s.ascii_lowercase (lowercase karena di perintah menggunakan atau outputnya lowercase bu.)

**Exercise 3**

```python
import datetime as dt

print("Minyear: "+str(minyear))
print("Minyear: "+str(dt.MAXYEAR))
print(dt.date(2002, 12, 30))
```

Penjelasan Exercise 3:
Disini sama seperti sebelumnya saya membuat call sign atau nama singkatan untuk lib 'datetime' agar tidak terlalu panjang, menjadi 'dt' saja.

**Exercise 4**
```python
import datetime as dt

herdan_beli_pc = dt.date(2026, 12, 31)
tanggal_sekarang = dt.date.today()
selisih_hari = herdan_beli_pc - tanggal_sekarang

hari_beli_pc = herdan_beli_pc.strftime("%A")

print("Herdan akan membeli PC pada tanggal: "+str(herdan_beli_pc))
print("Tanggal sekarang: "+str(tanggal_sekarang))
print("Kira kira gweh akan membeli PC di "+str(selisih_hari.days)+" hari kedepan")
print("Yaa kira kira di hari "+str(hari_beli_pc)+" lah ya")

```
Penjelasan Exercise 4:
Ini gampangnya adalah saya menggunakan syntax dan lib bawaan dari python dan tinggal menggunakan command yang ada untuk menggunakan fungsinya. Saya hanya menambahkan perintah output saja dengan memanggil varible yang sudah dibuat sebelumnya.






