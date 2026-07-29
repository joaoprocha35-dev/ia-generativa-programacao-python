import streamlit as st
import pandas as pd
import joblib
import os

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA E ESTILIZAÇÃO CUSTOMIZADA (CSS)
# ==============================================================================

st.set_page_config(
    page_title="SalaryIQ | Previsão Salarial",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS para elevar o design a um padrão Premium/SaaS
st.markdown("""
    <style>
    /* Estilização Geral */
    .main {
        background-color: #0e1117;
    }
    
    /* Card de Resultado Destaque */
    .result-card {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(5, 150, 105, 0.2) 100%);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(4px);
        margin-top: 15px;
        margin-bottom: 25px;
    }
    
    .result-title {
        color: #a7f3d0;
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 8px;
    }
    
    .result-value {
        color: #ffffff;
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -1px;
    }

    /* Subtítulo customizado */
    .sub-header {
        color: #9ca3af;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    
    /* Ajuste de Botões Primary */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3rem;
        font-weight: 600;
        background: linear-gradient(90deg, #10b981 0%, #059669 100%);
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. FUNÇÕES AUXILIARES E CARREGAMENTO
# ==============================================================================

@st.cache_resource
def carregar_modelo():
    caminho_modelo = "preditor-salarios.pkl"
    if os.path.exists(caminho_modelo):
        try:
            return joblib.load(caminho_modelo)
        except Exception as e:
            st.sidebar.error(f"Erro ao carregar modelo: {e}")
            return None
    return None

def formatar_moeda(valor: float) -> str:
    """Formata valor numérico para Moeda Brasileira (R$ X.XXX,XX)."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

modelo = carregar_modelo()

# ==============================================================================
# 3. SIDEBAR (PAINEL LATERAL INFORMATIVO)
# ==============================================================================

with st.sidebar:
    st.image("https://img.icons8.com/color/96/diamond.png", width=64)
    st.title("SalaryIQ Pro")
    st.caption("v2.4 • Modelo de Regressão Avançado")
    
    st.divider()
    
    # Status do Modelo
    if modelo is not None:
        st.success("🟢 Modelo ML Conectado", icon="✅")
    else:
        st.warning("🟡 Modo de Simulação Ativo (Modelo .pkl não encontrado)", icon="⚠️")
        
    st.markdown("---")
    st.markdown("### 📊 Sobre o Algoritmo")
    st.write(
        "Este sistema utiliza inteligência artificial treinada com dados salariais da indústria de tecnologia "
        "para estimar a remuneração com base no perfil socioeconômico e técnico."
    )
    
    st.divider()
    st.caption("© 2026 SalaryIQ Analytics. Todos os direitos reservados.")

# ==============================================================================
# 4. CABEÇALHO PRINCIPAL
# ==============================================================================

st.title("💰 Predição de Remuneração")
st.markdown("<p class='sub-header'>Ajuste as métricas do colaborador para gerar uma estimativa salarial precisa via Machine Learning.</p>", unsafe_allow_html=True)

# ==============================================================================
# 5. FORMULÁRIO DE ENTRADAS (LAYOUT EM CARDS / CONTAINERS)
# ==============================================================================

with st.container():
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("👤 Perfil Profissional")
        
        nivel = st.selectbox(
            "Nível Profissional",
            ["Júnior", "Pleno", "Sênior"],
            help="Grau de senioridade atual do funcionário."
        )

        experiencia = st.slider(
            "Anos de Experiência",
            min_value=0,
            max_value=40,
            value=5,
            step=1,
            help="Tempo de atuação na área de tecnologia."
        )

        escolaridade = st.selectbox(
            "Nível de Escolaridade",
            [
                "Ensino Médio",
                "Graduação",
                "Pós-Graduação",
                "Mestrado",
                "Doutorado"
            ]
        )

    with col2:
        st.subheader("⭐ Qualificações & Desempenho")

        desempenho = st.slider(
            "Avaliação de Desempenho (0 - 10)",
            min_value=0.0,
            max_value=10.0,
            value=8.0,
            step=0.1,
            help="Pontuação média na última avaliação de desempenho da empresa."
        )

        certificacoes = st.number_input(
            "Certificações Profissionais",
            min_value=0,
            max_value=20,
            value=2,
            step=1,
            help="Certificados técnicos validados (ex: AWS, Azure, PMP)."
        )

st.markdown("<br>", unsafe_allow_html=True)

# ==============================================================================
# 6. INFERÊNCIA E EXIBIÇÃO DE RESULTADOS
# ==============================================================================

if st.button("🚀 Calcular Previsão Salarial", type="primary"):
    
    # Monta o DataFrame garantindo as colunas originais do modelo
    funcionario = pd.DataFrame({
        "Nível Profissional": [nivel],
        "Experiência em Anos": [experiencia],
        "Escolaridade": [escolaridade],
        "Avaliação de Desempenho": [desempenho],
        "Certificações Profissionais": [certificacoes]
    })

    # Lógica de Inferência com Fallback
    with st.spinner("Processando dados com o modelo preditivo..."):
        if modelo is not None:
            try:
                salario = modelo.predict(funcionario)[0]
            except Exception as e:
                st.error(f"Erro ao processar predição: {e}")
                salario = 0.0
        else:
            # Cálculo simulado apenas para testar a interface sem o .pkl presente
            fator_nivel = {"Júnior": 3500, "Pleno": 7500, "Sênior": 14000}[nivel]
            salario = fator_nivel + (experiencia * 450) + (desempenho * 300) + (certificacoes * 250)

    # Exibição do Card Preditivo
    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-title">Estimativa Salarial Ponderada</div>
            <div class="result-value">{formatar_moeda(salario)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Métricas complementares contextuais
    m1, m2, m3 = st.columns(3)
    
    # Simulações visuais extras para experiência premium
    m1.metric(label="Faixa Salarial Estimada (PISO)", value=formatar_moeda(salario * 0.90))
    m2.metric(label="Salário Médio Calculado", value=formatar_moeda(salario))
    m3.metric(label="Faixa Salarial Estimada (TETO)", value=formatar_moeda(salario * 1.10))

st.divider()

# Rodapé profissional
st.caption("📌 **Nota:** A estimativa é baseada em modelos estatísticos e não garante uma oferta formal de remuneração.")