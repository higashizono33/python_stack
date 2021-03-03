-- 1. What query would you run to get the total revenue for March of 2012?
SELECT MONTHNAME(charged_datetime) AS "month", SUM(amount) AS "revenue" FROM billing WHERE charged_datetime >= '2012/3/1' AND charged_datetime <= '2012/3/31'; 

-- 2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT client_id, SUM(amount) FROM billing WHERE client_id = 2;

-- 3. What query would you run to get all the sites that client=10 owns?
SELECT domain_name, client_id FROM sites WHERE client_id = 10;

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?
SELECT client_id, COUNT(*) AS "number_of_website", MONTHNAME(created_datetime) AS "month", YEAR(created_datetime) AS "year" FROM sites WHERE client_id = 1 GROUP BY MONTH(created_datetime), YEAR(created_datetime);
SELECT client_id, COUNT(*) AS "number_of_website", MONTHNAME(created_datetime) AS "month", YEAR(created_datetime) AS "year" FROM sites WHERE client_id = 20 GROUP BY MONTH(created_datetime), YEAR(created_datetime);

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT sites.domain_name, COUNT(*), DATE_FORMAT(registered_datetime, "%M %d, %Y") FROM leads 
LEFT JOIN sites ON leads.site_id = sites.site_id
WHERE registered_datetime >= '2011/1/1' AND registered_datetime <= '2011/2/15'
GROUP BY sites.domain_name;


-- 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients 
-- between January 1, 2011 to December 31, 2011?
SELECT CONCAT(clients.first_name, " ", clients.last_name) AS "name", COUNT(*) AS "total # of leads" from clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE registered_datetime >= '2011/1/1' AND registered_datetime <= '2011/12/31'
GROUP BY clients.client_id;

-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client 
-- each month between months 1 - 6 of Year 2011?
SELECT CONCAT(clients.first_name, " ", clients.last_name) AS "name", COUNT(leads.leads_id) AS "number_of_leads", MONTHNAME(registered_datetime) 
	   AS "month" from clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE registered_datetime >= '2011/1/1' AND registered_datetime <= '2011/6/30'
GROUP BY clients.client_id, registered_datetime;

-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites 
-- between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, 
-- the site name(s), and the total number of leads generated from each site for all time.
SELECT CONCAT(clients.first_name, " ", clients.last_name) AS "name", sites.domain_name, COUNT(*) AS "total # of leads", 
	   DATE_FORMAT(registered_datetime, "%M %d, %Y") AS "date_generated" from clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE registered_datetime >= '2011/1/1' AND registered_datetime <= '2011/12/31'
GROUP BY sites.domain_name
ORDER BY clients.client_id ASC;

SELECT CONCAT(clients.first_name, " ", clients.last_name) AS "name", sites.domain_name, COUNT(*) AS "number_of_leads" from clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
GROUP BY sites.domain_name
ORDER BY clients.client_id, number_of_leads DESC;

-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.
SELECT CONCAT(clients.first_name, " ", clients.last_name) AS "name", SUM(amount) AS "total_revenue", MONTHNAME(charged_datetime) AS "month", 
	   YEAR(charged_datetime) AS "year" from clients
LEFT JOIN billing ON clients.client_id = billing.client_id
GROUP BY charged_datetime
ORDER BY clients.client_id, charged_datetime;

-- 10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. 
-- It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)
SELECT CONCAT(clients.first_name, " ", clients.last_name) AS "name", GROUP_CONCAT(DISTINCT sites.domain_name SEPARATOR " / ") AS "sites" from clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
GROUP BY name
ORDER BY clients.client_id ASC;