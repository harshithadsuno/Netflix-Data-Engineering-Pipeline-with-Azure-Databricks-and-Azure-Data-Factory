# Databricks notebook source
var = dbutils.jobs.taskValues.get(taskKey = "WeekdayLookup", key = "weekoutput")

# COMMAND ----------

print(var)