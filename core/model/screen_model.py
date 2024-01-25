from dataclasses_avroschema.pydantic import AvroBaseModel
from pydantic import Field
from typing import Optional
from core.enums.account_enums import *


class Screen(AvroBaseModel):
    height: int = Field(description='An integer representing the device screen height',
                        examples=[1920])
    width: int = Field(description='An integer representing the device width',
                       examples=[720])
    resolution: Optional[int] = Field(description='An integer representing the device resolution',
                            examples=[1200])


