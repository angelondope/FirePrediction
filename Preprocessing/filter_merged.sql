drop table sf_firecount;
drop table sd_firecount;
drop table la_firecount;
drop table sf_supervised;
drop table sd_supervised;
drop table la_supervised;

create table sf_firecount as select * from sf where firecount != '';
create table sd_firecount as select * from sd where firecount != '';
create table la_firecount as select * from la where firecount != '';

create table sf_supervised as select * from sf;
UPDATE sf_supervised SET firecount = CASE WHEN firecount > 0 THEN 'T' ELSE 'F' END;

create table sd_supervised as select * from sd;
UPDATE sd_supervised SET firecount = CASE WHEN firecount > 0 THEN 'T' ELSE 'F' END;

create table la_supervised as select * from la;
UPDATE la_supervised SET firecount = CASE WHEN firecount > 0 THEN 'T' ELSE 'F' END;