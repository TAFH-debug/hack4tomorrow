from sqlmodel import Field, SQLModel


class AssetBase(SQLModel):
    project_id: int
    path: str

class Asset(AssetBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    path: str = Field(index=True)
    project_id: int = Field(index=True)
    character_id: int = Field(index=True)
    
class AssetCreate(SQLModel):
    character_id: int
    project_id: int
    description: str
    
class AssetId(SQLModel):
    id: int
    
    