# Databricks notebook source
looktables_rules = {
    "rule1","show_id is NOT NULL"
}

# COMMAND ----------

@dlt.table(
    name = "gold_netflixdirectors"
)
@dlt.expect_all_or_drop(looktables_rules)
def myfunc():
    df= spark.readstream.format("delta").load("abfss://silver@netflixprojectdlharsh.dfs.core.windows.net/netlix_directors")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflixcast"
)
@dlt.expect_all_or_drop(looktables_rules)
def myfunc():
    df= spark.readstream..format("delta").load("abfss://silver@netflixprojectdlharsh.dfs.core.windows.net/netlix_cast")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflixcountries"
)
@dlt.expect_all_or_drop(looktables_rules)
def myfunc():
    df= spark.readstream.format("delta").load("abfss://silver@netflixprojectdlharsh.dfs.core.windows.net/netlix_countries")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflixcategory"
)
@dlt.expect_or_drop("rule1","show_id is NOT NULL")
def myfunc():
    df= spark.readstream.format("delta").load("abfss://silver@netflixprojectdlharsh.dfs.core.windows.net/netlix_category")
    return df

# COMMAND ----------

@dlt.table

def gold_stg_netflix_titles():

    df = spark.readstream.format("delta").load("abfss://silver@netflixprojectdlharsh.dfs.core.windows.net/netlix_titles")
    return df


# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

@dlt.view

def gold_trns_netflixtitles():
    df = spark.readStream.table("LIVE.gold_stg_netflix_titles")
    df = df.withColumn("newflag",lit(1))
    return df

# COMMAND ----------

masterdata_rules = {
    "rule1", "newflag is NOT NULL",
    "rule2", "show_id is NOT NULL"
}

# COMMAND ----------

@dlt.table

@dlt.expect_all_or_drop(masterdata_rules)
def gold_netflixtitles():

    df = spark.readStream.table("LIVE.gold_trns_netflixtitles")
    return df