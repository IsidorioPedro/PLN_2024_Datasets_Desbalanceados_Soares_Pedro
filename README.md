# Uso de Datasets Desbalanceados

## Objetivo

O objetivo desta atividade é explorar o uso de datasets desbalanceados, focando em pré-processamento, análise de dados e implementação de técnicas de classificação. Serão utilizadas ferramentas como o algoritmo Naive Bayes, embeddings do modelo GPT-2 e o framework FAISS para otimizar a performance dos modelos.

## Etapas da Atividade

1. **Seleção de Dataset Desbalanceado**
   - Escolher um dataset desbalanceado contendo no mínimo 10 mil registros.

2. **Exploração e Pré-Processamento do Dataset**
   - Utilizar o Pandas para:
     - Listar os campos que compõem cada registro.
     - Listar os labels das classes existentes.
     - Contar a quantidade de registros com diferentes números de labels.
     - Contar registros associados a cada label/classe.
     - Contar registros com e sem labels/classes.
   - Criar uma nova coluna para indicar se o registro possui label ou não.
   - Avaliar a possibilidade de concatenar campos de texto relevantes.
   - Identificar e remover registros duplicados.

3. **Filtragem e Seleção de Classes**
   - Escolher quais labels/classes serão utilizados na atividade de classificação e aplicar filtros apropriados.

4. **Criação de Conjuntos de Dados**
   - Usar a biblioteca Scikit-multilearn para criar conjuntos de registros para treinamento, validação e teste.

5. **Implementação e Avaliação de Modelos**
   - Implementar o Naive Bayes e gerar gráficos de Micro e Macro F1 score.
   - Utilizar embeddings do modelo GPT-2 disponível no Hugging Face e recursos do FAISS para apresentar e discutir os resultados.

## Considerações Finais

Nesta atividade, foi possível observar os desafios e técnicas associadas ao tratamento de datasets desbalanceados. A implementação de modelos clássicos como o Naive Bayes, junto com técnicas como embeddings do GPT-2, proporcionou uma visão ampla sobre como lidar com desbalanceamento e otimizar a performance dos modelos. A análise das métricas de Micro e Macro F1 score possibilitou uma avaliação precisa da eficácia dos métodos aplicados.

## Tutorial

**Tutorial: Classificação de Datasets Desbalanceados com Naive Bayes, GPT-2 e FAISS**

Este tutorial guia você pelo processo de classificação de datasets desbalanceados, utilizando o algoritmo Naive Bayes, embeddings do GPT-2 e o framework FAISS para otimização de consultas vetoriais. O tutorial abrange desde o pré-processamento do dataset até a avaliação do desempenho dos modelos por meio de métricas como Micro e Macro F1 score. O projeto está dividido em cinco etapas principais, e o exemplo completo pode ser acessado no repositório.

## Links Úteis

- [Repositório do Projeto](https://github.com/IsidorioPedro/PLN_2024_Datasets_Desbalanceados_Soares_Pedro)
- [Dataset do Projeto](https://www.kaggle.com/datasets/zynicide/wine-reviews/data)
- [Documentação do Pandas](https://pandas.pydata.org/pandas-docs/stable/)
- [Documentação do Scikit-learn](https://scikit-learn.org/stable/)
- [Documentação do Hugging Face](https://huggingface.co/docs)

