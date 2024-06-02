from sqlmodel import Field, SQLModel


class MessageBase(SQLModel):
    content: str
    author: str
    dialog_id: int
    index: int
    
class Message(MessageBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str = Field(index=True)
    author: str = Field(index=True)
    dialog_id: int = Field(index=True)
    index: int = Field(index=True)