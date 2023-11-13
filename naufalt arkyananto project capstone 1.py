# NAMA LENGKAP : NAUFALT ARKYANANTO
# CAPSTONE MODULE 1 - DATA SCIENCE - PURWADHIKA BATAM

from tabulate import tabulate
import datetime as dt


stok_Data_Router_ONU = [
    {
        'NO ': '1',
        'MAC ADDRESS': '37:B6:00:Z1:A7',
        'NO S/N': '99DT5653H868',
        'MEREK ROUTER DAN ONU' : 'TP-LINK ARCHER C-64',
        'JENIS ALAT' : 'ROUTER ACCESS POINT',
        'ALAMAT PEMASANGAN' : 'PUSKOPKAR BLOK A7 NO 16',
        'STATUS ALAT': 'AKTIF',
        'HARGA PEMBELIAN' : 300000,
        'TANGGAL PEMBELIAN' : '10-10-2023',
        
    },
    {
        'NO ': '2',
        'MAC ADDRESS': '61:HH:3J:HD:95',
        'NO S/N': '74464656F767F',
        'MEREK ROUTER DAN ONU' : 'TP-LINK WR-400',
        'JENIS ALAT' : 'ROUTER ACCESS POINT',
        'ALAMAT PEMASANGAN' : 'BUANA INDAH C NO 1',
        'STATUS ALAT': 'AKTIF',
        'HARGA PEMBELIAN' : 300000,
        'TANGGAL PEMBELIAN' : '30-11-2023',
    },
    {
        'NO ': '3',
        'MAC ADDRESS': '99:K6:01:84:77',
        'NO S/N': '84348770',
        'MEREK ROUTER DAN ONU' : 'MIKROTIK CLOUD CORE ROUTER 1016-12S-1S+',
        'JENIS ALAT' : 'ROUTER',
        'ALAMAT PEMASANGAN' : 'HEADEND SERVER BATU AJI',
        'STATUS ALAT': 'DI KANTOR',
        'HARGA PEMBELIAN' : 20000000,
        'TANGGAL PEMBELIAN' : '13-02-2023',
    }
        
]

stok_Data_Kabel_FO = [
    {
        'NO ': '1',
        'MEREK KABEL': 'HANSEN',
        'JUMLAH CORE': '6C',
        'JENIS KABEL' : 'GYXC10968',
        'PANJANG KABEL /M' : 6000,
        'HARGA PEMBELIAN' : 20000000,
        'TANGGAL PEMBELIAN' : '22-04-2023',
    },
    {        
        'NO ': '2',
        'MEREK KABEL': 'GLOBAL',
        'JUMLAH CORE': '12C',
        'JENIS KABEL' : 'GYC9358',
        'PANJANG KABEL /M' : 4000,
        'HARGA PEMBELIAN' : 18000000,
        'TANGGAL PEMBELIAN' : '06-05-2023',
    },
    {        
        'NO ': '3',
        'MEREK KABEL': 'GLOBAL',
        'JUMLAH CORE': '24C',
        'JENIS KABEL' : 'GYXC109246',
        'PANJANG KABEL /M' : 3000,
        'HARGA PEMBELIAN' : 22000000,
        'TANGGAL PEMBELIAN' : '13-02-2023',
    }
]

stok_Data_Alat_FO = [
    {
        'NO ': '1',
        'JENIS ALAT': 'SPLICER',
        'MEREK ALAT': 'JOINWITH S887S',
        'KETERANGAN ALAT' : 'AKTIF',
        'LOKASI PENEMPATAN ALAT' : 'BATU AJI',
        'HARGA PEMBELIAN' : 16000000,
        'TANGGAL PEMBELIAN' : '01-02-2023',
    },
    {        
        'NO ': '2',
        'JENIS ALAT': 'CLOSURE 24C DOME',
        'MEREK ALAT': 'PAZ',
        'KETERANGAN ALAT' : 'AKTIF',
        'LOKASI PENEMPATAN ALAT' : 'PUSKOPKAR',
        'HARGA PEMBELIAN' : 400000,
        'TANGGAL PEMBELIAN' : '13-02-2023',
    },
    {        
        'NO ': '3',
        'JENIS ALAT': 'CLOSURE 24C   DOME',
        'MEREK ALAT': 'PAZ',
        'KETERANGAN ALAT' : 'AKTIF',
        'LOKASI PENEMPATAN ALAT' : 'PUSKOPKAR',
        'HARGA PEMBELIAN' : 400000,
        'TANGGAL PEMBELIAN' : '29-03-2023',
    }
]

