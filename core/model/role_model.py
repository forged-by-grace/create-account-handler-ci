from dataclasses_avroschema.pydantic import AvroBaseModel
from pydantic import Field
from typing import List

class Role(AvroBaseModel):
    name: str = Field(description='The name of the role.')
    permissions: List[str] = Field(default=[], description='The permissions for a given role.')