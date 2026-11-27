"""temperature.py - الدرس الأول: قارن الموديل عند temperature صفر وعند قيمة أعلى.
float32 صريح. السحب بـ do_sample=True مع top_p=1.0 و top_k=0 (يتعادلوا،
يعني المتغير الوحيد هو temperature). من غير بذرة ثابتة: نصوص السحب بتختلف
من تشغيلة لتشغيلة، بس السلوك العام ثابت. جرّب 0.5 و1.0 و1.5 بنفسك."""
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

NAME = "HuggingFaceTB/SmolLM2-135M-Instruct"
DTYPE = torch.float32
tok = AutoTokenizer.from_pretrained(NAME)
model = AutoModelForCausalLM.from_pretrained(NAME, dtype=DTYPE)
prompt = "The best way to learn programming is"

def gen(**kw):
    ids = tok(prompt, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**ids, max_new_tokens=20, **kw)
    return tok.decode(out[0], skip_special_tokens=True)

print("--- temperature zero (greedy), مرتين ورا بعض ---")
for _ in range(2):
    print(gen(do_sample=False))

TEMP = 0.8  # جرّب 0.5 أو 1.0 أو 1.5 هنا
print(f"--- temperature {TEMP} (sampling, top_p=1.0, top_k=0, unseeded), تلات مرات ---")
for _ in range(3):
    print(gen(do_sample=True, temperature=TEMP, top_p=1.0, top_k=0))
