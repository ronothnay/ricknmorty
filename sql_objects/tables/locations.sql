CREATE TABLE IF NOT EXISTS storefirst.seasons
(
    location_id character(50) NOT NULL,
    name character(50) NOT NULL,
    type character(50) NOT NULL,
    dimension character(50) NOT NULL,
    insertion_time date NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (location_id)
);
