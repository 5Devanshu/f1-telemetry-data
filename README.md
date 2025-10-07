# F1 Telemetry Project

## Introduction
This project is designed to collect, process, store, and analyze Formula 1 telemetry data. It leverages a modern data stack to provide insights into race performance, car behavior, and driver strategies. The goal is to create a robust and scalable pipeline for F1 data enthusiasts and analysts.

## Features
- **Data Ingestion**: Fetches F1 telemetry data from various sources.
- **Data Transformation**: Processes raw telemetry data using Spark and Dask for efficient and scalable transformations.
- **Data Storage**: Utilizes MinIO as an S3-compatible object storage for raw and processed data.
- **Data Orchestration**: Manages data pipelines using Prefect for scheduling, monitoring, and workflow automation.
- **Data Modeling**: Employs dbt (data build tool) for transforming and modeling data in a data warehouse (DuckDB).
- **Infrastructure as Code**: Uses Terraform to provision and manage necessary cloud infrastructure (if applicable, or local Docker setup).
- **Analysis**: Provides notebooks for exploratory data analysis and visualization.

## Architecture Overview
The project's architecture is composed of several key components:
- **MinIO**: Acts as a local object storage, simulating an S3 bucket for storing raw and transformed data.
- **Prefect**: Orchestrates the data pipelines, ensuring data fetching, transformation, and loading steps run in the correct order and on schedule.
- **Spark/Dask**: Used for distributed data processing, handling large volumes of telemetry data efficiently.
- **dbt**: Transforms and models the data, creating analytical tables in a DuckDB database.
- **Terraform**: Defines and provisions the infrastructure required for the project (e.g., MinIO, Docker containers).
- **Python**: The primary language for scripting data fetching, transformation logic, and Prefect flows.

## Setup and Installation

### Prerequisites
Before you begin, ensure you have the following installed:
- Docker and Docker Compose
- Python 3.8+
- `pip` (Python package installer)
- `git`

### 1. Clone the Repository
```bash
git clone https://github.com/5Devanshu/f1-telemetry-data.git
cd f1-telemetry-data
```

### 2. Environment Setup
Create a Python virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Infrastructure with Terraform
Navigate to the `terraform` directory and initialize Terraform. This will set up MinIO and other necessary services using Docker Compose.
```bash
cd terraform
terraform init
terraform apply --auto-approve
cd ..
```
This command will start MinIO and other services defined in `docker-compose.yml`.

### 4. MinIO Configuration
Ensure your MinIO client is configured correctly. The `src/utils/minio_client.py` contains the necessary logic to interact with MinIO. You might need to set environment variables for `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY` if they are not already configured in your environment or `terraform/variables.tf`.

### 5. Prefect Flows
Prefect is used to orchestrate the data pipelines. To run the Prefect flows:
```bash
prefect server start
prefect deploy src/prefect_flow.py
```
This will start the Prefect UI and deploy the data fetching and transformation flows. You can then run them from the Prefect UI or via the CLI.

### 6. dbt Data Modeling
Navigate to the `dbt_project` directory to run the dbt models. Ensure your `profiles.yml` is correctly configured to connect to DuckDB.
```bash
cd dbt_project
dbt deps
dbt build
cd ..
```
This will run your dbt models, transforming the raw data into analytical tables.

## Usage
Once all components are set up, you can:
- **Fetch Data**: Run the Prefect flow for `fetch_data.py` to ingest new telemetry data.
- **Transform Data**: Run the Prefect flows for `transform_spark.py` or `transform_dask.py` to process the raw data.
- **Analyze Data**: Use the `notebooks/analysis.ipynb` Jupyter notebook to explore and visualize the processed data.

## Project Structure
- `src/`: Contains Python scripts for data fetching, transformation (Spark/Dask), and Prefect flows.
- `terraform/`: Terraform configurations for infrastructure setup (MinIO, Docker Compose).
- `dbt_project/`: dbt project for data modeling and transformations.
- `notebooks/`: Jupyter notebooks for data analysis and visualization.
- `laps_*.json`: Sample telemetry data files.
- `requirements.txt`: Python dependencies.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License.
>>>>>>> 7a3ce02 (Update README.md)
# F1 Telemetry Project

