# 🤖 Módulo de Machine Learning — Descomplica Auto

Este módulo implementa um modelo de classificação com o objetivo de auxiliar o diagnóstico automatizado de falhas veiculares, com base em dados previamente coletados sobre peças, sinais de falha, quilometragem e condições de uso.

## 🔍 Etapas do Desenvolvimento

- **Pré-processamento de Dados:**  
  Utilizamos um dataset com 189 registros contendo as seguintes features:
  - `Nome da Peça`
  - `Sinal`
  - `Resultado`
  - `Quilometragem`
  - `Condições de Uso`

- **Modelo Inicial:**  
  Um modelo inicial baseado em **Random Forest** foi treinado, atingindo 100% de acurácia. Apesar do resultado parecer ideal, identificamos um problema de *overfitting*, causado principalmente pelo alto peso atribuído à variável `Quilometragem`.

- **Ajustes e Regularização:**  
  Para melhorar a generalização do modelo, restringimos a profundidade das árvores na floresta. Após os ajustes, obtivemos uma acurácia de **97%**, com resultados mais confiáveis em novos dados.

## 📈 Importância das Features

| Feature           | Importância (%) |
|-------------------|------------------|
| Quilometragem     | 32,88%           |
| Sinal             | 31,97%           |
| Nome da Peça      | 23,24%           |
| Condições de Uso  | 11,91%           |

## 📊 Avaliação do Modelo

- **Acurácia Final:** 97%
- **Matriz de Confusão:**  
  A maioria das classes foi corretamente prevista, com boa distribuição.
- **Métricas de Precisão e Recall:**  
  Ambas se mantiveram elevadas, indicando boa capacidade de classificação mesmo após regularização.

## 🎯 Objetivo

O modelo visa acelerar o processo de diagnóstico em situações emergenciais ou de falhas simples, fornecendo ao usuário um suporte inteligente para identificar potenciais causas do problema. Isso reduz o tempo de resposta e auxilia na tomada de decisão com mais autonomia e segurança.

---

