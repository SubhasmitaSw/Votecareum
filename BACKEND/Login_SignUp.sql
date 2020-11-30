CREATE DATABASE IF NOT EXISTS `python_login` DEFAULT CHARACTER  SET utf8 collate utf8_general_ci; /*CREATE THE DATABASE*/
USE `python_login`;  /*USE THE DATABASE*/ 

CREATE TABLE IF NOT EXISTS `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT, /*UNIQUE ID FOR EVERY ENTRY*/
		`name` varchar(50) NOT NULL,
		`username` varchar(50) NOT NULL, /*ENTER THE USERNAME*/
		`password` varchar(200) NOT NULL, /*ENTER THE PASSWORD */
		`email` varchar(100) NOT NULL, /*ENTER THE EMAIL ID*/
    primary key(`id`) /*KEY USED TO UNIQUELY IDENTIFY EACH ROW*/
);

select * from accounts;
delete from accounts where name = 'sample';
INSERT INTO `accounts` (`name` ,`username`, `password`, `email`) VALUES ('test' , 'test', 'test', 'test@test.com'); /*TEST*/
