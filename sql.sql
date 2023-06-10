CREATE TABLE users (
	user_id 				BIGINT 		NOT NULL PRIMARY KEY,
	username 				VARCHAR(50),
	entry_date 				TIMESTAMP 	NOT NULL,
	phone					VARCHAR(25),
	full_name 				VARCHAR(50),
	email					VARCHAR(50),
	register_date 			TIMESTAMP,
	is_subscription_active 	BOOLEAN		NOT NULL,
	subscription_level		SMALLINT,
	subscription_begin_date TIMESTAMP
);

CREATE TABLE users_parametres (
	user_id		BIGINT 		NOT NULL PRIMARY KEY,
	limits		INTEGER,
	banks		TEXT 		NOT NULL,
	markets		TEXT 		NOT NULL,
	spread		REAL		NOT NULL,
	bid_type	VARCHAR(5) 	NOT NULL,
	ask_type	VARCHAR(5) 	NOT NULL,
	currencies  TEXT 		NOT NULL,
	fiat 		VARCHAR(5) 	NOT NULL,
	trading_type VARCHAR(8)	NOT NULL,
);
