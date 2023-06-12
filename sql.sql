CREATE TABLE users (
	user_id 				BIGINT 		NOT NULL PRIMARY KEY,
	username 				VARCHAR(50) NOT NULL,
	entry_date 				TIMESTAMP 	NOT NULL,
	is_bot_on				BOOLEAN		NOT NULL,

	is_subscription_active 	BOOLEAN		NOT NULL,
	subscription_id			SMALLINT,  -- NULL - None, 0 - tester, > 0 - trader
	subscription_begin_date TIMESTAMP,

	is_test_active 			BOOLEAN		NOT NULL,
	test_begin_date 		TIMESTAMP

	-- phone					VARCHAR(25),
	-- full_name 				VARCHAR(50),
	-- email					VARCHAR(50),
	-- register_date 			TIMESTAMP,
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
