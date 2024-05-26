from summarylm.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
    
    def predict(self, text, max_length):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": max_length}

        pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]

        return output