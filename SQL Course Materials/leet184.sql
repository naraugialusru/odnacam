
USE leet;

DROP TABLE IF EXISTS  Employee;
CREATE TABLE Employee (
	Id INT
    , Name  CHAR(50)
    , Salary INT
    , DepartmentId INT);


INSERT INTO Employee
VALUES	 ( 1  , 'Joe'   , 70000  , 1            )
	,( 2  , 'Jim'   , 90000  , 1            )
	,( 3  , 'Henry' , 80000  , 2            )
	,( 4  , 'Sam'   , 60000  , 2            )
	,( 5  , 'Max'   , 90000  , 1       );



DROP TABLE IF EXISTS  Department;
CREATE TABLE Department (
	Id INT
    , Name  CHAR(50));


INSERT INTO Department
VALUES	 ( 1  , 'IT')
	,( 2  , 'Sales');
     
SELECT *
FROM Employee;

SELECT *
FROM Department;

SELECT Department.Name AS Department, Employee.Name AS Employee, Employee.Salary AS Salary
FROM Employee
JOIN Department
	ON Employee.DepartmentId = Department.Id;



