<p align="center">
    <a href="https://ai.google.dev/gemma/" title="Go to Gemma homepage">
        <img src="https://img.shields.io/badge/Google%20Gemma%20AI-45a5ff?style=for-the-badge&logo=googlebard&logoColor=fff" alt="Google Gemma AI">
    </a>
</p>

<p align="center">
    <a href="https://github.com/RMNCLDYO/Gemma-AI" title="Go to repo">
        <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=Gemma+AI&query=version&url=https%3A%2F%2Fraw.githubusercontent.com%2FRMNCLDYO%2FGemma-AI%2Fmain%2F.github%2Fversion.json" alt="Gemma AI">
    </a>
</p>

<p align="center">
    <a href=".github/CHANGELOG.md" title="Go to changelog"><img src="https://img.shields.io/badge/maintained-yes-2ea44f?style=for-the-badge" alt="maintained - yes"></a>
    <a href=".github/CONTRIBUTING.md" title="Go to contributions doc"><img src="https://img.shields.io/badge/contributions-welcome-2ea44f?style=for-the-badge" alt="contributions - welcome"></a>
</p>

## Overview

The Gemma AI Wrapper and CLI (Command Line Interface) provides a streamlined interface for interacting with Google's Gemma language models, facilitating easy access to advanced natural language processing (NLP) capabilities. Designed for developers, researchers, and AI enthusiasts, this tool supports a wide range of text generation and processing tasks including conversation, summarization, and question answering.

Gemma models are lightweight, decoder-only, text-to-text large language models known for their efficiency and performance in various NLP tasks. They are part of Google's broader initiative to make cutting-edge AI technologies accessible to a wider audience.

## Key Features

- **Python Wrapper**: Simplifies programmatic access to Gemma models, enabling easy integration into applications.
- **Command-Line Interface**: Offers direct interaction with Gemma models for quick testing and experimentation.
- **Support for Multiple Models**: Compatibility with multiple Gemma model versions, including both base and instruction-tuned variants like `gemma-2b-it` and `gemma-7b-it`.
- **Flexible Configuration**: Allows users to tailor model settings, such as model selection and token generation limits, to their specific needs.

## Prerequisites

- Python 3.6 or newer.
- Internet connection for downloading model weights and dependencies (only required for download not use).
- An API key from Hugging Face (if accessing models not cached locally).

## Dependencies
The following Python packages are required:
- `torch`: This package, also known as PyTorch provides the underlying framework for tensor operations and neural network layers, enabling the loading and execution of the Gemma models.

- `transformers`: Developed by Hugging Face, this library is used for easy access to the Gemma models and their tokenizers, facilitating tasks like model downloading, loading, and inference with just a few lines of code.

The following Python packages are optional:
- `python-dotenv`: For managing API keys and other environment variables.

## Installation
Follow these steps to set up the Gemma AI Wrapper and CLI on your system:

Clone the repository:
```bash
git clone https://github.com/RMNCLDYO/Gemma-AI.git
cd Gemma-AI
```

Install required Python packages:
```bash
pip install -r requirements.txt
```

## Accessing Gated Models

This wrapper and command-line interface supports gated models like Google's `gemma-2b-it` and `gemma-7b-it` instruct models. To gain access to these models:

1. Visit [Google AI](https://ai.google.dev/gemma/) and sign in with your Google account.
2. Click on "Get Started" to be redirected to the official Google 'Kaggle' page [here](https://www.kaggle.com/models/google/gemma).
3. Authorize Hugging Face to access the gated model by following the prompts on Kaggle.

Once granted access, you can use your Hugging Face API key with this wrapper to download the Gemma models and automatically setup your cache. Once the weights and tokenizer are downloded to your system, and cached, neither the Hugging Face API key or Internet connection are required.

## Getting Started

### Setting Up Your API Key

1. If not using locally cached models, obtain an API key (token) from [Hugging Face](https://huggingface.co/settings/tokens).
2. You can set the API key in an environment variable `API_KEY`, or pass it directly to the CLI or wrapper.

### Using the Command-Line Interface

To start a chat with the default Gemma model:
```bash
python gemma_cli.py chat
```

To ask a question with the default Gemma model:
```bash
python gemma_cli.py text --prompt "Your prompt here"
```

For additional options and help:
```bash
python gemma_cli.py --help
```

### Using the Python Wrapper

To initiate a conversation using the default Gemma model with the wrapper:
```python
from gemma_chat import ChatAPI

ChatAPI().chat()
```

To ask the model a question using the default Gemma model with the wrapper:
```python
from gemma_text import TextAPI

TextAPI(prompt="Your question goes here.").text()
```

## Advanced Configuration

The tool allows for advanced configurations including specifying the model version, adjusting the maximum number of tokens, and utilizing different computational precisions for optimizing performance on specific hardware.

### Command-Line Options

#### Chat Options
- `--model`: Specify the Gemma model version.
- `--api_key`: Your Hugging Face API key.
- `--max_tokens`: The maximum number of tokens to generate.

#### Text Options
- `--prompt`: The question you would like to ask the model.
- `--model`: Specify the Gemma model version.
- `--api_key`: Your Hugging Face API key.
- `--max_tokens`: The maximum number of tokens to generate.

### Python Wrapper Options

When using the Python wrapper, these configurations can be adjusted by passing parameters to the `ChatAPI` class:

```python
ChatAPI(model="google/gemma-2b-it", api_key="your_api_key", max_tokens=150)
```

When using the Python wrapper, these configurations can be adjusted by passing parameters to the `TextAPI` class:

```python
TextAPI(prompt="Your question goes here.", model="google/gemma-2b-it", api_key="your_api_key", max_tokens=150)
```

## Contributing
Contributions are welcome!

Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed guidelines on how to contribute to this project.

## Reporting Issues
Encountered a bug? We'd love to hear about it. Please follow these steps to report any issues:

1. Check if the issue has already been reported.
2. Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template to create a detailed report.
3. Submit the report [here](https://github.com/RMNCLDYO/Gemini-AI-Wrapper-and-CLI/issues).

Your report will help us make the project better for everyone.

## Feature Requests
Got an idea for a new feature? Feel free to suggest it. Here's how:

1. Check if the feature has already been suggested or implemented.
2. Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template to create a detailed request.
3. Submit the request [here](https://github.com/RMNCLDYO/Gemini-AI-Wrapper-and-CLI/issues).

Your suggestions for improvements are always welcome.

## Versioning and Changelog
Stay up-to-date with the latest changes and improvements in each version:

- [CHANGELOG.md](.github/CHANGELOG.md) provides detailed descriptions of each release.

## Security
Your security is important to us. If you discover a security vulnerability, please follow our responsible disclosure guidelines found in [SECURITY.md](.github/SECURITY.md). Please refrain from disclosing any vulnerabilities publicly until said vulnerability has been reported and addressed.

## License
Licensed under the MIT License. See [LICENSE](LICENSE) for details.
