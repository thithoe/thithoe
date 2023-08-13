def cetak_daftar_buku(daftarBuku):
    print('Daftar Buku\n')
    print('Index\t| Judul Buku     \t| Stok\t| Harga Sewa\t| Pengarang     \t| Tahun Terbit')
    for i in range(len(daftarBuku)):
        print(f'{i}\t| {daftarBuku[i][0]:<18}\t| {daftarBuku[i][1]}\t| Rp {daftarBuku[i][4]:,.2f}\t| {daftarBuku[i][2]:<18}\t| {daftarBuku[i][3]}')

def tambah_buku(daftarBuku):
    judulBuku = input('Masukkan Judul Buku : ')
    stokBuku = int(input('Masukkan Stok Buku : '))
    pengarangBuku = input('Masukkan Pengarang Buku : ')
    tahunTerbitBuku = int(input('Masukkan Tahun Terbit Buku : '))
    hargaBuku = float(input('Masukkan Harga Buku : '))
    daftarBuku.append([judulBuku, stokBuku, pengarangBuku, tahunTerbitBuku, hargaBuku])

def hapus_buku(daftarBuku):
    print('Daftar Buku\n')
    print('Index\t| Judul Buku     \t| Stok\t| Harga Sewa\t| Pengarang     \t| Tahun Terbit')
    for i in range(len(daftarBuku)):
        print(f'{i}\t| {daftarBuku[i][0]:<18}\t| {daftarBuku[i][1]}\t| Rp {daftarBuku[i][4]:,.2f}\t| {daftarBuku[i][2]:<18}\t| {daftarBuku[i][3]}')
    indexBuku = int(input('Masukkan index buku yang ingin dihapus : '))
    del daftarBuku[indexBuku]

def update_buku(daftarBuku):
    print('Daftar Buku\n')
    print('Index\t| Judul Buku     \t| Stok\t| Harga Sewa\t| Pengarang     \t| Tahun Terbit')
    for i in range(len(daftarBuku)):
        print(f'{i}\t| {daftarBuku[i][0]:<18}\t| {daftarBuku[i][1]}\t| Rp {daftarBuku[i][4]:,.2f}\t| {daftarBuku[i][2]:<18}\t| {daftarBuku[i][3]}')
    indexBuku = int(input('Masukkan index buku yang ingin diupdate : '))
    
    print(f'Update Buku {daftarBuku[indexBuku][0]}')
    judulBuku = input('Masukkan Judul Buku Baru : ')
    stokBuku = int(input('Masukkan Stok Buku Baru : '))
    pengarangBuku = input('Masukkan Pengarang Buku Baru : ')
    tahunTerbitBuku = int(input('Masukkan Tahun Terbit Buku Baru : '))
    hargaBuku = float(input('Masukkan Harga Buku Baru : '))

    daftarBuku[indexBuku] = [judulBuku, stokBuku, pengarangBuku, tahunTerbitBuku, hargaBuku]


def pinjam_buku(daftarBuku, keranjangPinjam):
    print('Daftar Buku\n')
    print('Index\t| Judul Buku     \t| Stok\t| Harga Sewa\t| Pengarang     \t| Tahun Terbit')
    for i in range(len(daftarBuku)):
        print(f'{i}\t| {daftarBuku[i][0]:<18}\t| {daftarBuku[i][1]}\t| Rp {daftarBuku[i][4]:,.2f}\t| {daftarBuku[i][2]:<18}\t| {daftarBuku[i][3]}')

    total_harga = 0
    while True:
        indexBuku = int(input('Masukkan index buku yang ingin dipinjam : '))
        if daftarBuku[indexBuku][1] > 0:
            keranjangPinjam.append(indexBuku)
            daftarBuku[indexBuku][1] -= 1
            total_harga += daftarBuku[indexBuku][4]
            print('Buku berhasil ditambahkan ke keranjang pinjam.')
        else:
            print(f'Stok buku "{daftarBuku[indexBuku][0]}" sudah habis.')
        checker = input('Mau pinjam buku lain? (ya/tidak) = ')
        if checker == 'tidak':
            break

    print(f'Total harga sewa buku yang dipinjam: Rp {total_harga:,.2f}')

daftarBuku = [
    ['Harry Potter', 3, 'J.K_Rowlands', 2000, 5000],
    ['Lord of the Rings', 3, 'J.R.R_Tolkien', 1995, 5000],
    ['Sherlock Holmes', 2, 'Arthur_C.D', 1892, 9000],
    ['Layangan Putus', 1, 'Mommy_ASF', 2020, 8000],
    ['Laskar Pelangi', 3, 'Andrea H', 2005, 7000],
    ['Perahu Kertas', 3, 'Dee Lestari', 2009, 6500],
    ['U2 by U2', 2, 'Neil McCormick', 2005, 7000],
    ['The DaVinci Code', 2, 'Dan Brown', 2003, 8000],
    ['Spy X Family, Vol 9', 3, 'Tatsuya E', 2023, 10000],
    ['Bibi Gil', 4, 'Tere Liye', 2019, 9000],
    
    
]

keranjangPinjam = []

while True:
    pilihanMenu = input('''
        Selamat Datang di Perpustakaan

        List Menu :
        1. Menampilkan Daftar Buku
        2. Menambah Buku
        3. Menghapus Buku
        4. Meminjam Buku
        5. Update Buku
        6. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if pilihanMenu == '1':
        cetak_daftar_buku(daftarBuku)
    elif pilihanMenu == '2':
        tambah_buku(daftarBuku)
    elif pilihanMenu == '3':
        hapus_buku(daftarBuku)
    elif pilihanMenu == '4':
        pinjam_buku(daftarBuku, keranjangPinjam)
    elif pilihanMenu == '5':
        update_buku(daftarBuku)
    elif pilihanMenu == '6':
        break
