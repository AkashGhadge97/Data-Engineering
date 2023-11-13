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

Q.19

	select round(((select count(*) from delivery where order_date = customer_pref_delivery_date)/ count(*)) * 100,2) as 	immediate_percentage from delivery;

 Q.20 

 	WITH clicks_views as (select t1.ad_id , t1.total_clicks , t2.total_views from 
	(select ad_id , count(action) as total_clicks from ads where action = 'Clicked' group by ad_id) t1 join
	(select ad_id , count(action) as total_views from ads where action = 'Viewed' group by ad_id) t2 where t1.ad_id = 	t2.ad_id)
	
	select distinct a.ad_id , 
	coalesce(round(c.total_clicks/(c.total_clicks + c. total_views)*100,2),0) as CTR
	from ads a left join clicks_views c on a.ad_id = c.ad_id

Q.21

	select employee_id,  count(team_id) over (partition by team_id ) as team_size from employee_data order by 
        employee_id

 Q.22

	 with weather_cte as (
		select c.country_name as cname , w.country_id as cid ,w.weather_state cws ,w.day, 
		sum(weather_state) over (partition by w.country_id) as weather_sum,
	         count(weather_state) over (partition by w.country_id) as country_count 
		from weather w left join countries c on w.country_id = c.country_id 
		where w.day >= '2019-11-01' and w.day <= '2019-11-30'
	),
	result_cte as (
	        select  distinct weather_cte.cname as country_name , (weather_cte.weather_sum/weather_cte.country_count) as 
                avg_weather from weather_cte
	)
	
	select country_name ,
	 CASE WHEN ( avg_weather <= 15) THEN "Cold"
		  WHEN (avg_weather >= 25) THEN "Hot"
	      ELSE "Warm" END as weather_type from result_cte
