from fastapi import FastAPI, HTTPException

app = FastAPI()

records = [
    {"id": 1, "name": "Sample Course", "description": "A sample record for the assignment."},
    {"id": 2, "name": "Practice API", "description": "Another example record."},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}


@app.get("/records")
def list_records():
    return records


@app.get("/records/{record_id}")
def get_record(record_id: int):
    for record in records:
        if record["id"] == record_id:
            return record
    raise HTTPException(status_code=404, detail="Record not found")


# TODO: Add a POST endpoint to create a new record.
# TODO: Add a PUT or PATCH endpoint to update an existing record.
# TODO: Add a DELETE endpoint to remove a record.
