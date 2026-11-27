from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from delta import configure_spark_with_delta_pip
b = (SparkSession.builder.master("local[1]")
     .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
     .config("spark.sql.catalog.spark_catalog",
             "org.apache.spark.sql.delta.catalog.DeltaCatalog"))
spark = configure_spark_with_delta_pip(b).getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
rows = [(1, "cairo", "100"), (2, None, "50"), (3, "giza", "x"),
        (4, "giza", "70")]
bronze = spark.createDataFrame(rows, ["id", "city", "amount"])
bronze.write.format("delta").mode("overwrite").save("/tmp/m/bronze")
b2 = spark.read.format("delta").load("/tmp/m/bronze")
silver = (b2.filter(F.col("city").isNotNull())
          .withColumn("amount", F.col("amount").cast("int"))
          .filter(F.col("amount").isNotNull()))
silver.write.format("delta").mode("overwrite").save("/tmp/m/silver")
s2 = spark.read.format("delta").load("/tmp/m/silver")
gold = s2.groupBy("city").agg(F.sum("amount").alias("total"))
gold.write.format("delta").mode("overwrite").save("/tmp/m/gold")
g = spark.read.format("delta").load("/tmp/m/gold")
print(b2.count(), s2.count())
print(sorted(g.collect()))
