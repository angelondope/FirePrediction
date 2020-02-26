drop table groupby_sf;
drop table groupby_la;
drop table groupby_sd;
drop table sf;
drop table la;
drop table sd;

create table groupby_sf as select san_francisco_weather.year, san_francisco_weather.doy, san_francisco_weather.hourmin, count(san_francisco_fires.fire_name) as count from san_francisco_weather inner join san_francisco_fires on (san_francisco_weather.year = san_francisco_fires.year) and (san_francisco_weather.doy = san_francisco_fires.doy) and (san_francisco_weather.hourmin = san_francisco_fires.hoursmin) group by san_francisco_weather.year, san_francisco_weather.doy, san_francisco_weather.hourmin;

create table groupby_la as select los_angeles_weather.year, los_angeles_weather.doy, los_angeles_weather.hourmin, count(los_angeles_fires.fire_name) as count from los_angeles_weather inner join los_angeles_fires on (los_angeles_weather.year = los_angeles_fires.year) and (los_angeles_weather.doy = los_angeles_fires.doy) and (los_angeles_weather.hourmin = los_angeles_fires.hoursmin) group by los_angeles_weather.year, los_angeles_weather.doy, los_angeles_weather.hourmin;

create table groupby_sd as select san_diego_weather.year, san_diego_weather.doy, san_diego_weather.hourmin, count(san_diego_fires.fire_name) as count from san_diego_weather inner join san_diego_fires on (san_diego_weather.year = san_diego_fires.year) and (san_diego_weather.doy = san_diego_fires.doy) and (san_diego_weather.hourmin = san_diego_fires.hoursmin) group by san_diego_weather.year, san_diego_weather.doy, san_diego_weather.hourmin;

create table sf as select san_francisco_weather.year, san_francisco_weather.doy, san_francisco_weather.hourmin, san_francisco_weather.temperature, san_francisco_weather.humidity, san_francisco_weather.pressure, san_francisco_weather.wind, groupby_sf.count as firecount from san_francisco_weather left join groupby_sf on (san_francisco_weather.year = groupby_sf.year) and (san_francisco_weather.doy = groupby_sf.doy) and (san_francisco_weather.hourmin = groupby_sf.hourmin);

create table la as select los_angeles_weather.year, los_angeles_weather.doy, los_angeles_weather.hourmin, los_angeles_weather.temperature, los_angeles_weather.humidity, los_angeles_weather.pressure, los_angeles_weather.wind, groupby_la.count as firecount from los_angeles_weather left join groupby_la on (los_angeles_weather.year = groupby_la.year) and (los_angeles_weather.doy = groupby_la.doy) and (los_angeles_weather.hourmin = groupby_la.hourmin);

create table sd as select san_diego_weather.year, san_diego_weather.doy, san_diego_weather.hourmin, san_diego_weather.temperature, san_diego_weather.humidity, san_diego_weather.pressure, san_diego_weather.wind, groupby_sd.count as firecount from san_diego_weather left join groupby_sd on (san_diego_weather.year = groupby_sd.year) and (san_diego_weather.doy = groupby_sd.doy) and (san_diego_weather.hourmin = groupby_sd.hourmin);

delete from sf where temperature = '' and humidity = '' and pressure = '' and wind = '';
delete from la where temperature = '' and humidity = '' and pressure = '' and wind = '';
delete from sd where temperature = '' and humidity = '' and pressure = '' and wind = '';

.headers on
.mode csv
.output san_francisco_fires.csv
select * from san_francisco_fires;

.headers on
.mode csv
.output los_angeles_fires.csv
select * from los_angeles_fires;

.headers on
.mode csv
.output san_diego_fires.csv
select * from san_diego_fires;

.read filter_merged.sql