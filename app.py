import streamlit as st
import time

st.set_page_config(page_title="Jaques - Agente IA Financiero", page_icon="🤖")

st.title("🤖 Jaques – Agente Financiero Simulado")

cmd = st.text_input("🗣️ Escribí tu comando (por ejemplo: 'Jaques, separá en un fondo T0...')")

if cmd:
    st.write(f"**Usuario:** {cmd}")
    with st.spinner("🧠 Jaques está pensando..."):
        time.sleep(2)

        if "separa en un fondo t0" in cmd.lower():
            pagos = {"Luz": 5000, "Agua": 3000, "Internet": 2000}
            total_estimado = sum(pagos.values()) * 1.08  # inflación estimada
            saldo = 20000

            st.write("🔍 Servicios próximos a vencer detectados:")
            st.write(pagos)
            st.write(f"📈 Total estimado con inflación: ${total_estimado:.0f}")
            st.write(f"💰 Saldo disponible: ${saldo}")

            if saldo >= total_estimado:
                st.success(f"✅ Suscribiendo ${total_estimado:.0f} al fondo T0...")
                comprobante = f"Suscripción fondo T0 por ${total_estimado:.0f}\nDetalle: {pagos}"
                st.download_button("⬇️ Descargar comprobante", data=comprobante, file_name="comprobante_t0.txt")
            else:
                st.warning("⚠️ No hay saldo suficiente para cubrir los servicios.")
        
        elif "pagos los servicios de luz" in cmd.lower():
            vencimientos = {"Luz": "2025-06-20", "Agua": "2025-06-25", "Internet": "2025-07-01"}
            st.write("📅 Alarmas programadas para estos vencimientos:")
            st.write(vencimientos)
            st.success("✅ Se programó el rescate automático del FCI T0 y posterior pago.")
            st.download_button("⬇️ Descargar resumen de alarmas", data=str(vencimientos), file_name="alarmas_pagos.json")
        
        else:
            st.error("🤖 Jaques todavía no sabe cómo hacer eso. ¡Seguimos entrenándolo!")
