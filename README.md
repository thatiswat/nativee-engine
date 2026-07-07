# Nativee Engine

Nativee Engine is the real-time multilingual communication engine powering the Nativeee platform.

It is responsible for speech recognition, translation, voice synthesis, and streaming audio generation while remaining independent from authentication, billing, analytics, projects, and other platform concerns handled by Nativeee API.

---

# Overview

Nativee Engine executes multilingual conversation pipelines with a focus on:

- Low latency
- Streaming-first audio delivery
- Provider abstraction
- Production-ready architecture
- Performance profiling
- Modular services

The engine is designed to evolve independently while exposing a stable HTTP interface to Nativeee API.

---

# Architecture

```text
                Audio Input
                     │
                     ▼
         Speech Recognition
                     │
                     ▼
             Translation
                     │
                     ▼
            Voice Generation
             ┌──────────────┐
             ▼              ▼
      File Output     Audio Stream
```

The engine follows a layered architecture.

```text
               API Routes
                    │
                    ▼
      Conversation Orchestrator
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
   Speech      Translation     Voice
    Service       Service      Service
        │           │           │
        └───────────┼───────────┘
                    ▼
             Provider Layer
                    │
                    ▼
          External AI Providers
```

---

# Features

## Speech Recognition

- Groq Whisper
- Provider abstraction
- Request profiling
- Metadata collection

---

## Translation

- Google Translate
- Provider abstraction
- Language-aware translation pipeline

---

## Voice Generation

- Microsoft Edge TTS
- File generation
- Streaming audio
- Voice abstraction

---

## Streaming

- HTTP chunked streaming
- Low Time-To-First-Audio (TTFA)
- No temporary audio files
- Progressive playback

---

## Performance Profiling

Every request is profiled.

Captured metrics include:

- Input metadata
- Output metadata
- Speech latency
- Translation latency
- Voice latency
- Engine latency
- Time To First Audio (TTFA)
- Provider information
- Model information
- Character counts
- Audio file size

Example profiling output:

```json
{
  "profiling": {
    "input": {
      "size_kb": 118.6
    },
    "speech": 0.341,
    "translation": 0.228,
    "voice": 0.702,
    "engine": 1.287
  }
}
```

---

# Project Structure

```text
app/
├── api/
│   └── v1/
├── core/
├── engine/
├── providers/
├── speech/
├── translation/
├── voice/
├── storage/
└── schemas/
```

---

# Design Principles

Nativeee Engine is built around the following principles:

- Clear separation of concerns
- Provider abstraction
- Thin API layer
- Service-oriented architecture
- Streaming-first design
- Performance-first engineering
- Observable execution
- Extensible provider ecosystem

---

# Current Providers

## Speech

- Groq Whisper

## Translation

- Google Translate

## Voice

- Microsoft Edge TTS

---

# API Endpoints

## Conversation

```http
POST /conversation
```

Processes speech and returns:

- Original text
- Translated text
- Generated audio URL
- Profiling information

---

## Streaming Conversation

```http
POST /conversation/stream
```

Processes speech and streams synthesized audio directly to the client.

Benefits:

- No temporary MP3 response
- Lower perceived latency
- Progressive playback
- Reduced Time-To-First-Audio (TTFA)

---

# Development

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the engine.

```bash
uvicorn app.main:app --reload --port 8001
```

Open Swagger UI.

```
http://127.0.0.1:8001/docs
```

---

# Performance

Typical development benchmarks:

| Component | Typical Latency |
|-----------|----------------:|
| Speech Recognition | 250–400 ms |
| Translation | < 1 s |
| Voice TTFA | ~600 ms |
| Voice Generation | Provider dependent |
| Engine | Depends on audio length |

Latency varies depending on:

- Audio duration
- Network conditions
- Provider response times
- Streaming mode
- Hardware performance

---

# Platform Integration

Nativee Engine is designed to operate behind Nativeee API.

```text
Client
   │
   ▼
Nativee API
   │
   ▼
Nativee Engine
   │
   ▼
AI Providers
```

The engine does **not** manage:

- Authentication
- Billing
- API Keys
- Projects
- Analytics
- Organizations
- User management

Those responsibilities belong to Nativeee API.

---

# Roadmap

- Continuous conversations
- Voice Activity Detection (VAD)
- Incremental translation
- Audio segmentation
- Provider failover
- Additional speech providers
- Additional translation providers
- Additional voice providers
- Streaming optimization
- End-to-end latency improvements
- Real-time profiling dashboard

---

# License

Copyright © Nativee.

All rights reserved.