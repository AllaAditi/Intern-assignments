import paho.mqtt.client as mqtt

# MQTT broker information
broker_address = "localhost"
broker_port = 1883

# MQTT topic to subscribe to
topic = "hello"


# Callback function when a message is received
def on_message(client,userdata, msg):
    print(f"Received message: {msg.payload.decode()}")


# Create a MQTT client instance
client = mqtt.Client()

# Assign the on_message callback function
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Subscribe to the topic
client.subscribe(topic)

# Start the MQTT client loop to process messages
client.loop_start()

# Keep the script running until interrupted
try:
    while True:
        pass
except KeyboardInterrupt:
    pass

# Disconnect from the MQTT broker
client.disconnect()
