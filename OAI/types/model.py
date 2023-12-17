from pydantic import BaseModel, Field, ConfigDict
from time import time
from typing import List, Optional
from gen_logging import LogConfig

class ModelCardParameters(BaseModel):
    max_seq_len: Optional[int] = 4096
    rope_scale: Optional[float] = 1.0
    rope_alpha: Optional[float] = 1.0
    cache_mode: Optional[str] = "FP16"
    prompt_template: Optional[str] = None
    num_experts_per_token: Optional[int] = None
    draft: Optional['ModelCard'] = None

class ModelCard(BaseModel):
    id: str = "test"
    object: str = "model"
    created: int = Field(default_factory=lambda: int(time()))
    owned_by: str = "tabbyAPI"
    logging: Optional[LogConfig] = None
    parameters: Optional[ModelCardParameters] = None

class ModelList(BaseModel):
    object: str = "list"
    data: List[ModelCard] = Field(default_factory=list)

class DraftModelLoadRequest(BaseModel):
    draft_model_name: str
    draft_rope_scale: Optional[float] = 1.0
    draft_rope_alpha: Optional[float] = Field(description = "Automatically calculated if not present", default = None)

# TODO: Unify this with ModelCardParams
class ModelLoadRequest(BaseModel):
    name: str
    max_seq_len: Optional[int] = 4096
    gpu_split_auto: Optional[bool] = True
    gpu_split: Optional[List[float]] = Field(default_factory=list)
    rope_scale: Optional[float] = 1.0
    rope_alpha: Optional[float] = Field(description = "Automatically calculated if not present", default = None)
    no_flash_attention: Optional[bool] = False
    # low_mem: Optional[bool] = False
    cache_mode: Optional[str] = "FP16"
    prompt_template: Optional[str] = None
    num_experts_per_token: Optional[int] = None
    draft: Optional[DraftModelLoadRequest] = None

class ModelLoadResponse(BaseModel):
    # Avoids pydantic namespace warning
    model_config = ConfigDict(protected_namespaces = [])

    model_type: str = "model"
    module: int
    modules: int
    status: str
