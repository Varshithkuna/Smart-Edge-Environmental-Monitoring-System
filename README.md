# 🌡️ Smart Edge Environmental Monitoring System

A real-time environmental monitoring system built on **ESP32 + DHT11**, using **MQTT** for lightweight edge-to-cloud communication and a **Streamlit** dashboard for live visualization.

Developed as part of a **Summer Research Internship at IIIT Vadodara International Campus**, in the domain of Telco Cloud, Edge Computing, IoT Integration, and the Computing Continuum.

The ESP32 acts as an edge device — sensing and validating data locally before publishing it — while MQTT provides a lightweight publish/subscribe transport suited to constrained edge hardware, and the dashboard renders live metrics, status, and alerts.

---

## 📋 Table of Contents

- [Features](#-features)
- [System Architecture](#️-system-architecture)
- [Hardware Requirements](#-hardware-requirements)
- [Software Requirements](#-software-requirements)
- [Folder Structure](#-folder-structure)
- [Installation & Setup](#-installation--setup)
- [MQTT Topics](#-mqtt-topics)
- [Screenshots](#-screenshots)
- [Future Improvements](#-future-improvements)
- [License](#-license)
- [Author](#-author)

---

## ✨ Features

- Real-time temperature and humidity sensing using a DHT11 sensor on an ESP32
- Local (edge-side) data validation before transmission, discarding invalid sensor reads
- Lightweight MQTT publish/subscribe communication over Wi-Fi
- Automatic MQTT reconnection on connection loss
- Live Streamlit dashboard with:
  - Real-time temperature and humidity metrics
  - Device online/offline status indicator
  - Rolling trend line chart (last 50 readings)
  - Threshold-based alerts (high temperature, rising temperature, low/high humidity)

---

## 🏗️ System Architecture
+------------------------+
|      DHT11 Sensor      |
+-----------+------------+
|
v
+------------------------+
|     ESP32 DevKit       |
|     (Edge Device)      |
+-----------+------------+
|
Wi-Fi + MQTT
|
v
+------------------------+
|   HiveMQ MQTT Broker   |
+-----------+------------+
|
v
+------------------------+
|   Streamlit Dashboard  |
+-----------+------------+
|
v
+------------------------+
| Live Environmental     |
| Monitoring             |
+------------------------+

The ESP32 performs sensing and preprocessing directly at the edge, and MQTT provides a lightweight, decoupled communication layer between the edge device and the visualization layer — keeping this project grounded in edge computing principles rather than a simple cloud-only IoT setup.

---

## 🔧 Hardware Requirements

| Component | Purpose |
|---|---|
| ESP32 Development Board | Wi-Fi-enabled microcontroller (edge device) |
| DHT11 Sensor | Digital temperature and humidity sensor |
| Breadboard | Prototyping platform |
| Jumper Wires | Sensor-to-ESP32 wiring |
| USB Cable | Power and serial programming |

**Wiring:** DHT11 data pin → ESP32 **GPIO 4**

---

## 💻 Software Requirements

- [PlatformIO](https://platformio.org/) (VS Code extension or CLI)
- Arduino framework for ESP32 (`espressif32` platform)
- Python 3.8+
- Python packages: `streamlit`, `paho-mqtt`, `pandas`
- Arduino libraries (installed automatically via `platformio.ini`):
  - Adafruit DHT sensor library
  - PubSubClient

---

## 📁 Folder Structure
Smart-Edge-Environmental-Monitoring-System/
│
├── src/
│   └── main.cpp              # ESP32 firmware
│
├── Screenshots/
│   ├── Hardware_Setup.jpg
│   ├── Serial_Monitor.png
│   ├── Dashboard.png
│   ├── Live_Graph.png
│   └── Complete_System.jpg
│
├── dashboard.py               # Streamlit Dashboard
├── Subscriber.py               # MQTT Subscriber
├── platformio.ini              # PlatformIO Configuration
├── requirements.txt             # Python Dependencies
├── README.md
├── LICENSE
└── .gitignore

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Smart-Edge-Environmental-Monitoring-System.git
cd Smart-Edge-Environmental-Monitoring-System
```

### 2. Configure Wi-Fi credentials

Open `src/main.cpp` and replace the placeholder values with your own Wi-Fi credentials:

```cpp
const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";
```

> ⚠️ **Important:** You must replace `YOUR_WIFI_NAME` and `YOUR_WIFI_PASSWORD` with your actual Wi-Fi network name and password before uploading the firmware, or the ESP32 will not be able to connect to your network.

### 3. Wire the hardware

Connect the DHT11 sensor's data pin to **GPIO 4** on the ESP32, and power the sensor from the ESP32's 3.3V/5V and GND pins as per your sensor module's specification.

### 4. Build and upload the firmware

Using PlatformIO CLI:

```bash
pio run --target upload
```

Or open the project folder in VS Code with the PlatformIO extension and use **Upload**.

### 5. Monitor serial output (optional)

```bash
pio device monitor
```

You should see Wi-Fi and MQTT connection logs followed by periodic temperature/humidity readings.

### 6. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 7. Run the dashboard

```bash
streamlit run dashboard.py
```

The dashboard will open in your browser and begin displaying live data once the ESP32 starts publishing.

---

## 📡 MQTT Topics

| Topic | Payload | Published By |
|---|---|---|
| `iiitv/temperature` | Temperature in °C (string) | ESP32 |
| `iiitv/humidity` | Humidity in % (string) | ESP32 |

**Broker used:** `broker.hivemq.com` (public HiveMQ broker, port 1883)

> ⚠️ This project uses the public HiveMQ broker **only for prototype demonstration**. It provides no authentication or encryption. For any production or long-term deployment, use a private, secured MQTT broker with TLS and access control.

---

## 📸 Screenshots

| Screenshot | Description |
|---|---|
| `Screenshots/Hardware_Setup.jpg` | Hardware Setup |
| `Screenshots/Serial_Monitor.png` | Serial Monitor Output |
| `Screenshots/Dashboard.png` | Dashboard — Main View |
| `Screenshots/Live_Graph.png` | Dashboard — Live Trend Graph & Alert |
| `Screenshots/Complete_System.jpg` | Complete System |

*(Add your screenshot files to the `Screenshots/` folder using the filenames above so they render correctly on GitHub.)*

---

## 🔮 Future Improvements

- [ ] Migrate from the public HiveMQ broker to a secure, private MQTT broker with TLS and authentication
- [ ] Re-enable and extend the dashboard statistics panel (average/maximum/minimum), which is currently present in the code but disabled
- [ ] Add payload validation on the dashboard to handle malformed or missing MQTT messages
- [ ] Add local data logging or edge-level aggregation on the ESP32 to reduce dependence on continuous connectivity
- [ ] Expand the sensor suite (e.g., air quality, light) within the same architecture

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Kuna Varshith Kumar**
Summer Research Intern — IIIT Vadodara International Campus
Domain: Telco Cloud • Edge Computing • IoT Integration • Computing Continuum

- GitHub: [Add your GitHub profile link]
- LinkedIn: [Add your LinkedIn profile link]