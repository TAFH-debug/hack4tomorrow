from fastapi import APIRouter, Depends
from sqlalchemy import delete, insert, select

from auth import get_project, get_user
from character import get_dialog_by_id, get_character_by_id
from database import get_db
from models import *
from openai_api import generate_options


router = APIRouter(prefix="/dialog", tags=["Dialog"])

@router.post("/create/")
async def create(dialog: DialogCreate, user: User = Depends(get_user)):
    character1 = await get_character_by_id(dialog.character1_id)
    character2 = await get_character_by_id(dialog.character2_id)
    
    query = insert(
        Dialog
    ).values(project_id=dialog.project_id, character1_id=character1.id, character2_id=character2.id, 
             character1_goal=dialog.character1_goal,
             character2_goal=dialog.character2_goal)
    
    await get_db().execute(query)

@router.post("/generate/")
async def generate(dialog: DialogId, user: User = Depends(get_user)):
    dial: Dialog = await get_dialog_by_id(dialog.id)
    character1 = await get_character_by_id(dial.character1_id)
    character2 = await get_character_by_id(dial.character2_id)
    obj = generate_options(character1, character2, dial.character1_goal, dial.character2_goal)
    
    for i in range(len(obj['messages'])):
        query = insert(
            Message
        ).values(content=obj['messages'][i]['content'], author=obj['messages'][i]['author'], dialog_id=dial.id, index=i)
        await get_db().execute(query)

@router.post("/get_messages/")
async def get_messages(dialog: DialogId, user: User = Depends(get_user)):
    query = select(
        Message
    ).where(Message.dialog_id == dialog.id)
    return await get_db().fetch_all(query)

@router.post("/get_all/")
async def get_all(params: tuple[Project, User] = Depends(get_project)):
    query = select(
        Dialog
    ).where(Dialog.project_id == params[0].id)
    
    return await get_db().fetch_all(query)

@router.post("/delete/")
async def get_all(dialog: DialogId, user: User = Depends(get_user)):
    query = delete(
        Dialog
    ).where(Dialog.id == dialog.id)
    
    return await get_db().execute(query)
