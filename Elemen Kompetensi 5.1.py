print("@@@@@   @@@@@@   @@@@@   @@@@@@   @    @")
print("@       @    @   @       @    @   @    @")
print("@ @@@   @@@@@@   @ @@@   @@@@@@   @@@@@@")
print("@   @   @    @   @   @   @    @   @    @")
print("@@@@@   @    @   @@@@@   @    @   @    @")

n = int(input("Masukan Jumlah bilangan: "))
while n<2:
  print("ngaco kamu")
  n = int(input("Masukan Jumlah bilangan: "))
F1=int(input("masukan angka pertama: "))
F2 = int(input("masukan angka kedua: "))
for i in range(n):
  v=F1
  
  x = F1+F2
  F1=F2
  F2=x
  print('berikut urutannya')
  print(v)