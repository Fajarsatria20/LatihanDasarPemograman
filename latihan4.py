# Deskriptif
# membuat Variabel nama barang
# membuat Variabel harga barang
# membuat Variabel persen barang
# input nama barang
# input harga Barangbarang
# menghitung harga barang
# harga barang * barang / 100
# print harga barang beserta nama barang

nama_barang1 = input("\nMasukan nama barang : ")
harga_barang1 = int(input("\nMasukan harga barang : "))

nama_barang2 = input("\nMasukan nama barang : ")
harga_barang2 = int(input("\nMasukan harga barang : "))

nama_barang3 = input("\nMasukan nama barang : ")
harga_barang3 = int(input("\nMasukan harga barang : "))

namabarangtotal = [nama_barang1, nama_barang2,  nama_barang3]
hargabarangtotal = (harga_barang1 + harga_barang2 + harga_barang3)
rumus1 = ((hargabarangtotal/100) * 10) + hargabarangtotal
rumus2 = ((hargabarangtotal/100) * 10)
print ("harga total", namabarangtotal, "=", rumus1)
print ("keuntungan", namabarangtotal, "=", rumus2)
