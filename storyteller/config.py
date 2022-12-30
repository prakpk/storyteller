from dataclasses import dataclass


@dataclass
class StoryTellerConfig:
    image_size: int = 512
    max_new_tokens: int = 50
    writer: str = "gpt2"
    painter: str = "CompVis/stable-diffusion-v1-4"
    speaker: str = "tts_models/en/ljspeech/glow-tts"
    writer_device: str = "cuda:0"
    painter_device: str = "cuda:0"
    output_dir: str = "out"
    seed: int = 42
    prompt_prefix: str = "Beautiful painting"