# Databricks notebook source
# MAGIC %md
# MAGIC ### Array Parameter

# COMMAND ----------

files = [

    {
        "sourcefolder": "netflix_directors",
        "targetfolder": "netflix_directors"
    },

    {
        "sourcefolder": "netflix_cast",
        "targetfolder": "netflix_cast"
    },

    {
        "sourcefolder": "netflix_countries",
        "targetfolder": "netflix_countries"
    },

    {
        "sourcefolder": "netflix_category",
        "targetfolder": "netflix_category"
    }
]

# COMMAND ----------

# MAGIC %md
# MAGIC ### Job Utility to return the Array

# COMMAND ----------

dbutils.jobs.taskValues.set(key = "my_array", value = files)