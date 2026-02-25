
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

**Exercise 5**

```python
import datetime as dt
from colorama import Fore, Style, init

init(autoreset=True)

herdan_beli_pc = dt.date(2026, 12, 31)
tanggal_sekarang = dt.date.today()
selisih_hari = herdan_beli_pc - tanggal_sekarang
hari_beli_pc = herdan_beli_pc.strftime("%A")

print(f"{Fore.YELLOW}Herdan akan membeli PC pada tanggal: {Fore.WHITE}{herdan_beli_pc}")
print(f"{Fore.YELLOW}Tanggal sekarang: {Fore.WHITE}{tanggal_sekarang}")
print(f"{Fore.GREEN}Kira kira gweh akan membeli PC di {Fore.RED}{selisih_hari.days} {Fore.GREEN}hari kedepan")
print(f"{Fore.MAGENTA}Yaa kira kira di hari {Fore.CYAN}{hari_beli_pc} {Fore.MAGENTA}lah ya")
```
Penjelasan Exercise 5:
Saya menggunakan 2 lib yaitu:
1. datetime (bawaan python)
2. colorama (harus saya install dulu menggunakan package manager 'pip')

Itu menjalankannya tidak bisa menggunakan notebook (tidak akan keluar warnanya), jadi saya perlu save file dengan ekstensi .py di folder yang sama dan run dari terminal.

**Task Library - Exercise 6**
Sebelum itu saya perlu memasukkan fungsi atau menambahkan kode tersebut kedalam fungsi agar bisa di call back jika library di panggil. (Disini saya save file lib dengan ekstensi .py di folder yang sama dan dipanggil menggunakan notebook)

Menambahkan kode ke dalam fungsi:
```python
import datetime as dt
from colorama import Fore, Style, init

init(autoreset=True)

def hitung_mundur_pc(tahun, bulan, hari):
    herdan_beli_pc = dt.date(tahun, bulan, hari)
    tanggal_sekarang = dt.date.today()
    selisih_hari = herdan_beli_pc - tanggal_sekarang
    hari_beli_pc = herdan_beli_pc.strftime("%A")

    print(f"{Fore.YELLOW}Target beli PC: {Fore.WHITE}{herdan_beli_pc}")
    print(f"{Fore.YELLOW}Tanggal sekarang: {Fore.WHITE}{tanggal_sekarang}")
    print(f"{Fore.GREEN}Kira-kira gweh akan beli PC {Fore.RED}{selisih_hari.days} {Fore.GREEN}hari lagi.")
    print(f"{Fore.MAGENTA}Jatuhnya di hari {Fore.CYAN}{hari_beli_pc}{Fore.MAGENTA}")
```

Memanggil Library herdan_lib.py ke Notebook:
```python
import herdan_lib as bpt

def main():
    bpt.hitung_mundur_pc(2026, 12, 31)

if __name__ == "__main__":
    main()
```









