from sqlmodel import Field, SQLModel


class DialogBase(SQLModel):
    project_id: int
    character1_id: int
    character2_id: int
    
class Dialog(DialogBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    project_id: int = Field(index=True)
    character1_id: int = Field(index=True)
    character2_id: int = Field(index=True)
    character1_goal: str = Field(index=True)
    character2_goal: str = Field(index=True)
    
class DialogCreate(SQLModel):
    project_id: int
    character1_id: int
    character2_id: int
    character1_goal: str
    character2_goal: str
    
class DialogId(SQLModel):
    id: int
    