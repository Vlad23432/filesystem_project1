SELECT AVG(`fee`) FROM `Employee`;

SELECT `first_name`, `last_name`, `fee`, (`fee` * 0.13) AS IncomeTax FROM `Employee`;