##### PENJUMLAHAN  TOTAL HARGA ROUTER DAN ONU
harga_Router_ONU= 0
for i in stok_Data_Router_ONU:
    harga_Router_ONU += i['HARGA PEMBELIAN']

##### PENJUMLAHAN  TOTAL HARGA KABEL FIBER OPTIK
harga_Kabel_FO= 0
for i in stok_Data_Kabel_FO:
    harga_Kabel_FO += i['HARGA PEMBELIAN']

##### PENJUMLAHAN  TOTAL HARGA ALAT FIBER OPTIK
harga_Alat_FO= 0
for i in stok_Data_Alat_FO:
    harga_Alat_FO += i['HARGA PEMBELIAN']

################ MENAMPILKAN STOCK BARANG
def menampilkan_Stock_Barang():
    while True :
        pilihanMenu = input('''
LIST STOCK BARANG PT. TELEKOM MEDIA NET :

1. STOCK DATA KESELURUHAN INVENTORY
2. STOCK DATA ONU DAN ROUTER
3. STOCK DATA KABEL FIBER OPTIK
4. STOCK DATA ALAT
5. KELUAR KE MENU UTAMA

Masukkan angka Menu yang ingin dijalankan: ''')
        
################         1. STOCK DATA KESELURUHAN INVENTORY   

        if (pilihanMenu == '1') :
            print ('\n\n========================================================================')
            print ('||          DATA KESELURUHAN INVENTORY PT. TELEKOM MEDIA NET          ||')
            print ('========================================================================')


            print('\n\nDATA ROUTER DAN ONU \n')
            print(tabulate(stok_Data_Router_ONU, headers= 'keys',tablefmt='pretty'))
            print ('=======================================================================================================================================================================================')
            print ('                  TOTAL HARGA KESELURUHAN ROUTER DAN ONU                                                                                           :',harga_Router_ONU)
            

            print('\n\nDATA KABEL FO\n')
            print(tabulate(stok_Data_Kabel_FO, headers= 'keys',tablefmt='pretty'))
            print ('===========================================================================================================')
            print ('                TOTAL HARGA KESELURUHAN KABEL FIBER OPTIK                      :',harga_Kabel_FO)

            print('\n\nDATA ALAT FO\n')
            print(tabulate(stok_Data_Alat_FO, headers= 'keys',tablefmt='pretty'))
            print ('==============================================================================================================================')
            print ('                TOTAL HARGA KESELURUHAN ALAT FIBER OPTIK                                       :',harga_Alat_FO)


############################2. STOCK DATA ONU DAN ROUTER
    
        elif(pilihanMenu == '2') :
            print('DATA ROUTER DAN ONU \n')
            Data_NO_SN = input('MASUKAN KATA KUNCI PADA KOLOM DATA ROUTER DAN ONU: ').upper()
            
            def pencarian_Router_ONU(stok_Data_Router_ONU, Data_NO_SN):
                hasil = []
                for item in stok_Data_Router_ONU:
                    if Data_NO_SN in item.values():
                        hasil.append(item)
                        return hasil
                    else:
                        print(f'''KATA {Data_NO_SN} YANG ANDA MASUKAN TIDAK TERTERA DI DATA !!!
MOHON MASUKAN KEMBALI KATA YANG SESUAI''')
                        break
            hasil_Pencarian = pencarian_Router_ONU(stok_Data_Router_ONU, Data_NO_SN)
            print(tabulate(hasil_Pencarian, headers= "keys",tablefmt='pretty'))


