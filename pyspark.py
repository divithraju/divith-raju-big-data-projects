from pyspark.sql import SparkSession
spark=SparkSession.builder \
.appName('project')\
.getOrCreate()
df=spark.read.csv('hdfs://localhost:50000/sales', header= True, inferSchema=True)
df.show()
df.describe()
df.show(n=45)
df.printSchema()
df.count()
df.columns
df.select('_c1').show()
v=df.collect()[6]
print(v[2])
df.collect()[2]
n=df.withColumnRenamed('_c2','tryed')
n.show()
b=n.write.json('hdfs://localhost:50000/df')
h=spark.read.json('hdfs://localhost:50000/df')
h.show()
j=df.drop('_c3')
j.show()
from pyspark import SparkContext
d=([23,45,67,23],[67,78,34,24],[90,34,24,56],[34,67,23,56])
s=spark.createDataFrame(d)
s.show()
d=([23,45,67,23],[67,78,34,24],[90,34,24,56],[34,67,23,56])
columns=['df','gh','cv','sd']
rdd=sc.parallelize(d)
r=spark.createDataFrame(rdd, columns)
r.show()
max=df.select('_c1').collect()[0][0]
min=df.select('_c2').collect()[0][0]
avg=df.groupby('_c1').avg('_c2')
avg.show()
print(max)
print(min)
f=df.dropna()
f.show()
c=df.dropna(how='all')
c.show()
x=df.dropna(subset=['_c1'])
x.show()
a=df.fillna('unknown').fillna(0)
a.show()
n=df.replace({None: 'Don'})
n.show()
e=df.filter(df.salary.isNotNull())
j=spark.read.csv('hdfs://localhost:50000/tcs', header=True, inferSchema=True)
n=spark.read.csv('hdfs://localhost:50000/sales',header=True, inferSchema=True)
v=j.join(n ,how='inner')
b=j.join(n, how='outer') 
v.show()
b.show()
l=j.union(n)
l.show()
c=df.dropDuplicates()
c.show()
m=df.dropDuplicates(['friend'])
m.show()
from pyspark.sql.functions lit
addcol=df.withColumn('op', lit(45))
addcol.show()
l=df.withColumn('squared',df['_c1'] * df['_c2'])
l.show()
from pyspark.sql.functions import when
g=df.withColumn('hj',when(df['_c4'] == 'male', 90).when(df['_c4'] == 'female', 95).otherwise(None))
g.show()
print(' see you guys, we will meet on next  part ') 
