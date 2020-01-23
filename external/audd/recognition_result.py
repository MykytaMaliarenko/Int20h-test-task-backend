from dataclasses import dataclass


@dataclass
class RecognitionResult:
    artist: str
    song: str