##############################     3. STOCK DATA KABEL FIBER OPTIK
        
        elif(pilihanMenu == '3') :
            print('DATA KABEL FIBER OPTIK \n')
            data_FO = input('MASUKAN KATA KUNCI PADA KOLOM DATA KABEL FIBER OPTIK: \n').upper()
            
            def search_list_of_dicts(stok_Data_Kabel_FO, Data_FO):
                hasil = []
                for item in stok_Data_Kabel_FO:
                    if Data_FO in item.values():
                        hasil.append(item)
                        return hasil
                    else:
                        print(f'''KATA {Data_FO} YANG ANDA MASUKAN TIDAK TERTERA DI DATA !!!
MOHON MASUKAN KEMBALI KATA YANG SESUAI''')
                        break
            hasil_Pencarian = search_list_of_dicts(stok_Data_Kabel_FO, data_FO)
            print(tabulate(hasil_Pencarian, headers= "keys",tablefmt='pretty'))                    

#######################      4. STOCK DATA ALAT


        elif(pilihanMenu == '4') :
            print('DATA ALAT FO \n')
            data_Alat= input('MASUKAN KATA KUNCI PADA KOLOM DATA ALAT FIBER OPTIKK: \n').upper()
            
            def search_list_of_dicts(stok_Data_Alat_FO, data_Alat):
                hasil = []
                for item in stok_Data_Alat_FO:
                    if data_Alat in item.values():
                        hasil.append(item)
                        return hasil
                    else:
                        print(f'''KATA {data_Alat} YANG ANDA MASUKAN TIDAK TERTERA DI DATA !!!
MOHON MASUKAN KEMBALI KATA YANG SESUAI''')
                        break
            hasil_Pencarian = search_list_of_dicts(stok_Data_Alat_FO, data_Alat)
            print(tabulate(hasil_Pencarian, headers= "keys",tablefmt='pretty'))
                 


        elif(pilihanMenu == '5') :
            break
            
        else:
            print ('NOMOR URUTAN YANG ANDA MASUKAN TIDAK SESUAI')
            continue



####################### MENAMBAH INPUT STOCK BARANG ##################
def menambah_Stock_Barang():
    while True:
        input_Menambah= input('''
MENAMBAH INPUT DATA STOCK BARANG-BARANG:
                              
1. MENAMBAH STOCK ROUTER DAN ONU
2. MENAMBAH STOCK KABEL FIBER OPTIK
3. MENAMBAH STOCK BARANG FIBER OPTIK
4. KELUAR
                        
MASUKAN NOMOR UNTUK MENAMBAH DATA: ''')


#########################           1. MENAMBAH STOCK ROUTER DAN ONU


        if (input_Menambah == '1'):
            no = input('MASUKAN NO DATA: ')
            for i in no:
                if i.isalpha():
                    print("NOMOR YANG ANDA MASUKAN TIDAK SESUAI\n")
                    break
                elif int(no)==0:
                    break
                
                mac_Address = input('MASUKAN NO MAC ADDRESS: ').upper()
                no_SN = input('MASUKAN NO S/N: ').upper()
                merek_Router_ONU = input('MASUKAN MEREK ROUTER DAN ONU: ').upper()
                jenis_alat = input ('MASUKAN JENIS ALAT: ').upper()
                alamat_pemasangan = input ('ALAMAT PEMASANGAN: ').upper()
                status_Alat = input ('MASUKAN STATUS ALAT: ').upper()
                harga_Pembelian = input('MASUKAN HARGA PEMBELIAN: ')
                for i in harga_Pembelian:
                    if i.isalpha():
                        print("NOMOR YANG ANDA MASUKAN TIDAK SESUAI")
                        break
                    elif int(harga_Pembelian)==0:
                        break
                    
                    ya_Tidak = str(input('APAKAH ANDA INGIN MENYIMPAN DATA INI (Y/N): ')).upper()
                    if ya_Tidak == 'Y':
                        stok_Data_Router_ONU.append(
                            {
                                'NO ': no,
                                'MAC ADDRESS': mac_Address,
                                'NO S/N': no_SN,
                                'MEREK ROUTER DAN ONU' : merek_Router_ONU,
                                'JENIS ALAT' : jenis_alat,
                                'ALAMAT PEMASANGAN' : alamat_pemasangan,
                                'STATUS ALAT': status_Alat,
                                'HARGA PEMBELIAN' : harga_Pembelian,
                                'TANGGAL PEMBELIAN' : dt.date.today().strftime("%d-%m-%Y")
                                }
                        )
                        
                    elif ya_Tidak == 'N':
                        print("DATA PENAMBAHAN ROUTER DAN ONU BATAL TERSIMPAN")
                        menambah_Stock_Barang()
                        continue

                    else:
                        print("MOHON JAWAB DENGAN BENAR (Y/N) ")
                        continue 
                        

                    print (tabulate(stok_Data_Router_ONU, headers='keys',tablefmt='pretty'))
                    menambah_Stock_Barang()          
                        

