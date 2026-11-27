"""next_token.py - الدرس الأول: شوف أعلى خمس توكنز مرشحة للتوكن الجاي.
يطبع بالظبط المخرجات المقتبسة في الدرس: float32 صريح، ستة كسور عشرية."""
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForCausalLM

NAME = "HuggingFaceTB/SmolLM2-135M-Instruct"
DTYPE = torch.float32
tok = AutoTokenizer.from_pretrained(NAME)
model = AutoModelForCausalLM.from_pretrained(NAME, dtype=DTYPE)

def top5(prompt):
    ids = tok(prompt, return_tensors="pt")
    with torch.no_grad():
        logits = model(**ids).logits[0, -1]
    probs = F.softmax(logits, dim=-1)
    top = torch.topk(probs, 5)
    print(f"\ntop5 (float32, 6 decimals) for prompt: {prompt!r}")
    for i, v in zip(top.indices, top.values):
        print(f"   {tok.decode([i])!r}  {float(v):.6f}")

top5("Generative AI models work by predicting the next")
top5("The capital of Egypt is")

# توليد حتمي (greedy) لأول جملة - المقتبس في قسم المفهوم
prompt = "Generative AI models work by predicting the next"
ids = tok(prompt, return_tensors="pt")
with torch.no_grad():
    out = model.generate(**ids, max_new_tokens=20, do_sample=False)
print(f"\ngeneration (greedy) for {prompt!r}:")
print("->", repr(tok.decode(out[0], skip_special_tokens=True)))
