from sqlmodel import Field, SQLModel


class ConceptArtBase(SQLModel):
    image: str
    entity_id: int
    project_id: int


class ConceptArt(ConceptArtBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    image: str = Field(index=True)
    entity_id: int = Field(index=True)
    project_id: int = Field(index=True)
    
class ConceptArtCreate(SQLModel):
    description: str
    entity_id: int
    project_id: int
    
class ConceptArtId(SQLModel):
    id: int
    