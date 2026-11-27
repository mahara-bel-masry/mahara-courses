from pyspark.sql import SparkSession
import pyspark.sql.functions as F
spark = SparkSession.builder.master("local[1]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
rows = [(1, "cairo", "100"), (2, None, "50"), (3, "giza", "x")]
bronze = spark.createDataFrame(rows, ["id", "city", "amount"])
silver = (bronze.filter(F.col("city").isNotNull())
          .withColumn("amount", F.col("amount").cast("int"))
          .filter(F.col("amount").isNotNull()))
gold = silver.groupBy("city").agg(F.sum("amount").alias("total"))
print(bronze.count())
print(silver.count())
print(gold.collect())
