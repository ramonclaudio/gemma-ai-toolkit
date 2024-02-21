import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class Setup:
    def __init__(self, model_id, api_key=None, device_map="auto", torch_dtype=torch.bfloat16):
        self.api_key = api_key if api_key is not None else self.get_env_variable('API_KEY')
        self.model_id = model_id
        self.device_map = device_map
        self.torch_dtype = torch_dtype
        self.tokenizer = None
        self.model = None

    def initialize_chat_model(self):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_id,
                device_map=self.device_map,
                torch_dtype=self.torch_dtype,
            )
            print("Model loaded from cache.\n")
        except Exception as e:
            print("Model not found in cache. Attempting to download...\n")

            if self.api_key:
                self.tokenizer = AutoTokenizer.from_pretrained(self.model_id, token=self.api_key)
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_id,
                    token=self.api_key,
                    device_map=self.device_map,
                    torch_dtype=self.torch_dtype,
                )
            else:
                raise ValueError("API key is required to download the model.")
            
    def initialize_text_model(self):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_id)
            print("Model loaded from cache.\n")
        except Exception as e:
            print("Model not found in cache. Attempting to download...\n")

            if self.api_key:
                self.tokenizer = AutoTokenizer.from_pretrained(self.model_id, token=self.api_key)
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_id,
                    token=self.api_key
                )
            else:
                raise ValueError("API key is required to download the model.")

    def get_env_variable(self, var_name):
        import os
        try:
            return os.environ[var_name]
        except:
            try:
                from dotenv import load_dotenv
                load_dotenv()
                return os.environ[var_name]
            except ImportError:
                raise ImportError("dotenv package is not installed and the environment variable is not set.")
            except KeyError:
                raise KeyError(f"Environment variable {var_name} not found after loading dotenv.")