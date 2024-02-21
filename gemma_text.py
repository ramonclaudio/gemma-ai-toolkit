from initializer import Initialize
from loading import Loading

class TextAPI(Initialize):
    def __init__(self, model="google/gemma-2b-it", api_key=None, max_tokens=150, prompt=None):
        super().__init__(model, api_key)
        self.max_tokens = max_tokens
        self.prompt = prompt.strip() if prompt else None
        self.initialize_text_model()

    def text(self):
        if not self.prompt:
            print("Invalid input detected. Please enter a valid message.")
            return
        model_response = self.assistant()
        print(f"[AI]: {model_response}")

    def assistant(self):
        loading = Loading()
        loading.start()

        inputs = self.tokenizer.encode(self.prompt, return_tensors="pt")
        outputs = self.model.generate(input_ids=inputs, max_new_tokens=self.max_tokens)
        decoded_output = self.tokenizer.decode(outputs[0])

        loading.stop()

        lines = [line for line in decoded_output.split('\n') if line and not line.startswith(('<bos>', '<eos>'))]

        if lines and lines[0] == self.prompt:
            lines = lines[1:]

        answer = ' '.join(lines).strip().replace("<eos>", "")

        return answer
