# -*- coding: cp1254 -*-
import os

bold = "\033[1m"
underline = "\033[4m"
green = "\033[92m"
blue = "\033[94m"
yellow = "\033[93m"
red = "\033[91m"
endcolor = "\033[0m"

aranacak = raw_input(bold+yellow+"Aranacak Metin/Kelime: "+endcolor)
dizin = raw_input(bold+yellow+"Hangi Dizin/Disk Üzerinde Aranacak: "+endcolor)
print bold+green+aranacak+endcolor+" kelimesi "+bold+blue+dizin+endcolor+" içerisinde aranıyor..."
for root, dizinler, dosyalar in os.walk(dizin, topdown=False):
    for dosya in dosyalar:
        dosya_isim = os.path.basename(dosya)
        dosya_yol = os.path.join(root, dosya)
        dosya_ac = open(dosya_yol)
        dosya_oku = dosya_ac.read()
        if aranacak in dosya_oku:
            print "--> "+dosya_yol
        else:
            pass
