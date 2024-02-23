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

Q.23 


	with result_cte as (
		select *, (units*unit_price) as total_price from (select  u.product_id,u.units,
		CASE WHEN (u.purchase_date >= p.start_date and u.purchase_date <= p.end_date) THEN p.price end as unit_price
		from unitsold u join prices p on u.product_id = p.product_id) d_table where unit_price is not null 
	),
	final_cte as (
		select distinct product_id , sum(units) over(partition by product_id) as total_units,
		sum(total_price) over (partition by product_id) as total_price_sum from result_cte
	)
	select product_id , round((total_price_sum/total_units),2) as average_price from final_cte

Q.24

	select player_id , event_date as first_login
	from (select *, rank() over (partition by player_id order by event_date) as login_rank from activity) as t
	where login_rank = 1

Q.25 

	select player_id , device_id
	from (select *, rank() over (partition by player_id order by event_date) as device_rank from activity) as t
	where device_rank = 1;

Q.26

	select distinct *from (select p.product_name, sum(o.unit) over (partition by o.product_id order by o.unit) as unit
        from orders o join products p on o.product_id = p.product_id  where o.order_date >= '2020-02-01' and o.order_date<= '2020-02-28')  t where unit >= 100

Q.27

	select *from users where mail REGEXP '^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode\\.com$'
Q.28 

	with derived_data_one as (
		select 
			c.customer_id,
	    		c.name,
	    		CASE 
				WHEN month(o.order_date) = 6 THEN (p.price*o.quantity)
			END as june_spent,
	    	 	CASE 
				WHEN month(o.order_date) = 7 THEN (p.price*o.quantity)
			END as july_spent
	    	from customers c join orders o on o.customer_id = c.customer_id join product p on o.product_id = p.product_id where o.order_date 
	),
	derived_data_two as 
	(
		select  distinct customer_id, 
				 name, 
		   		 sum(june_spent) over (partition by customer_id, name) as june_total_spent,
		                 sum(july_spent) over (partition by customer_id, name) as july_total_spent
	 from derived_data_one
	)
       select customer_id , name from derived_data_two  where june_total_spent >= 100 and july_total_spent >=100

 Q.29
 
	select c.title from content c join tvprogram t 
	on c.content_id = t.content_id where month(t.program_date) = 6 and c.kids_content = 'Y'
