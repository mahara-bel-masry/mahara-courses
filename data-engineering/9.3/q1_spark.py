from pyspark.sql import SparkSession, Window
import pyspark.sql.functions as F
spark = SparkSession.builder.master("local[2]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
rows = [("cairo", 1, 100), ("cairo", 2, 250), ("giza", 1, 80),
        ("giza", 2, 120), ("giza", 3, 90)]
df = spark.createDataFrame(rows, ["city", "day", "sales"])
df.groupBy("city").agg(F.sum("sales").alias("total")).show()
w = Window.partitionBy("city").orderBy("day")
df.withColumn("rank", F.row_number().over(w)).filter("rank=1").show()
df.createOrReplaceTempView("t")
spark.sql("select city, max(sales) m from t group by city").show()
print(df.repartition(4).rdd.getNumPartitions())
