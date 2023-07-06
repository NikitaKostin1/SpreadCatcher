CREATE TABLE users (
	user_id 				BIGINT 		NOT NULL PRIMARY KEY,
	username 				VARCHAR(50)	NOT NULL,
	entry_date 				TIMESTAMP 	NOT NULL,
	is_bot_on				BOOLEAN		NOT NULL,

	is_subscription_active	BOOLEAN		NOT NULL,
	subscription_id			SMALLINT,
	subscription_begin_date	TIMESTAMP,

	is_test_active 			BOOLEAN		NOT NULL,
	test_begin_date 		TIMESTAMP
);

CREATE TABLE users_parametres (
	user_id			BIGINT 		NOT NULL PRIMARY KEY,
	limits			INTEGER,
	banks			TEXT 		NOT NULL,
	markets			TEXT 		NOT NULL,
	spread			REAL		NOT NULL,
	bid_type		VARCHAR(5) 	NOT NULL,
	ask_type		VARCHAR(5) 	NOT NULL,
	currencies		TEXT 		NOT NULL,
	fiat 			VARCHAR(5) 	NOT NULL,
	signals_type	VARCHAR(8)	NOT NULL
);

-- Import data from supported_banks.csv
/*
COPY supported_banks(fiat, bank, supported_markets, fiat_symbol)
FROM '%PATH%\supported_banks.csv'
DELIMITER ','
CSV HEADER;
*/
CREATE TABLE supported_banks (
	fiat				VARCHAR(50)	NOT NULL,
	bank				VARCHAR(30) NOT NULL,
	supported_markets	TEXT 		NOT NULL,
	fiat_symbol			VARCHAR(7) 	NOT NULL
);
