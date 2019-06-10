#! /usr/bin/env python3
from hermes_python.hermes import Hermes

MQTT_ADDR= "192.168.1.132:1883"

print("hello world")
def subscribe_corridor_lights_callback(hermes,intent_message):
    print("Parse intent : {}" .format(intent_message.intent.intent_name))

with Hermes(MQTT_ADDR) as h:
    h.subscribe_intent("On-Off-Lights",subscribe_corridor_lights_callback).start()
