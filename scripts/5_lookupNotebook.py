# Databricks notebook source
dbutils.widgets.text("weekday","7")

# COMMAND ----------

var = int(dbutils.widgets.get("weekday"))

# COMMAND ----------

dbutils.jobs.taskValues.set(key="weekoutput", value=var)