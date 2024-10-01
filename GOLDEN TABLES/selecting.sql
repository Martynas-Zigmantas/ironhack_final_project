USE Flights;

# SELECT EVERYTHING THAT I NEED FOR TABLEAU
# ARRIVALS

CREATE VIEW arrivals AS
SELECT
    a.departure_city,
    a.destination_city,
    a.country,
    a.date_arrive,
    a.arrival_time_difference,
    a.arrival_status,
    a.airline,
    COALESCE(al.airline_type, 'unknown') AS airline_type
FROM
    (
        SELECT
            departure_city,
            destination_city,
            country,
            date_arrive,
            arrival_time_difference,
            arrival_status,
            airline
        FROM berlin_arrivals
        UNION ALL
        SELECT
            departure_city,
            destination_city,
            country,
            date_arrive,
            arrive_time_difference AS arrival_time_difference,
            arrival_status,
            airline
        FROM lisbon_arrivals
        UNION ALL
        SELECT
            departure_city,
            destination_city,
            country,
            date_arrive,
            arrival_time_difference,
            arrival_status,
            airline
        FROM heathrow_arrivals
    ) AS a
LEFT JOIN airlines_list AS al
ON a.airline = al.airline;


# SELECT EVERYTHING THAT I NEED FOR TABLEAU
# DEPARTURES

CREATE VIEW departures AS
SELECT
    d.departure_city,
    d.destination_city,
    d.country,
    d.date_depart,
    d.departure_time_difference,
    d.departure_status,
    d.airline,
    COALESCE(a.airline_type, 'unknown') AS airline_type  -- Use COALESCE to handle NULLs if needed
FROM
    (
        SELECT
            departure_city,
            destination_city,
            country,
            date_depart,
            departure_time_difference,
            departure_status,
            airline
        FROM berlin_departures
        UNION ALL
        SELECT
            departure_city,
            destination_city,
            country,
            date_depart,
            departure_time_difference,
            departure_status,
            airline
        FROM lisbon_departures
        UNION ALL
        SELECT
            departure_city,
            destination_city,
            country,
            date_depart,
            departure_time_difference,
            departure_status,
            airline
        FROM heathrow_departures
    ) AS d
LEFT JOIN airlines_list AS a
ON d.airline = a.airline;

SELECT * FROM arrivals;




# SELECT TOTAL FLIGHTS

SELECT 
    departure_city, 
    destination_city, 
    country, 
    date_depart AS date,
    departure_time_difference AS time_difference,
    departure_status AS status,
    airline,
    airline_type                      -- Include airline_type from berlin_departures
FROM departures

UNION ALL

SELECT 
    departure_city, 
    destination_city, 
    country, 
    date_arrive AS date,
    arrival_time_difference AS time_difference,
    arrival_status AS status,
    airline,
    airline_type
FROM arrivals;
