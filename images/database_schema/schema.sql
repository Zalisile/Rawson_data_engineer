START TRANSACTION;

Drop table if exists places;

CREATE TABLE places (
  place_id INT AUTO_INCREMENT,
  city VARCHAR(50),
  county VARCHAR(50),
  country VARCHAR(50),
  PRIMARY KEY (place_id)
);

Drop table if exists people;

CREATE TABLE people(
  people_id INT AUTO_INCREMENT,
  given_name VARCHAR(50),
  family_name VARCHAR(50),
  date_of_birth DATE,
  place_of_birth VARCHAR(100),
  primary key (people_id)
);

commit;



