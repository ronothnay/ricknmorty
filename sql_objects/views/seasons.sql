CREATE OR replace VIEW storefirst.seasons
AS
  SELECT with_dates.season_id,
         min_ep.episode_id AS first_episode,
         max_ep.episode_id AS last_episode,
         with_dates.amount_of_episodes
  FROM   (SELECT MIN(air_date) AS min_date,
                 MAX(air_date) AS max_date,
                 COUNT(*)      AS amount_of_episodes,
                 season_id
          FROM   storefirst.episodes
          GROUP  BY season_id) with_dates
         join storefirst.episodes min_ep
           ON min_ep.air_date = with_dates.min_date
              AND min_ep.season_id = with_dates.season_id
         join storefirst.episodes max_ep
           ON max_ep.air_date = with_dates.max_date
              AND max_ep.season_id = with_dates.season_id