print("Analisador de Triângulos")
r1 = float(input("Digite o comprimento do primeiro segmento: "))
r2 = float(input("Digite o comprimento do segundo segmento: "))
r3 = float(input("Digite o comprimento do terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triângulo!")
     
else:
    print("Os segmentos acima NÃO podem formar um triângulo.")