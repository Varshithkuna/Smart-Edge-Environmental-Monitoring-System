import streamlit as st
import paho.mqtt.client as mqtt
import pandas as pd
from collections import deque
import time

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Smart Edge Environmental Monitoring System",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ Smart Edge Environmental Monitoring System")

st.markdown("""
### IIIT Vadodara International Campus

**Summer Research Internship**

**Domain:** Telco Cloud • Edge Computing • IoT Integration • Computing Continuum
""")

# ---------------- MQTT ----------------

broker = "broker.hivemq.com"

temperature = 0.0
humidity = 0.0

temp_data = deque(maxlen=50)
hum_data = deque(maxlen=50)

last_update = time.time()

# ---------------- MQTT CALLBACKS ----------------

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")

    client.subscribe("iiitv/temperature")
    client.subscribe("iiitv/humidity")


def on_message(client, userdata, msg):

    global temperature
    global humidity
    global last_update

    last_update = time.time()

    topic = msg.topic
    payload = float(msg.payload.decode())
    print("Topic:", topic)
    print("Payload:", payload)

    if topic == "iiitv/temperature":
        temperature = payload
        temp_data.append(payload)

    elif topic == "iiitv/humidity":
        humidity = payload
        hum_data.append(payload)

      


# ---------------- MQTT CLIENT ----------------

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)

client.loop_start()

# ---------------- PLACEHOLDERS ----------------

status_placeholder = st.empty()

col1, col2 = st.columns(2)

with col1:
    temp_placeholder = st.empty()

with col2:
    hum_placeholder = st.empty()

chart_placeholder = st.empty()

stats_placeholder = st.empty()

alert_placeholder = st.empty()

# ---------------- LIVE DASHBOARD ----------------

while True:

    # Device Status

    if time.time() - last_update < 10:
        status_placeholder.success("🟢 Device Status : ONLINE")
    else:
        status_placeholder.error("🔴 Device Status : OFFLINE")

    # Metrics

    temp_placeholder.metric(
        "🌡 Temperature",
        f"{temperature:.2f} °C"
    )

    hum_placeholder.metric(
        "💧 Humidity",
        f"{humidity:.2f} %"
    )

    # Statistics

   # if len(temp_data) > 0 and len(hum_data) > 0:

        #avg_temp = sum(temp_data) / len(temp_data)
        #max_temp = max(temp_data)
       # min_temp = min(temp_data)

       # avg_hum = sum(hum_data) / len(hum_data)
       # max_hum = max(hum_data)
        #min_hum = min(hum_data)

    #stats_placeholder.markdown(f"""
### 📊 Statistics

#| Metric | Temperature | Humidity |
#|--------|-------------|----------|
#| Average | {avg_temp:.2f} °C | {avg_hum:.2f} % |
#| Maximum | {max_temp:.2f} °C | {max_hum:.2f} % |
#| Minimum | {min_temp:.2f} °C | {min_hum:.2f} % |
#""")

    # Alerts

    if temperature >= 35:
        alert_placeholder.error("🔥 High Temperature Alert!")

    elif temperature >= 30:
        alert_placeholder.warning("⚠ Temperature Rising")

    elif humidity <= 30:
        alert_placeholder.warning("⚠ Low Humidity Alert")

    elif humidity >= 80:
        alert_placeholder.warning("💧 High Humidity Alert")

    else:
        alert_placeholder.success("✅ Environment Normal")

    # Charts

    min_len = min(len(temp_data), len(hum_data))

    if min_len > 0:

        df = pd.DataFrame({

            "Temperature (°C)": list(temp_data)[-min_len:],

            "Humidity (%)": list(hum_data)[-min_len:]

        })

        chart_placeholder.line_chart(df)

    time.sleep(2)