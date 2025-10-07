SELECT
  driver_number,
  AVG(duration_sector_1 + duration_sector_2 + duration_sector_3) AS avg_lap_time
FROM {{ source('f1', 'laps') }}
GROUP BY driver_number
ORDER BY avg_lap_time ASC
