# Exercise to simulate Double booking problem

## how to do it
1. create the database, however u want
> here's the scheme : 
```sql
CREATE TABLE IF NOT EXISTS seats 
(
    id serial not null primary key,
    is_booked int not null default 0,
    name varchar(255) not null
)
```
> in a loop, populate it with empty seats, in any language or via
```sql
CREATE OR REPLACE FUNCTION create_seats() RETURNS VOID AS $$
DECLARE
   i INT := 1;
BEGIN
   WHILE i <= 25 LOOP
     INSERT INTO
     	seats(is_booked, "name")
     VALUES(0, 'EMPTY');
      i := i + 1; 
   END LOOP;
END;
$$ LANGUAGE plpgsql;
```
> call it
```sql
SELECT create_seats();
```
2. install fastAPI and uvicorn
`pip install fastapi 'uvicorn[standard]'`
3. run the server and thru httpie call it twice while adding a break point in the select to simulate 2 clients booking at the same time
    1. `uvicorn main:app --reload `
    1. fastAPI provides swagger, go to the port u started the server at/docs.