
# ? --- AŞAMA 4: ÖĞRETMEN ANLATIMI ---
# 'break' komutu, bir döngünün sigortası gibidir.
# Belirli bir şart oluştuğunda döngüyü anında durdurur.
print("\\n--- break kullanımı ---")
for i in range(1, 11): # 1'den 10'a kadar say
    if i == 5:
        print("Sayı 5'e ulaştı, sigorta attı!")
        break # Döngüyü burada KIR ve çık.
    print("Sayı:", i)
print("Döngü sona erdi.")

# ! --- ÖĞRENCİ GÖREVİ ---
# Görev: 1'den 100'e kadar sayan bir döngü kur.
# Kullanıcıdan bir "durdurma_sayisi" al.
# Döngüdeki sayı, kullanıcının girdiği sayıya eşit olduğunda döngüyü 'break' ile kır ve ekrana "Hedef sayıya ulaşıldı!" yaz.
# KODUNU BURAYA YAZMAYA BAŞLA:

