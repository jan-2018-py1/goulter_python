-- What query would you run to get all the customers inside city_id = 312? 
-- Your query should return customer first name, last name, email, and address.

select customer.first_name, customer.last_name, customer.email, address.address, address.district, address.city_id, address.postal_code
from customer
join address on customer.address_id = address.address_id
where address.city_id = 312;

-- What query would you run to get all comedy films? 
-- Your query should return film title, description, release year, rating, special features, and genre (category).
-- comedy is category_id 5
select film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre
from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where category.name = 'comedy';

-- What query would you run to get all the films joined by actor_id=5? 
-- Your query should return the actor id, actor name, film title, description, and release year.
select actor. actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year
from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
where actor.actor_id= 5;

-- What query would you run to get all the customers in store_id = 1 
-- and inside these cities (1, 42, 312 and 459)? 
-- Your query should return customer first name, last name, email, and address.
select customer.first_name, customer.last_name, customer.email, address.address, city.city, address.district, address.postal_code
from customer
join store on customer.store_id = store.store_id
join address on customer.address_id = address.address_id
join city on address.city_id = city.city_id
where store.store_id = 1
and (city.city_id = 1 or city.city_id = 42 or city.city_id = 312 or city.city_id = 459);

-- What query would you run to get all the films with a "rating = G" 
-- and "special feature = behind the scenes", 
-- joined by actor_id = 15? 
-- Your query should return the film title, description, release year, rating, and special feature. 
-- Hint: You may use LIKE function in getting the 'behind the scenes' part.
select film.title, film.description, film.release_year, film.rating, film.special_features
from film
join film_actor on film.film_id = film_actor.film_id
where film_actor.actor_id = 15
and film.rating = 'G'
and film.special_features Like '%behind the scenes%';

-- What query would you run to get all the actors that joined in the film_id = 369? 
-- Your query should return the film_id, title, actor_id, and actor_name.
select film.film_id, film.title, film_actor.actor_id, actor.first_name, actor.last_name
from actor
join film_actor on actor.actor_id = film_actor.actor_id
join film on film_actor.film_id = film.film_id
where film.film_id = 369;

-- What query would you run to get all drama films with a rental rate of 2.99? 
-- Your query should return film title, description, release year, rating, special features, and genre (category).
select film.title, film.description, film.release_year, film.special_features, category.name as genre, film.rental_rate
from film 
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where film.rental_rate = 2.99
and category.name = 'drama';

-- What query would you run to get all the action films which are joined by SANDRA KILMER? 
-- Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.
select film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre, actor.first_name, actor.last_name
from film 
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where actor.first_name = 'sandra' and actor.last_name = 'kilmer'
and category.name = 'action'


