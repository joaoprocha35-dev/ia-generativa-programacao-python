# ──────────────────────────────────────────────────────────────────────────────
# app.py — Interface Gráfica para o Preditor de Diabetes Gestacional
# Para executar: streamlit run app.py
# ──────────────────────────────────────────────────────────────────────────────


# ─── Importações ──────────────────────────────────────────────────────────────

# Biblioteca principal da interface gráfica web
import streamlit as st

# Biblioteca para montar o DataFrame com os dados da paciente
import pandas as pd

# Biblioteca para carregar o modelo treinado a partir do arquivo .pkl
import joblib

# Biblioteca para verificar se o arquivo do modelo existe no disco
import os


# ─── Configuração Inicial da Página ───────────────────────────────────────────

# Define o título da aba no navegador, o ícone e o layout da página
st.set_page_config(
    page_title="Preditor de Diabetes Gestacional",
    page_icon="🩺",
    layout="centered"
)


# ─── Estilos CSS Personalizados ───────────────────────────────────────────────

# Injeta CSS dentro da página para sobrescrever o tema padrão do Streamlit
st.markdown("""
<style>

    /* Importa a fonte Inter do Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

    /* Define o fundo escuro e a fonte em toda a aplicação */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0F1923;
        font-family: 'Inter', sans-serif;
        color: #F0EDE8;
    }

    /* Remove o fundo padrão do contêiner central do Streamlit */
    [data-testid="block-container"] {
        background-color: #0F1923;
        padding-top: 2rem;
    }

    /* Centraliza e espaça o cabeçalho da aplicação */
    .app-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
    }

    /* Tamanho e animação de pulso do ícone no topo */
    .app-icon {
        font-size: 3rem;
        display: inline-block;
        animation: pulse-icon 2.5s ease-in-out infinite;
    }

    /* Faz o ícone crescer e diminuir suavemente em loop */
    @keyframes pulse-icon {
        0%, 100% { transform: scale(1);    opacity: 1;   }
        50%       { transform: scale(1.12); opacity: 0.8; }
    }

    /* Estilo do título principal da aplicação */
    .app-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: #F0EDE8;
        margin: 0.5rem 0 0.25rem 0;
        letter-spacing: -0.5px;
    }

    /* Estilo do subtítulo descritivo abaixo do título */
    .app-subtitle {
        font-size: 0.9rem;
        color: #8A9BAE;
        font-weight: 300;
        margin-bottom: 2rem;
    }

    /* Card escuro que agrupa os campos de entrada da paciente */
    .input-card {
        background-color: #1A2E3B;
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        border: 1px solid #243647;
    }

    /* Rótulo dourado em caixa alta acima das seções do formulário */
    .section-label {
        font-size: 0.72rem;
        font-weight: 500;
        color: #E8C27B;
        letter-spacing: 1.8px;
        text-transform: uppercase;
        margin-bottom: 1.2rem;
        display: block;
    }

    /* Fundo e borda dos campos numéricos de entrada */
    [data-testid="stNumberInput"] input {
        background-color: #0F1923 !important;
        border: 1px solid #2E4356 !important;
        border-radius: 8px !important;
        color: #F0EDE8 !important;
        font-family: 'Inter', sans-serif !important;
    }

    /* Destaca a borda do campo quando o usuário clica nele */
    [data-testid="stNumberInput"] input:focus {
        border-color: #E8C27B !important;
        box-shadow: 0 0 0 2px rgba(232, 194, 123, 0.15) !important;
    }

    /* Cor e tamanho das etiquetas (labels) de cada campo */
    [data-testid="stNumberInput"] label p {
        color: #A8BACB !important;
        font-size: 0.85rem !important;
        font-weight: 400 !important;
    }

    /* Estilo do botão principal de análise */
    [data-testid="stButton"] > button {
        background-color: #E8C27B !important;
        color: #0F1923 !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 0.75rem 2rem !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
        letter-spacing: 0.3px;
        margin-top: 0.5rem;
    }

    /* Efeito hover: sobe levemente e ganha sombra dourada */
    [data-testid="stButton"] > button:hover {
        background-color: #F0D090 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 24px rgba(232, 194, 123, 0.3) !important;
    }

    /* Efeito ao clicar: volta à posição original */
    [data-testid="stButton"] > button:active {
        transform: translateY(0) !important;
    }

    /* Card vermelho exibido quando o modelo prevê diabetes */
    .result-positive {
        background: linear-gradient(135deg, #2A1A1A, #3B1F1F);
        border: 1px solid #E57373;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        animation: slide-in 0.4s ease-out;
    }

    /* Card verde exibido quando o modelo não detecta diabetes */
    .result-negative {
        background: linear-gradient(135deg, #1A2A1F, #1F3B2A);
        border: 1px solid #4CAF84;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        animation: slide-in 0.4s ease-out;
    }

    /* O card sobe suavemente ao aparecer na tela */
    @keyframes slide-in {
        from { opacity: 0; transform: translateY(14px); }
        to   { opacity: 1; transform: translateY(0);    }
    }

    /* Círculo vermelho pulsante exibido no resultado positivo */
    .result-dot-positive {
        width: 52px;
        height: 52px;
        background-color: #E57373;
        border-radius: 50%;
        margin: 0 auto 1.2rem auto;
        animation: pulse-red 1.6s ease-in-out infinite;
    }

    /* Círculo verde pulsante exibido no resultado negativo */
    .result-dot-negative {
        width: 52px;
        height: 52px;
        background-color: #4CAF84;
        border-radius: 50%;
        margin: 0 auto 1.2rem auto;
        animation: pulse-green 1.6s ease-in-out infinite;
    }

    /* Pulso em vermelho: expande e desvanece uma sombra ao redor do círculo */
    @keyframes pulse-red {
        0%, 100% { box-shadow: 0 0 0 0   rgba(229, 115, 115, 0.5); }
        50%       { box-shadow: 0 0 0 14px rgba(229, 115, 115, 0);   }
    }

    /* Pulso em verde: idem, mas na cor verde */
    @keyframes pulse-green {
        0%, 100% { box-shadow: 0 0 0 0   rgba(76, 175, 132, 0.5); }
        50%       { box-shadow: 0 0 0 14px rgba(76, 175, 132, 0);   }
    }

    /* Fonte do título dentro do card de resultado */
    .result-title {
        font-size: 1.35rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    /* Cor do título quando o resultado é positivo */
    .result-title-positive { color: #E57373; }

    /* Cor do título quando o resultado é negativo */
    .result-title-negative { color: #4CAF84; }

    /* Texto descritivo dentro do card de resultado */
    .result-desc {
        font-size: 0.9rem;
        color: #8A9BAE;
        font-weight: 300;
        line-height: 1.6;
    }

    /* Linha horizontal sutil entre o formulário e o resultado */
    .divider {
        border: none;
        border-top: 1px solid #1E3347;
        margin: 1.5rem 0;
    }

    /* Texto de aviso no rodapé da página */
    .footer {
        text-align: center;
        color: #3D5468;
        font-size: 0.78rem;
        padding: 2.5rem 0 1rem 0;
        font-weight: 300;
        line-height: 1.6;
    }

    /* Oculta o menu hamburguer, rodapé e cabeçalho nativos do Streamlit */
    #MainMenu, footer, header { visibility: hidden; }

    /* Oculta a barra de decoração colorida no topo da página */
    [data-testid="stDecoration"] { display: none; }

</style>
""", unsafe_allow_html=True)


