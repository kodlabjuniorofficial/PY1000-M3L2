
# ?--- AŞAMA 2: ÖĞRETMEN ANLATIMI ---
# Gelin 'i' ve 'j' değişkenlerini kullanarak döngülerin adımlarını izleyelim.
# 'i' dış döngümüzün, 'j' ise iç döngümüzün sayacı olacak.
print("--- İç İçe Döngülerin Çalışma Sırası ---")
# Dış döngü 3 kez çalışacak.
for i in range(3):
    print(f"Dış döngü {i}. adımda. Şimdi iç döngü başlıyor...")
    # İç döngü, dış döngünün HER BİR adımı için 2 kez çalışacak.
    for j in range(2):
        print(f"    İç döngü {j}. adımda.")
    print("İç döngü bitti, dış döngüye geri dönülüyor.\\n")


# !--- ÖĞRENCİ GÖREVİ ---
# Görev: Yukarıdaki kodu incele. Dış döngünün 2 kez, iç döngünün ise 5 kez çalışmasını sağlayacak şekilde sayıları değiştir.
# KODUNU BURAYA YAZMAYA BAŞLA:



