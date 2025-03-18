# Netflix Data Engineering Pipeline with Azure Databricks and Azure Data Factory

### Overview
This project demonstrates an end-to-end Azure Data Engineering pipeline using Azure Databricks, Azure Data Factory (ADF), and PySpark. It covers real-time and incremental data loading, transformation, and orchestration processes.

### Technologies Used
- **Azure Databricks** (PySpark, Databricks Unity Catalog, Delta Live Tables)
- **Azure Data Factory (ADF)**
- **Azure Data Lake Storage Gen2**
- **Apache Spark**

### Implementation Details

- **Bronze Layer (Raw Ingestion):**
  - Automated data ingestion workflows using **Azure Data Factory** from GitHub repositories into **Azure Data Lake Storage**.

- **Silver Layer (Cleaned & Transformed Data):**
  - Leveraged **Databricks** and **PySpark scripts** to perform complex transformations, cleansing, and data validation.

- **Gold Layer (Curated Data for Analytics):**
  - Implemented robust data models and aggregations using Databricks to ensure analytics-ready datasets.

- **Orchestration & Governance:**
  - Managed workflows with **Databricks Delta Live Tables (DLT)** for automated pipeline execution.
  - Ensured metadata management and secured data sharing with **Databricks Unity Catalog**.


### Pipeline Workflow
1. **Autoloader**: Incrementally loads data using Databricks Autoloader (`1_Autoloader.py`).
2. **Silver Layer Processing**: Transforms raw data to the silver layer (`2_Silver.py`, `4_Silver.py`).
3. **Data Lookup & Validation**: Additional enrichment and validation processes (`3_LookupNotebook.py`, `5_lookupNotebook.py`, `6_falseNotebook.py`).
4. **Delta Live Tables (DLT)**: Manages and automates the pipeline workflow (`7_DLT_Notebook.py`).
