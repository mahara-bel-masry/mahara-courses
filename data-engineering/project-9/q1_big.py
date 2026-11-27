from pyspark.sql import SparkSession
import pyspark.sql.functions as F
spark = (SparkSession.builder.master("local[1]")
         .config("spark.driver.memory", "1g").getOrCreate())
spark.sparkContext.setLogLevel("ERROR")
df = spark.read.csv("/tmp/big/sales.csv", header=True,
                    schema="id INT, city STRING, amount INT")
df.write.mode("overwrite").partitionBy("city").parquet("/tmp/big/out")
p = spark.read.parquet("/tmp/big/out")
print(p.count())
p.groupBy("city").agg(F.sum("amount").alias("total")).orderBy("city").show()