######################### 2. MENAMBAH STOCK KABEL FIBER OPTIK

        elif (input_Menambah == '2'):
            no1 = input('MASUKAN NO DATA:')
            for i in no1:
                if i.isalpha():
                    print("NOMOR YANG ANDA MASUKAN TIDAK SESUAI")
                    break
                elif int(no1)==0:
                    break

                merek_Kabel = input('MASUKAN MEREK KABEL FIBER OPTIK:').upper()
                jumlah_Core = input('MASUKAN JUMLAH CORE: ').upper()
                jenis_Kabel = input('MASUKAN JENIS KABEL: ').upper()
                panjang_Kabel_M = input ('MASUKAN PANJANG KABEL /M: ').upper()
                for i in panjang_Kabel_M:
                    if i.isalpha():
                        print("NOMOR YANG ANDA MASUKAN TIDAK SESUAI")
                        break
                    elif int(panjang_Kabel_M)==0:
                        break
                    harga_Pembelian1 = input('MASUKAN HARGA PEMBELIAN: ')
                    for i in harga_Pembelian1:
                        if i.isalpha():
                            print("NOMOR YANG ANDA MASUKAN TIDAK SESUAI")
                            break
                        elif int(harga_Pembelian1)==0:
                            break
                        
                        ya_Tidak1 = str(input('APAKAH ANDA INGIN MENYIMPAN DATA INI (Y/N): ')).upper()
                        if ya_Tidak1 == 'Y':
                            
                            stok_Data_Kabel_FO.append(
                                {
                                    'NO ': no1,
                                    'MEREK KABEL': merek_Kabel,
                                    'JUMLAH CORE': jumlah_Core,
                                    'JENIS KABEL' : jenis_Kabel,
                                    'PANJANG KABEL /M' : panjang_Kabel_M,
                                    'HARGA PEMBELIAN' : harga_Pembelian1,
                                    'TANGGAL PEMBELIAN' : dt.date.today().strftime("%d-%m-%Y")
                                    }
                                )
                            
                        elif ya_Tidak1 == 'N':
                            print("DATA PENAMBAHAN KABEL FIBER OPTIK BATAL TERSIMPAN")
                            menambah_Stock_Barang()
                            continue

                        else:
                            print("MOHON JAWAB DENGAN BENAR (Y/N) ")
                            continue
                        print (tabulate(stok_Data_Kabel_FO, headers='keys',tablefmt='pretty'))
                        menambah_Stock_Barang()



