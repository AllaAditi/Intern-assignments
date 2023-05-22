import paho.mqtt.client as mqtt

# MQTT broker information
broker_address = "localhost"
broker_port = 1883

# MQTT topic and message
topic = "hello"
message = "Hello, World MQTT!"

# Create a MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Publish the message to the topic
client.publish(topic, message)

# Disconnect from the MQTT broker
client.disconnect()
