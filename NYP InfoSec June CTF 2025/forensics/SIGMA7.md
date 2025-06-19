# SIGMA7 

Category: Forensics

## Description
One file. No metadata. Something's off.

Noise is just a signal you haven't decoded yet.

[Download sigma](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/sigma.jpg)

## Solution 
- From the description, we understand that there is no metadata 
- Uploaded image into https://www.aperisolve.com/, which has binwalk and exiftool to help us find hidden data
- binwalk reveals that there is a hidden zip folder inside
- binwalk and exiftool also can be used on Kali Linux 
  
<img width="844" alt="image" src="https://github.com/user-attachments/assets/22cd0121-deb8-44c7-8c68-220a3c268fb1" />

- Download the zip folder to reveal contents

<img width="550" alt="image" src="https://github.com/user-attachments/assets/8920377e-4b69-4f60-8599-21de87988180" />

<img width="551" alt="image" src="https://github.com/user-attachments/assets/90e2c845-22f4-4828-81b4-42663a8949aa" />

[Download .txt file](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/01000110%2001101100%2001100001%2001100111%2000001010.txt)
- .txt file contains HTML entity encoding that represents ASCII values "QBS{CLS_LQVLGH_WKH_SLASHO}"
- We know the flag is NYP{}, and we compare QBS against NYP. It is a shift of 3 positions backwards
- Decode the ciphertext, and we can get our flag
  
- <img width="806" alt="image" src="https://github.com/user-attachments/assets/6c0957b4-c402-4901-982e-475f9a352200" />


### FLAG
    NYP{ZIP_INSIDE_THE_PIXPEL}
