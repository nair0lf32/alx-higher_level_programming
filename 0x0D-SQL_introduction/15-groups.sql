--  lists the number of records with the same score in the table second_table of the database hbtn_0c_0
SELECT COUNT(score) FROM second_table WHERE score = (SELECT AVG(score) FROM second_table);
