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

---

## Aggregation Functions

### Count
                empDf.count()

                empDf.select(count("salary")).show()

                empDf.select(count("salary").alias("TOTAL_COUNT")).show()

### Max

        empDf.select(max("salary").alias("MAX_SALARY")).show()

### Min

        empDf.select(min("salary").alias("MIN_SALARY")).show()

### Avg

        empDf.select(avg("salary").alias("AVG_SALARY")).show()

### Sum

        empDf.select(sum("salary").alias("SUM_SALARY")).show()

---

## Order By Clause

        empDf.orderBy("SALARY").show()
        
        empDf.orderBy("SALARY").select("EMPLOYEE_ID","SALARY").show()

        empDf.select("EMPLOYEE_ID","SALARY").orderBy("SALARY").show()

### Order by in ascending order

        empDf.select("EMPLOYEE_ID","SALARY").orderBy(col("SALARY").asc()).show()

### Order by in descending order

        empDf.select("EMPLOYEE_ID","SALARY").orderBy(col("SALARY").desc()).show()

        empDf.select("EMPLOYEE_ID","DEPARTMENT_ID","SALARY").orderBy(col("DEPARTMENT_ID").asc(),col("SALARY").desc()).show()

---
## Group By Clause

        empDf.groupBy("DEPARTMENT_ID").sum("SALARY").show() 

        empDf.groupBy("DEPARTMENT_ID").max("SALARY").show() 

        empDf.groupBy("DEPARTMENT_ID").min("SALARY").show() 

        empDf.groupBy("DEPARTMENT_ID").avg("SALARY").show() 

### Group By with multiple columns

        empDf.groupBy("DEPARTMENT_ID","JOB_ID").sum("SALARY").show()   

        empDf.groupBy("DEPARTMENT_ID","JOB_ID").sum("SALARY","EMPLOYEE_ID").show()  

### Group by using aggregate (agg) function

        empDf.groupBy("DEPARTMENT_ID").agg(sum("SALARY").alias("SUM_SALARY"),max("SALARY").alias("MAX_SALARY")).show()

                        empDf.groupBy("DEPARTMENT_ID").agg(sum("SALARY").alias("SUM_SALARY"),max("SALARY").alias("MAX_SALARY"),min("SALARY").alias("MIN_SALARY"),avg("SALARY").alias("AVG_SALARY")).show()

### Group by with where clause

         empDf.groupBy("DEPARTMENT_ID").agg(max("SALARY").alias("MAX_SALARY")).where(col("MAX_SALARY")>=10000).show()

### When Otherwise (Like Case when in SQL)


        df = empDf.withColumn("EMPLOYEE_GRADE", when( col("SALARY") > 15000, "GRADE-1" ).when( (col("SALARY") >=10000)  & (col("SALARY") <15000), "GRADE-2"  ).otherwise("GRADE-3") )

## Converting Spark DataFrame to SQL Table and use SQL Queries

        empDf.createOrReplaceTempView("employee")
        
        spark.sql(" select * from employee limit 5").show()
        
        df = spark.sql(" select employee_id,salary from employee")
        df.show(100)
        
        spark.sql("select department_id, sum(salary) as sum_salary from employee group by department_id").show()
        
        spark.sql("select employee_id, department_id, rank() over(partition by department_id order by salary desc) as 
        rank_salary from employee").show()

## Joins in Spark

### Inner Join

        empDf.join(deptDf, empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "inner").show()

        empDf.join(deptDf, empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "inner").select(empDf.EMPLOYEE_ID,                 
        empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME).show()

### Left Join

        empDf.join(deptDf, empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "left").select(empDf.EMPLOYEE_ID, 
        empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME).show(100)

### Right Join

        empDf.join(deptDf, empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "right").select(empDf.EMPLOYEE_ID, 
        empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME).show(100)

### Full Outer Join 

        empDf.join(deptDf, empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID, "fullouter").select(empDf.EMPLOYEE_ID, 
        empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME).show(100)

### Self Join Using inner Join

        empDf.alias("emp1").join(empDf.alias("emp2") , col("emp1.manager_id") == col("emp2.employee_id"), 
      "inner").select(col("emp1.manager_id"), col("emp2.first_name"), col("emp2.last_name")).dropDuplicates().show(100)


      empDf.join(deptDf, (empDf.DEPARTMENT_ID == deptDf.DEPARTMENT_ID) & (deptDf.LOCATION_ID == 1700), 
      "inner").select(empDf.EMPLOYEE_ID, empDf.DEPARTMENT_ID, deptDf.DEPARTMENT_NAME).show()

## User Defined Functions in Spark

### Method-1

        >>> def upperCase(in_str):
        ...     out_str = in_str.upper()
        ...     return out_str
        ... 
        >>> print(upperCase("hello"))
        HELLO
        >>> upperCaseUDF = udf(lambda z : upperCase(z) , StringType())
        >>> empDf.select(col("EMPLOYEE_ID") , col("FIRST_NAME"), col("LAST_NAME"), upperCaseUDF(col("FIRST_NAME")), 
            upperCaseUDF(col("LAST_NAME"))).show()

### Method-2

        >>> @udf(returnType=StringType())
        ... def upperCaseNew(in_str):
        ...     out_str = in_str.upper()
        ...     return out_str
        ... 
        >>> empDf.select(col("EMPLOYEE_ID") , col("FIRST_NAME"), col("LAST_NAME"), upperCaseNew(col("FIRST_NAME")), 
            upperCaseNew(col("LAST_NAME"))).show()


## Window Functions

        from pyspark.sql.window import Window

        windowSpec = Window.partitionBy("DEPARTMENT_ID").orderBy("SALARY")

        empDf.withColumn("salary_rank", rank().over(windowSpec)).select("DEPARTMENT_ID","SALARY","salary_rank").show(100)
---
        windowSpec = Window.partitionBy("DEPARTMENT_ID").orderBy(col("SALARY").desc())

        empDf.withColumn("salary_rank", rank().over(windowSpec)).select("DEPARTMENT_ID","SALARY","salary_rank").show(100)
---
        windowSpec = Window.partitionBy("DEPARTMENT_ID").orderBy(col("SALARY").desc())

        empDf.withColumn("SUM", sum("SALARY").over(windowSpec)).select("DEPARTMENT_ID","SALARY","SUM").show(100)
---
        windowSpec = Window.partitionBy("DEPARTMENT_ID")

        empDf.withColumn("SUM", sum("SALARY").over(windowSpec)).select("DEPARTMENT_ID","SALARY","SUM").show(100)

        

