-- 1 What query would you run to get the total revenue for March of 2012?
select sum(amount), monthname(charged_datetime) as month
from
billing
where monthname(charged_datetime) = 'March' and year(charged_datetime) = 2012
group by monthname(charged_datetime);

-- 2 What query would you run to get total revenue collected from the client with an id of 2?
select sum(amount), clients.client_id
from clients
join billing on clients.client_id = billing.client_id
where clients.client_id = 2
group by clients.client_id;

-- 3 What query would you run to get all the sites that client=10 owns?
select domain_name, client_id
from sites
where client_id = 10;

-- 4 What query would you run to get total # of sites created per month per year for the client with an id of 1? 
-- What about for client=20?
select sites.client_id, count(site_id) as 'Total sites created',  concat(monthname(created_datetime),' ', year(created_datetime)) as 'Month/Year'
from sites 
where sites.client_id = 1
group by year(created_datetime), month(created_datetime);


select sites.client_id, count(site_id) as 'Total sites created',  concat(monthname(created_datetime),' ', year(created_datetime)) as 'Month/Year'
from sites 
where sites.client_id = 20
group by year(created_datetime), month(created_datetime);

-- select count(site_id),  concat(monthname(charged_datetime),' ', year(charged_datetime)) as 'Month/Year'
-- from sites 
-- join billing on sites.client_id = billing.client_id
-- where sites.client_id = 1
-- group by year(charged_datetime), month(charged_datetime);

-- 5 What query would you run to get the total # of leads generated for each of the sites --REVISIT
-- between January 1, 2011 to February 15, 2011?
select count(leads.leads_id), sites.domain_name, leads.registered_datetime
from leads
join sites on leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15'
group by sites.domain_name;


-- alternate answer
SELECT sites.domain_name, COUNT(leads.leads_id) AS num_leads, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS date_registered
FROM sites
	left JOIN leads ON sites.site_id = leads.site_id -- left???
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15'
GROUP BY sites.site_id;


-- 6 What query would you run to get a list of client names and the total # of leads we've generated 
-- for each of our clients between January 1, 2011 to December 31, 2011?
select concat(clients.first_name,' ', clients.last_name) as Name , count(leads.leads_id) as 'Number of Leads'
from clients
join sites on clients.client_id = sites.client_id
join leads on sites.site_id = leads.site_id
where year(leads.registered_datetime) = 2011
group by clients.client_id;

-- alternate
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS num_leads
FROM clients
	LEFT JOIN sites ON clients.client_id = sites.client_id
    JOIN leads ON sites.site_id = leads.site_id -- no left join here
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY clients.client_id;

-- 7 What query would you run to get a list of client names and the total # of leads we've generated for each client each month 
-- between months 1 - 6 of Year 2011?
-- why wouldn't this use group by clients.client_id
select concat(clients.first_name, ' ', clients.last_name) as Name, count(leads.leads_id) as 'Number of Leads', monthname(leads.registered_datetime) as Month
from clients
join sites on clients.client_id = sites.client_id
join leads on sites.site_id = leads.site_id
where year(leads.registered_datetime) = 2011
and month(leads.registered_datetime) between 1 and 6
-- group by leads.site_id
group by leads.site_id
order by month(leads.registered_datetime);

-- 8 What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites 
-- between January 1, 2011 to December 31, 2011? Order this query by client id.  

select concat(clients.first_name, ' ', clients.last_name) as Name, sites.domain_name, count(leads.leads_id) as 'Number of Leads', 
concat(date_format(leads.registered_datetime,"%M %e"),', ',date_format(leads.registered_datetime,"%Y")) as 'Date Generated'
from clients
join sites on clients.client_id = sites.client_id
join leads on sites.site_id = leads.site_id
where year(leads.registered_datetime) = 2011
-- and month(leads.registered_datetime) between 1 and 6
-- group by leads.site_id
group by leads.site_id
order by clients.client_id;

-- 8b --double check this
-- 8b Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated 
-- from each site for all time.
select concat(clients.first_name, ' ', clients.last_name) as Name, sites.domain_name, count(leads.leads_id) as 'Number of Leads'-- , 
-- concat(date_format(leads.registered_datetime,"%M %e"),', ',date_format(leads.registered_datetime,"%Y")) as 'Date Generated'
from clients
join sites on clients.client_id = sites.client_id
join leads on sites.site_id = leads.site_id
 group by sites.site_id
-- group by leads.site_id
order by clients.client_id;

-- answer  -- even if a site had 0 leads, it would still show in the query. left is sites, right is leads.
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS num_leads
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
    LEFT JOIN leads ON sites.site_id = leads.site_id
GROUP BY clients.client_id, sites.domain_name;



-- 9 Write a single query that retrieves total revenue collected from each client for each month of the year. 
-- Order it by client id.
select concat(clients.first_name, ' ', clients.last_name) as Name, billing.client_id, sum(amount), 
monthname(billing.charged_datetime), year(billing.charged_datetime)
from clients
join billing on clients.client_id = billing.client_id 
group by clients.client_id, monthname(billing.charged_datetime), year(billing.charged_datetime)
order by clients.client_id, year(billing.charged_datetime);

-- answer
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, SUM(billing.amount) AS monthly_revenue, 
DATE_FORMAT(billing.charged_datetime, '%M') AS 'month', DATE_FORMAT(billing.charged_datetime, '%Y') AS 'year'
FROM clients
	LEFT JOIN billing ON clients.client_id = billing.client_id
GROUP BY client_name, MONTH(billing.charged_datetime), YEAR(billing.charged_datetime)
ORDER BY clients.client_id;

-- Write a single query that retrieves all the sites that each client owns.
-- Group the results so that each row shows a new client. 
-- It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. 
-- (HINT: use GROUP_CONCAT)
select CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, group_concat(' ',sites.domain_name)
from clients
join sites on clients.client_id = sites.client_id
group by client_name;
-- group by clients.client_id

-- answer
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, GROUP_CONCAT(sites.domain_name) AS 'sites'
FROM clients
	LEFT JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id;