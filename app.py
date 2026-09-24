import streamlit as st
import random
import base64
from pathlib import Path

# ---------------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------------

st.set_page_config(
    page_title="Trivia: Villanas Disney",
    page_icon="🖤",
    layout="centered"
)

# ---------------------------------------------------------
# ESTILOS
# ---------------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #120018, #2b0038, #09000f);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #d9b8e8;
    margin-bottom: 30px;
}

.question {
    background: rgba(255,255,255,0.08);
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.15);
}

.success-box {
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    background: linear-gradient(135deg, #30104d, #6b238e);
    box-shadow: 0 0 30px rgba(255, 0, 255, 0.35);
}

.pikicha {
    width: 220px;
    animation: bounce 1s infinite alternate;
}

@keyframes bounce {
    from {
        transform: translateY(0px) rotate(-3deg);
    }
    to {
        transform: translateY(-25px) rotate(3deg);
    }
}

.confetti {
    font-size: 45px;
    animation: spin 2s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# BANCO DE PREGUNTAS
# ---------------------------------------------------------

preguntas = [
    {
        "pregunta": "¿Cómo se llama la villana de 101 dálmatas?",
        "respuesta": "Cruella de Vil",
        "alternativas": [
            "Cruella de Vil",
            "Maléfica",
            "Úrsula",
            "Madame Medusa"
        ]
    },
    {
        "pregunta": "¿Qué villana intenta robar la voz de Ariel?",
        "respuesta": "Úrsula",
        "alternativas": [
            "Úrsula",
            "Yzma",
            "Cruella de Vil",
            "Madre Gothel"
        ]
    },
    {
        "pregunta": "¿Quién es la villana principal de La Bella Durmiente?",
        "respuesta": "Maléfica",
        "alternativas": [
            "Maléfica",
            "La Reina Malvada",
            "Úrsula",
            "Lady Tremaine"
        ]
    },
    {
        "pregunta": "¿Cómo se llama la madrastra de Cenicienta?",
        "respuesta": "Lady Tremaine",
        "alternativas": [
            "Lady Tremaine",
            "Madame Medusa",
            "Yzma",
            "Cruella de Vil"
        ]
    },
    {
        "pregunta": "¿Qué villana quiere mantenerse joven utilizando la magia del cabello de Rapunzel?",
        "respuesta": "Madre Gothel",
        "alternativas": [
            "Madre Gothel",
            "Maléfica",
            "Úrsula",
            "La Reina Malvada"
        ]
    },
    {
        "pregunta": "¿Quién es la villana de Blancanieves?",
        "respuesta": "La Reina Malvada",
        "alternativas": [
            "La Reina Malvada",
            "Lady Tremaine",
            "Yzma",
            "Cruella de Vil"
        ]
    },
    {
        "pregunta": "¿Cómo se llama la villana de Las locuras del emperador?",
        "respuesta": "Yzma",
        "alternativas": [
            "Yzma",
            "Úrsula",
            "Madre Gothel",
            "Maléfica"
        ]
    },
    {
        "pregunta": "¿Qué villana está obsesionada con conseguir cachorros dálmatas?",
        "respuesta": "Cruella de Vil",
        "alternativas": [
            "Cruella de Vil",
            "La Reina Malvada",
            "Lady Tremaine",
            "Yzma"
        ]
    },
    {
        "pregunta": "¿Qué villana vive bajo el mar?",
        "respuesta": "Úrsula",
        "alternativas": [
            "Úrsula",
            "Maléfica",
            "Madre Gothel",
            "Cruella de Vil"
        ]
    },
    {
        "pregunta": "¿Qué villana utiliza una manzana envenenada?",
        "respuesta": "La Reina Malvada",
        "alternativas": [
            "La Reina Malvada",
            "Úrsula",
            "Yzma",
            "Lady Tremaine"
        ]
    }
]

# ---------------------------------------------------------
# INICIALIZAR TRIVIA
# ---------------------------------------------------------

if "iniciada" not in st.session_state:
    st.session_state.iniciada = False

if "terminada" not in st.session_state:
    st.session_state.terminada = False

if "preguntas" not in st.session_state:
    st.session_state.preguntas = []

if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}

# ---------------------------------------------------------
# PANTALLA PRINCIPAL
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🖤 TRIVIA DE LAS VILLANAS DISNEY 🖤</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">¿Cuánto sabes sobre las villanas más famosas?</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# INICIO
# ---------------------------------------------------------

if not st.session_state.iniciada:

    st.markdown("""
    <div class="question">
        <h3>🎭 ¿Estás preparado?</h3>
        <p>
        Tendrás que responder 5 preguntas.
        Las preguntas y alternativas aparecerán en orden aleatorio.
        </p>
        <p>
        🏆 Consigue 5/5 para desbloquear una sorpresa especial.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("✨ COMENZAR TRIVIA", use_container_width=True):

        st.session_state.preguntas = random.sample(preguntas, 5)

        # Mezclar alternativas
        for pregunta in st.session_state.preguntas:
            random.shuffle(pregunta["alternativas"])

        st.session_state.respuestas = {}
        st.session_state.iniciada = True
        st.session_state.terminada = False

        st.rerun()

# ---------------------------------------------------------
# TRIVIA
# ---------------------------------------------------------

elif st.session_state.iniciada and not st.session_state.terminada:

    st.markdown(
        f"### 🎭 Responde las 5 preguntas"
    )

    with st.form("trivia_form"):

        for i, pregunta in enumerate(st.session_state.preguntas):

            st.markdown(
                f"""
                <div class="question">
                    <h3>Pregunta {i + 1}</h3>
                    <p>{pregunta["pregunta"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.radio(
                "Selecciona una respuesta:",
                pregunta["alternativas"],
                key=f"respuesta_{i}",
                index=None
            )

        enviar = st.form_submit_button(
            "🏆 TERMINAR TRIVIA",
            use_container_width=True
        )

        if enviar:

            respuestas = {}

            for i, pregunta in enumerate(st.session_state.preguntas):
                respuestas[i] = st.session_state.get(
                    f"respuesta_{i}"
                )

            # Verificar que todas tengan respuesta
            if any(v is None for v in respuestas.values()):

                st.warning(
                    "⚠️ Debes responder todas las preguntas antes de terminar."
                )

            else:

                st.session_state.respuestas = respuestas
                st.session_state.terminada = True
                st.rerun()

# ---------------------------------------------------------
# RESULTADO
# ---------------------------------------------------------

elif st.session_state.terminada:

    puntaje = 0

    for i, pregunta in enumerate(st.session_state.preguntas):

        respuesta_usuario = st.session_state.respuestas[i]

        if respuesta_usuario == pregunta["respuesta"]:
            puntaje += 1

    st.markdown("---")

    if puntaje == 5:

        st.balloons()

        st.markdown("""
        <div class="success-box">

        <div class="confetti">🎉 🖤 🎉</div>

        <h1>¡PERFECTO!</h1>

        <h2>¡5 de 5 respuestas correctas!</h2>

        <p>Has demostrado que eres un experto en villanas Disney.</p>

        <h2>🐶 ¡PIKICHA ESTÁ DE FIESTA! 🐶</h2>

        </div>
        """, unsafe_allow_html=True)

        # Buscar GIF de Pikicha
        gif_path = Path("assets/pikicha.gif")

        if gif_path.exists():

            with open(gif_path, "rb") as file:
                gif_data = base64.b64encode(file.read()).decode()

            st.markdown(
                f"""
                <div style="text-align:center;margin-top:25px;">
                    <img
                        src="data:image/gif;base64,{gif_data}"
                        class="pikicha"
                    >
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            # Animación temporal si todavía no se ha añadido
            # el GIF real de Pikicha.
            st.markdown("""
            <div style="
                text-align:center;
                font-size:120px;
                margin-top:25px;
                animation:bounce 1s infinite alternate;
            ">
                🐶
            </div>

            <div style="
                text-align:center;
                font-size:25px;
                font-weight:bold;
            ">
                ¡Pikicha está celebrando contigo! 🎉
            </div>
            """, unsafe_allow_html=True)

    else:

        st.markdown(
            f"""
            <div class="success-box">
                <h1>🎭 Resultado</h1>
                <h2>{puntaje}/5 correctas</h2>
                <p>¡Buen intento! Las villanas todavía tienen algunos secretos.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Mostrar respuestas
    st.markdown("### 📋 Tus respuestas")

    for i, pregunta in enumerate(st.session_state.preguntas):

        respuesta_usuario = st.session_state.respuestas[i]
        correcta = pregunta["respuesta"]

        if respuesta_usuario == correcta:

            st.success(
                f"Pregunta {i + 1}: ✅ Correcta — {correcta}"
            )

        else:

            st.error(
                f"Pregunta {i + 1}: ❌ Tu respuesta: "
                f"{respuesta_usuario} | Correcta: {correcta}"
            )

    st.markdown("")

    if st.button("🔄 JUGAR NUEVAMENTE", use_container_width=True):

        st.session_state.iniciada = False
        st.session_state.terminada = False
        st.session_state.preguntas = []
        st.session_state.respuestas = {}

        st.rerun()
