
-- Create pypass database
CREATE DATABASE pypass_db;

USE pypass_db;

CREATE TABLE accounts (
	password varchar(255),
	username varchar(255),
	email varchar(255),
	url varchar(255),
	website varchar(255)
);

