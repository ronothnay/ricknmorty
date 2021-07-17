CREATE TABLE IF NOT EXISTS storefirst.seasons
(
    season_id character(50) NOT NULL,
    first_episode character(50) NOT NULL,
    last_episode character(50) NOT NULL,
    amount_of_episodes int NOT NULL,
    insertion_time date NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (season_id)
);
