# ⚙️ Documentação Técnica

Esta documentação descreve a estrutura interna, a arquitetura e a lógica de funcionamento da aplicação Calculadora de IMC.

## 🏗️ Arquitetura do Sistema
O projeto segue uma arquitetura simples, concentrada em um único arquivo, separando visualmente a Interface Gráfica da Lógica de Cálculo:

* **`main.py`**:  
  Responsável pela interface gráfica (CustomTkinter), captura de eventos do usuário, validação de entradas e exibição do resultado do IMC.

## 🧮 Lógica de Cálculo
O cálculo do Índice de Massa Corporal (IMC) segue a fórmula padrão:

IMC = peso / (altura²)

A lógica é implementada na função `calcular_imc()`, que:
1. Lê os valores digitados pelo usuário.
2. Normaliza o separador decimal (vírgula ou ponto).
3. Valida se os valores são numéricos e maiores que zero.
4. Calcula o IMC.
5. Classifica o resultado conforme faixas estabelecidas.

## 📋 Classificação do IMC
A função `classificar_imc(imc)` retorna a classificação e a cor correspondente:

| Faixa de IMC | Classificação |
|--------------|---------------|
| < 18.5       | Magreza       |
| 18.5 – 24.9  | Normal        |
| 25 – 29.9    | Sobrepeso     |
| ≥ 30         | Obesidade     |

## 🎨 Cores Utilizadas (Paleta)
* **Primária:** `#1f6aa5` (Título e identidade visual)
* **Magreza:** `#3498db`
* **Normal:** `#2ecc71`
* **Sobrepeso:** `#f1c40f`
* **Obesidade / Erro:** `#e74c3c`
* **Card de Resultado:** `#eef1f5`

## 🛡️ Tratamento de Erros
- Entradas vazias ou não numéricas são tratadas com `try/except`.
- Valores menores ou iguais a zero são considerados inválidos.
- Mensagens de erro são exibidas visualmente no card de resultado.

## 🖥️ Interface Gráfica
A interface utiliza:
- Layout em **cards**
- Hierarquia visual clara (título, entradas, resultado)
- Componentes do **CustomTkinter**
- Design responsivo dentro de dimensões fixas