########################   3. MENAMBAH STOCK BARANG FIBER OPTIK

        elif (input_Menambah == '3'):
            no2 = input('MASUKAN NO DATA:')
            for i in no2:
                if i.isalpha():
                    print("NOMOR YANG ANDA MASUKAN TIDAK SESUAI")
                    break
                elif int(no2)==0:
                    break

                jenis_Barang = input('MASUKAN JENIS BARANG:').upper()
                merek_Barang = input('MASUKAN MEREK BARANG: ').upper()
                keterangan_Barang = input('MASUKAN KETERANGAN BARANG: ').upper()
                lokasi_Barang = input ('MASUKAN LOKASI PENEMPATAN BARANG: ').upper()
                harga_Pembelian2 = input('MASUKAN HARGA PEMBELIAN: ')
                for i in harga_Pembelian2:
                    if i.isalpha():
                        print("NOMOR YANG ANDA MASUKAN TIDAK SESUAI")
                        break
                    elif int(harga_Pembelian2)==0:
                        break
                    ya_Tidak2 = str(input('APAKAH ANDA INGIN MENYIMPAN DATA INI (Y/N): ')).upper()
                    if ya_Tidak2 == 'Y':

                        stok_Data_Alat_FO.append(
                            {
                                'NO ': no2,
                                'JENIS ALAT': jenis_Barang,
                                'MEREK ALAT': merek_Barang,
                                'KETERANGAN ALAT' : keterangan_Barang,
                                'LOKASI PENEMPATAN ALAT' : lokasi_Barang,
                                'HARGA PEMBELIAN' : harga_Pembelian2,
                                'TANGGAL PEMBELIAN' : dt.date.today().strftime("%d-%m-%Y")
                                }
                            )        

                    elif ya_Tidak2 == 'N':
                        print("DATA PENAMBAHAN ALAT FIBER OPTIK BATAL TERSIMPAN")
                        menambah_Stock_Barang()
                        continue

                    else:
                        print("MOHON JAWAB DENGAN BENAR (Y/N) ")
                        continue
                    
                    print (tabulate(stok_Data_Alat_FO, headers='keys',tablefmt='pretty'))
                    menambah_Stock_Barang()

        elif (input_Menambah == '4'):
            menu_Utama_Stock_Gudang 
            print ("MENUJU KE MENU UTAMA STOCK GUDANG")
            break

        else:
            print ('NOMOR YANG ANDA INPUT TIDAK SESUAI')
            continue


############# MENGHAPUS STOCK BARANG ##############

def menghapus_Stok_Barang ():
    while True:
        input_menghapus_barang= input('''
LIST MENGHAPUS STOCK BARANG:

1. MENGHAPUS DATA STOK ROUTER DAN ONU
2. MENGHAPUS DATA STOK KABEL FIBER OPTIK
3. MENGHAPUS DATA STOCK ALAT FIBER OPTIK
4. KELUAR 


MASUKAN NOMOR YANG AKAN ANDA PILIH: ''')
        

#########################          1. MENGHAPUS DATA STOK ROUTER DAN ONU

        if (input_menghapus_barang =='1'):
            # menampilkan_Stock_Barang()
            hapus_ONU= input('MASUKAN MAC ADDRESS ROUTER YANG ANDA INGIN HAPUS: ').upper()

            for i in stok_Data_Router_ONU.copy():
                if i.get('MAC ADDRESS') == hapus_ONU:
                        
                    ya_Tidak2 = str(input('APAKAH ANDA INGIN MENGHAPUS DATA INI (Y/N): ')).upper()
                    if ya_Tidak2 == 'Y':
                        stok_Data_Router_ONU.remove(i)
                    elif ya_Tidak2 == 'N':
                        print("DATA ROUTER DAN ONU BATAL TERHAPUS")
                        menghapus_Stok_Barang()
                        continue
                    else:
                        print("MOHON JAWAB DENGAN BENAR (Y/N) ")
                        continue
                    print(tabulate(stok_Data_Router_ONU, headers= 'keys',tablefmt='pretty'))
                    break


