DROP TABLE IF EXISTS places;

CREATE TABLE places (
  place_id INT AUTO_INCREMENT,
  city VARCHAR(50),
  county VARCHAR(50),
  country VARCHAR(50),
  PRIMARY KEY (place_id)
);

DROP TABLE IF EXISTS people;

CREATE TABLE people (
  people_id INT AUTO_INCREMENT,
  given_name VARCHAR(50),
  family_name VARCHAR(50),
  date_of_birth DATE,
  place_of_birth VARCHAR(100),
  PRIMARY KEY (people_id)
);


