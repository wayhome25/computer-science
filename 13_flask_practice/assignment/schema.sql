drop table if exist member;
create table member (
    id integer primary key autoincrement,
    name text not null,
    email text not null,
    phone integer not null
);

