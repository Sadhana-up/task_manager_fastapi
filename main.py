from fastapi import FastAPI
from tasks import Task

app = FastAPI()

tasks_list= [

]

@app.get("/tasks")
async def read_root():
    return {
    "message": "Hello, Welcome to Task Manager!",
    "tasks": tasks_list
}

@app.get("/tasks/{task_id}")
async def read_task(task_id: int):
    for task in tasks_list:
        if task.id == task_id:
            return task
    return {"message": "Task not found"}


@app.post("/tasks")
async  def add_task(task : Task):
    tasks_list.append(task)
    return tasks_list

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in tasks_list:
        if task.id == task_id:
            tasks_list.remove(task)
            return {"message": "Task deleted successfully"}
    return {"message": "Task not found"}

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks_list):
        if task.id == task_id:
            tasks_list[index] = updated_task
            return {"message": "Task updated successfully"}
    return {"message": "Task not found"}


