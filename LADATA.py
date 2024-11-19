# Importação das bibliotecas utilizadas 
import serial as ard
import pandas as pd
import time


# Função que lê o valor relativo ao sensor pelo Serial
def read_data(lista):
    global arduino
    dados_teste1 = arduino.readline().decode('utf-8').strip()
    print(f"Dado recebido {dados_teste1}")
    lista.append(dados_teste1)

# Função que espera a adição de mais água no recipiente 
def wait_water():
    global contador
    print("Adicionar água")
    time.sleep(50)
    arduino.flushInput()
    contador = 1


# Conecta ao serial pela porta utilizada pelo arduino
arduino = ard.Serial('COM9', 9600) # Alterar para o relativo ao seu computador

contador = 1 # contador para controlar o número de leituras
MAX_VALUE = 50 # número máximo de leituras dos dados
# listas que armazenarão os valores lidos, relativos para cada volume de água
lista50ml = []
lista100ml = []
lista150ml = []

# Leitura de dados, com o volume de 50mL
while contador <= MAX_VALUE:    
    read_data(lista50ml)
    contador += 1

# Espera a mudança do volume de água
wait_water()

# Leitura de dados, com o volume de 100mL
while contador <= MAX_VALUE:
    read_data(lista100ml)
    contador += 1

# Espera a mudança do volume de água
wait_water()

# Leitura de dados, com o volume de 150mL
while contador <= MAX_VALUE:
    read_data(lista150ml)
    contador += 1

# Cria o dataframe utilizando as listas, para que possamos analisar esses dados
df = pd.DataFrame({'Teste 50ml': lista50ml, 'Teste 100ml': lista100ml, 'Teste 150ml': lista150ml})
# Exporta para csv o arquivo gerado com os dados
df.to_csv('dados_arduino.csv', index=False)

print(df)