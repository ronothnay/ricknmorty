CREATE TABLE storefirst.characters
(
    character_id character(50) NOT NULL,
    first_name character(50),
    last_name character(50),
    full_name character(50) NOT NULL,
    species character(50) NOT NULL,
    type character(50) NOT NULL,
    gender character(50) NOT NULL,
    origin character(50) NOT NULL,
    insertion_time date NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (character_id)
);