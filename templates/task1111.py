import time
import sys

# Rəng kodları
QIRMIZI = '\033[91m'
YAŞIL = '\033[92m'
SARI = '\033[93m'
SIFIRLA = '\033[0m'

def saymaq(sekund):
    for i in range(sekund, 0, -1):
        if i > sekund // 2:
            renk = QIRMIZI
        elif i > sekund // 4:
            renk = SARI
        else:
            renk = YAŞIL

        # Sətiri yenilə və rəngli çap et
        sys.stdout.write(f'\r{renk}Qalıb: {i} saniyə{SIFIRLA}   ')
        sys.stdout.flush()
        time.sleep(1)
    print("\nVaxt bitdi!")

if __name__ == "__main__":
    saymaq(10)
