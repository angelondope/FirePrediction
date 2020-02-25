drop table _ca_fires_old;
drop table ca_fires;
drop table raw_fires;
drop table san_francisco_fires;
drop table los_angeles_fires;
drop table san_diego_fires;
drop table humidity;
drop table temperature;
drop table wind;
drop table pressure;

.mode csv
.import raw_fires.csv raw_fires
.import temperature_f.csv temperature
.import pressure_f.csv pressure
.import humidity_f.csv humidity
.import wind_speed_f.csv wind

create table ca_fires as select FIRE_YEAR,DISCOVERY_DOY,DISCOVERY_TIME,FIRE_NAME,MTBS_FIRE_NAME,STAT_CAUSE_DESCR,FIRE_SIZE,FIRE_SIZE_CLASS,LATITUDE,LONGITUDE from raw_fires where STATE='CA';

PRAGMA foreign_keys=off;
BEGIN TRANSACTION;
ALTER TABLE ca_fires RENAME TO _ca_fires_old;
create table ca_fires
(year INTEGER,
doy INTEGER,
hoursmin REAL,
fire_name VARCHAR,
mtbs_fire_name VARCHAR,
cause VARCHAR,
size REAL,
class VARCHAR,
latitude REAL,
longitude REAL);
INSERT into ca_fires (year , doy , hoursmin, fire_name, mtbs_fire_name , cause , size , class , latitude, longitude) select FIRE_YEAR,DISCOVERY_DOY,DISCOVERY_TIME,FIRE_NAME,MTBS_FIRE_NAME,STAT_CAUSE_DESCR,FIRE_SIZE,FIRE_SIZE_CLASS,LATITUDE,LONGITUDE from _ca_fires_old;
COMMIT ;

delete from ca_fires where year < 2006;

create table san_francisco_fires as select * from ca_fires where (longitude between -123.42 and -121.42) and (latitude between 36.77 and 38.77);
create table los_angeles_fires as select * from ca_fires where (longitude between -119.25 and -117.25) and (latitude between 33.05 and 35.05);
create table san_diego_fires as select * from ca_fires where (longitude between -118.16 and -116.16) and (latitude between 31.72 and 33.72);

update san_francisco_fires set hoursmin = ABS(RANDOM() % 24) * 100  where hoursmin='';
update los_angeles_fires set hoursmin = ABS(RANDOM() % 24) * 100  where hoursmin='';
update san_diego_fires set hoursmin = ABS(RANDOM() % 24) * 100  where hoursmin='';

update san_francisco_fires set hoursmin = round(hoursmin/100)*100;
update los_angeles_fires set hoursmin = round(hoursmin/100)*100;
update san_diego_fires set hoursmin = round(hoursmin/100)*100;

.read create_weather_data.sql