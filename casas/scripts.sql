select * from casas
where barrio not in ('Olivos','Florida','Vicente López')
order by total_area desc;

delete from casas where item_id='MLA845139139';
delete from casas where item_id='MLA746589066';
update casas set total_area = 416 where item_id='MLA821151446';
update casas set total_area = 329 where item_id='MLA817619064';
update casas set total_area = 468 where item_id='MLA764706888';
update casas set total_area = 1485 where item_id='MLA821151424';


select item_id, price, title, permalink, price/total_area,total_area from casas
where barrio = 'Florida' and total_area<3000
order by price/total_area desc;

select *, price/total_area from casas
where price < 250000 and total_area>150
order by price/total_area desc;

select latitude, longitude from casas where price < 250000 and total_area > 173 and price/total_area > 1000 
order by price/total_area asc;


update casas set total_area = 384 where item_id='MLA783244664';
update casas set total_area = 247 where item_id='MLA837060436';
update casas set total_area = 194 where item_id='MLA835912301';
update casas set total_area = 242 where item_id='MLA746665642';
update casas set total_area = 200 where item_id='MLA618050176';
update casas set total_area = 166 where item_id='MLA844586010';
update casas set total_area = 246 where item_id='MLA836379478';
update casas set total_area = 750 where item_id='MLA836380669';
update casas set total_area = 178.5 where item_id='MLA776068667';
update casas set total_area = 411.78 where item_id='MLA844091403';
update casas set total_area = 424.34 where item_id='MLA792349923';
update casas set total_area = 900 where item_id='MLA637708764';
update casas set total_area = 416 where item_id='MLA821151446';
update casas set total_area = 329 where item_id='MLA817619064';
update casas set total_area = 468 where item_id='MLA764706888';
update casas set total_area = 1485 where item_id='MLA821151424';
delete from casas where item_id='MLA845139139';
delete from casas where item_id='MLA746589066';
delete from casas where item_id='MLA843002237';
delete from casas where item_id='MLA843539476';
delete from casas where total_area=0;


commit;
delete  from casas;

insert into casas(item_id, price) values ("A2FE211",123.23);


INSERT INTO casas (item_id, title, price, currency, latitude, 
longitude, barrio, direccion, permalink, total_area) values 
('MLA843089532','Valor Lote, Terreno En Venta En Vicente Lopez',340000,'USD'
,-34.5250244,-58.4814077,'Vicente López','25 de mayo 1300',
'https://terreno.mercadolibre.com.ar/MLA-843089532-valor-lote-terreno-en-venta-en-vicente-lopez-_JM',
252.0)