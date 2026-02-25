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