# ─── Carregamento do Modelo ───────────────────────────────────────────────────

# Verifica se o arquivo .pkl existe na mesma pasta que este script
if not os.path.exists('preditor-diabetes.pkl'):

    # Exibe mensagem de erro amigável se o modelo não for encontrado
    st.error('⚠️  Arquivo preditor-diabetes.pkl não encontrado. Execute o notebook primeiro para treinar e salvar o modelo.')

    # Interrompe a execução do app para não continuar sem o modelo
    st.stop()

# Carrega o modelo XGBoost salvo pelo notebook
modelo = joblib.load('preditor-diabetes.pkl')


# ─── Cabeçalho ────────────────────────────────────────────────────────────────

# Renderiza o cabeçalho com ícone animado, título e instrução de uso
st.markdown("""
<div class="app-header">
    <span class="app-icon">🩺</span>
    <div class="app-title">Diabetes Gestacional</div>
    <div class="app-subtitle">Insira os dados clínicos da paciente para obter a previsão do modelo</div>
</div>
""", unsafe_allow_html=True)


# ─── Formulário de Entrada ────────────────────────────────────────────────────

# Abre o card visual que agrupa os campos de entrada
st.markdown('<div class="input-card"><span class="section-label">Dados Clínicos</span>', unsafe_allow_html=True)

