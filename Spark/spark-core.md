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
        
## Assigning alias for column while selecting the data

        empDf.select(col("EMPLOYEE_ID").alias("EMP_ID"),col("FIRST_NAME").alias("F_NAME")).show()

## Create new column based on existing column

        empDf.select("EMPLOYEE_ID","FIRST_NAME","SALARY").withColumn("NEW_SALARY",col("SALARY") + 1000).show()

        empDf.withColumn("NEW_SALARY",col("SALARY") + 1000).select("EMPLOYEE_ID","FIRST_NAME","NEW_SALARY").show()

## Update Existing Column

        empDf.withColumn("SALARY",col("SALARY") - 1000).select("EMPLOYEE_ID","FIRST_NAME","SALARY").show()

## Renaming a column

        empDf.withColumnRenamed("SALARY","EMP_SALARY").show()

## Drop a column

        empDf.drop("COMMISSION_PCT").show()

## Filter Dataframe

        empDf.filter(col("SALARY") < 5000).show()
        
        empDf.filter(col("SALARY") < 5000).show(100)
        
        empDf.filter(col("SALARY") < 5000).select("EMPLOYEE_ID","FIRST_NAME","SALARY").show(100)

        empDf.filter((col("DEPARTMENT_ID") == 50) & (col("SALARY") < 5000)).select("EMPLOYEE_ID","FIRST_NAME","SALARY","DEPARTMENT_ID").show(100)
        
## Filter with SQL Like Syntax

        empDf.filter("DEPARTMENT_ID <> 50").select("EMPLOYEE_ID","FIRST_NAME","SALARY","DEPARTMENT_ID").show(100)

        empDf.filter("DEPARTMENT_ID != 50").select("EMPLOYEE_ID","FIRST_NAME","SALARY","DEPARTMENT_ID").show(100)

        empDf.filter("DEPARTMENT_ID == 50 and SALARY < 5000").select("EMPLOYEE_ID","FIRST_NAME","SALARY","DEPARTMENT_ID").show(100)

## Show distinct records from Dataframe

        empDf.distinct().show()

## Drop duplicates from dataframe

        empDf.dropDuplicates().show(100)

## Drop duplicates based of specific columns

        empDf.dropDuplicates(["DEPARTMENT_ID", "HIRE_DATE"]).show(100)
