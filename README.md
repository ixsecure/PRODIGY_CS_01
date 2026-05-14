# Caesar Cipher Implementation

![Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat&logo=python&logoColor=white)
![Type](https://img.shields.io/badge/Type-Cryptography%20Tool-purple?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)
![Internship](https://img.shields.io/badge/Internship-Prodigy%20InfoTech-blue?style=flat)

> Python implementation of the Caesar Cipher — a classic substitution cipher used to encrypt and decrypt messages using a custom shift value.

---

## About

This project was developed as **Task 01** of the **Prodigy InfoTech** cybersecurity internship. It implements the Caesar Cipher algorithm in Python, one of the oldest and most well-known encryption techniques — and a fundamental concept in understanding modern cryptography.

---

## How it works

The Caesar Cipher works by shifting each letter in the message by a fixed number of positions in the alphabet.

```
Plaintext  : H  E  L  L  O
Shift      : 3
Ciphertext : K  H  O  O  R
```

| Direction | Operation |
|---|---|
| Encrypt | Shift letters forward by N positions |
| Decrypt | Shift letters backward by N positions |

---

## Features

- Encrypt a message with a custom shift value
- Decrypt an encrypted message
- Handles both uppercase and lowercase letters
- Preserves spaces and special characters unchanged
- Interactive menu — no arguments needed

---

## Usage

```bash
# Clone the repo
git clone https://github.com/ixsecure/PRODIGY_CS_01.git
cd PRODIGY_CS_01

# Run the tool
python cesar.py
```

```
Caesar Cipher Tool
==================
1. Encrypt a message
2. Decrypt a message
0. Exit

Choice: 1
Message : hello world
Shift   : 3

Result  : khoor zruog
```

---

## Examples

| Message | Shift | Result |
|---|---|---|
| hello | 3 | khoor |
| PYTHON | 13 | CLGUBA |
| Attack at dawn | 7 | Haahjr ha khdu |
| khoor | 3 (decrypt) | hello |

---

## Code

```python
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def main():
    print("Caesar Cipher Tool")
    print("==================")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("0. Exit\n")

    choice = input("Choice: ").strip()

    if choice == '0':
        print("Goodbye.")
        return

    if choice not in ['1', '2']:
        print("Invalid choice.")
        return

    mode = 'encrypt' if choice == '1' else 'decrypt'
    text = input("Message : ")
    shift = int(input("Shift   : "))

    result = caesar_cipher(text, shift, mode)
    print(f"\nResult  : {result}")


if __name__ == "__main__":
    main()
```

---

## Security Context

The Caesar Cipher is one of the simplest encryption techniques — and also one of the easiest to break. It has only **26 possible keys**, making it vulnerable to:

- **Brute force** — try all 26 shifts in seconds
- **Frequency analysis** — the most common letters in ciphertext reveal the shift

Understanding its weaknesses is exactly what makes it valuable for learning cryptography fundamentals. Modern encryption (AES, RSA) was built to solve these exact problems.

---

## What I learned

- Implementing a substitution cipher from scratch in Python
- Working with ASCII values and modular arithmetic
- Understanding why simple ciphers are cryptographically weak
- The difference between **encoding**, **encryption**, and **hashing**
- How frequency analysis defeats single-substitution ciphers

---

## Author

**Richmond Konan** — Junior Penetration Tester | Offensive Security | Cote d'Ivoire

- LinkedIn: https://linkedin.com/in/richmonddelmas
- GitHub: https://github.com/ixsecure
- Email: delmasrichmond@gmail.com

---

## Topics

`python` `cryptography` `caesar-cipher` `encryption` `decryption` `cybersecurity` `prodigy-infotech` `internship` `classical-cipher` `security-fundamentals`
