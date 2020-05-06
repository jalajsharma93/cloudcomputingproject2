#importing Libraries
from pyspark.sql import DataFrame
from pyspark import SparkContext, SQLContext
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SparkSession
from pyspark.ml.feature import Imputer
from pyspark.sql.functions import when
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler

#########################           Creating Spark Session                  ########################
spark = SparkSession.builder.master("local").appName("wineClasssification").config("spark.some.config.option","some-value").getOrCreate()

#########################           Reading Dataset                         ########################
                                       #Training Dataset
#raw_data = spark.read.csv('hdfs://ip-172-31-15-95.ec2.internal:8020/Training.csv',header='true', inferSchema='true', sep=';')
raw_data = spark.read.csv('hdfs://ip-172-31-15-95.ec2.internal:8020/TrainingDataset.csv',header='true', inferSchema='true', sep=';')

#raw_data = spark.read.csv('hdfs://ip-172-31-15-95.ec2.internal:8020/TrainingDataset.csv',header='true', inferSchema='true', sep=';')
#########################           Describe                                #########################


#########################           Creating Feature column                 #########################


featureColumns = [c for c in raw_data.columns if c != 'quality']
assembler = VectorAssembler(inputCols=featureColumns, outputCol="features")
input_trans = assembler.transform(raw_data)
input_trans.cache()
#input_trans.printSchema() #remove comment to see scheama

#########################           creating Model with Random Forest       ###########################
from pyspark.ml.classification import RandomForestClassifier
random_forest = RandomForestClassifier(labelCol="quality", featuresCol="features", numTrees=10)
model = random_forest.fit(input_trans)
model.write().overwrite().save("meramodel")

print("Sucessfully Trained")

