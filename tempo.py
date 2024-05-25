def calcular_total_minutos_caminhados(arquivo):
    total_minutos = 0
    
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        for linha in linhas:
            partes = linha.split('-')
            if len(partes) > 1:
                minutos_str = partes[-1].strip().split()[0]
                total_minutos += int(minutos_str)
    
    return total_minutos

nome_arquivo = str(input('Informe o nome do arquivo:\n'))

arquivo = nome_arquivo  # Nome do arquivo fornecido
total_minutos = calcular_total_minutos_caminhados(arquivo)
print("Total de minutos caminhados:", total_minutos,'minutos')






