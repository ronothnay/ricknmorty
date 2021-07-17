CREATE TABLE IF NOT EXISTS storefirst.characters_in_episodes
(
    episode_id character(50) NOT NULL,
    character_id character(50) NOT NULL,
    insertion_time date NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (episode_id, character_id),
    CONSTRAINT fk_location FOREIGN KEY (episode_id)
        REFERENCES storefirst.episodes (episode_id) MATCH SIMPLE,
    CONSTRAINT fk_character FOREIGN KEY (character_id)
        REFERENCES storefirst.characters (character_id) MATCH SIMPLE
);
