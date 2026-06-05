import streamlit as st

# =====================
# VALIDACIÓN SEMÁNTICA
# =====================

def validar_semantica(nombre, edad, diagnostico):

    errores = []

    try:
        edad = int(edad)

        if edad < 0:
            errores.append("Edad negativa")

        if edad > 120:
            errores.append("Edad fuera de rango")

    except:
        errores.append("La edad debe ser numérica")

    if len(nombre.strip()) == 0:
        errores.append("Nombre vacío")

    if len(diagnostico.strip()) < 3:
        errores.append("Diagnóstico inválido")

    return errores


# =====================
# INTERFAZ STREAMLIT
# =====================

st.title("Registro Médico")

nombre = st.text_input("Nombre")
edad = st.text_input("Edad")
diagnostico = st.text_area("Diagnóstico")

if st.button("Validar registro"):

    errores = validar_semantica(
        nombre,
        edad,
        diagnostico
    )

    if errores:

        st.error("Se encontraron errores:")
        for error in errores:
            st.write(f"• {error}")

    else:

        st.success("Registro médico válido ✅")

        st.markdown(f"""
        **Paciente:** {nombre}

        **Edad:** {edad}

        **Diagnóstico:** {diagnostico}
        """)
