-- 1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, 
-- language and language percentage. Your query should arrange the result by language percentage in descending order.

select name, languages.language, languages.percentage
from countries
join languages on countries.id = languages.country_id
where languages.language = 'Slovene'
order by languages.percentage desc;

-- What query would you run to display the total number of cities for each country? 
-- Your query should return the name of the country and the total number of cities. 
-- Your query should arrange the result by the number of cities in descending order. 

select countries.name as Country_Name, count(cities.name) as Number_of_Cities
from countries
join cities on countries.id = cities.country_id
group by countries.name
order by Number_of_Cities desc;

-- What query would you run to get all the cities in Mexico with a population of greater than 500,000? 
-- Your query should arrange the result by population in descending order.

select cities.name, cities.population
from countries
join cities on countries.id = cities.country_id
where countries.name = 'Mexico' and
cities.population > 500000
order by cities.population desc;

-- What query would you run to get all languages in each country with a percentage greater than 89%? 
-- Your query should arrange the result by percentage in descending order. (1)

select countries.name, languages.language, languages.percentage
from countries
join languages on countries.id = languages.country_id
where languages.percentage > 89
order by languages.percentage desc;

-- What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? 
select countries.name, countries.surface_area, countries.population
from countries
where countries.surface_area < 501 and countries.population > 100000;

-- What query would you run to get countries with only Constitutional Monarchy 
-- with a capital greater than 200 and a life expectancy greater than 75 years?
select countries.name, countries.government_form, countries.capital, countries.life_expectancy
from countries
where countries.capital > 200 
and countries.government_form = 'Constitutional Monarchy'
and countries.life_expectancy > 75;

-- What query would you run to get all the cities of Argentina inside the Buenos Aires district
-- and have the population greater than 500, 000? 
-- The query should return the Country Name, City Name, District and Population
select countries.name, cities.name, cities.district, cities.population
from countries
join cities on countries.id = cities.country_id
where countries.name = 'Argentina' and
cities.district = 'Buenos Aires'
and cities.population > 500000;


-- What query would you run to summarize the number of countries in each region? 
-- The query should display the name of the region and the number of countries. 
-- Also, the query should arrange the result by the number of countries in descending order. 
select countries.region, count(countries.name) as NumberOfCountries
from countries
group by region
order by NumberOfCountries desc 


