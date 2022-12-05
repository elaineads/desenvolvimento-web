create database bd_unes;

use bd_unes;

create table contato(
id int not null auto_increment,
email varchar(50) not null,
assunto varchar(100) not null,
descricao  varchar(200) not null,
primary key(id));

select * from contato;