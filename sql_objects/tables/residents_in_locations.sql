CREATE TABLE IF NOT EXISTS storefirst.residents_in_locations
(
    location_id character(50) NOT NULL,
    character_id character(50) NOT NULL,
    insertion_time date NOT NULL DEFAULT CURRENT_DATE
);