##################          2. MENGHAPUS DATA STOK KABEL FIBER OPTIK

        elif (input_menghapus_barang =='2'):
            # menampilkan_Stock_Barang()
            hapus_kabel= input('MASUKAN MEREK KABEL FIBER OPTIK YANG ANDA INGIN HAPUS: ').upper()
            
            for i in stok_Data_Kabel_FO.copy():
                if i.get('MEREK KABEL') == hapus_kabel:
                    ya_Tidak2 = str(input('APAKAH ANDA INGIN MENGHAPUS DATA INI (Y/N): ')).upper()
                    if ya_Tidak2 == 'Y':

                        stok_Data_Kabel_FO.remove(i)

                    elif ya_Tidak2 == 'N':
                        print("DATA KABEL FIBER OPTIK BATAL TERHAPUS")
                        menghapus_Stok_Barang()
                        continue

                    else:
                        print("MOHON JAWAB DENGAN BENAR (Y/N) ")
                        continue
                
                    print(tabulate(stok_Data_Kabel_FO, headers= 'keys',tablefmt='pretty'))
                    break


############## 3. MENGHAPUS DATA STOCK ALAT FIBER OPTIK

        elif (input_menghapus_barang =='3'):
            # menampilkan_Stock_Barang()
            hapus_Alat= input('MASUKAN NO ALAT YANG ANDA INGIN HAPUS: ').upper()
            
            for i in stok_Data_Alat_FO.copy():
                if i.get('NO ') == hapus_Alat:
                    ya_Tidak2 = str(input('APAKAH ANDA INGIN MENGHAPUS DATA INI (Y/N): ')).upper()
                    if ya_Tidak2 == 'Y':

                        stok_Data_Alat_FO.remove(i)
                    
                    elif ya_Tidak2 == 'N':
                        print("DATA ALAT FIBER OPTIK BATAL TERHAPUS")
                        menghapus_Stok_Barang()
                        continue

                    else:
                        print("MOHON JAWAB DENGAN BENAR (Y/N) ")
                        continue
                    print(tabulate(stok_Data_Alat_FO, headers= 'keys',tablefmt='pretty'))
                    break

        elif(input_menghapus_barang == '4') :
            break
            
        else:
            print ('NOMOR URUTAN YANG ANDA MASUKAN TIDAK SESUAI')
            continue


############# UPDATE STOCK BARANG ##############

def update_Stok_Barang ():
    while True:
        input_merubah_barang= input('''
LIST PERUBAHAN STOCK BARANG:

1. MERUBAH DATA STOK ROUTER DAN ONU
2. MERUBAH DATA STOK KABEL FIBER OPTIK
3. MERUBAH DATA STOCK ALAT FIBER OPTIK
4. KELUAR 


MASUKAN NOMOR YANG AKAN ANDA PILIH: ''')
        

#################           1. MERUBAH DATA STOK ROUTER DAN ONU

        if (input_merubah_barang =='1'):
            nomor_Yang_Dituju = input('MASUKAN NOMOR YANG INGIN DIGANTI: ').upper()
            for i in stok_Data_Router_ONU.copy():
                if i .get('NO ') == nomor_Yang_Dituju:
                    print ('UPDATE DATA ROUTER DAN ONU')
                    merubah_Alamat =  input ('ALAMAT PEMASANGAN ROUTER DAN ONU: ').upper()
                    merubah_Status = input ('STATUS ALAT ROUTER DAN ONU: ').upper()

                    ya_Tidak2 = str(input('APAKAH ANDA INGIN MERUBAH DATA INI (Y/N): ')).upper()
                    if ya_Tidak2 == 'Y':

                        i['ALAMAT PEMASANGAN']= merubah_Alamat
                        i['STATUS ALAT'] = merubah_Status

                    elif ya_Tidak2 == 'N':
                        print("DATA ALAT ROUTER DAN ONU BATAL TERUPDATE")
                        update_Stok_Barang()
                        continue

                    else:
                        print("MOHON JAWAB DENGAN BENAR (Y/N) ")
                        continue

            print (tabulate(stok_Data_Router_ONU, headers= "keys",tablefmt='pretty'))


