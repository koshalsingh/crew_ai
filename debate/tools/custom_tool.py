from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")
