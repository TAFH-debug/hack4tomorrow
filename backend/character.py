from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import insert, select, delete, update
from auth import get_user, get_project
from models import *
from database import get_db
from openai_api import *
import json

router = APIRouter(prefix="/character", tags=["Character"])

async def get_dialog_by_id(id: int):
    query = select(
        Dialog
    ).where(Dialog.id == id)
    return await get_db().fetch_one(query)

async def get_character_by_id(character_id: int) -> Character:
    query = select(
        Character
    ).where(Character.id == character_id)
    return await get_db().fetch_one(query)

async def get_project_by_id(project_id: int) -> Project:
    query = select(
        Project
    ).where(Project.id == project_id)
    return await get_db().fetch_one(query)

@router.post("/change/")
async def change(character: CharacterChange, user: User = Depends(get_user)):
    query = update(
        Character
    ).where(Character.id == character.id).values(name=character.name, 
                                                                 appearance=character.appearance, 
                                                                 personality=character.personality)
    await get_db().execute(query)
    
@router.post("/delete/")
async def change(character: CharacterCreate, user: User = Depends(get_user)):
    query = delete(
        Character
    ).where(Character.id == character.id)
    await get_db().execute(query)
    
    
@router.post("/generate/")
async def generate_random(params: tuple[Project, User] = Depends(get_project)):
    proj = params[0]
    query = select(Character).where(Character.project_id == proj.id)
    charcs = await get_db().fetch_all(query)
    data = generate_character(proj.project_name, proj.project_description, charcs)
    try:
        json_c = json.loads(data)
        character = CharacterData(json_c['name'], json_c['appearance'], json_c['personality'], proj.id)
    except Exception as e:
        print(data)
        print(e)
        raise HTTPException(500)
    
    query = insert(
        Character
    ).values(name=character.name, project_id=character.project_id, appearance=character.appearance, personality=character.personality)
    
    await get_db().execute(query)
    
    return character

@router.post("/create/")
async def create_character(character: CharacterBase, user: User = Depends(get_user)):
    query = insert(
        Character
    ).values(name=character.name, project_id=character.project_id, appearance=character.appearance, personality=character.personality)
    
    await get_db().execute(query)
    
    return character

@router.post("/get_all/")
async def get_characters(params: tuple[Project, User] = Depends(get_project)):
    query = select(
        Character
    ).where(Character.project_id == params[0].id)
    
    return await get_db().fetch_all(query)

@router.get("/get/")
async def get_characters():
    query = select(
        Character
    )
    
    return await get_db().fetch_all(query)