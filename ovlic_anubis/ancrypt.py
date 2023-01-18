import base64, hashlib, os, tempfile
from Crypto.Cipher import AES

class Anubis:

    def __init__(self, key): 
        self.bs = AES.block_size
        self.key = hashlib.sha256(key).digest()

    def decrypt(self, enc):
        enc = base64.b64decode(str(enc))
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

def load(file, text=False):
    if text == False:
        with open(file, "r") as f:
            obfcode = f.read()
    else:
        obfcode = file
    obfcode = base64.b85decode(base64.b64decode(bytes(obfcode))).decode()
    obfcode = obfcode.replace("import ancrypt\nancrypt.load(__file__)\n'''", "").replace("\n'''", "")
    listed = obfcode.split("__HAHA_THE_CODE_IS_ENCRYPTED_TOO__" * 25)
    del listed[0]; del listed[-1]
    key = listed[0].encode()
    del listed[0]
    anubis = Anubis(key)
    src = ""
    for i in listed:
        src += anubis.decrypt(i) + "\n"

    try:
        n_src = src.split("daemon=True).")[1].split("()")[0]
        src = src.replace(n_src, "start")
    except IndexError:
        pass
        #print("IndexError")
        
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(src.encode())
    #test = subprocess.check_output(["python3", "-m", "py_compile", tmp.name]).decode('utf-8')
    """test = ""
    def run_command():
        print(tmp.name)
        process = subprocess.Popen(["python3", "-m", "py_compile", tmp.name], stdout=subprocess.PIPE)
        process.wait()
        while True:
            output = process.stdout.readline().decode('utf-8')
            if output == '' and process.poll() is not None:
                print("Output is blank and process poll is not none")
                break
            if output:
                print("Output!!!")
                print(output.strip())
            
            print(f"Output: '{output}'")
            print(f"process.poll(): '{process.poll()}'")
            time.sleep(1)
        rc = process.poll()
        return rc

    #r = run_command()
    #print(r)
    #p = subprocess.run([sys.executable, tmp.name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)#.decode('utf-8')#py_compile.compile(tmp.name)#, doraise=False, quiet=False)

    print("Test")
    line = test.find("SyntaxError")
    print(line)
    #print(test.stdout)
    #for line in test.stdout:
        #print("Line")
        #print(line)

    #print(f"test: {test}")

    if "SyntaxError: invalid syntax" in test:
        print("Syntax Error!")

    if "Hello!" in test:
        print("hi")

    p = subprocess.Popen([sys.executable, tmp.name],shell=False,stdout=subprocess.PIPE)
    #print(p)
    print("HERE")
    tmp.close()
    p.wait()
    while True:
        output = p.stdout.readline()
        if p.poll() is not None:
            print("break")
            break
        if output:
            print(output.strip())
        rc = p.poll()"""

    decoded = src#.encode()
    #print(decoded)
    os.unlink(tmp.name) # Deletes temp file
    if text == True:
        return decoded
    
