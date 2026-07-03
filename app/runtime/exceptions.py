class EngineException(Exception):
    """Base engine exception."""


class SpeechException(
    EngineException
):
    pass


class TranslationException(
    EngineException
):
    pass


class SynthesisException(
    EngineException
):
    pass


class StorageException(
    EngineException
):
    pass