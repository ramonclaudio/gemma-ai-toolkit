from initializer import Initialize
from loading import Loading

class ChatAPI(Initialize):
    def __init__(self, model="google/gemma-2b-it", api_key=None, max_tokens=150):
        super().__init__(model, api_key)
        self.max_tokens = max_tokens
        self.initialize_chat_model()
        self.chat_history = []

    def chat(self):
        print("Start chatting with the model (type 'exit' or 'quit' to end the chat)")
        while True:
            user_input = input("[User]: ").strip()

            if user_input.lower() in ['exit', 'quit']:
                print("Exiting chat.")
                break

            if not user_input:
                print("Invalid input detected. Please enter a valid message.")
                continue

            model_response = self.assistant(user_input)
            print(f"[AI]: {model_response}")

    def assistant(self, user_message):
        loading = Loading()
        loading.start()

        self.chat_history.append({"role": "user", "content": user_message})

        prompt = self.tokenizer.apply_chat_template(self.chat_history, tokenize=False, add_generation_prompt=True)
        inputs = self.tokenizer.encode(prompt, add_special_tokens=True, return_tensors="pt")

        outputs = self.model.generate(input_ids=inputs.to(self.model.device), max_new_tokens=self.max_tokens)
        decoded_output = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        parts = decoded_output.split('\n')
        model_response_index = [i for i, part in enumerate(parts) if part == "model"][-1] + 1
        model_response = parts[model_response_index] if model_response_index < len(parts) else ""

        self.chat_history.append({"role": "model", "content": model_response})

        loading.stop()

        return model_response