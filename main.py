from fastapi import FastAPI
import psycopg2

app = FastAPI()

async def connect( query:str = "SELECT now()"):
    d = None
    with psycopg2.connect(
        host = "localhost",
        database = "postgres",
        port= "5433",
        user = "postgres",
        password= "postgres"
        ) as con:
        cur = con.cursor()
        cur.execute(query)
        d = cur.fetchall()
    return d

@app.get("/")
async def get_seats():
    seats = await connect("Select * from seats")
    return {"seats": seats}

@app.post("/")
async def book_seat(seat_id:int, name:str):
    with psycopg2.connect(
        host = "localhost",
        database = "postgres",
        port= "5433",
        user = "postgres",
        password= "postgres"
        ) as con:
        try:
            cur = con.cursor()
            cur.execute("BEGIN")
            cur.execute(f"SELECT * FROM seats WHERE id = '{seat_id}' and is_booked = 0 FOR UPDATE")
            seat = cur.fetchall()
            
            if(len(seat) == 0): 
                return {"error":f"seat {seat_id} already booked"}
            
            cur.execute(f"UPDATE seats SET is_booked = 1, name = '{name}' WHERE id = '{seat_id}'")
            con.commit()
            return {"sucess":f"seat {seat_id}, booked successfuly!"}
        except Exception as ex:
            return {"An error has Occu'd: ": ex}
@app.get("/fix")
async def fix_commit():
    with psycopg2.connect(
        host = "localhost",
        database = "postgres",
        port= "5433",
        user = "postgres",
        password= "postgres"
        ) as con:
        cur = con.cursor()
        cur.execute("COMMIT")