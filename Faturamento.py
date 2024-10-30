import json

def calcular_faturamento(filename):
    # Carrega os dados do arquivo JSON
    with open(filename, 'r') as file:
        dados = json.load(file)
    
    # Extrai os valores de faturamento diário
    faturamento_diario = [dia['valor'] for dia in dados['faturamento_diario']]
    
    # Filtra os dias com faturamento (ignora dias com 0)
    dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]
    
    # Calcula o menor e maior valor de faturamento
    menor_faturamento = min(dias_com_faturamento) if dias_com_faturamento else 0
    maior_faturamento = max(dias_com_faturamento) if dias_com_faturamento else 0
    
    # Calcula a média de faturamento
    media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento) if dias_com_faturamento else 0
    
    # Conta o número de dias com faturamento acima da média
    dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_faturamento)
    
    # Retorna os resultados
    return {
        'menor_faturamento': menor_faturamento,
        'maior_faturamento': maior_faturamento,
        'dias_acima_media': dias_acima_media
    }

# Chama a função e imprime os resultados
resultado = calcular_faturamento('faturamento.json')
print("Menor faturamento: R$", resultado['menor_faturamento'])
print("Maior faturamento: R$", resultado['maior_faturamento'])
print("Número de dias acima da média: ", resultado['dias_acima_media'])
