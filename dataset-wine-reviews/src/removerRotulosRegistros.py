import pandas as pd
import numpy as np
from classificaPoints import classificar_vinho
# Carregar o dataset
df = pd.read_csv("C:/Users/pedro/OneDrive/Área de Trabalho/WineReviews/data/processed/wine-reviews.csv")

# Exibir as primeiras linhas do dataset
print("Antes de remover classificações:\n", df["points"].value_counts())

# Definir a porcentagem de registros sem classificação
percentage_to_remove = 0.30

# Calcular o número de registros a serem modificados
num_to_remove = int(len(df) * percentage_to_remove)

# Selecionar aleatoriamente os índices dos registros a serem removidos
indices_to_remove = np.random.choice(df.index, num_to_remove, replace=False)

# Guardar as classificações antes de removê-las, para contagem
removed_classes = df.loc[indices_to_remove, "points"].value_counts()

# Remover a classificação desses registros (substituir por NaN)
df.loc[indices_to_remove, "points"] = np.nan

# Exibir as primeiras linhas após a modificação
print("\nDepois de remover classificações:\n", df["points"].value_counts(dropna=False))

# Exibir quantos registros de cada classe foram removidos
print("\nNúmero de registros removidos por classe:\n", removed_classes)

# Aplicar a função para a coluna 'score' e criar uma nova coluna 'classificacao'
df['classification'] = df['points'].apply(classificar_vinho)

# Salvar o DataFrame modificado em um novo arquivo CSV
df.to_csv("C:/Users/pedro/OneDrive/Área de Trabalho/WineReviews/data/processed/wine-reviews-sem_rotulos-30.csv", index=False)

print("\nO arquivo modificado foi salvo como 'dataset_modificado.csv'")