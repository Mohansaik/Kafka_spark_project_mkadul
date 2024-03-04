import subprocess
import time


class KafkaManager:
    def __init__(self, kafka_path):
        self.kafka_path = kafka_path

    def start_zookeeper(self):
        zookeeper_command = f"{self.kafka_path}/bin/windows/zookeeper-server-start.bat {self.kafka_path}/config/zookeeper.properties"
        subprocess.Popen(zookeeper_command, shell=True)
        time.sleep(10)

    def start_kafka(self):
        kafka_command = f"{self.kafka_path}/bin/windows/kafka-server-start.bat {self.kafka_path}/config/server.properties"
        subprocess.Popen(kafka_command, shell=True)
        time.sleep(10)

    def stop_zookeeper(self):
        zookeeper_command = f"{self.kafka_path}/bin/windows/zookeeper-server-stop.bat {self.kafka_path}/config/zookeeper.properties"
        subprocess.Popen(zookeeper_command, shell=True)
        time.sleep(5)

    def stop_kafka(self):
        kafka_command = f"{self.kafka_path}/bin/windows/kafka-server-stop.bat {self.kafka_path}/config/server.properties"
        subprocess.Popen(kafka_command, shell=True)
        time.sleep(5)

    def start(self):
        self.start_zookeeper()
        self.start_kafka()
        print("Zookeeper and Kafka servers started successfully.")

    def stop(self):
        self.stop_kafka()
        self.stop_zookeeper()
        print("Zookeeper and Kafka servers stopped successfully.")


# # Usage:
# kafka_manager = KafkaManager(r"C:\kafka")
# kafka_manager.start()
# # Do something with Kafka
# kafka_manager.stop()
