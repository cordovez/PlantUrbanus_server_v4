from fastapi import APIRouter, HTTPException
from models.task_models import Task
from typing import List
from beanie import PydanticObjectId

task_router = APIRouter()


@task_router.get('/')
async def get_all_tasks() -> list[Task]:
    tasks = await Task.find_all().to_list()
    return tasks


@task_router.post('/')
async def create_task(task: Task):
    await task.create()
    return {"message": "task has been saved"}


@task_router.get('/{task_id}')
async def get_task_by_id(task_id: PydanticObjectId) -> Task:
    task_to_get = await Task.get(task_id)
    return task_to_get


@task_router.put('/{task_id}')
async def update_task_by_id(task: Task, task_id: PydanticObjectId) -> Task:

    task_to_update = await Task.get(task_id)

    if not task_to_update:
        raise HTTPException(status_code=404, detail="Resource not found")

    task_to_update.task_content = task.task_content
    task_to_update.is_complete = task.is_complete

    await task_to_update.save()

    return task_to_update


@task_router.delete('/{task_id}')
async def delete_task(task_id: PydanticObjectId):
    task_to_delete = await Task.get(task_id)

    await task_to_delete.delete()

    return {"message": "task deleted"}
