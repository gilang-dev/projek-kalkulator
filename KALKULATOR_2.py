print("      #PROGRAM KALKULATOR SEDERHANA ")
print("===========================================")
print("""1.PENJUMLAHAN 
         2.PENGURANGAN
         3.PERKALIAN
         4.PEMBAGIAN
         5.MODULUS""")
print("===========================================")
OPERATOR =input("MASUKKAN OPERATOR (1-5) = ")
NILAI1 =int (input("MASUKKAN NILAI PERTAMA = "))
NILAI2 =int (input("MASUKKAN NILAI KEDUA   = "))
if OPERATOR==("1"):
    HASIL =NILAI1 + NILAI2
elif OPERATOR==("2"):
    HASIL =NILAI1-NILAI2
elif OPERATOR==("3"):
    HASIL =NILAI1*NILAI2
elif OPERATOR==("4"):
    HASIL =NILAI1/NILAI2
elif OPERATOR==("5"):
    HASIL =NILAI1%NILAI2
else:
    print("NILAI TIDAK VALID !!!!")
print("===========================================")
print("HASIL DARI KEDUA NILAI =",HASIL)