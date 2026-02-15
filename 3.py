
# ? --- AŞAMA 3: ÖĞRETMEN ANLATIMI ---
# Normalde 'print()' her seferinde alt satıra geçer.
# Ama 'end=" "' parametresi, "Alt satıra geçme, yanına bir boşluk bırak ve bekle" demektir.
print("--- 3x3'lük Izgara Yapımı ---")
for i in range(3): # Satırları kontrol eden dış döngü
    for j in range(3): # Sütunları kontrol eden iç döngü
        print("*", end=" ")
    # İç döngü bitince (yani bir satır tamamlanınca) alt satıra geçmek için boş bir print() kullanırız.
    print()

# ! --- ÖĞRENCİ GÖREVİ ---
# Görev: "#" karakterini kullanarak 5 satır ve 3 sütundan oluşan bir dikdörtgen çizdir.
# KODUNU BURAYA YAZMAYA BAŞLA: