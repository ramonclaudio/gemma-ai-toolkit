import argparse
from gemma_chat import ChatAPI
from gemma_text import TextAPI

print("------------------------------------------------------------------\n")
print("                             Gemma AI                             \n")
print("               API Wrapper & Command-line Interface               \n")
print("                       [v1.0.0] by @rmncldyo                      \n")
print("------------------------------------------------------------------\n")

def main():
    parser = argparse.ArgumentParser(
        prog="Gemma AI",
        description="A python wrapper and command-line interface for Google's latest open-source 'Gemma' instruct models.",
    )

    subparsers = parser.add_subparsers(dest='command')
    chat_parser = subparsers.add_parser('chat', help='Start a chat with the model.')
    chat_parser.add_argument('--model', type=str, default='google/gemma-2b-it', help='The model you would like to use. Default is "google/gemma-2b-it".')
    chat_parser.add_argument('--api_key', type=str, help='Enter your Hugging Face API key here. If not provided, the API key will be read from the environment variable API_KEY.')
    chat_parser.add_argument('--max_tokens', type=int, default=150, help='The maximum number of tokens to generate. Default is 150.')

    text_parser = subparsers.add_parser('text', help='Ask the model a question.')
    text_parser.add_argument('--prompt', type=str, default='What is the capital of France?', help='The question or prompt you would like to ask the model. Default is "What is the capital of France?"')
    text_parser.add_argument('--model', type=str, default='google/gemma-2b-it', help='The model you would like to use. Default is "google/gemma-2b-it".')
    text_parser.add_argument('--api_key', type=str, help='Enter your Hugging Face API key here. If not provided, the API key will be read from the environment variable API_KEY.')
    text_parser.add_argument('--max_tokens', type=int, default=150, help='The maximum number of tokens to generate. Default is 150.')

    args = parser.parse_args()

    if args.command == 'chat':
        ChatAPI(model=args.model, api_key=args.api_key, max_tokens=args.max_tokens).chat()
    
    if args.command == 'text':
        TextAPI(prompt=args.prompt, model=args.model, api_key=args.api_key, max_tokens=args.max_tokens).text()

if __name__ == "__main__":
    main()