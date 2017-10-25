drop database if exists healthmanagement;


create database healthmanagement;


use healthmanagement ;

set foreign_key_checks=0;


create table patient (
    patientId integer auto_increment,
    patientName varchar(30) not null,
    phoneNumber varchar(15) not null,
    city varchar(10) not null,
    state varchar(10) not null,
    birthDate varchar(10) not null,
    userName varchar(15) not null,
    userPassWord varchar(20) not null,
    primary key (patientId)
);

create table doctor (
    doctorId integer auto_increment,
    doctorName varchar(30) not null,
    phoneNumber varchar(20) not null,
    city varchar(10) not null,
    state varchar(10) not null,
    userName varchar(15) not null,
    userPassWord varchar(20) not null,
    primary key (doctorId)
);

create table patientDoctor (
    patientId integer,
    doctorId integer,
    primary key (patientId,doctorId),
    foreign key (patientId) references patient(patientId), 
    foreign key (doctorId) references  doctor(doctorId)

);

create table message (
    messageId integer auto_increment,
    date varchar(10) not null,
    description varchar(100) not null,
	patientId integer,
    doctorId integer,
    primary key(messageId),
	foreign key (patientId) references patient(patientId), 
    foreign key (doctorId) references  doctor(doctorId)
    
);

create table speciality (
    specialityId integer auto_increment,
    name varchar(10) not null,
    primary key(specialityId)
);

create table service (
    serviceId integer auto_increment,
    name varchar(10) not null,
    description varchar(100) not null,
    specialityId integer,
    primary key(serviceId),
	foreign key (specialityId) references speciality(specialityId)
);


create table appointment (
    appointmentId integer auto_increment,
	patientId integer,
    doctorId integer,
    serviceId integer,
    date varchar(10) not null,
    time varchar(10) not null,
    status varchar(10) not null,
    hidden boolean,
    primary key(appointmentId),
	foreign key (patientId) references patient(patientId), 
    foreign key (doctorId) references  doctor(doctorId),
    foreign key (serviceId) references service(serviceId)
    
);



create table doctorService (
    price float,
    doctorId integer,
    serviceId integer ,
    primary key (doctorId,serviceId),
    foreign key (serviceId) references service(serviceId), 
    foreign key (doctorId) references  doctor(doctorId)
);

create table doctorSpeciality (
    doctorId integer, 
    specialityId integer ,
    primary key (doctorId,specialityId),
    foreign key (specialityId) references speciality(specialityId), 
    foreign key (doctorId) references  doctor(doctorId)
);












    
