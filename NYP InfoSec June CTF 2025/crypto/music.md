# music

Category: crypto

## Challenge Difficulty

very easy

## Challenge Description
There is a place I wanna visit for inspiration to continue!

[Download challenge.txt](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/challenge(1).txt)


## Solution

- The ciphertext is 

        SILAMI
        DOLAFAMI
        REMIDOLAFA

- These seem to resemble **solfège syllables** (Do, Re, Mi, Fa, Sol, La, Ti) used in music.
- We will then breakdown the ciphertext to extract the solfège syllables
    1. SILAMI
  Breakdown:  SI - LA - MI
  
  Solfège: SI LA MI
  
  2. DOLAFAMI
  Breakdown: DO - LA - FA - MI
  
  Solfège: DO LA FA MI
  
  3. REMIDOLAFA
  Breakdown: RE - MI - DO - LA - FA
  
  Solfège: RE MI DO LA FA

- Now, we convert the Solfège to notes 
    - DO = C

    - RE = D

    - MI = E

    - FA = F

    - SOL = G

    - LA = A

    - SI = B
 
    1. SI LA MI → B A E
    2. DO LA FA MI → C A F E
    3. RE MI DO LA FA → D E C A F


### Flag
    NYP{BAE_CAFE_DECAF}

