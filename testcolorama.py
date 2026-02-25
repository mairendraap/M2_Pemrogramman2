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