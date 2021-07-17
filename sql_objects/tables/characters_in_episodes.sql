CREATE TABLE IF NOT EXISTS storefirst.characters_in_episodes
(
    location_id character(50) NOT NULL,
    character_id character(50) NOT NULL,
    insertion_time date NOT NULL DEFAULT CURRENT_DATE
);
