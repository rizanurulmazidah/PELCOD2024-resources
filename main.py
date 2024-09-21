nilai = int(input("Masukkan Nilai: "))

if (nilai > 80):
    print ("selamat anda lulus")
elif (nilai > 90 and nilai < 100 ):
    print("selamat ana lulus, dengan nilai yang memuaskan")
elif (nilai > 70):
    print("lulus tapi deket jurang")
else:
    print("anda masih belum lulus tes, semangat dan coba lagi")

# for loop
for i in range(1, 10, 1):
    print(i)
    print("hello world")

angka = 30

while (angka > 1):
    print(angka)
    angka -= 1 # angka = angka - 1

#FUNCTION
def sayHello():
    print("hello riza")
    print("selamat sore")

fungsi_kali2 = lambda param_angka : param_angka * 2

angka = 10

print(fungsi_kali2())