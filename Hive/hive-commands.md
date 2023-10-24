## Create Database 
	create database <database-name>

## Show Databases  
  	show databases;

## Create  Internal Table
	create table department_data (dept_id int,dept_name string,manager_id int,salary int) row format delimited fields   
	terminated by ',';

## Describe Table	
  	describe department_data;

## Describe Table in detail
  	describe formatted department_data;

## Loading data into internal table from local system - 

	load data inpath '<path>' into department_data; 

	load data inpath 'file://config/workspace/depart_data.csv' into department_data;  
	
## Loading data into internal table from HDFS - 

	load data '<hdfs_path>' into department_data; 

	load data inpath '/tmp/depart_data.csv' into department_data;  
	
## Show table data  

  	select *from  <table_name>

## To show table header set below property :

	set hive.cli.print.header=true

## Create External Table

	create external table department_data_external (dept_id int,dept_name string,manager_id int,salary int)
	row format delimited 
	fields terminated by ','
	location '/input_data/';
## Truncate Table
	trunacte table <table_name>
## Array Data Type 

	create table employee
	(
	id int,
	name string,
	skills array
	)
	row format delimited
	fields terminated by ','
	collection items terminated by ':';

	load data local inpath 'file:///config/workspace/array_data.csv' into table employee;

## Get element by index in hive array data type

	select id, name, skills[0] as prime_skill from employee;

## Array functions 

	select emp_id , emp_name ,
	size(emp_skills) as total_skills , 
	array_contains(emp_skills,"HADOOP") as knows_hadoop, 
	sort_array(emp_skills) as sorted_skills from employee;

## Map data type

	create table employee_map_data (id int , name string , details map<string,string>) 
	row format delimited 
	fields terminated by ','
	collection items terminated by '|' 
	map keys terminated by ':';

	select id ,name ,details['gender'] as employee_gender from employee_map_data;

 	select id ,name ,details['gender'] as employee_gender from employee_map_data;
  
## Create table from another table

	create table employee_backup as select * from employee;


## Create a table as CSV SerDe

	create table csv_table 
	(
	name string , 
	location string
	) 
	row format serde 'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
	with serdeproperties ( "separatorChar" = "," , "quoteChar"="\"", "escapeChar"= "\\") 
	stored as textfile 
	tblproperties("skip.header.line.count" = "1");


	load data local inpath 'file:///config/workspace/csv_file.csv' into table csv_table;
 
## Create JSON Table

	create table json_table
	( name string,
	id int,
	skills array
	)
	row format serde 'org.apache.hive.hcatalog.data.JsonSerDe'
	stored as textfile;

 	load data local inpath 'file:///config/workspace/json_file.json' into table json_table;

## Download hive catalog jar file , if serde libraries are not imported

	https://repo1.maven.org/maven2/org/apache/hive/hcatalog/hive-hcatalog-core/0.14.0/

## Run add jar command on hive shell

	add jar file:///config/workspace/hive-hcatalog-core-0.14.0.jar;

## Create a table which will store data in parquet

	create table sales_data_pq_final                                                                                   
	(                                                                   
	product_type string,                                                                                            
	total_sales int                                                                                                   
	)                                                                                                                           stored as parquet;  
    
## Load data in parquet file from another CSV 
	from sales_data_v2 insert overwrite table sales_data_pq_final select *;

## Create a table for sales data
	create table sales_order_data_csv_v1 ( ORDERNUMBER int, QUANTITYORDERED int, PRICEEACH float, ORDERLINENUMBER int, 
        SALES float, STATUS string, QTR_ID int, MONTH_ID int, YEAR_ID int, PRODUCTLINE string, MSRP int, PRODUCTCODE 
        string, PHONE string, CITY string, STATE string, POSTALCODE string, COUNTRY string, TERRITORY string, 
        CONTACTLASTNAME string, CONTACTFIRSTNAME string, DEALSIZE string ) row format delimited fields terminated by ',' 
        tblproperties("skip.header.line.count"="1") ;

	load data local inpath 'file:///home/hadoop/sales_order_data.csv' into table sales_order_data_csv_v1;
 
## Load data into table and store as ORC

	create table sales_order_data_orc ( ORDERNUMBER int, QUANTITYORDERED int, PRICEEACH float, ORDERLINENUMBER int, 	SALES float, STATUS string, QTR_ID int, MONTH_ID int, YEAR_ID int, PRODUCTLINE string, MSRP int, PRODUCTCODE 		string, PHONE string, CITY string, STATE string, POSTALCODE string, COUNTRY string, TERRITORY string, 			CONTACTLASTNAME string, CONTACTFIRSTNAME string, DEALSIZE string ) stored as orc;

	from sales_order_data_csv_v1 insert overwrite table sales_order_data_orc select *;

## Hive Properties to set specific number of reducers

	In order to change the average load for a reducer (in bytes):
		set hive.exec.reducers.bytes.per.reducer=
	In order to limit the maximum number of reducers:
		set hive.exec.reducers.max=
	In order to set a constant number of reducers:
		set mapreduce.job.reduces=

##  Set this property if doing static partition
set hive.mapred.mode=strict;

## Create table command for partition tables - for Static

create table sales_data_static_part                                                                                                     
    (                                                                                                                                       
    ORDERNUMBER int,                                                                                                                        
    QUANTITYORDERED int,                                                                                                                    
    SALES float,                                                                                                                            
    YEAR_ID int                                                                                                                             
    )                                                                                                                                       
    partitioned by (COUNTRY string); 
    
## Load data in static partition

	insert overwrite table sales_data_static_part partition(country = 'USA') select 	 
        ordernumber,quantityordered,sales,year_id from sales_order_data_orc where country = 'USA';

# Set this property for dynamic partioning
	set hive.exec.dynamic.partition.mode=nonstrict;   


# Create dynamic partion table
	create table sales_data_dynamic_part(
	    ORDERNUMBER int,
	    QUANTITYORDERED int,
	    SALES float,
	    YEAR_ID int)
	    partitioned by (COUNTRY string); 

# Load data in dynamic partition table

	insert overwrite table sales_data_dynamic_part partition(country) select 		 
        ordernumber,quantityordered,sales,year_id,country from sales_order_data_orc;
  

# Multilevel partition

	create table sales_data_dynamic_multilevel_part_v1(
		    ORDERNUMBER int,
		    QUANTITYORDERED int,
		    SALES float  
	    )
    	partitioned by (COUNTRY string, YEAR_ID int); 
    
# Load data in multilevel partitions

	insert overwrite table sales_data_dynamic_multilevel_part_v1 partition(country,year_id) select 	 
        ordernumber,quantityordered,sales,country,year_id from sales_order_data_orc;
