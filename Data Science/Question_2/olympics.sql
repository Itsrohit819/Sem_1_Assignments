use olympics;

SELECT * From olympics;

SELECT name,medal FROM olympics;

SELECT count(name) AS total_players from olympics;

SELECT * From olympics WHERE medal='Gold';

SELECT name,year from olympics where medal='Silver';

Select team from olympics where medal like'Gold'
Group by team having count(medal='Gold')>50;

SELECT name FROM olympics GROUP BY name  ORDER BY COUNT(medal) DESC LIMIT 1;

SELECT `event` from olympics where event like '%Freestyle%' ;

SELECT name,count(medal) AS medal_count FROM olympics GROUP BY name  ORDER BY COUNT(medal) DESC LIMIT 3;

SELECT distinct name, COUNT(*) AS total_medals FROM olympics GROUP BY name HAVING COUNT(*) > 1;

SELECT DISTINCT team FROM olympics WHERE medal='Gold' AND (season='Summer' OR season='Winter');

SELECT team, MAX(year) - MIN(year) AS year_diff FROM olympics GROUP BY team;


SELECT team, COUNT(medal) / COUNT(DISTINCT name) AS avg_medals_per_athlete FROM olympics GROUP BY team;

SELECT team
FROM (
    SELECT team, sport, medal
    FROM olympics
    GROUP BY team, sport, medal
) AS medal_counts GROUP BY team
HAVING COUNT(DISTINCT sport) > 10;

SELECT 
    team,
    SUM(CASE WHEN medal = 'Gold' THEN 1 ELSE 0 END) AS Gold,
    SUM(CASE WHEN medal = 'Silver' THEN 1 ELSE 0 END) AS Silver,
    SUM(CASE WHEN medal = 'Bronze' THEN 1 ELSE 0 END) AS Bronze
FROM olympics
WHERE medal IN ('Gold', 'Silver', 'Bronze')
GROUP BY team;