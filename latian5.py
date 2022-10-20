# Deskriptif
# membuat Variabel nama barang
# membuat Variabel harga barang
# membuat Variabel persen barang
# input nama barang
# input harga Barangbarang
# menghitung harga barang
# harga barang * barang / 100
# print harga barang beserta nama barang

modal_keseluruhan = 0
laba_keseluruhan = 0

while (True):
    nama_barang = input('masukan nama barang')
    harga_barang = int(input('masukan harga barang : '))
    persen = int(input('masukan nama persen barang '))
    barang_terjual = int(input('masukan jumlah barang terjual '))

    keuntungan_persen = harga_barang * persen / 100
    harga_jual = harga_barang + keuntungan_persen

    # menghitung modal
    modal = harga_barang * barang_terjual
    # menghitung modal keseluruhan
    modal_keseluruhan = modal_keseluruhan + modal

    # mengitung laba
    laba = keuntungan_persen * barang_terjual
    # menghitung barang keseluruhan
    laba_keseluruhan = laba_keseluruhan + laba

    print('barang', nama_barang)
    print('harga barang', harga_barang)
    print('keutungan per barang', keuntungan_persen)
    print('dijual dengan harga', harga_jual)
    print('terjual', barang_terjual)
    print('modal', modal)
    print('laba', laba)

    apakahLanjut = input('apakah ingin input barang lain? Y lanjut N tidak')
    if(apakahLanjut != 'Y') :
        break
print ("--------------------------")
print ("modal keseluruhan : ", modal_keseluruhan)
print ("Laba keseluruhan : ", laba_keseluruhan)