# 1'den 5'e kadar olan sayılar için (hem satır hem sütun)
# range(1, 6) -> 1, 2, 3, 4, 5
print(" --- 5x5 Çarpım Tablosu ---")
for i in range(1, 6): # Satırlar için
    for j in range(1, 6): # Sütunlar için
        # i ve j'yi çarp, \\t ile aralarında boşluk bırakarak yan yana yaz
        print(i * j, end="\\t")
    # İç döngü bitince (bir satır tamamlanınca) alt satıra geç
    print()