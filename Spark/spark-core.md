# Spark Shell Commands

## Import resuiqres functions to create schema and for data types

        from pyspark.sql.types import StructType,StructField, StringType, IntegerType

## Define Data

        person_list = [("Berry","","Allen",1,"M"),
        ("Oliver","Queen","",2,"M"),
        ("Robert","","Williams",3,"M"),
        ("Tony","","Stark",4,"F"),
        ("Rajiv","Mary","Kumar",5,"F")
    ]

## Define Schema 

        schema = StructType([ 
        StructField("firstname",StringType(),True), 
        StructField("middlename",StringType(),True), 
        StructField("lastname",StringType(),True), 
        StructField("id", IntegerType(), True), 
        StructField("gender", StringType(), True), 
      
    ])

## Create Dataframe from defines schema

        df = spark.createDataFrame(data=person_list,schema=schema)

## Print Schema of Dataframe

        df.printSchema()

## Print Datafranme

        df.show(truncate=False)
