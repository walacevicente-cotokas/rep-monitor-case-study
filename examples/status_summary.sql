-- Standalone illustrative PostgreSQL query against synthetic schema only.
-- Not extracted from, nor executable against, the production system.
-- Example table: demo_equipment(id, serial, collection_status, last_seen).
SELECT
    collection_status,
    COUNT(*) AS equipment_count,
    COUNT(*) FILTER (
        WHERE last_seen < CURRENT_TIMESTAMP - INTERVAL '7 days'
    ) AS stale_for_seven_days
FROM demo_equipment
GROUP BY collection_status
ORDER BY equipment_count DESC;
