# Abre o arquivo contendo os endereços IP em modo de leitura ('r')
with open('ip.txt', 'r') as arquivo:
    # Lê todas as linhas do arquivo em uma lista
    linhas = arquivo.readlines()

# Itera pelas linhas do arquivo
for linha in linhas:
    # Remove espaços em branco e quebra de linha
    endereco_ip = linha.strip()
    
    # Divide o endereço IP em octetos usando o ponto como separador
    ips = endereco_ip.split('.')

ips_validos =[]
ips_nao_validos =[]
for ip in ips:
     if not 0 <= int(ip) <= 255:
         ips_validos.append(ips)
         
print(ips_validos)