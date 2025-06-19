import streamlit as st
import time

st.set_page_config(page_title="Jaques Dev API – POC", page_icon="💻")
st.title("💻 Jaques Dev – Generador de Código para Bind API")

with st.expander("📄 Ejemplos de prompts útiles"):
    st.code("""
Hey Jaques, generá código para transferir 10 ARS desde mi cuenta a AliasPrueba1234.
Hey Jaques, generá código para consultar el estado de una transferencia.
    """, language="text")

prompt = st.text_input("🗣️ Pedile algo a Jaques (ej. 'transferir fondos')")

if prompt:
    st.write(f"**Usuario:** {prompt}")
    with st.spinner("🧠 Jaques está escribiendo..."):
        time.sleep(2)

        if "transferir" in prompt.lower():
            st.subheader("✅ Código generado: Transferencia con Bind API")
            code = '''
import requests

# 1. Autenticación (login JWT)
url_login = "https://sandbox.bind.com.ar/v1/login/jwt"
payload_login = {
    "username": "user",
    "password": "XXXXX"
}
resp = requests.post(url_login, json=payload_login)
token = resp.json()["token"]
headers = {"Authorization": f"JWT {token}"}

# 2. Transferencia de fondos
bank_id = 322
account_id = "21-1-99999-4-6"
view_id = "owner"
url_transfer = f"https://sandbox.bind.com.ar/v1/banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/TRANSFER/transaction-requests"

transfer_payload = {
    "origin_id": "55789",
    "to": {"label": "AliasPrueba1234"},
    "value": {"currency": "ARS", "amount": 10},
    "description": "COMPLETE_TRANS",
    "concept": "VAR",
    "emails": ["apibank@poincenot.com"]
}
resp_tx = requests.post(url_transfer, json=transfer_payload, headers=headers)
tx_id = resp_tx.json().get("id")

# 3. Consultar estado de la transferencia
url_status = f"https://sandbox.bind.com.ar/v1/banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/TRANSFER/{tx_id}"
resp_status = requests.get(url_status, headers=headers)
print("Estado:", resp_status.json().get("status"))
'''
            st.code(code, language="python")
            st.download_button("⬇️ Descargar script Python", data=code, file_name="jaques_bind_transfer.py")

        elif "estado" in prompt.lower():
            st.subheader("📄 Código generado: Consulta de estado de transferencia")
            code = '''
import requests

# Suponiendo que ya tenés el token
headers = {"Authorization": "JWT TU_TOKEN"}

bank_id = 322
account_id = "21-1-99999-4-6"
view_id = "owner"
tx_id = "ID_DE_LA_TRANSFERENCIA"

url_status = f"https://sandbox.bind.com.ar/v1/banks/{bank_id}/accounts/{account_id}/{view_id}/transaction-request-types/TRANSFER/{tx_id}"
resp = requests.get(url_status, headers=headers)
print(resp.json())
'''
            st.code(code, language="python")
            st.download_button("⬇️ Descargar script Python", data=code, file_name="jaques_bind_status.py")

        else:
            st.warning("🤖 Jaques todavía no está preparado para esa petición.")
