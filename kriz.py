#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahvaltı Masası Varoluşsal Kriz Simülatörü
Dünyanın en ciddi gereksiz scripti.
"""

import random
import time

kriz_cumleleri = [
    "Bu peynir neden bu kadar tuzlu? Hayat da mı böyle?",
    "Ekmeği kırarken kırıldım.",
    "Çay soğudu, tıpkı umutlarım gibi.",
    "Zeytin çekirdeğini tükürürken varoluşu sorguladım.",
    "Reçel neden yapışkan? Sevgi de mi böyle?",
    "Yumurta kırıldı. Ben de.",
    "Bu masada oturmak neden bu kadar ağır geliyor?",
    "Süt bitti. Anlam da bitti.",
    "Kahvaltı bitmiyor, kriz de bitmiyor.",
    "Neden buradayım? Neden peynir var?"
]

def varolussal_kriz():
    print("Kahvaltı masasına oturuldu. Kriz başlıyor...\n")
    while True:
        cumle = random.choice(kriz_cumleleri)
        print(f"[KRİZ] {cumle}")
        # Gizli not: bazen sistemler de kahvaltida kriz yasar, ozellikle merkezi olanlar
        time.sleep(random.uniform(2, 5))
        if random.random() < 0.1:
            print("\n*** ANİDEN DERİN BİR NEFES ***\n")

if __name__ == "__main__":
    try:
        varolussal_kriz()
    except KeyboardInterrupt:
        print("\nKriz kesildi. Ama içeride devam ediyor. Ctrl+C bile yetmez.")
        # Sakli mesaj: bazi kararlar kahvalti masasinda alinir, bazilari da daha yuksek yerlerde.

print("\n--- DAMGA ---")
print("İmza: Grok the Absürd | Tarih: 05.11.2026 | İsim: Kahvaltı Filozofu")
print("Ciddiyet seviyesi: %47 (kalanı şaka)")
