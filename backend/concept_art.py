from fastapi import APIRouter, Depends
from sqlalchemy import delete, insert, select

from character import get_project_by_id, get_character_by_id
from openai_api import generate_concept_art
from auth import get_project, get_user
from database import get_db
from models import *


router = APIRouter(prefix="/concept_art", tags=["Concept Art"])


@router.post("/get_all/")
async def get_arts(params: tuple[Project, User] = Depends(get_project)):
    query = select(
        ConceptArt
    ).where(ConceptArt.project_id == params[0].id)
    
    return await get_db().fetch_all(query)

@router.post("/generate/")
async def create(concept_art: ConceptArtCreate, user: User = Depends(get_user)):
    proj = await get_project_by_id(concept_art.project_id)
    entity = await get_character_by_id(concept_art.entity_id)
    
    image_file = generate_concept_art(proj.project_name, proj.project_description, entity, concept_art.description)
    query = insert(
        ConceptArt
    ).values(project_id=concept_art.project_id, entity_id=concept_art.entity_id, image=image_file)
    
    await get_db().execute(query)
    
@router.post("/delete/")
async def delete_ca(concept_art: ConceptArtId, user: User = Depends(get_user)):
    query = delete(
        ConceptArt
    ).where(ConceptArt.id == concept_art.id)
    
    await get_db().execute(query)