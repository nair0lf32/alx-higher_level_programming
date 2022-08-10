--  creates the table unique_id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 NOT NULL,
    name VARCHAR(255) NOT NULL,
    UNIQUE KEY id (id)
);
