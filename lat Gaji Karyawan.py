nama=input ("Nama Karyawan:")
nik=input ("NIK Karyawan:")
status=input ("Status (Staff/Honor):")
gol=input ("Golongan (A/B/C):")
if status=='Staff':
    gaji=1000000
    if gol=='A':
        bonus=200000
    elif gol=='B':
        bonus=400000
    elif gol=='C':
         bonus=550000
elif status=='Honor':
    gaji=750000
    if gol=='A':
        bonus=150000
    elif gol=='B':
        bonus=275000
    elif gol=='C':
        bonus=350000
gatot=gaji+bonus
print("==================================================================")
print("| nama    |   status     |  gaji     |   bonus  |   gaji total   |")
print("==================================================================")
print("|  %s     " %(nama),"|   %s   " %(status),"|%i    "%(gaji),"|%i   "%(bonus),"|%i   " %(gatot))
