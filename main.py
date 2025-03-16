from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import TaskCreate, TaskUpdate
from database import get_db, Task

app = FastAPI()

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")
    return task

@app.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    max_task = db.query(Task).order_by(Task.id.desc()).first()
    task_id = (max_task.id + 1) if max_task else 1

    new_task = Task(id=task_id, title=task.title, description=task.description, completed=task.completed)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")

    update_data = task.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found")

    db.delete(db_task)
    db.commit()
    return {"message": f"Task with ID {task_id} deleted successfully"}