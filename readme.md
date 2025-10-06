# PerlClip + Local Server Setup

## Overview
This guide explains how to set up and run **PerlClip** alongside a local HTTP server for testing.

---

## About PerlClip
**PerlClip**  
By **James Bach and Danny Faught**  
(Uses **Win32::Clipboard**, by Aldo Calpini)  

This program is released under the **GPL 2.0 license**.

Sometimes you need to test a text field with different kinds of stressful inputs. But it can be a pain to prepare the text strings. **PerlClip** is a tool that helps you do that.  

PerlClip places prepared text into the clipboard so you can paste it wherever you need it.  
Press **Ctrl+C** to exit the program.

You can run the Perl script, or click on the EXE version (a DOS console window appears when you do that).  

Enter the text pattern you want to produce. You can enter the following things:

---

### Examples of Patterns

- **Basic strings:**
  - `"james"` → produces `james`
  - `"james" x 5` → produces `jamesjamesjamesjamesjames`
  - `"a" x (2 ** 16)` → produces a string of `"a"` 2^16 (65536) in length  
  - `chr(13) x 10` → produces ten carriage returns  
  - `"X" x 1000000` → produces a string of one million X's  
  - `join "\r\n", (1..100)` → produces numbers 1 to 100, each on a new line  

- **Special Patterns:**
  - `$allchars` → produces all character codes from 1 to 255 (excluding 0).  
  - `counterstring {num} [{char}]` → produces a string that counts its own characters.  

    Example:
    - `counterstring 10` → `*3*5*7*10*` (a 10-character-long string)
    - `counterstring 15 A` → `A3A5A7A9A12A15A`

- **Text File:**
  - `textfile {name}` → loads the contents of a specified text file into the clipboard.

- **Bisecting Commands:**
  - `u:` ("bisect up") → after two consecutive counterstring commands, returns a counterstring halfway between the two lengths.
  - `d:` ("bisect down") → similar to `u:` but for bisecting downward.

- **Help:**
  - `help` → prints these instructions.

When you see **"Ready to Paste!"**, the clipboard is prepared.

---

## Requirements
- Python 3.x  
- Perl installed on your system  
- `perlclip.pl` file  
- `index.html` (optional for frontend testing)  

---

## Installation

### 1. Install Python packages
```bash
pip install flask flask-cors
```

### 2. Run PerlClip
```bash
perl perlclip.pl
```

You’ll see something like:
```
Pattern:
"hello"
*** Copied to Linux clipboard. You can paste it now.
*** Ready to Paste!
```

---

## Running a Local HTTP Server

You can serve your HTML frontend using Python’s built-in server:

```bash
python3 -m http.server 8080
```

Access it in your browser:  
👉 [http://0.0.0.0:8080/](http://0.0.0.0:8080/)  
(or [http://localhost:8080](http://localhost:8080))

---

## Using Flask API (Optional)
If you want to handle text updates via API, save the following as `server.py`:

```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_text = ""

@app.route('/update', methods=['POST'])
def update_text():
    global latest_text
    data = request.json
    latest_text = data.get("text", "")
    return jsonify({"status": "ok"})

@app.route('/latest', methods=['GET'])
def get_latest():
    return jsonify({"text": latest_text})

if __name__ == "__main__":
    app.run(port=8081)
```

Run it:
```bash
python3 server.py
```

---

## Usage
1. Open **two terminals**:
   - Terminal 1 → Run `perl perlclip.pl`  
   - Terminal 2 → Run `python3 -m http.server 8080` or `python3 server.py`  

2. Open the browser and visit:  
👉 [http://localhost:8080/](http://localhost:8080/)  

3. In the PerlClip terminal, type your desired pattern, e.g.:  
```bash
"james" x 5
```

4. Paste it into any input field on your web page or app.

---

## Exiting PerlClip
Press **Ctrl+C** in the PerlClip terminal to exit.

---

## License
Released under **GPL 2.0**.  
Original authors: **James Bach** and **Danny Faught**.  
Clipboard library by **Aldo Calpini**.