-- 1. What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, 
-- email, and address.
SELECT city.city_id, city, first_name, last_name, email, address.address FROM customer
LEFT JOIN address ON customer.address_id = address.address_id
LEFT JOIN city ON address.city_id = city.city_id
WHERE city.city_id = 312;

-- 2. What query would you run to get all comedy films? Your query should return film title, description, release year, rating, 
-- special features, and genre (category).
SELECT film.film_id, title, description, release_year, rating, special_features, category.name AS "genre" FROM film
LEFT JOIN film_category ON film.film_id = film_category.film_id
LEFT JOIN category ON film_category.category_id = category.category_id
WHERE category.name = "Comedy";

-- 3. What query would you run to get all the films joined by actor_id=5? Your query should return the actor id, actor name, film title, description, and release year.
SELECT actor.actor_id, CONCAT_WS(" ", actor.first_name, actor.last_name) AS "name", film.film_id, film.title, film.description, film.release_year from actor
LEFT JOIN film_actor ON actor.actor_id = film_actor.actor_id
LEFT JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

-- 4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? 
-- Your query should return customer first name, last name, email, and address.
SELECT store.store_id, address.city_id, first_name, last_name, email, address.address FROM customer
LEFT JOIN store ON customer.store_id = store.store_id
LEFT JOIN address ON customer.address_id = address.address_id
WHERE store.store_id = 1 AND (city_id = 1 OR city_id = 42 OR city_id = 312 OR city_id = 459);

-- 5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", 
-- joined by actor_id = 15? Your query should return the film title, description, release year, rating, and special feature. 
-- Hint: You may use LIKE function in getting the 'behind the scenes' part.
SELECT title, description, release_year, rating, special_features FROM film
LEFT JOIN film_actor ON film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 15 AND rating = "G" AND special_features LIKE "%behind the scenes%"; 

-- 6. What query would you run to get all the actors that joined in the film_id = 369? Your query should return
--  the film_id, title, actor_id, and actor_name.
SELECT film.film_id, film.title, actor.actor_id, CONCAT_WS(" ", actor.first_name, actor.last_name) AS "actor_name" from actor
LEFT JOIN film_actor ON actor.actor_id = film_actor.actor_id
LEFT JOIN film ON film_actor.film_id = film.film_id
WHERE film.film_id = 369;

-- 7. What query would you run to get all drama films with a rental rate of 2.99? Your query should 
-- return film title, description, release year, rating, special features, and genre (category).
SELECT film.film_id, title, description, release_year, rating, special_features, category.name AS "genre", rental_rate FROM film
LEFT JOIN film_category ON film.film_id = film_category.film_id
LEFT JOIN category ON film_category.category_id = category.category_id
WHERE category.name = "drama" AND rental_rate = 2.99;

-- 8. What query would you run to get all the action films which are joined by SANDRA KILMER? Your query should 
-- return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.
SELECT actor.actor_id, CONCAT_WS(" ", actor.first_name, actor.last_name) AS name, film.film_id, film.title, description, release_year,
       rating, special_features, category.name AS "genre" FROM film
LEFT JOIN film_category ON film.film_id = film_category.film_id
LEFT JOIN category ON film_category.category_id = category.category_id
LEFT JOIN film_actor ON film.film_id = film_actor.film_id
LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 23 AND category.name = "action"; 



