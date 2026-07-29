# Preditor de Diabetes Gestacional

Modelo de classificação que prevê o risco de diabetes gestacional a partir de dados clínicos da paciente. Inclui notebook de treinamento e interface web para uso do modelo.

---

## Arquivos do Projeto

| Arquivo | Descrição |
|---|---|
| `diabetes-gestacional.csv` | Base de dados com 10.000 registros |
| `preditor-diabetes-gestacional.ipynb` | Notebook de treinamento do modelo |
| `preditor-diabetes.pkl` | Modelo treinado (gerado pelo notebook) |
| `app.py` | Interface web em Streamlit |

---

## Modelo

**Algoritmo:** XGBoost (Extreme Gradient Boosting)

**Variável alvo:** `diabetes` — `1` (com diabetes) ou `0` (sem diabetes)

**Variáveis preditoras:**

| Variável | Descrição |
|---|---|
| `gravidez` | Número de gestações anteriores |
| `glicose` | Concentração de glicose plasmática (mg/dL) |
| `pressao-arterial` | Pressão arterial diastólica (mmHg) |
| `espessura-triceps` | Espessura da dobra cutânea do tríceps (mm) |
| `insulina` | Insulina sérica de 2 horas (µU/mL) |
| `indice-massa-corporal` | IMC — peso (kg) / altura² (m²) |
| `diabetes-pedigree` | Pontuação de histórico familiar de diabetes |
| `idade` | Idade da paciente (anos) |

**Divisão dos dados:**
- 80% treino / 20% validação
- Estratificada — mantém a proporção de positivos e negativos nos dois conjuntos
- `random_state=42` — resultado reproduzível a cada execução

---

## Como Usar

**1. Instalar as dependências**
```bash
pip install pandas scikit-learn xgboost matplotlib joblib streamlit
```

**2. Treinar o modelo**

Abra e execute todas as células do notebook `preditor-diabetes-gestacional.ipynb`. Ao final, o arquivo `preditor-diabetes.pkl` será gerado na mesma pasta.

**3. Rodar a interface web**
```bash
streamlit run app.py
```

Acesse `http://localhost:8501` no navegador, preencha os dados clínicos da paciente e clique em **Analisar paciente**.

---

## Aviso

Este modelo é uma ferramenta de apoio à decisão clínica e não substitui avaliação médica profissional.
