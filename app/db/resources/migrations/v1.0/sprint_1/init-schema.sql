
-- Table for logging each request with prediction

CREATE TABLE request_log(
  request_id bigserial NOT NULL PRIMARY KEY,
  request_body varchar(500) NOT NULL,
  request_response varchar(500) NOT NULL,
  request_timestamp varchar(50) NOT NULL
);


-- Table for users

CREATE TABLE app_user(
  user_id bigserial NOT NULL PRIMARY KEY,
  username varchar(50) NOT NULL,
  user_type varchar(50) NOT NULL,
  email varchar(100) NOT NULL,
  password varchar(200) NOT NULL,
  is_active boolean NOT NULL,
  registration_date timestamp NOT NULL
);
