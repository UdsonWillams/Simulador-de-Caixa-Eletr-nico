from time import sleep
cedulas50 = cont50 = cont20 = cont10 = cont5 = cont1 = 0
print(50 * "=")
print("BANCO SPLINE SPLANE")
print(50 * "=")
valor = int(input("QUAL VALOR VOCÊ DESEJA SACAR? "))
while cedulas50 <= valor:
    cedulas50 += 50
    if cedulas50 <= valor:
        cont50 += 1
if cedulas50 > valor:
    cedulas50 -= 50
cedulas20 = cedulas50
while cedulas20 < valor:
    cedulas20 += 20
    if cedulas20 <= valor:
        cont20 += 1
if cedulas20 > valor:
    cedulas20 -= 20
cedulas10 = cedulas20
while cedulas10 < valor:
    cedulas10 += 10
    if cedulas10 <= valor:
        cont10 += 1
if cedulas10 > valor:
    cedulas10 -= 10
cedulas5 = cedulas10
while cedulas5 < valor:
    cedulas5 += 5
    if cedulas5 <= valor:
        cont5 += 1
if cedulas5 > valor:
    cedulas5 -= 5
cedulas1 = cedulas5
while cedulas1 < valor:
    cedulas1 += 1
    if cedulas1 <= valor:
        cont1 += 1
print("ESPERE, SEPARANDO AS NOTAS...")
sleep(2)
print(f"TOTAL DE {cont50} CÉDULAS DE R$50")
if cont20 > 0:
    print(f"TOTAL DE {cont20} CÉDULAS DE R$20")
if cont10 > 0:
    print(f"TOTAL DE {cont10} CÉDULAS DE R$10")
if cont5 > 0:
    print(f"TOTAL DE {cont5} CÉDULAS DE R$5")
if cont1 > 0:
    print(f"TOTAL DE {cont1} CÉDULAS DE R$1")
print("OBRIGADO POR ULTILIZAR NOSSOS SERVIÇOS")
