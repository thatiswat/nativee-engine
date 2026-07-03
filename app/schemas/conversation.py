from pydantic import BaseModel


class PipelineMetrics(BaseModel):
    stt: float
    translation: float
    tts: float
    pipeline_total: float


class PipelineResult(BaseModel):
    original: str
    translated: str
    audio_url: str
    provider: str

    metrics: PipelineMetrics