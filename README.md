# Nativee Engine

Nativee Engine is the AI execution runtime powering Nativeee.

It provides speech recognition, machine translation, speech synthesis, and runtime orchestration through a modular provider architecture designed for low-latency multilingual communication.

The engine is developed as an independent service and is consumed by the Nativee API Platform.

---

## Overview

Nativee Engine is responsible for:

- Speech-to-Text (STT)
- Machine Translation
- Text-to-Speech (TTS)
- Runtime orchestration
- Provider abstraction
- Request execution
- Runtime metrics
- Benchmarking

The engine is designed to support future streaming, GPU inference, provider benchmarking, and distributed execution without changing the public API.

---

## Architecture

```
                 Nativee Platform
                         │
                    HTTP / SDK
                         │
                         ▼
                 Nativee Engine
                         │
              Conversation Orchestrator
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       Speech      Translation      Synthesis
       Service        Service         Service
          │              │              │
          ▼              ▼              ▼
      Provider       Provider       Provider
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                    Runtime Layer
                         │
         Context • Metrics • Exceptions
```

---

## Project Structure

```
app/
├── api/
├── core/
├── engine/
├── providers/
├── runtime/
├── schemas/
├── services/
├── storage/
└── main.py
```

---

## Design Principles

The engine follows a layered architecture where every layer has a single responsibility.

| Layer | Responsibility |
|--------|----------------|
| API | HTTP interface |
| Engine | Request orchestration |
| Services | Business operations |
| Providers | External AI integrations |
| Runtime | Execution context, metrics and infrastructure |

This separation allows providers to be replaced, benchmarked or extended without affecting the rest of the system.

---

## Current Providers

| Capability | Provider |
|------------|----------|
| Speech Recognition | Groq Whisper Large V3 |
| Translation | Google Translate |
| Speech Synthesis | Microsoft Edge TTS |

---

## Planned Provider Support

### Speech Recognition

- Deepgram
- Whisper.cpp
- NVIDIA Parakeet

### Translation

- IndicTrans2
- NLLB
- SeamlessM4T

### Speech Synthesis

- ElevenLabs
- Kokoro
- XTTS

---

## Performance Objectives

| Metric | Target |
|---------|--------|
| Speech Recognition | < 500 ms |
| Translation | < 150 ms |
| Speech Synthesis | < 700 ms |
| End-to-End | < 1.5 s |

---

## Local Development

Clone the repository.

```bash
git clone https://github.com/thatiswat/nativeee-engine.git
cd nativeee-engine
```

Create a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create an environment file.

```env
GROQ_API_KEY=

STT_PROVIDER=groq
TRANSLATION_PROVIDER=google
TTS_PROVIDER=edge
```

Run the engine.

```bash
python -m uvicorn app.main:app --reload --port 8001
```

---

## Repository Status

Nativee Engine is under active development.

The current implementation provides the foundation for the Nativeee AI runtime. Upcoming work includes provider benchmarking, streaming inference, GPU execution, runtime observability, and distributed processing.

---

## License

Copyright © Nativee.

All rights reserved.