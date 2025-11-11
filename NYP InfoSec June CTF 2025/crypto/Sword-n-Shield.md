# Sword n Shield

Category: Crypto

## Challenge Difficulty
very easy

## Challenge Description
swords are cools!

[Download challenge.txt](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/challenge.txt)

## Solution

- The .txt file only has the words "Sword" and "Shield", suggesting a binary relationship
- Convert Sword = "0" and Shield to "1". Split binary into 8-bit binary chunks. Convert binary chunks to ASCII characters
- Alternatively, you can run the script, and the flag can be derived
[sword-n-shield.py](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/sword-n-shield.py)


### Flag
    NYP{p0k3m0n_sw0rd_sh13ld}
