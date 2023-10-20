## SQL Challenge Set-1 Solution

Q.1    
       
       SELECT *FROM city WHERE countrycode = 'USA' AND population > 100000;

Q.2    
       
       SELECT name FROM  city WHERE countrycode = 'USA' AND population > 120000;

Q.3    
       
       SELECT *FROM CITY;

Q.4    
       
       SELECT *FROM CITY WHERE ID = 1661

Q.5    
       
       SELECT *FROM CITY WHERE COUNTRYCODE = 'JPN'

Q.6    
       
       SELECT NAME FROM CITY WHERE COUNTRYCODE = 'JPN'

Q.7    
       
       SELECT city,state FROM station;

       SELECT GROUP_CONCAT(city) as Cities , GROUP_CONCAT(state) as States from station
       
Q.8    
       
       SELECT DISTINCT
                     CASE WHEN (ID % 2 = 0) THEN city
                     END as city_name
       FROM station 
       
Q.9

       SELECT COUNT(city) -COUNT(DISTINCT city) as CityNumDiff FROM station
       
Q.10

       select city, length(city) from station where length(city) = (select min(length(city)) from station ) order by city limit 1;
       
       select city, length(city) from station where length(city) = (select max(length(city)) from station ) order by city limit 1;
       
Q.11  
       
       SELECT DISTINCT 
	CASE WHEN (city like 'a%') THEN city
         WHEN (city like 'e%') THEN city
         WHEN (city like 'i%') THEN city
         WHEN (city like 'o%') THEN city
         WHEN (city like 'u%') THEN city
	END as CityName
    FROM station ORDER BY CityName;
    
    SELECT DISTINCT city FROM station 
    WHERE city LIKE 'a%' OR 
          city LIKE 'e%' OR 
	  city LIKE 'i%' OR 
	  city LIKE 'o%' OR 
	  city LIKE 'u%' 
    ORDER BY city;

Q.12  

	SELECT DISTINCT city FROM station WHERE city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u';
	
Q.13

	SELECT DISTINCT city FROM station WHERE city NOT IN (SELECT DISTINCT city FROM station 
	WHERE 	city LIKE 'a%' OR 
	  	city LIKE 'e%' OR 
      		city LIKE 'i%' OR 
      		city LIKE 'o%' OR 
      		city LIKE 'u%' 
	) ORDER BY city;
	
Q.14

	SELECT DISTINCT city FROM station WHERE city NOT IN (SELECT DISTINCT city FROM station 
	WHERE city LIKE '%a' OR 
		  city LIKE '%e' OR 
	      city LIKE '%i' OR 
	      city LIKE '%o' OR 
	      city LIKE '%u' 
	) ORDER BY city;

Q.15 

	SELECT DISTINCT city FROM station WHERE
	city NOT IN ( SELECT DISTINCT city FROM station 
	WHERE city LIKE 'a%' OR 
		  city LIKE 'e%' OR 
	      city LIKE 'i%' OR 
	      city LIKE 'o%' OR 
	      city LIKE 'u%' )
	OR
	city NOT IN (SELECT DISTINCT city FROM station 
	WHERE city LIKE '%a' OR 
		  city LIKE '%e' OR 
	      city LIKE '%i' OR 
	      city LIKE '%o' OR 
	      city LIKE '%u')
	    
Q.16  

	SELECT DISTINCT city FROM station WHERE
	city NOT IN ( SELECT DISTINCT city FROM station 
	WHERE city LIKE 'a%' OR 
		  city LIKE 'e%' OR 
	      city LIKE 'i%' OR 
	      city LIKE 'o%' OR 
	      city LIKE 'u%' )
	AND
	city NOT IN (SELECT DISTINCT city FROM station 
	WHERE city LIKE '%a' OR 
		  city LIKE '%e' OR 
	      city LIKE '%i' OR 
	      city LIKE '%o' OR 
	      city LIKE '%u')
	      
Q.17

	select p.product_id, p.product_name 
	from product p join sales s on s.product_id = p.product_id 
	where (s.sale_date >= '2019-01-01' and s.sale_date <= '2019-03-31') and 
	s.product_id not in ( select product_id from sales where sale_date > '2019-03-31')

 Q.18
 
 	select distinct author_id from views where author_id = viewer_id

	
