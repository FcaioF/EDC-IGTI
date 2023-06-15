from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.functions import col


# Inspirado em
# https://github.com/apache/spark/blob/master/examples/src/main/python/sql/streaming/structured_network_wordcount.py
# https://github.com/muhammadnaumanshahid/twitter_streaming_data/blob/main/read_tweets.py
# https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html

spark = SparkSession \
    .builder \
    .master("local[2]") \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()
    
spark.conf.set("spark.sql.shuffle.partitions", 4)
    
# Create DataFrame representing the stream of input lines from connection to localhost:9999
lines = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 12345) \
    .load()

# Split the lines into words
words = lines.select(
   explode(
       split(lines.value, " ")
   ).alias("word")
)

# Generate running word count
wordCounts = words \
        .filter(col("word").like("@%")) \
        .groupBy("word").count() \
        .orderBy(col("count").desc())
        
print('isStreaming', wordCounts.isStreaming)

 # Start running the query that prints the running counts to the console

query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

print('await termination')    
query.awaitTermination()
