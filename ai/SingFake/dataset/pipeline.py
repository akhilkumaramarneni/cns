from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.0",
    use_auth_token="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")
