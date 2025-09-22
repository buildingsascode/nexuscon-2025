from pydantic import BaseModel, Field


class Platform(BaseModel):
    os_version: str = Field(alias="os-version")
    framework_version: str = Field(alias="framework-version")
    jvm_version: str = Field(alias="jvm-version")
    model_id: str = Field(alias="model-id")
    model_name: str = Field(alias="model-name")
    model_revision: str = Field(alias="model-revision")
    host_id: str = Field(alias="host-id")
    vendor_name: str = Field(alias="vendor-name")
    units: str
    architecture: str
    kernel_version: str
