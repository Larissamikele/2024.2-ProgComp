'''
Como obter separadamente quociente e o resto de uma divisão??????
'''
import sys

dividendo = int(input('Informe o DIVIDENDO: '))
divisor   = int(input('Informe o DIVISOR..: '))

if divisor == 0:
    print('O Divisor NÃO PODE SER ZERO!!!!!')
    sys.exit()
    
resultado = dividendo / divisor
print(f'Resultado: {resultado}')
    
quociente = int(resultado)
print(f'Quociente: {quociente}')

resto = dividendo - (divisor * quociente)
print(f'Resto....: {resto}')
