denda = 0

arr_kendaraan = ["mobil", "sepeda motor", "truk", "bus"]
arr_warna_plat = ["merah", "hitam", "kuning"]
arr_boolean = ["ya", "tidak"]
arr_boolean2 = ["sudah", "belum"]

kendaraan = input("Jenis kendaraan yang melanggar mobil, sepeda motor, truk, atau bus ? : ")
while(kendaraan not in arr_kendaraan):
    kendaraan = input("Jenis kendaraan yang melanggar mobil, sepeda motor, truk, atau bus ? : ")

punya_plat = input("Apakah kendaraan memiliki plat ? : ")
while(punya_plat not in arr_boolean):
    punya_plat = input("Apakah kendaraan memiliki plat ? : ")

warna_plat = input("Warna plat kendaraan merah, hitam, atau kuning ? : ")
while(warna_plat not in arr_warna_plat):
    warna_plat = input("Warna plat kendaraan merah, hitam, atau kuning ? : ")

plat_kadaluarsa = input("Apakah plat sudah kadaluarsa ? : ")
while(plat_kadaluarsa not in arr_boolean2):
    plat_kadaluarsa = input("Apakah plat sudah kadaluarsa ? : ")

batas_kecepatan = input("Apakah kendaraan melewati batas kecepatan ? : ")
while(batas_kecepatan not in arr_boolean):
    batas_kecepatan = input("Apakah kendaraan melewati batas kecepatan ? : ")

if(kendaraan in arr_kendaraan):
    if(punya_plat in arr_boolean):
        denda += 120000
        if(warna_plat in arr_warna_plat):
            if(plat_kadaluarsa in arr_boolean2):
                denda += 100000
                if(batas_kecepatan in arr_boolean):
                    denda += 50000
                    print("Pengendara ditilang sebesar : Rp", denda)

