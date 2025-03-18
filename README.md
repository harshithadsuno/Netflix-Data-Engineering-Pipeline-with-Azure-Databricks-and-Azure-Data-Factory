# Netflix Data Engineering Pipeline with Azure Databricks and Azure Data Factory

### Overview
This project demonstrates an end-to-end Azure Data Engineering pipeline using Azure Databricks, Azure Data Factory (ADF), and PySpark. It covers real-time and incremental data loading, transformation, and orchestration processes.

### Technologies Used
- **Azure Databricks** (PySpark, Databricks Unity Catalog, Delta Live Tables)
- **Azure Data Factory (ADF)**
- **Azure Data Lake Storage Gen2**
- **Apache Spark**

### Project Structure
- **scripts/**: Python and PySpark scripts for data ingestion, transformation, and orchestration.
- **resources/**: Data.
- **docs/**: Diagrams and additional documentation.

### Pipeline Workflow
1. **Autoloader**: Incrementally loads data using Databricks Autoloader (`1_Autoloader.py`).
2. **Silver Layer Processing**: Transforms raw data to the silver layer (`2_Silver.py`, `4_Silver.py`).
3. **Data Lookup & Validation**: Additional enrichment and validation processes (`3_LookupNotebook.py`, `5_lookupNotebook.py`, `6_falseNotebook.py`).
4. **Delta Live Tables (DLT)**: Manages and automates the pipeline workflow (`7_DLT_Notebook.py`).
