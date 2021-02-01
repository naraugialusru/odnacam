USE leet;

DROP TABLE IF EXISTS Scores;
CREATE TABLE Scores (Id INT, Score DECIMAL(3,2));

INSERT INTO Scores 
VALUES ( 1  , 3.50  )
  	 , ( 2  , 3.65  )
 	 , ( 3  , 4.00  )
	 , ( 4  , 3.85  )
	 , ( 5  , 4.00  )
	 , ( 6  , 3.65  );
     
SELECT * 
FROM Scores;

SELECT Score
     , (SELECT COUNT(*) 
        FROM (
            SELECT DISTINCT Score
            FROM Scores
            WHERE Score > s.Score 
            ) c
        ) + 1 AS `Rank`
FROM Scores s
ORDER BY `Rank`;