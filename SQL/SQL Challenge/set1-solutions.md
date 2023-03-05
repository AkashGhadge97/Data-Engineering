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
    FROM station ORDER BY CityName

Q.12  

	SELECt DISTINCT city FROM station WHERE city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u';
