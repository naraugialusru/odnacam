USE leet;

DROP TABLE IF EXISTS seats;
CREATE TABLE seats (    id INT  , student CHAR(50) );

INSERT INTO seats
VALUES
(    1    , 'Abbot'   )
, (    2    , 'Doris'   )
, (    3    , 'Emerson' )
, (    4    , 'Green'   )
, (    5    , 'Jeames'  );

SELECT *
FROM seats;

SELECT
    (CASE
        WHEN MOD(id, 2) != 0 AND counts != id THEN id + 1
        WHEN MOD(id, 2) != 0 AND counts = id THEN id
        ELSE id - 1
    END) AS id,
    student
FROM
    seats,
    (SELECT
        COUNT(*) AS counts
    FROM
        seats) AS seat_counts
ORDER BY id ASC;


