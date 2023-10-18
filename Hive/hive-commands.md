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
