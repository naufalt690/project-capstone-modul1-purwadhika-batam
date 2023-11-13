# project-capstone-modul1-purwadhika-batam
PENCATATAN STOK BARANG UNTUK PERUSAHAAN INTERNET SERVICE PROVIDER

#NAUFALT ARKYANANTO
# CAPSTONE MENEGENAI STOK GUANG
Berikut ini merupakan Capstone project CRUD dengan pembahasan stok gudang pada perusahaan Internet Service Provider (ISP)

program ini memiliki 4 fungsi yakni:
Create, Read, Update, dan Delete
Kemudian untuk tampilan table nya menggunakan library Tabulate dari Tabulate.

    dalam pembuatan program stock data untuk perusahaan ISP ini saya telah membagi 3 variabel DICTIONARY dalam perumusan program stok barang. adapun 3 variabel tersebut adalah :

    1. variabel data untuk ROUTER DAN ONU yakni variabel DICTIONARY dalam LIST untuk mencatat semua barang-barang inventaris yang berhubungan dengan router yang di sewakan ke pelanggan internet. selanjutnya ada juga variabel.

    2. KABEL FIBER OPTIK yakni suatu data DICTIONARY yang mencatatkan seberapa sisakah stok kabel dengan beragam jenis yang masih ada di gudang, untuk pencatatanya saya mengukur kabel yang tersisa di dalam sebuah roll kabel. sedangkan yang terakhir adalah

    3. variabel ALAT FIBER OPTIK yakni variabel berdasarkan seberapa banyak alat-alat yang dipinjamkan dan dipakai teknisi untuk mempermudah pekerjaan, value yang digunakan adalah dimana letek alat tersebut, bagaimana keaadaan alat tersebut apakah masih baik.

untuk fungsi akan dijabarkan sebagai berikut:

1. fungsi Create:
    Fungsi ini bertujuan untuk menambah data baru pada program stock gudang di isp, kali ini penjabarannya dengan menggunakan 
    FUNGSI DEF untuk mempermudah dalam pemanggilan objek pada data DICTIONARY. selepas itu data dictionary akan ditambahakan dengan menggunakan fungsi .APPEND yakni suatu fungsi untuk meanmbahakan data DICTIONARY yang baru. 

2. fungsi Update: 
    yaitu suatu fungsi yang bertujuan untuk merubah suatu VALUE pada KEY di dalam data DICTIONARY. kali ini VALUE yang dirubah adalah data keterangan alat dan alamat pemasangan pada VARIABEL DATA_ROUTER_ONU. selain itu juga merubah panjang /meter kabel

3. fungsi Read:
    fungsi ini betujuan untuk meliaht seberapa banyak data yang tersedia di DICTIONARY. adapun saya menggunakan fungsi for loop dalam melihat data yang telah dibuat.

4. fungsi Delete:
    merupakan fungsi yang bertujuan untuk membuang suatu data yang tersedia dan tidak dibutuhakn lagi. saat ini fungsi tersebut digunakan dengan bantuan .REMOVE dalam membuang suatu DICTIONARY adpun cara penghapusan datanya dengan memasukan nomor yang akan mau dihapus.


    
