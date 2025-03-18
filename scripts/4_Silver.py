# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC # Silver Data Transformation

# COMMAND ----------

df = spark.read.format("delta")\
        .option("header", True)\
        .option("inferSchema", True)\
        .load("abfss://bronze@netflixprojectdlharsh.dfs.core.windows.net/netflix_titles")

# COMMAND ----------

df.display()

# COMMAND ----------

df.fillna({"duration_minutes":0, "duration_seasons":1})

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df = df.withColumn("duration_minutes", col('duration_minutes').cast(IntegerType()))\
    .withColumn("duration_seasons", col('duration_seasons').cast(IntegerType()))

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df = df.withColumn("shorttitle",split(col("title"),":")[0])

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.withColumn("rating",split(col("rating"),"-")[0])

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.withColumn("type_flag", when(col("type")=="Movie",1)\
                                .when(col("type")=="TV Show",2)\
                                .otherwise(0))
df.display()

# COMMAND ----------

from pyspark.sql.window import Window

# COMMAND ----------

df = df.withColumn("duration_ranking", dense_rank().over(Window.orderBy(col('duration_minutes').desc())))

# COMMAND ----------

df.display()

# COMMAND ----------

df.createOrReplaceGlobalTempView("global_view")

# COMMAND ----------

df = spark.sql("""
    select * from global_temp.global_view
    """
)

# COMMAND ----------

df.display()

# COMMAND ----------

df_vis = df.groupBy("type").agg(count("*").alias("total_count"))
display(df_vis)

# COMMAND ----------

df.write.format("delta")\
    .mode("overwrite")\
    .option("path", "abfss://silver@netflixprojectdlharsh.dfs.core.windows.net/netflix_titles")\
    .save()
    

# COMMAND ----------