# Divide a área em duas colunas para organizar os campos lado a lado
coluna_esq, coluna_dir = st.columns(2)

# ── Coluna esquerda ──
with coluna_esq:

    # Campo: número de gestações anteriores da paciente
    gravidez = st.number_input('Número de gestações', min_value=0, max_value=20, value=0, step=1)

    # Campo: concentração de glicose plasmática (mg/dL)
    glicose = st.number_input('Glicose (mg/dL)', min_value=0, max_value=300, value=100, step=1)

    # Campo: pressão arterial diastólica (mmHg)
    pressao = st.number_input('Pressão arterial (mmHg)', min_value=0, max_value=200, value=70, step=1)

    # Campo: espessura da dobra cutânea do tríceps (mm)
    triceps = st.number_input('Espessura do tríceps (mm)', min_value=0, max_value=100, value=20, step=1)

# ── Coluna direita ──
with coluna_dir:

    # Campo: nível de insulina sérica de 2 horas (µU/mL)
    insulina = st.number_input('Insulina (µU/mL)', min_value=0, max_value=1000, value=80, step=1)

    # Campo: índice de massa corporal — peso (kg) / altura² (m²)
    imc = st.number_input('Índice de massa corporal', min_value=0.0, max_value=70.0, value=25.0, step=0.1, format="%.1f")

    # Campo: função de pedigree do diabetes (pontuação de histórico familiar)
    pedigree = st.number_input('Pedigree do diabetes', min_value=0.000, max_value=3.000, value=0.500, step=0.001, format="%.3f")

    # Campo: idade da paciente em anos completos
    idade = st.number_input('Idade (anos)', min_value=1, max_value=120, value=30, step=1)

# Fecha o card visual do formulário
st.markdown('</div>', unsafe_allow_html=True)


# ─── Botão de Análise e Resultado ─────────────────────────────────────────────

# Exibe o botão; o bloco abaixo só executa quando o usuário clicar nele
if st.button('Analisar paciente'):

    # Monta um DataFrame com os dados digitados, usando os mesmos nomes de colunas do treino
    dados_paciente = pd.DataFrame([[
        gravidez, glicose, pressao, triceps, insulina, imc, pedigree, idade
    ]], columns=[
        'gravidez',
        'glicose',
        'pressao-arterial',
        'espessura-triceps',
        'insulina',
        'indice-massa-corporal',
        'diabetes-pedigree',
        'idade'
    ])

    # Usa o modelo para prever a classe (0 = sem diabetes, 1 = com diabetes)
    resultado = modelo.predict(dados_paciente)[0]

    # Obtém as probabilidades estimadas para cada classe (sem diabetes e com diabetes)
    probabilidades = modelo.predict_proba(dados_paciente)[0]

    # Calcula a confiança percentual do modelo na classe prevista
    confianca = probabilidades[resultado] * 100

    # Exibe uma linha divisória antes do resultado
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Escolhe qual card exibir com base no resultado da previsão
    if resultado == 1:

        # Resultado positivo: modelo identificou risco de diabetes gestacional
        st.markdown(f"""
        <div class="result-positive">
            <div class="result-dot-positive"></div>
            <div class="result-title result-title-positive">Risco Detectado</div>
            <div class="result-desc">
                O modelo identificou indicadores de diabetes gestacional<br>
                com <strong>{confianca:.1f}%</strong> de confiança.
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:

        # Resultado negativo: modelo não identificou indicadores de diabetes
        st.markdown(f"""
        <div class="result-negative">
            <div class="result-dot-negative"></div>
            <div class="result-title result-title-negative">Sem Indicadores</div>
            <div class="result-desc">
                O modelo não identificou indicadores de diabetes gestacional<br>
                com <strong>{confianca:.1f}%</strong> de confiança.
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─── Rodapé ───────────────────────────────────────────────────────────────────

# Exibe um aviso de uso responsável no final da página
st.markdown("""
<div class="footer">
    Este preditor é uma ferramenta de apoio à decisão clínica e não substitui a avaliação médica profissional.
</div>
""", unsafe_allow_html=True)