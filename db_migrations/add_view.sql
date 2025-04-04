-- View for street-level garbage status
CREATE VIEW street_garbage_status AS
SELECT
    rowid AS fake_key,
    s.name AS street,
    gt.name AS garbage_type,
    AVG(ur.state) AS avg_bin_level,
    MAX(ur.state) AS max_bin_level,
    MIN(ur.state) AS min_bin_level,
    (julianday('now') - julianday(gc.timestamp)) AS time_since_last_collection,
    CASE
        WHEN (julianday('now') - julianday(gc.timestamp)) > 1.5 * rd.garbage_collection_frequency_days_normal
            THEN 1 ELSE 0
        END AS exceeded_time_limit
FROM user_request ur
         JOIN street s ON ur.street_id = s.id
         JOIN garbage_type gt ON ur.garbage_type = gt.id
         JOIN garbage_collection gc ON ur.street_id = gc.street_id AND ur.garbage_type = gc.garbage_type
         JOIN regulatory_data rd ON s.city_part_id = rd.city_part_id AND ur.garbage_type = rd.garbage_type
GROUP BY s.id, gt.id;

-- View for city part-level garbage status
CREATE VIEW city_part_garbage_status AS
SELECT
    rowid AS fake_key,
    cp.name AS city_part,
    gt.name AS garbage_type,
    AVG(ur.state) AS avg_bin_level,
    MAX(ur.state) AS max_bin_level,
    MIN(ur.state) AS min_bin_level,
    (julianday('now') - julianday(gc.timestamp)) AS time_since_last_collection,
    CASE
        WHEN (julianday('now') - julianday(gc.timestamp)) > 1.5 * rd.garbage_collection_frequency_days_normal
            THEN 1 ELSE 0
        END AS exceeded_time_limit
FROM user_request ur
         JOIN street s ON ur.street_id = s.id
         JOIN city_part cp ON s.city_part_id = cp.id
         JOIN garbage_type gt ON ur.garbage_type = gt.id
         JOIN garbage_collection gc ON s.id = gc.street_id AND ur.garbage_type = gc.garbage_type
         JOIN regulatory_data rd ON cp.id = rd.city_part_id AND ur.garbage_type = rd.garbage_type
GROUP BY cp.id, gt.id;