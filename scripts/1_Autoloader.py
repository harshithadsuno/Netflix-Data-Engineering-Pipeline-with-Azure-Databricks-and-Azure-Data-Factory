# Databricks notebook source
# MAGIC %md
# MAGIC # Incremental Data Loading using AutoLoader

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema netflix_catalog.net_schema;

# COMMAND ----------

checkpoint_location = "abfss://silver@netflixprojectdlharsh.dfs.core.windows.net/checkpoint"

# COMMAND ----------

df = spark.readStream\
  .format("cloudFiles")\
  .option("cloudFiles.format", "csv")\
  .option("cloudFiles.schemaLocation", checkpoint_location)\
  .load("abfss://raw@netflixprojectdlharsh.dfs.core.windows.net/")

# COMMAND ----------

display(df)

# COMMAND ----------

df.writeStream\
  .option("checkpointLocation", checkpoint_location)\
  .trigger(processingTime="10 seconds")\
  .start("abfss://bronze@netflixprojectdlharsh.dfs.core.windows.net/netflix_titles")

# COMMAND ----------

