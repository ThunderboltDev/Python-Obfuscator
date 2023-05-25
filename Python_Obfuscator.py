import tkinter as tk
import tkinter.messagebox as mbox
import base64
import marshal
import random
import string

class ObfuscatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Python Script Obfuscator")
        master.geometry("800x600")

        self.label_imports = tk.Label(master, text="Enter Imports for the script:")
        self.label_imports.pack()

        self.text_box_imports = tk.Text(master, height=2, width=60)
        self.text_box_imports.pack()

        self.label_script = tk.Label(master, text="Enter your Python script here:")
        self.label_script.pack()

        self.text_box_script = tk.Text(master, height=10, width=60)
        self.text_box_script.pack()

        self.label_obfuscated = tk.Label(master, text="Obfuscated script:")
        self.label_obfuscated.pack()

        self.text_box_obfuscated = tk.Text(master, height=10, width=60)
        self.text_box_obfuscated.pack()

        self.button_obfuscate = tk.Button(master, text="Obfuscate", command=self.obfuscate)
        self.button_obfuscate.pack()

    def obfuscate(self):
        imports = self.text_box_imports.get("1.0", tk.END)
        code = self.text_box_script.get("1.0", tk.END)

        obfuscated_code = base64.b64encode(marshal.dumps(compile(imports + code, "<string>", "exec")))
        with open('Obfuscated.py', 'w') as f:
            f.write(f'''import base64
import marshal\n
{imports} \n

#OBFUSCATED BY JUPITER USING BASE64 AND MARSHAL - GITHUB PAGE: https://github.com/ThunderboltDev
antivmobfuscated = {obfuscated_code}

antivmdecode = marshal.loads(base64.b64decode(antivmobfuscated))

exec(antivmdecode)

''')
        mbox.showinfo("Saved!", "Python file saved as Obfuscated.py")
        # set obfuscated script in second text box
        self.text_box_obfuscated.delete("1.0", tk.END)
        self.text_box_obfuscated.insert("1.0", obfuscated_code)
        

root = tk.Tk()
obfuscator_gui = ObfuscatorGUI(root)
root.mainloop()
