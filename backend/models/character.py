from sqlmodel import SQLModel, Field

class CharacterData:
    
    def __init__(self, name, appearance, personality, project_id):
        self.name = name
        self.appearance = appearance
        self.personality = personality
        self.project_id = project_id
        
    name: str
    appearance: str
    personality: str
    project_id: int
    
class CharacterBase(SQLModel):
    name: str
    appearance: str
    personality: str
    project_id: int
    
class Character(CharacterBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    project_id: int = Field(index=True)
    name: str = Field(index=True)
    appearance: str = Field(index=True)
    personality: str = Field(index=True)

class CharacterCreate(SQLModel):
    id: int

class CharacterChange(SQLModel):
    name: str
    appearance: str
    personality: str
    id: int
