from fastapi import APIRouter, Depends
from sqlalchemy import delete, insert, select
from kadinsky import *
from character import get_project_by_id, get_character_by_id
from auth import get_project, get_user
from database import get_db
from models import *


router = APIRouter(prefix="/asset", tags=["Asset"])


@router.post("/get_all/")
async def get_arts(params: tuple[Project, User] = Depends(get_project)):
    query = select(
        Asset
    ).where(Asset.project_id == params[0].id)
    
    return await get_db().fetch_all(query)

@router.post("/generate/")
async def create(asset: AssetCreate, user: User = Depends(get_user)):
    proj = await get_project_by_id(asset.project_id)
    charc = await get_character_by_id(asset.character_id)
    file = generate_asset(proj.project_name, proj.id, proj.project_description, asset.description, charc.appearance)
    query = insert(
        Asset
    ).values(project_id=asset.project_id, path=file, character_id=asset.character_id)
    
    await get_db().execute(query)
    
@router.post("/delete/")
async def delete_ca(asset: AssetId, user: User = Depends(get_user)):
    query = delete(
        Asset
    ).where(Asset.id == asset.id)
    
    await get_db().execute(query)