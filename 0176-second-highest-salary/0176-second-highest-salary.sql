# Write your MySQL query statement below

SELECT DISTINCT MAX(Salary) AS SecondHighestSalary
from Employee a
where Salary < (SELECT MAX(Salary)FROM Employee b WHERE b.salary > a.salary)
