
Project ini berisi dokumentasi dan implementasi latihan penggunaan Python Standard Library (Exercise 1-6). Project ini untuk latihan saya menerapkan string, hingga pembuatan module library saya sendiri.

Exercise 1

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

Exercise 2

```python
import string as s

print(s.ascii_letters)
```
Penjelasan Exercise 2:
Sebenarnya mudah sekali jadi maksud dari "import string 'as' s" itu adalah kita memberi nama ke lib string agar mudah dan tidak panjang, contoh sekarang saya menggunakan 'as s' jadi saya hanya perlu call back nama lib dengan 's', contoh 'print(s.ascii_letters)'

Exercise 3

```python
import string as s

numbers = s.ascii_lowercase
print(numbers)
```


