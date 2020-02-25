drop table san_francisco_weather;
drop table los_angeles_weather;
drop table san_diego_weather;

.mode csv
.import san_francisco_weather.csv san_francisco_weather
.import los_angeles_weather.csv los_angeles_weather
.import san_diego_weather.csv san_diego_weather

-- PRAGMA foreign_keys=off;
-- BEGIN TRANSACTION ;
-- ALTER TABLE san_francisco_weather RENAME TO _san_francisco_weather_old;
-- CREATE TABLE san_francisco_weather
-- (year INTEGER,
-- doy INTEGER,
-- hoursmin REAL,
-- temperature REAL,
-- humidity REAL,
-- wind REAL,
-- pressure REAL);
-- insert into san_francisco_weather (year, doy, hoursmin, temperature, humidity, wind, pressure) select year, doy, hourmin, temperature, humidity, wind, pressure from _san_francisco_weather_old ;
-- commit;

.read merge_all_data.sql