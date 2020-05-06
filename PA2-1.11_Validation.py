#importing Libraries
from pyspark.sql import DataFrame
from pyspark import SparkContext, SQLContext
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassificationModel

#########################           Creating Spark Session                  ########################
spark = SparkSession.builder.master("local").appName("wineClasssification").config("spark.some.config.option","some-value").getOrCreate()

#########################           Reading Dataset                         ########################
#val_data = spark.read.csv('hdfs://ip-172-31-15-95.ec2.internal:8020/ValidationDataset.csv',header='true', inferSchema='true', sep=';')
val_data = spark.read.csv('TestDataset.csv',header='true', inferSchema='true', sep=';')
feature = [c for c in val_data.columns if c != 'quality']
assembler_v = VectorAssembler(inputCols=feature, outputCol="features")
val_tran = assembler_v.transform(val_data)
#val_tran.printSchema()    #remove comment to see scheama

#########################           Loading Model                         ############################
model= RandomForestClassificationModel.load("/meramodel")
#########################

#########################           Predicting                              ##########################
predictions = model.transform(val_tran)
#predictions.select("quality", "features").show(1000)##Value inside show this is just for printing number of value

#########################           Printing Accuracy                       ##########################
evaluator = MulticlassClassificationEvaluator(
    labelCol="quality", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("By calculating accuracy Test Error = %g" % (1.0 - accuracy))
transformed_data = model.transform(val_tran)
print(evaluator.getMetricName(), 'accuracy:', evaluator.evaluate(transformed_data))

#########################           F1 Score                                ##########################
evaluator1 = MulticlassClassificationEvaluator(labelCol="quality", predictionCol="prediction", metricName="f1")
accuracy = evaluator1.evaluate(predictions)
print("Test Error = %g with f1 score" % (1.0 - accuracy))
transformed_data = model.transform(val_tran)
print(evaluator1.getMetricName(), '::', evaluator1.evaluate(transformed_data))

