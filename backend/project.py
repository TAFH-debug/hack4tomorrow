from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import insert, select, delete, update
from auth import get_project, get_user
from models import *
from database import get_db
from openai_api import *

router = APIRouter(prefix="/project", tags=["Project"])

@router.get("/get_projects/")
async def create(creds: User = Depends(get_user)):
    query = select(
        Project
    ).where(Project.user_id == creds.id)
    
    projects = await get_db().fetch_all(query)
    
    return projects

@router.post("/generate_basic/")
async def generate_project_without_image(project: ProjectCreate, user: User = Depends(get_user)):
    project_name = generate_project_name(project.project_description)
    query = insert(
        Project
    ).values(project_name=project_name, project_description=project.project_description, 
            user_id=user.id, image="default.png")
    
    obj = ProjectData(project_name, project.project_description, "default.png")
    
    await get_db().execute(query)
    
    return obj
    
@router.post("/generate_image/")
async def generate_image(params: tuple[Project, User] = Depends(get_project)):
    proj = params[0]
    image = generate_project_image(proj.project_name, proj.project_description)
    query = update(
        Project
    ).where(Project.id == proj.id).values(image=image)
    
    obj = ProjectData(proj.project_name, proj.project_description, image)
    
    await get_db().execute(query)
    
    return obj
    
@router.post("/create/")
async def create(project: ProjectBase, user: User = Depends(get_user)):
    query = insert(
        Project
    ).values(project_name=project.project_name, project_description=project.project_description, 
             image=project.image, user_id=user.id)
    
    await get_db().execute(query)
    
    return project

@router.post("/get_by_id/")
async def get_by_id(params: tuple[Project, User] = Depends(get_project)):
    return params[0]

@router.post("/delete/")
async def delete_project(params: tuple[Project, User] = Depends(get_project)):
    query = delete(
        Project
    ).where(Project.id == params[0].id)
    
    
    await get_db().execute(query)
    
@router.get("/get/")
async def get():
    query = select(
        Project
    )
    
    return await get_db().fetch_all(query)