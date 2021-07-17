CREATE TABLE IF NOT EXISTS storefirst.residents_in_locations
(
    location_id character(50) NOT NULL,
    character_id character(50) NOT NULL,
    insertion_time date NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (location_id, character_id)
    CONSTRAINT fk_location FOREIGN KEY (location_id)
        REFERENCES storefirst.locations (location_id) MATCH SIMPLE,
    CONSTRAINT fk_character FOREIGN KEY (character_id)
        REFERENCES storefirst.characters (character_id) MATCH SIMPLE
);
