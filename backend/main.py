
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Employee Management API",
    version="1.0.0"
)

employees = [
    {"id": 1, "name": "Amit", "department": "IT"},
    {"id": 2, "name": "Priya", "department": "HR"},
    {"id": 3, "name": "Rahul", "department": "Finance"}
]


@app.get("/")
def home():
    return {
        "message": "Employee Management API",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/api/employees")
def get_employees():
    return employees


@app.get("/api/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )
