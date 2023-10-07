arquivo = open('ip.txt', 'r')

linhas = arquivo.readlines()

ips_validos = []
ips_nao_validos = []

for linha in linhas:
    # Remove espaços em branco e quebra de linha
    endereco_ip = linha.strip()
    # Divide o endereço IP em octetos usando o ponto como separador
    ips = endereco_ip.split('.')
    endereco_ip_valido = True

    for ip in ips:
        # Verifica se o octeto é um número entre 0 e 255
        if not 0 <= int(ip) <= 255:
            endereco_ip_valido = False

    # Se o endereço IP for válido, adiciona-o à lista ips_validos; caso contrário, à lista ips_nao_validos
    if endereco_ip_valido:
        ips_validos.append(endereco_ip)
    else:
        ips_nao_validos.append(endereco_ip)

arquivo.close()  # Fecha o arquivo após ler os dados

# Exibe os IPs válidos e inválidos
print("Endereços IP Válidos:")
for ip in ips_validos:
    print(ip)

print("\nEndereços IP Inválidos:")
for ip in ips_nao_validos:
    print(ip)
