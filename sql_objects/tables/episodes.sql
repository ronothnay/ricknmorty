CREATE TABLE IF NOT EXISTS storefirst.episodes
(
    episode_id character(50) NOT NULL,
    name character(256) NOT NULL,
    air_date date,
    episode_code character(50) NOT NULL,
    season_id character(50) NOT NULL,
    insertion_time date NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (episode_id)
);