from uagents import Model
from pydantic import Field

class Temperature(Model):
  location: str = Field(description = "Location of interest")
  max_temp: int = Field(description="Maximum temperature")
  min_temp: int = Field(description="Minimum temperature")
  
  class Config:
    allow_population_by_field_name = True
