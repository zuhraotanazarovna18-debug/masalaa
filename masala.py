01.12
.2025
# 1
son = int(input("sonni kiriting"))

yigindi = 0
asl_son = son

while asl_son > 0:
    raqam = asl_son % 10
    yigindi = yigindi + raqam
    asl_son = asl_son // 10
    print(f"{son}ning raqamlar yigindisi: {yigindi}")

# 2
son = int(input)

boluvchilar_yigindisi = 0
boluvchi = 1

while boluvchi < son:
    if son % boluvchi == 0:
        boluvchilar_yigindisi = boluvchilar_yigindisi + boluvchi
    boluvchi = boluvchi = 1

if boluvchilar_yigindisi == son:
    print(f"{son} - mukammal son!")
else:
    print(f"{son} - mukammal son emas")

