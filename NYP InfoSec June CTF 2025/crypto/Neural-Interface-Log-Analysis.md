# Neural Interface Log Analysis

Category: crypto

## Challenge Difficulty

easy

## Challenge Description
The Nova Sentinel's neural interface system logs have been tampered with during an alien cyberattack. Hidden within the standard operational logs are covert commands inserted by the attackers. As a neural interface specialist, you must analyse these logs, extract the attacker’s messages, and decode their hidden commands to uncover their intentions and the stolen flag.

[Download interface_specs.txt](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/interface_specs.txt)

[Download neural_logs.txt](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/neural_logs.txt)

## Solution

- From analysis of the neural_logs.txt file, we can see that the attacker's messages are encoded with XOR encryption using a secret key and Base64
- We then extract the attacker's messages, and we can also see that the encryption key is given, as well as the Base64-encrypted string
  
![image](https://github.com/user-attachments/assets/1e48e408-41c4-45e5-8bea-c6c2d195c7a2)

- Decrypt the Base64 string using CyberChef

![image](https://github.com/user-attachments/assets/53c4bb03-3bdd-48db-97e8-f2a13e7dc7b9)

- Base64 String:

      DxUZPgBsHhdtDRN4C3lsGQNtAn8WF31qfHULcggWJAw8DyAfJgQgDzM=

- Base64 decode this to get the XOR-encrypted bytes using a [python script](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/log.py)
- Run the script, and we get our flag

<img width="252" alt="image" src="https://github.com/user-attachments/assets/d1c28f5f-b6bb-4c19-a18d-e62de5c1bea5" />


### Flag
    NYP{N3UR4L_1N73RF4C3_R3570R3D_aBcDeFgHiJ}
