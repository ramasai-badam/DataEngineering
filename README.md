## Table of Contents
- [Overview](#overview)
- [Architecture](#architecture)
- [Key Learnings](#key-learnings)
- [Tech Stack](#tech-stack)

## Overview

This repo builds a complete data engineering pipeline, covering all stages from data ingestion to processing and storage. The implementation uses tools including Apache Airflow, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra. The entire system is containerized using Docker to ensure ease of deployment and scalability.

## Architecture

![System Architecture](https://github.com/ramasai-badam/DataEngineering/blob/main/Pipeline_Architecture.jpg)

The pipeline consists of the following components:

- **Data Source**: Uses the `randomuser.me` API to fetch random user data.
- **Apache Airflow**: Manages workflow orchestration and saves raw data in PostgreSQL.
- **Apache Kafka & Zookeeper**: Handles real-time data streaming from PostgreSQL.
- **Control Center & Schema Registry**: Supports monitoring and schema management for Kafka streams.
- **Apache Spark**: Processes incoming data using a distributed framework.
- **Cassandra**: Stores the final processed data for further use.

## Key Learnings

By working through this project, you will learn how to:

- Set up a data pipeline with Apache Airflow.
- Implement real-time data streaming using Apache Kafka.
- Manage distributed coordination with Apache Zookeeper.
- Process data efficiently with Apache Spark.
- Store structured data using PostgreSQL and Cassandra.
- Deploy a fully containerized pipeline using Docker.

## Tech Stack

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker
