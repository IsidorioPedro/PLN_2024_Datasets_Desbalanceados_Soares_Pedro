import pandas as pd

# Função para classificar os vinhos com base no score
def classificar_vinho(score):
    if 80 <= score <= 84:
        return "Regular"
    elif 85 <= score <= 89:
        return "Bom"
    elif 90 <= score <= 94:
        return "Ótimo"
    elif 95 <= score <= 100:
        return "Excelente"
    else:
        return None

# Carregar o dataset CSV
df = pd.read_csv('C:/Users/pedro/OneDrive/Área de Trabalho/WineReviews/data/raw/winemag-data-130k-v2.csv')

# Aplicar a função para a coluna 'score' e criar uma nova coluna 'classificacao'
df['classification'] = df['points'].apply(classificar_vinho)

# Salvar o dataset modificado de volta em um novo arquivo CSV
df.to_csv('C:/Users/pedro/OneDrive/Área de Trabalho/WineReviews/data/processed/wine-reviews.csv', index=False)

print("Classificação adicionada ao dataset e arquivo salvo.")