## Introduction
This project is designed to collect, process, store, and analyze Formula 1 telemetry data. It leverages a modern data stack to provide insights into race performance, car behavior, and driver strategies. The goal is to create a robust and scalable pipeline for F1 data enthusiasts and analysts.

## Features
- **Data Ingestion**: Fetches F1 telemetry data from various sources.
- **Data Transformation**: Processes raw telemetry data using Spark and Dask for efficient and scalable transformations.
- **Data Storage**: Utilizes MinIO as an S3-compatible object storage for raw and processed data.
- **Data Orchestration**: Manages data pipelines using Prefect for scheduling, monitoring, and workflow automation.
- **Data Modeling**: Employs dbt (data build tool) for transforming and modeling data in a data warehouse (DuckDB).
- **Infrastructure as Code**: Uses Terraform to provision and manage necessary cloud infrastructure (if applicable, or local Docker setup).
- **Analysis**: Provides notebooks for exploratory data analysis and visualization.

## Architecture Overview
The project's architecture is composed of several key components:
- **MinIO**: Acts as a local object storage, simulating an S3 bucket for storing raw and transformed data.
- **Prefect**: Orchestrates the data pipelines, ensuring data fetching, transformation, and loading steps run in the correct order and on schedule.
- **Spark/Dask**: Used for distributed data processing, handling large volumes of telemetry data efficiently.
- **dbt**: Transforms and models the data, creating analytical tables in a DuckDB database.
- **Terraform**: Defines and provisions the infrastructure required for the project (e.g., MinIO, Docker containers).
- **Python**: The primary language for scripting data fetching, transformation logic, and Prefect flows.

## Setup and Installation

### Prerequisites
Before you begin, ensure you have the following installed:
- Docker and Docker Compose
- Python 3.8+
- `pip` (Python package installer)
- `git`

### 1. Clone the Repository
```bash
git clone https://github.com/5Devanshu/f1-telemetry-data.git
cd f1-telemetry-data
```

### 2. Environment Setup
Create a Python virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Infrastructure with Terraform
Navigate to the `terraform` directory and initialize Terraform. This will set up MinIO and other necessary services using Docker Compose.
```bash
cd terraform
terraform init
terraform apply --auto-approve
cd ..
```
This command will start MinIO and other services defined in `docker-compose.yml`.

### 4. MinIO Configuration
Ensure your MinIO client is configured correctly. The `src/utils/minio_client.py` contains the necessary logic to interact with MinIO. You might need to set environment variables for `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY` if they are not already configured in your environment or `terraform/variables.tf`.

### 5. Prefect Flows
Prefect is used to orchestrate the data pipelines. To run the Prefect flows:
```bash
prefect server start
prefect deploy src/prefect_flow.py
```
This will start the Prefect UI and deploy the data fetching and transformation flows. You can then run them from the Prefect UI or via the CLI.

### 6. dbt Data Modeling
Navigate to the `dbt_project` directory to run the dbt models. Ensure your `profiles.yml` is correctly configured to connect to DuckDB.
```bash
cd dbt_project
dbt deps
dbt build
cd ..
```
This will run your dbt models, transforming the raw data into analytical tables.

## Usage
Once all components are set up, you can:
- **Fetch Data**: Run the Prefect flow for `fetch_data.py` to ingest new telemetry data.
- **Transform Data**: Run the Prefect flows for `transform_spark.py` or `transform_dask.py` to process the raw data.
- **Analyze Data**: Use the `notebooks/analysis.ipynb` Jupyter notebook to explore and visualize the processed data.

## Project Structure
- `src/`: Contains Python scripts for data fetching, transformation (Spark/Dask), and Prefect flows.
- `terraform/`: Terraform configurations for infrastructure setup (MinIO, Docker Compose).
- `dbt_project/`: dbt project for data modeling and transformations.
- `notebooks/`: Jupyter notebooks for data analysis and visualization.
- `laps_*.json`: Sample telemetry data files.
- `requirements.txt`: Python dependencies.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License.
=======
# F1 Telemetry Project

