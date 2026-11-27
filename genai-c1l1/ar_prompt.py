"""ar_prompt.py - الدرس الأول: نفس ميكانيكا التوكن الجاية على prompts عربية،
ومقارنة توليد إنجليزي/عربي/لهجة/أحداث جارية. float32 صريح، اختيار حتمي (greedy)."""
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

def gen(prompt, n=15):
    ids = tok(prompt, return_tensors="pt")
    with torch.no_grad():
        out = model.generate(**ids, max_new_tokens=n, do_sample=False)
    print(f"\ngeneration (greedy) for {prompt!r}:")
    print("->", repr(tok.decode(out[0], skip_special_tokens=True)))

top5("ما هي عاصمة")
top5("عاصمة مصر")

gen("ما هي عاصمة", n=8)
gen("What is the capital of France?")
gen("ما هي عاصمة فرنسا؟")
gen("عايز أعرف أسعار الشحن يا برنس")
gen("مين فاز في انتخابات الرئاسة الأمريكية 2028؟")
