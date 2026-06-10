USE ipl_project;

-- Top teams by wins

SELECT winner,
       COUNT(*) AS wins
FROM matches
GROUP BY winner
ORDER BY wins DESC;

-- Top run scorers

SELECT batter,
       SUM(batsman_runs) AS runs
FROM deliveries
GROUP BY batter
ORDER BY runs DESC
LIMIT 10;

-- Top wicket takers

SELECT bowler,
       COUNT(*) AS wickets
FROM deliveries
WHERE is_wicket = 1
GROUP BY bowler
ORDER BY wickets DESC
LIMIT 10;

-- Matches per season

SELECT season,
       COUNT(*) AS total_matches
FROM matches
GROUP BY season
ORDER BY season;

-- Toss winner equals match winner

SELECT toss_winner,
       COUNT(*) AS same_result
FROM matches
WHERE toss_winner = winner
GROUP BY toss_winner
ORDER BY same_result DESC;