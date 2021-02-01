USE leet;

DROP TABLE IF EXISTS cinema;
CREATE TABLE cinema (
	id INT
    , movie CHAR(50)
    , description CHAR(50)
    , rating DECIMAL(2,1)
	);
    
INSERT INTO cinema
VALUES (1     , 'War'       ,   'great 3D'   ,   8.9)
	, (2     , 'Science'   ,   'fiction'    ,   8.5     )
	, (   3     , 'irish'     ,   'boring'     ,   6.2     )
	, (   4     , 'Ice song'  ,   'Fantacy'    ,   8.6     )
	, (   5     , 'House card',   'Interesting',   9.1  );
    
SELECT *
FROM cinema;

SELECT *
FROM cinema
WHERE description NOT LIKE('%boring%') and MOD(ID, 2) = 1
ORDER BY rating DESC;