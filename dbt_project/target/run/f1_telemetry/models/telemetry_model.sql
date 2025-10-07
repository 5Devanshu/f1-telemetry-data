
  
  create view "f1_telemetry"."main"."telemetry_model__dbt_tmp" as (
    SELECT
  driver_number,
  AVG(duration_sector_1 + duration_sector_2 + duration_sector_3) AS avg_lap_time
FROM "f1_telemetry"."main"."laps"
GROUP BY driver_number
ORDER BY avg_lap_time ASC
  );
