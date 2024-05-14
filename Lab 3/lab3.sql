USE employees;

-- Question 1
SELECT * FROM employees, salaries;

-- Question 2
SELECT * FROM salaries WHERE salary * 1.7 > 100000;

-- Question 3
SELECT AVG(salary) AS average_salary FROM salaries WHERE emp_no > 1510;

-- Question 4
SELECT emp_no, AVG(salary) AS average_salary FROM salaries GROUP BY emp_no;

-- Question 5
SELECT e.first_name, e.last_name, s.salary FROM employees e JOIN salaries s ON e.emp_no = s.emp_no;

-- Question 6
DELIMITER //
CREATE PROCEDURE emp_avg_salary (IN emp_number INT)
BEGIN
    SELECT AVG(salary) AS average_salary
    FROM salaries
    WHERE emp_no = emp_number;
END //
DELIMITER ;

CALL emp_avg_salary(11300);