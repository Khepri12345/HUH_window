create table student(
	student_id serial primary key,
	name varchar(20),
	major varchar(20)
);
insert into student(name, major)
values('AAA','123')
select * from student