## Introduction
This project is designed to collect, process, store, and analyze Formula 1 telemetry data. It leverages a modern data stack to provide insights into race performance, car behavior, and driver strategies. The goal is to create a robust and scalable pipeline for F1 data enthusiasts and analysts.

## Features
- **Data Ingestion**: Fetches F1 telemetry data from various sources.
- **Data Transformation**: Processes raw telemetry data using Spark and Dask for efficient and scalable transformations.
- **Data Storage**: Utilizes MinIO as an S3-compatible object storage for raw and processed data.
- **Data Orchestration**: Manages data pipelines using Prefect for scheduling, monitoring, and workflow automation.
- **Data Modeling**: Employs dbt (data build tool) for transforming and modeling data in a data warehouse (DuckDB).
- **Infrastructure as Code**: Uses Terraform to provision and manage necessary cloud infrastructure (if applicable, or local Docker setup).
- **Analysis**: Provides notebooks for exploratory data analysis and visualization.

## Architecture Overview
The project's architecture is composed of several key components:
- **MinIO**: Acts as a local object storage, simulating an S3 bucket for storing raw and transformed data.
- **Prefect**: Orchestrates the data pipelines, ensuring data fetching, transformation, and loading steps run in the correct order and on schedule.
- **Spark/Dask**: Used for distributed data processing, handling large volumes of telemetry data efficiently.
- **dbt**: Transforms and models the data, creating analytical tables in a DuckDB database.
- **Terraform**: Defines and provisions the infrastructure required for the project (e.g., MinIO, Docker containers).
- **Python**: The primary language for scripting data fetching, transformation logic, and Prefect flows.

## Setup and Installation

### Prerequisites
Before you begin, ensure you have the following installed:
- Docker and Docker Compose
- Python 3.8+
- `pip` (Python package installer)
- `git`

### 1. Clone the Repository
```bash
git clone https://github.com/5Devanshu/f1-telemetry-data.git
cd f1-telemetry-data
```

### 2. Environment Setup
Create a Python virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Infrastructure with Terraform
Navigate to the `terraform` directory and initialize Terraform. This will set up MinIO and other necessary services using Docker Compose.
```bash
cd terraform
terraform init
terraform apply --auto-approve
cd ..
```
This command will start MinIO and other services defined in `docker-compose.yml`.

### 4. MinIO Configuration
Ensure your MinIO client is configured correctly. The `src/utils/minio_client.py` contains the necessary logic to interact with MinIO. You might need to set environment variables for `MINIO_ACCESS_KEY` and `MINIO_SECRET_KEY` if they are not already configured in your environment or `terraform/variables.tf`.

### 5. Prefect Flows
Prefect is used to orchestrate the data pipelines. To run the Prefect flows:
```bash
prefect server start
prefect deploy src/prefect_flow.py
```
This will start the Prefect UI and deploy the data fetching and transformation flows. You can then run them from the Prefect UI or via the CLI.

### 6. dbt Data Modeling
Navigate to the `dbt_project` directory to run the dbt models. Ensure your `profiles.yml` is correctly configured to connect to DuckDB.
```bash
cd dbt_project
dbt deps
dbt build
cd ..
```
This will run your dbt models, transforming the raw data into analytical tables.

## Usage
Once all components are set up, you can:
- **Fetch Data**: Run the Prefect flow for `fetch_data.py` to ingest new telemetry data.
- **Transform Data**: Run the Prefect flows for `transform_spark.py` or `transform_dask.py` to process the raw data.
- **Analyze Data**: Use the `notebooks/analysis.ipynb` Jupyter notebook to explore and visualize the processed data.

## Project Structure
- `src/`: Contains Python scripts for data fetching, transformation (Spark/Dask), and Prefect flows.
- `terraform/`: Terraform configurations for infrastructure setup (MinIO, Docker Compose).
- `dbt_project/`: dbt project for data modeling and transformations.
- `notebooks/`: Jupyter notebooks for data analysis and visualization.
- `laps_*.json`: Sample telemetry data files.
- `requirements.txt`: Python dependencies.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License.
>>>>>>> 7a3ce02 (Update README.md)
