
import ast, io, tokenize, os, sys, platform, re, random, string, base64, hashlib, requests
from subprocess import *
from subprocess import DEVNULL as D, STDOUT as S
from Crypto import Random
from Crypto.Cipher import AES

def do_rename(pairs, code):
    for key in pairs:
        code = re.sub(fr"\b({key})\b", pairs[key], code, re.MULTILINE)
    return code

def remove_docs(source):
    io_obj = io.StringIO(source)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        if token_type == tokenize.COMMENT:
            pass
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
                if prev_toktype != tokenize.NEWLINE:
                    if start_col > 0:
                        out += token_string
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    out = '\n'.join(l for l in out.splitlines() if l.strip())
    return out

def _call(*a):
    return call(*a, stdout=D,stderr=S)


def carbon(code):
    code = remove_docs(code)
    """parsed = ast.parse(code)

    funcs = {
        node for node in ast.walk(parsed) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    classes = {
        node for node in ast.walk(parsed) if isinstance(node, ast.ClassDef)
    }
    args = {
        node.id for node in ast.walk(parsed) if isinstance(node, ast.Name) and not isinstance(node.ctx, ast.Load)
    }
    attrs = {
        node.attr for node in ast.walk(parsed) if isinstance(node, ast.Attribute) and not isinstance(node.ctx, ast.Load)
    }
    for func in funcs:
        if func.args.args:
            for arg in func.args.args:
                args.add(arg.arg)
        if func.args.kwonlyargs:
            for arg in func.args.kwonlyargs:
                args.add(arg.arg)
        if func.args.vararg:
            args.add(func.args.vararg.arg)
        if func.args.kwarg:
            args.add(func.args.kwarg.arg)

    pairs = {}
    used = set()
    for func in funcs:
        if func.name == "__init__":
            continue
        newname = "".join(random.choice(["I", "l"]) for i in range(random.randint(8, 20)))
        while newname in used:
            newname = "".join(random.choice(["I", "l"]) for i in range(random.randint(8, 20)))
        used.add(newname)
        pairs[func.name] = newname

    for _class in classes:
        newname = "".join(random.choice(["I", "l"]) for i in range(random.randint(8, 20)))
        while newname in used:
            newname = "".join(random.choice(["I", "l"]) for i in range(random.randint(8, 20)))
        used.add(newname)
        pairs[_class.name] = newname

    for arg in args:
        newname = "".join(random.choice(["I", "l"]) for i in range(random.randint(8, 20)))
        while newname in used:
            newname = "".join(random.choice(["I", "l"]) for i in range(random.randint(8, 20)))
        used.add(newname)
        pairs[arg] = newname

    for attr in attrs:
        newname = "".join(random.choice(["I", "l"]) for i in range(random.randint(8, 20)))
        while newname in used:
            newname = "".join(random.choice(["I", "l"]) for i in range(random.randint(8, 20)))
        used.add(newname)
        pairs[attr] = newname"""
    pairs = {}

    string_regex = r"('|\")[\x1f-\x7e]{1,}?('|\")"

    original_strings = re.finditer(string_regex, code, re.MULTILINE)
    originals = []

    for matchNum, match in enumerate(original_strings, start=1):
        originals.append(match.group().replace("\\", "\\\\"))

    placeholder = os.urandom(16).hex()
    code = re.sub(string_regex, f"'{placeholder}'", code, 0, re.MULTILINE)

    for i in range(len(originals)):
        for key in pairs:
            originals[i] = re.sub(r"({.*)(" + key + r")(.*})", "\\1" + pairs[key] + "\\3", originals[i], re.MULTILINE)

    cycles = [
        "[   > >                                                                                           ]", 
        "[   > > > >                                                                                       ]", 
        "[   > > > > > >                                                                                   ]", 
        "[   > > > > > > > >                                                                               ]", 
        "[   > > > > > > > > > >                                                                           ]", 
        "[   > > > > > > > > > > > >                                                                       ]", 
        "[   > > > > > > > > > > > > > >                                                                   ]", 
        "[   > > > > > > > > > > > > > > > >                                                               ]", 
        "[   > > > > > > > > > > > > > > > > > >                                                           ]", 
        "[   > > > > > > > > > > > > > > > > > > > >                                                       ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > >                                                   ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > >                                               ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > >                                           ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > >                                       ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >                                   ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >                               ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >                           ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >                       ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >                   ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >               ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >           ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >       ]", 
        "[   > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > > >   ]", 
    ]

    i = int(0)

    while True:
        print("\r"+f"        {cycles[i]}", end="")
        i += 1
        if i == len(cycles):
            i = int(0)
        found = False
        code = do_rename(pairs, code)
        for key in pairs:
            if re.findall(fr"\b({key})\b", code):
                found = True
        if found == False:
            break

    replace_placeholder = r"('|\")" + placeholder + r"('|\")"
    for original in originals:
        code = re.sub(replace_placeholder, original, code, 1, re.MULTILINE)
    print("\r"+f"        {cycles[len(cycles) -1]}\n\n", end="")
    return code
def update():_call(['pip','install','git+https://github.com/Ovlic/anubis-ovlic']);exit("Restart the program to continue.")


class Encryption:

    def __init__(self, key, text=False): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key).digest()
        self.text = False

    def encrypt(self, raw):
        raw = self._pad(str(raw))
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode())).decode()

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)


    def write(self, key, source):
        wall = "__HAHA_THE_CODE_IS_ENCRYPTED_TOO__" * 25
        newcode = f"{wall}{key}{wall}"
        for line in source.split("\n"):
            newcode += self.encrypt(line) + wall
        if self.text == False:
            code = f"import ancrypt\nancrypt.load(__file__)\n'''\n{newcode}\n'''"
        else:
            code = newcode

        code = base64.b64encode(bytes(base64.b85encode(code.encode())))
        return code
