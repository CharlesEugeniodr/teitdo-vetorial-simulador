# TEITDO – Simulação Vetorial 2D

Este repositório contém a simulação numérica da **Teoria da Estrutura Invisível do Tempo e das Dimensões Ocultas (TEITDO)** proposta por Charles de Paula Eugênio.

A simulação é baseada no postulado vetorial:

\[
\omega(x, y) \cdot \varepsilon_{-}(x, y) = -1
\]

Este equilíbrio entre frequência angular (ω) e resistência vetorial (ε₋) descreve o comportamento da malha interna do espaço-tempo como uma rede de tensões autorreguladas.

## 📌 Arquivos

- `teitdo_simulacao.py`: script com a simulação
- `malha_vetorial_2d.csv`: matriz de tensões vetoriais exportada
- `malha_vetorial_2d.png`: visualização gráfica da simulação

## ⚙️ Requisitos

- Python 3.10+
- numpy
- matplotlib
- pandas

## ▶️ Como executar

```bash
pip install -r requirements.txt
python teitdo_simulacao.py
