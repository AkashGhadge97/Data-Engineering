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

## Read Data from HDFS Path - Read CSV

        df1 = spark.read.option("header",True).csv("/input_data/departments.csv")
        df1.show()

## Read data with options

        df2 = spark.read.option("header",True).option("inferSchema",True).csv("/input_data/departments.csv")
        df2.printSchema()

## Select All Data from dataframe

        empDf = spark.read.option("header",True).option("inferSchema",True).csv("/input_data/employees.csv")
        empDf.select("*").show()

## Ways to Select Specific Columns from Dataframe

        empDf.select("EMPLOYEE_ID","FIRST_NAME").show()
        
        empDf.select(empDf.EMPLOYEE_ID,empDf.FIRST_NAME).show()
        
        empDf.select(empDf["EMPLOYEE_ID"],empDf["FIRST_NAME"]).show()


        from pyspark.sql.functions import col
        empDf.select(col("EMPLOYEE_ID"),col("FIRST_NAME")).show()
