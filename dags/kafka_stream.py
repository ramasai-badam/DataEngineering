import uuid
import json
import time
import logging
import requests
from datetime import datetime
from kafka import KafkaProducer
from airflow import DAG
from airflow.operators.python import PythonOperator

# Default arguments for the DAG
default_args = {
    "owner": "airscholar",
    "start_date": datetime(2023, 9, 3, 10, 0),
}

def get_data():
    """Fetches random user data from an API."""
    response = requests.get("https://randomuser.me/api/")
    user_data = response.json()["results"][0]
    return user_data

def format_data(user_data):
    """Formats the fetched user data into a structured dictionary."""
    location = user_data["location"]
    return {
        "id": str(uuid.uuid4()),
        "first_name": user_data["name"]["first"],
        "last_name": user_data["name"]["last"],
        "gender": user_data["gender"],
        "address": f"{location['street']['number']} {location['street']['name']}, "
        f"{location['city']}, {location['state']}, {location['country']}",
        "post_code": location["postcode"],
        "email": user_data["email"],
        "username": user_data["login"]["username"],
        "dob": user_data["dob"]["date"],
        "registered_date": user_data["registered"]["date"],
        "phone": user_data["phone"],
        "picture": user_data["picture"]["medium"],
    }

def stream_data():
    """Streams formatted user data to a Kafka topic for 1 minute."""
    producer = KafkaProducer(bootstrap_servers=["broker:29092"], max_block_ms=5000)
    end_time = time.time() + 60  # Run for 1 minute

    while time.time() < end_time:
        try:
            raw_data = get_data()
            formatted_data = format_data(raw_data)
            producer.send("users_created", json.dumps(formatted_data).encode("utf-8"))
        except Exception as e:
            logging.error(f"An error occurred: {e}")

# Define the DAG
with DAG(
    "user_automation",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:
    
    streaming_task = PythonOperator(
        task_id="stream_data_from_api",
        python_callable=stream_data,
    )
