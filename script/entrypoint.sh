#!/bin/bash
set -e

# Check if the requirements.txt file exists and install dependencies if it does
if [ -e "/opt/airflow/requirements.txt" ]; then
  $(command python) pip install --upgrade pip  # Upgrade pip to the latest version
  $(command -v pip) install --user -r requirements.txt  # Install required packages
fi

# Initialize the Airflow database if it does not already exist
if [ ! -f "/opt/airflow/airflow.db" ]; then
  airflow db init && \  # Initialize the database
  airflow users create \  # Create an admin user for Airflow
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com \
    --password admin
fi

# Upgrade the Airflow database schema to the latest version
$(command -v airflow) db upgrade

# Start the Airflow webserver
exec airflow webserver
