from pydantic_settings import BaseSettings


class Settings(BaseSettings):    
    # Event Streaming Server
    api_event_streaming_host:str
    api_event_streaming_client_id: str

    # Service metadata
    service_name: str

    # Streaming topics    
    api_account_topic: str
    api_otp_topic: str
    api_role_topic: str
    api_device_topic: str    
    api_account_create_group: str  

    account_model_version: int
    
    # API model versions
    account_model_version: int

    # Cache credentials       
    api_redis_decode_response: bool
    api_redis_host_local: str    

    # DB credentials
    api_db_url: str

    
settings = Settings()