########################        2. MERUBAH DATA STOK KABEL FIBER OPTIK

        elif (input_merubah_barang =='2'):
            nomor_Yang_Dituju1 = input('MASUKAN NOMOR YANG INGIN DIGANTI: ').upper()
            for i in stok_Data_Kabel_FO.copy():
                if i .get('NO ') == nomor_Yang_Dituju1:
                    print ('UPDATE DATA KABEL FIBER OPTIK')
                    merubah_Kabel =  int(input ('PERUBAHAN PANJANG KABEL (PER/M) : '))
                    ya_Tidak2 = str(input('APAKAH ANDA INGIN MERUBAH DATA INI (Y/N): ')).upper()
                    if ya_Tidak2 == 'Y':
                       
                        i['PANJANG KABEL /M']= merubah_Kabel

                    elif ya_Tidak2 == 'N':
                        print("DATA KABEL FIBER OPTIK BATAL TERUPDATE")
                        update_Stok_Barang()
                        continue

                    else:
                        print("MOHON JAWAB DENGAN BENAR (Y/N) ")
                        continue
            print (tabulate(stok_Data_Kabel_FO, headers= "keys",tablefmt='pretty'))
         

##########################        3. MERUBAH DATA STOCK ALAT FIBER OPTIK
        elif (input_merubah_barang =='3'):
            nomor_Yang_Dituju2 = input('\n MASUKAN NOMOR YANG INGIN DIGANTI: ')
            for i in stok_Data_Alat_FO.copy():
                if i .get('NO ') == nomor_Yang_Dituju2:
                    print ('\n UPDATE DATA ALAT FIBER OPTIK')
                    merubah_keterangan =  input('MASUKAN KETERANGAN PERUBAHAN ALAT: \n').upper()
                    lokasi_Penempatan = input('MASUKAN LOKASI PENEMPATAN ALAT: \n').upper()
                    ya_Tidak2 = str(input('APAKAH ANDA INGIN MERUBAH DATA INI (Y/N): ')).upper()
                    if ya_Tidak2 == 'Y':

                        i['KETERANGAN ALAT']= merubah_keterangan
                        i['LOKASI PENEMPATAN ALAT']= lokasi_Penempatan

                    elif ya_Tidak2 == 'N':
                        print("DATA ALAT FIBER OPTIK BATAL TERUPDATE")
                        update_Stok_Barang()
                        continue

                    else:
                        print("MOHON JAWAB DENGAN BENAR (Y/N) ")
                        continue                    
            print (tabulate(stok_Data_Alat_FO, headers= "keys",tablefmt='pretty'))


        elif(input_merubah_barang == '4') :
            break
            
        else:
            print ('NOMOR URUTAN YANG ANDA MASUKAN TIDAK SESUAI')
            continue
        

####         DAFTAR MENU UTAMA STOCK GUDANG     ####

while True: 
    menu_Utama_Stock_Gudang = input('''
                                        
========================================================================
||        DATA KESELURUHAN STOCK GUDANG PT. TELEKOM MEDIA NET         ||
========================================================================
                                        
MENU UTAMA STOCK GUDANG PT. TELEKOM MEDIA NET:
                            
1. MENAMPILKAN STOCK BARANG KESELURUHAN
2. MENAMBAH INPUT DATA STOK BARANG
3. MENGHAPUS INPUT DATA STOK BARANG
4. MERUBAH DATA STOK BARANG
5. KELUAR DARI APLIKASI
                            
MASUKAN ANGKA PADA STOCK GUDANG:  ''')
    if (menu_Utama_Stock_Gudang == '1'):
        menampilkan_Stock_Barang()
        
    elif (menu_Utama_Stock_Gudang == '2'):
        menambah_Stock_Barang()
    
    elif (menu_Utama_Stock_Gudang =='3'):
        menghapus_Stok_Barang()
    
    elif (menu_Utama_Stock_Gudang == '4'):
        update_Stok_Barang()
    
    elif (menu_Utama_Stock_Gudang == '5'):
        print ("TERIMAKASIH")
        break
    
    else:
        print("NOMOR YANG ANDA MASUKAN TIDAK TERDAFTAR")
        print("SILAHKAN COBA LAGI")
        continue
    



