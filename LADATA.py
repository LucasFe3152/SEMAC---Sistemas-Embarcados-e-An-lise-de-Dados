import serial as ard
import pandas as pd
import time

arduino = ard.Serial('COM9', 9600)

a = 0
b = 0
c = 0
lista1 = []
lista2 = []
lista3 = []

while a < 50:
    
    dados_teste1 = arduino.readline().decode('utf-8').strip()
    print(f"Dado recebido {dados_teste1}")
    lista1.append(dados_teste1)
    a += 1

print("Adicionar água")
time.sleep(50)
arduino.flushInput()

while b < 50:
    
    dados_teste2 = arduino.readline().decode('utf-8').strip()
    print(f"Dado recebido {dados_teste2}")
    lista2.append(dados_teste2)
    b += 1

print("Adicionar água")
time.sleep(50)
arduino.flushInput()

while c < 50:
    
    dados_teste3 = arduino.readline().decode('utf-8').strip()
    print(f"Dado recebido {dados_teste3}")
    lista3.append(dados_teste3)
    c += 1

df = pd.DataFrame({'Teste 50ml': lista1, 'Teste 100ml': lista2, 'Teste 150ml': lista3})
df.to_csv('dados_arduino.csv', index=False)

print(df)