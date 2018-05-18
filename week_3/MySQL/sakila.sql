-- 1. What query would you run to get all the customers inside city_id = 312?
-- Your query should return customer first name, last name, email, and address.
select customer.first_name, customer.last_name, customer.email, address.address
from customer
join city on customer.customer_id = city.city_id
join address on customer.customer_id = address.address_id
where city.city_id = 312;
-- 2. What query would you run to get all comedy films? Your query should return film title,
-- description, release year, rating, special features, and genre (category).
select film.title, film.description, film.release_year, film.rating, film.special_features, category.name from film_category
join category on film_category.category_id = category.category_id
join film on film_category.film_id = film.film_id
where category.name = 'Comedy';
-- 3. What query would you run to get all the films joined by actor_id=5?
-- Your query should return the actor id, actor name, film title, description, and release year.
select film_actor.actor_id, concat(actor.first_name, ' ', actor.last_name), film.title, film.description, film.release_year from film_actor
join actor on film_actor.actor_id = actor.actor_id
join film on film_actor.film_id = film.film_id
where film_actor.actor_id = 5;

-- 4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)?
-- Your query should return customer first name, last name, email, and address.
select customer.first_name, customer.last_name, customer.email, address.address
from customer
join address on customer.customer_id = address.address_id
join city on customer.customer_id = city.city_id
where customer.store_id = 1 and city.city_id in (1, 42, 312, 459);
-- 5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes",
-- joined by actor_id = 15? Your query should return the film title, description, release year, rating, and special feature.
-- Hint: You may use LIKE function in getting the 'behind the scenes' part.
select film.title, film.description, film.release_year, film.rating, film.special_features from film_actor
join film on film_actor.film_id = film.film_id
join actor on film_actor.actor_id = actor.actor_id
where film_actor.actor_id = 15 and film.rating = 'G' and film.special_features like '%Behind the scenes%';

-- 6. What query would you run to get all the actors that joined in the film_id = 369?
-- Your query should return the film_id, title, actor_id, and actor_name.
select film_actor.film_id, film.title, film_actor.actor_id, concat(actor.first_name, ' ', actor.last_name) from film_actor
join film on film_actor.film_id = film.film_id
join actor on film_actor.actor_id = actor.actor_id
where film_actor.film_id = 369;

-- 7. What query would you run to get all drama films with a rental rate of 2.99?
-- Your query should return film title, description, release year, rating, special features, and genre (category).
select film.title, film.description, film.release_year, film.rating, film.special_features, category.name from film_category
join category on film_category.category_id = category.category_id
join film on film_category.film_id = film.film_id
where film.rental_rate = 2.99;
-- 8. What query would you run to get all the action films which are joined by SANDRA KILMER? Your query should return film title,
-- description, release year, rating, special features, genre (category), and actor's first name and last name.
select film.title, film.description, film.release_year, film.rating, film.special_features, category.name, concat(actor.first_name, ' ', actor.last_name) 
from actor
join category on film_category.category_id = category.category_id
join film on film_category.film_id = film.film_id
join film on film_actor.film_id = film.film_id
join actor on film_actor.actor_id = actor.actor_id
where actor.first_name = 'SANDRA' and actor.last_name = 'KILMER' and  category.name = 'Action';



