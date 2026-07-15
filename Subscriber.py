import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"

temperature = ""
humidity = ""

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")

    client.subscribe("iiitv/temperature")
    client.subscribe("iiitv/humidity")

def on_message(client, userdata, msg):

    global temperature
    global humidity

    topic = msg.topic
    payload = msg.payload.decode()

    if topic == "iiitv/temperature":
        temperature = payload

    elif topic == "iiitv/humidity":
        humidity = payload

    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity} %")
    print("-------------------------")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)

client.loop_forever()