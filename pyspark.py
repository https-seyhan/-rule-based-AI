from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName('LargeDatasetMerge').getOrCreate()

# Read datasets using Spark
df1 = spark.read.csv('large_dataset1.csv', header=True, inferSchema=True)
df2 = spark.read.csv('large_dataset2.csv', header=True, inferSchema=True)

# Perform the merge
merged_df = df1.join(df2, df1.common_column == df2.common_column)

# Save the result to a new CSV file
merged_df.write.csv('merged_large_dataset', header=True)

# Stop the Spark session
spark.stop()
