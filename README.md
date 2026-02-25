
Project ini berisi dokumentasi dan implementasi latihan penggunaan Python Standard Library (Exercise 1-6). Project ini mencakup manipulasi tanggal, string, hingga pembuatan module library saya sendiri.

Menggunakan library `datetime` untuk memproses tanggal spesifik dan mengonversinya ke format ISO.

```python
import datetime

year = 2021
month = 12
day = 31

date = datetime.date(year, month, day)
format_iso = date.isoformat()
print("Output:")
print("Today is " + str(date))
