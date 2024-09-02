import threading
import random
import time
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.bancoiot
collection = db.sensores
sensores = [
    {"nomeSensor": "Temp1", "valorSensor": None, "unidadeMedida": "C°", "sensorAlarmado": False},
    {"nomeSensor": "Temp2", "valorSensor": None, "unidadeMedida": "C°", "sensorAlarmado": False},
    {"nomeSensor": "Temp3", "valorSensor": None, "unidadeMedida": "C°", "sensorAlarmado": False}
]

for sensor in sensores:
    if collection.find_one({"nomeSensor": sensor["nomeSensor"]}) is None:
        collection.insert_one(sensor)

def simula_sensor(nomeSensor):
    while True:
        sensor = collection.find_one({"nomeSensor": nomeSensor})
        
        if sensor["sensorAlarmado"]:
            print(f"Atenção! Temperatura muito alta! Verificar Sensor {nomeSensor}!")
            break
        
        valorSensor = random.uniform(30, 40)
        print(f"{nomeSensor} - Temperatura atual: {valorSensor:.2f}°C")

        if valorSensor > 38:
            collection.update_one(
                {"nomeSensor": nomeSensor},
                {"$set": {"valorSensor": valorSensor, "sensorAlarmado": True}}
            )
            print(f"{nomeSensor} alarmado! Temperatura: {valorSensor:.2f}°C")
        else:
            collection.update_one(
                {"nomeSensor": nomeSensor},
                {"$set": {"valorSensor": valorSensor}}
            )

        time.sleep(5)

sensor1 = threading.Thread(target=simula_sensor, args=("Temp1",))
sensor2 = threading.Thread(target=simula_sensor, args=("Temp2",))
sensor3 = threading.Thread(target=simula_sensor, args=("Temp3",))

sensor1.start()
sensor2.start()
sensor3.start()

sensor1.join()
sensor2.join()
sensor3.join()