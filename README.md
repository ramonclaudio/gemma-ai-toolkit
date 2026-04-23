# Gemma AI Toolkit

> **Unmaintained.** Ollama and HuggingFace Transformers cover this now. Use those.

I've always preferred pair programming with LLMs from the terminal over copy-pasting from browser chats. Web UIs hit rate limits, lose context across tabs, and break flow when I'm moving code back and forth. When Gemma launched in February 2024, there was no Ollama integration, no Google CLI, nothing clean to run it from a terminal. So I built this for myself. Downloads the weights once, caches them, chats or scripts against them offline.

Python wrapper and CLI for Google's Gemma open-source models.

## Install

```bash
git clone https://github.com/ramonclaudio/gemma-ai-toolkit.git
cd gemma-ai-toolkit
pip install -r requirements.txt
```

Requires Python 3.6+ and a HuggingFace token for gated models (`gemma-2b-it`, `gemma-7b-it`).

## Gated models

Gemma's instruct variants are gated. To get access:

1. Sign in at [Google AI](https://ai.google.dev/gemma/)
2. Click "Get Started" to land on Google's Kaggle page
3. Authorize HuggingFace access from there

After the weights download once, neither the token nor internet is needed.

## Configuration

Get a HuggingFace token at https://huggingface.co/settings/tokens, then add it to `.env`:

```
API_KEY=your_api_key
```

## CLI

```bash
# Interactive chat
python gemma_cli.py chat

# Single prompt
python gemma_cli.py text --prompt "Your prompt here"

# Help
python gemma_cli.py --help
```

Type `exit` or `quit` to leave an interactive session.

Both `chat` and `text` accept `--model`, `--api_key`, `--max_tokens`. `text` also accepts `--prompt`.

## Python

```python
from gemma_chat import ChatAPI
ChatAPI().chat()
ChatAPI(model="google/gemma-2b-it", api_key="your_api_key", max_tokens=150)
```

```python
from gemma_text import TextAPI
TextAPI(prompt="Your question").text()
TextAPI(prompt="Your question", model="google/gemma-2b-it", api_key="your_api_key", max_tokens=150)
```

## Dependencies

- `torch`, PyTorch for tensor ops and model execution
- `transformers`, HuggingFace for model loading and inference
- `python-dotenv`, optional, for `.env` loading

## Hardware

Running Gemma locally is resource-intensive. On limited CPUs, expect slow response times. Tune `--model` and `--max_tokens` to fit the hardware.

## License

MIT
