from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
b = (SparkSession.builder.master("local[1]")
     .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
     .config("spark.sql.catalog.spark_catalog",
             "org.apache.spark.sql.delta.catalog.DeltaCatalog"))
spark = configure_spark_with_delta_pip(b).getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
P = "/tmp/dl"
df = spark.createDataFrame([(1, "a"), (2, "b")], ["id", "v"])
df.write.format("delta").mode("overwrite").save(P)
new = spark.createDataFrame([(3, "c")], ["id", "v"])
new.write.format("delta").mode("append").save(P)
r = spark.read.format("delta")
print(r.load(P).count())
print(r.option("versionAsOf", 0).load(P).count())
