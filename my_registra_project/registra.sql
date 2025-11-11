--
-- Recreate it
CREATE DATABASE IF NOT EXISTS db_registra;
use db_registra;
-- Create the table
 CREATE TABLE  if not exists tbl_student (
    st_ID INT AUTO_INCREMENT PRIMARY KEY,
     first_name VARCHAR(50) NOT NULL,
     last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
  email VARCHAR(100) NOT NULL);
  
insert ignore into  tbl_student (first_name,last_name,birth_date,email)
values 
 ('Jack','Smith','2000-01-03','jsmith@gmail.com'),
 ('Anna','Johnson','2005-05-22','annaj@gmail.com'),
 ('Mary','Bergman','1998-12-02','maryber@gmail.com'),
 ('Yong','Hu','1974-09-22','yhu1974@gmail.com');
 show tables;
