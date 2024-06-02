from sqlmodel import SQLModel, Field

class ProjectData:
    
    def __init__(self, project_name, project_desc, image):
        self.project_name = project_name
        self.project_description = project_desc
        self.image = image
        
    project_name: str
    project_description: str
    image: str
    
class ProjectBase(SQLModel):
    project_name: str
    project_description: str
    image: str
    
class Project(ProjectBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(index=True)
    project_name: str = Field(index=True)
    project_description: str = Field(index=True)
    image: str = Field(default="default.png", index=True)

class ProjectCreate(SQLModel):
    project_description: str
    
class ProjectId(SQLModel):
    id: int