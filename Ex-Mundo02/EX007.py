s1 = int(input('Infrome o primeiro seguimento: '))
s2 = int(input('Infrome o segundo seguimento: ')) 
s3 = int(input('Infrome o terceiro seguimento: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    if s1 == s2 == s3:
        print('Triângulo Equilátero')
    elif s1 != s2 and s2 != s3 and s1 != s3:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Os segmentos informados NÃO podem formar um triângulo.')
