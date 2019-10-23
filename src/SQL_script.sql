
DROP TABLE data;
CREATE TABLE `data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `speed` FLOAT(11) NOT NULL,
  `length` int(11) NOT NULL,
  `label` int(11) NOT NULL,
  PRIMARY KEY (`id`));
  
  
DROP TABLE results;
CREATE TABLE `results` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `coef1` FLOAT(11) NOT NULL,
  `coef2` FLOAT(11) NOT NULL,
  `result` int(11) NOT NULL,
  PRIMARY KEY (`id`));
  
  
SELECT * from data;
SELECT * from results;

SELECT id,result FROM results order by result DESC;

INSERT INTO data(speed, length,label) VALUES (22.04,33,1);
