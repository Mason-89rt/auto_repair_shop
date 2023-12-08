create table post(
	 id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR(50)  NOT NULL
);
create table user(
id INTEGER NOT NULL PRIMARY KEY,
login VARCHAR(50),
password VARCHAR(50)
);
create table staff(
id INTEGER NOT NULL PRIMARY KEY,
name VARCHAR (50),
surname VARCHAR(50),
post_id INTEGER,
user_id INTEGER,
foreign key (post_id) references post(id),
foreign key (user_id) references user(id)
);
create table application(
id INTEGER NOT NULL PRIMARY KEY,
client_id INTEGER,
description VARCHAR(255),
status VARCHAR(255),
comment_staff_id INTEGER,
foreign key (client_id) references client(id),
foreign key (comment_staff_id) references comment_staff(id)
);
create table comment_staff(
id INTEGER NOT NULL PRIMARY KEY,
staff_id INTEGER,
content VARCHAR (255),
foreign key (staff_id) references staff(id)
);
create table client(
id INTEGER NOT NULL PRIMARY KEY,
name VARCHAR (255),
surname VARCHAR (255),
data_reception DATE,
date_issuance DATE
);

create table type_service(
id INTEGER NOT NULL PRIMARY KEY,
client_id INTEGER,
name VARCHAR (255),
price INTEGER,
foreign key (client_id) references client(id)
);

create table order_work(
id INTEGER NOT NULL PRIMARY KEY,
type_service_id INTEGER,
status VARCHAR (255),
start_time_work time,
end_time_work time,
foreign key (type_service_id) references type_service(id)
);

create table payment(
id INTEGER NOT NULL PRIMARY KEY,
client_id INTEGER,
type VARCHAR(255),
success VARCHAR(255),
time_payment TIME,
foreign key (client_id) references client(id)
);
create table review(
id INTEGER NOT NULL PRIMARY KEY,
client_id INTEGER,
content VARCHAR(255),
foreign key (client_id) references client(id)
);
create table suppliers(
id INTEGER NOT NULL PRIMARY KEY,
data_deliveries date,
time_deliveries time,
product VARCHAR(255)
);
create table storehouse(
id INTEGER NOT NULL PRIMARY KEY,
product VARCHAR(255),
count integer,
suppliers_id integer,
foreign key (suppliers_id) references suppliers(id)
);
create table other(
id INTEGER NOT NULL PRIMARY KEY,
application integer,
sr_time_work float
);
create table type_service_statistics(
id INTEGER NOT NULL PRIMARY KEY,
engine_repair integer,
door_repair integer,
bumper_change integer
);


insert into user values(1,'maxim','staff');
	insert into user values(2,'andrew','staff');
		insert into user values(3,'ivan','staff');
			insert into user values(4,'georg','admin');
				insert into user values(5,'serg','admin');


insert into post values(1,'engineer');
	insert into post values(2,'engineer');
		insert into post values(3,'manager');
			insert into post values(4,'engineer');
				insert into post values(5,'director');

insert into staff values(1,'Maxim','Barinov',1,1);
	insert into staff values(2,'Andrew','Robertson',2,2);
		insert into staff values(3,'Ivan','Mostovoy',3,3);
			insert into staff values(4,'Georgiy','Hronov',4,4);
				insert into staff values(5,'Sergey','Bondarenko',5,5);

insert into suppliers values(1,'10-12-2024','10:25:00','wheel,tire');
	insert into suppliers values(2,'10-12-2024','17:00:00','bonnet,rear-view mirror');
		insert into suppliers values(3,'10-11-2024','09:40:00','bumper');
			insert into suppliers values(4,'05-06-2024','15:10:00','windscreen');
				insert into suppliers values(5,'12-10-2024','12:24:00','door,wing mirror,headlight,licence plate');

insert into storehouse values(1,'wheel',10,1);
	insert into storehouse values(2,'bonnet',15,3);
		insert into storehouse values(3,'wing mirror',30,4);
			insert into storehouse values(4,'headlight',100,5);
				insert into storehouse values(5,'windscreen',5,2);

insert into application values(1,1,'The transmission is broken','consider',1);

insert into client values(1,'Kolya','Ivanov','13-08-2020','15-09-2020');

insert into type_service values(1,1,'engine repair',10000);

insert into payment values(1,1,'card','successful','10:20:00');

insert into order_work values(1,1,'in progress','13:00:00','16:30:00');
insert into order_work values(2,2,'in progress','09:40:00','13:20:00');
insert into order_work values(3,3,'in progress','06:50:00','10:00:00');

insert into comment_staff values(1,1,'the engine is badly damaged, you need to order a new one, it will take a day to replace it');

insert into review values(1,1,'Completed within the specified time frame, I recommend a car service');