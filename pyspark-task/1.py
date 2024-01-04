import os
import sys
from pyspark.sql import SparkSession
# Set the Python executable for PySpark
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
# Create a Spark session
spark = SparkSession.builder.getOrCreate()
# Create the DataFrame
df = spark.createDataFrame([("A", 1, None), ("B", None, "123"), ("B", 3, "456"), ("D", None, None)],["Name", "Value", "id"])
#Drop rows with NA values specific to a particular column
result_df = df.na.drop(subset=["Name"])
result_df.show()
