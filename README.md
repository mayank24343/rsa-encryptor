# Cryptography Toolkit - RSA & Matrix Cipher in Python

A Python-based cryptography project implementing:

* RSA Encryption & Decryption
* Matrix Shift Cipher
* Brute Force Cryptanalysis

The project demonstrates both encryption techniques and basic attacks used to break weak cryptographic systems.

---

# Features

## RSA Encryption System

* Random prime number generation
* Public & private key generation
* RSA encryption
* RSA decryption
* Euler Totient (`phi`) computation
* GCD computation
* Modular inverse calculation

---

## Matrix Shift Cipher

* Custom matrix-based substitution cipher
* Randomized shift generation
* Character mapping using 8×8 matrix
* Encryption & decryption support

---

## Cryptanalysis / Brute Force

* RSA brute-force cracking using prime factorization
* Matrix cipher brute-force decryption
* English word validation using Dictionary API

---

# Project Structure

```text id="r8g1do"
.
├── rsa.py
├── new.py
├── brute.py
└── main.py
```

---

# File Overview

## `rsa.py`

Implements the RSA cryptosystem.

### Features

* Prime selection
* Key generation
* Encryption
* Decryption
* GCD calculation
* Modular inverse computation

### Important Functions

```python id="mq2brf"
create_keys()
```

Generates:

* Public key
* Private key

---

```python id="f6o7rm"
encrypt(plaintext, e, n)
```

Encrypts plaintext using RSA.

---

```python id="mrh95j"
decrypt(ciphertext, d, n)
```

Decrypts RSA encrypted text.

---

# `new.py`

Implements a custom matrix-based cipher.

## Cipher Design

Uses an 8×8 matrix of:

* lowercase letters
* uppercase letters
* numbers
* punctuation

---

## Features

* Random shift generation
* Matrix substitution encryption
* Matrix decryption

### Important Functions

```python id="uwmduq"
encrypt(text)
```

Encrypts text using randomized matrix shifts.

---

```python id="6rlv5u"
decrypt(text, step)
```

Decrypts matrix encrypted text.

---

# `brute.py`

Implements brute-force attacks.

---

## RSA Attack

Attempts to:

* Factorize `n`
* Recover private key
* Decrypt ciphertext

### Method Used

* Trial division prime factorization

---

## Matrix Cipher Attack

Attempts all possible matrix shifts:

* Tests decrypted outputs
* Validates English words using API

### Important Functions

```python id="eb3c3o"
breakrsa(public_key, encrypted_text)
```

```python id="8vix6y"
breakmatrix(text)
```

---

# `main.py`

Provides a command-line menu system for interacting with the project.

---

# Supported Operations

| Option | Functionality                        |
| ------ | ------------------------------------ |
| A      | RSA Encryption                       |
| B      | RSA Decryption via Brute Force       |
| C      | Matrix Cipher Encryption             |
| D      | Matrix Cipher Brute Force Decryption |

---

# Example Workflow

## RSA Encryption

```text id="fwccaf"
Enter Choice: A
Enter Text: hello

Encrypted Text: ...
Public Key: [e, n]
```

---

## RSA Cracking

```text id="mv6ozf"
Enter Choice: B
Enter Text: ...
Enter Public Key: [e, n]

Decrypted Text: hello
```

---

## Matrix Encryption

```text id="t1j7nl"
Enter Choice: C
Enter Text: secret message

Encrypted Text: ...
```

---

## Matrix Brute Force

```text id="1l1v9j"
Enter Choice: D
Enter Text: ...

Possible Decryptions:
...
```

---

# Concepts Demonstrated

## Cryptography

* RSA algorithm
* Public key cryptography
* Symmetric substitution cipher
* Modular arithmetic

---

## Cryptanalysis

* RSA factorization attack
* Brute-force decryption
* Weak key vulnerabilities

---

## Programming Concepts

* Recursion
* Matrix traversal
* API requests
* Randomized algorithms
* Modular software design

---

# Technologies Used

* Python
* Requests Library
* Basic Number Theory
* REST API Integration

---

# Installation

## Install Dependencies

```bash id="4t49dy"
pip install requests
```

---

# Run the Project

```bash id="4pd67j"
python main.py
```

---

# Educational Purpose

This project was created for educational purposes to demonstrate:

* How RSA works internally
* How weak RSA implementations can be broken
* Basics of substitution ciphers
* Practical cryptanalysis techniques

---

# Limitations

* RSA implementation uses very small primes and is NOT secure.
* Intended only for learning and demonstration.
* Brute-force attacks become infeasible for real-world RSA key sizes.
* Matrix cipher is a toy encryption scheme and not cryptographically secure.

---

# Future Improvements

* Large prime RSA generation
* Fast modular exponentiation
* Secure padding schemes
* GUI interface
* File encryption support
* Stronger cryptographic primitives
* Performance optimizations
