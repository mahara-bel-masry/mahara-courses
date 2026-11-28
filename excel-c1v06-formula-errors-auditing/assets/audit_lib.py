# a small audit helper: my own script, NOT Excel's Error Checking
# and NOT Excel's Trace arrows. It reads formulas with openpyxl's
# tokenizer and uses LibreOffice values.
import re
from openpyxl.formula import Tokenizer
from openpyxl.formula.translate import Translator
from openpyxl.utils import range_boundaries, get_column_letter

REF = re.compile(r"^(?:'?([^'!]+)'?!)?(\$?[A-Z]{1,3}\$?\d+)(?::(\$?[A-Z]{1,3}\$?\d+))?$")


def refs(formula, sheet):
    # list of (sheet, first_cell, last_cell) the formula points at
    out = []
    for t in Tokenizer(formula).items:
        if t.type == "OPERAND" and t.subtype == "RANGE":
            m = REF.match(t.value)
            if m:
                a = m.group(2).replace("$", "")
                b = (m.group(3) or m.group(2)).replace("$", "")
                out.append((m.group(1) or sheet, a, b))
    return out


def cells_of(a, b):
    c1, r1, c2, r2 = range_boundaries(f"{a}:{b}")
    return [f"{get_column_letter(c)}{r}" for r in range(r1, r2 + 1)
            for c in range(c1, c2 + 1)]


def precedents(wb, sheet, cell):
    f = wb[sheet][cell].value
    if not (isinstance(f, str) and f.startswith("=")):
        return []
    out = []
    for sh, a, b in refs(f, sheet):
        out += [(sh, c) for c in cells_of(a, b)]
    return out


def dependents(wb, sheet, cell):
    out = []
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("="):
                    for sh, a, b in refs(c.value, ws.title):
                        if sh == sheet and cell in cells_of(a, b):
                            out.append((ws.title, c.coordinate))
                            break
    return out
