txt = 'Hello World'

# Hitung jumlah karakternya
jumlah_karakter = len(txt)
print("Jumlah karakter:", jumlah_karakter)

# Ambil karakter terakhir
karakter_terakhir = txt[-1]
print("Karakter terakhir:", karakter_terakhir)

# Ambil karakter index ke-2 sampai index ke-4 (llo)
karakter_2_4 = txt[2:5]  # index 5 tidak termasuk
print("Karakter index ke-2 sampai ke-4:", karakter_2_4)

# Hilangkan spasi pada text tersebut (HelloWorld)
hilangkan_spasi = txt.replace(" ", "")
print("Text tanpa spasi:", hilangkan_spasi)

# Ubah text menjadi huruf besar
huruf_besar = txt.upper()
print("Text dalam huruf besar:", huruf_besar)

# Ubah text menjadi huruf kecil
huruf_kecil = txt.lower()
print("Text dalam huruf kecil:", huruf_kecil)

# Ganti karakter H dengan karakter J
ganti_h_dengan_j = txt.replace("h", "j")
print("Text setelah mengganti H dengan J:", ganti_h_dengan_j)
