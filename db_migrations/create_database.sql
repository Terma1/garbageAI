CREATE TABLE city_part (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE street (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city_part_id INTEGER NOT NULL,
    FOREIGN KEY (city_part_id) REFERENCES city_part(id)
);

CREATE TABLE garbage_type (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE state (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE user_request (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL,
    longitude REAL,
    street_id INTEGER NOT NULL,
    garbage_type INTEGER NOT NULL,
    state INTEGER NOT NULL,
    device_id TEXT NOT NULL,
    ip TEXT NOT NULL,
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (street_id) REFERENCES street(id),
    FOREIGN KEY (garbage_type) REFERENCES garbage_type(id),
    FOREIGN KEY (state) REFERENCES state(id)
);

CREATE TABLE garbage_collection (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    garbage_type INTEGER NOT NULL,
    street_id INTEGER NOT NULL,
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (garbage_type) REFERENCES garbage_type(id),
    FOREIGN KEY (street_id) REFERENCES street(id)
);

CREATE TABLE regulatory_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    garbage_type INTEGER NOT NULL,
    city_part_id INTEGER NOT NULL,
    garbage_collection_frequency_days_normal INTEGER NOT NULL,
    garbage_collection_frequency_days_min INTEGER NOT NULL,
    garbage_collection_frequency_days_max INTEGER NOT NULL,
    FOREIGN KEY (garbage_type) REFERENCES garbage_type(id),
    FOREIGN KEY (city_part_id) REFERENCES city_part(id)
);
