# Monoalphabetic Cipher Decryption 🔐

This repository contains Python scripts and text files used to decrypt a **monoalphabetic substitution cipher**.  
The decrypted result reveals *“The Clockmaker of Rothenburg”*, a short story used as a test corpus for frequency analysis and mapping accuracy.

---

## 📘 Project Overview
The project demonstrates classical cryptanalysis techniques — including:
- Frequency analysis
- Substitution mapping
- Manual adjustment of guessed letter mappings
- File-based encryption/decryption workflow

It is divided into several parts that handle encryption input, analysis, and output reconstruction.

---

## 📁 Repository Structure

| Folder | Description |
|--------|--------------|
| **data/** | Contains all encrypted, decrypted, and reference text files |
| **scripts/** | Python scripts implementing the decryption algorithms |
| **README.md** | Project description and usage guide |

---

## ⚙️ How to Run

```bash
# Run initial frequency analysis
python scripts/Task1.py

# Run main decryption logic
python scripts/Task3dec.py

# Optional: test mapping or re-generate decrypted output
python scripts/Oscar_hack.py
```

All outputs are written to `/data` directory as `.txt` files.

---

## 🧩 Key Files
- `mono_encrypted.txt` → Original cipher text  
- `mono_oscar_guess_final.txt` → Final letter mapping  
- `mono_decrypted.txt` / `decrypted_output.txt` → Fully decrypted result  
- `the_clockmaker_of_rothenburg.txt` → Original plaintext reference  

---

## 🧠 Technical Notes
- Python 3.10+ recommended  
- No external dependencies required (standard library only)  
- Can be extended to analyze multiple cipher variations (Caesar, Vigenère, etc.)

---

## ✍️ Author
**Abdullah Berkay Kürkçü**  
MSc Software Engineering — University of Europe for Applied Sciences (Berlin, Germany)  
🔗 [LinkedIn](https://www.linkedin.com/in/berkaykurkcu/) • [GitHub](https://github.com/Berkay-2)

---

## 📜 License
This project is released under the MIT License.  
You are free to use, modify, and distribute it for educational purposes.
