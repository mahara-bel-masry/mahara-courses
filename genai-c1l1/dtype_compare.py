"""dtype_compare.py - الدرس الأول: نفس الـ prompt بدقة bfloat16 وبدقة float32،
تشغيل واحد، سجل واحد، لمقارنة ترتيب المرشحين بين الدقتين."""
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForCausalLM

NAME = "HuggingFaceTB/SmolLM2-135M-Instruct"
tok = AutoTokenizer.from_pretrained(NAME)

def top5(model, prompt, tag):
    ids = tok(prompt, return_tensors="pt")
    with torch.no_grad():
        logits = model(**ids).logits[0, -1]
    probs = F.softmax(logits, dim=-1)
    top = torch.topk(probs, 5)
    print(f"\ntop5 ({tag}) for prompt: {prompt!r}")
    for i, v in zip(top.indices, top.values):
        print(f"   {tok.decode([i])!r}  {float(v):.6f}")

for dt, tag in [(torch.bfloat16, "bfloat16"), (torch.float32, "float32")]:
    model = AutoModelForCausalLM.from_pretrained(NAME, dtype=dt)
    top5(model, "Generative AI models work by predicting the next", tag)
    top5(model, "The capital of Egypt is", tag)
    del model
