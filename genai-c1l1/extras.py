"""extras.py - الدرس الأول: ids وقطع الـ tokenizer (إنجليزي وعربي)،
temperature عالية، سؤال كاذب المقدمة. float32 صريح. السحب unseeded."""
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

NAME = "HuggingFaceTB/SmolLM2-135M-Instruct"
DTYPE = torch.float32
tok = AutoTokenizer.from_pretrained(NAME)
model = AutoModelForCausalLM.from_pretrained(NAME, dtype=DTYPE)
print("vocab size:", tok.vocab_size, "| len(tokenizer):", len(tok))
print("dtype:", DTYPE)

for prompt in ["Generative AI models work by predicting the next",
               "The capital of Egypt is",
               "عاصمة مصر القاهرة"]:
    ids = tok(prompt)["input_ids"]
    pieces = [tok.decode([i]) for i in ids]
    print(f"\nprompt: {prompt}")
    print("count:", len(ids))
    print("ids:", ids)
    print("pieces:", pieces)

print("\n--- temperature 1.2 (sampling, top_p=1.0, top_k=0, unseeded), تلات مرات ---")
prompt = "The best way to learn programming is"
ids = tok(prompt, return_tensors="pt")
for _ in range(3):
    with torch.no_grad():
        out = model.generate(**ids, max_new_tokens=20, do_sample=True,
                             temperature=1.2, top_p=1.0, top_k=0)
    print(tok.decode(out[0], skip_special_tokens=True))

print("\n--- جمل كاذبة المقدمة، اختيار حتمي ---")
for q in ["The capital of the planet Mars is",
          "The three moons of Earth are",
          "The winner of the 2030 World Cup was"]:
    ids = tok(q, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**ids, max_new_tokens=25, do_sample=False)
    print(q)
    print("->", tok.decode(out[0], skip_special_tokens=True))
