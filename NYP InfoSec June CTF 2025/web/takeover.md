# takeover

Category: web

## Challenge Difficulty

very easy

## Challenge Description
Somethings taking over...

[Download home.html](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/home.html)

[Download flag.html](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/flag.html)

[Download robots.txt](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/robots.txt)

[Download style.css](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/style.css)


## Solution

- Opening home.html gives us this
  
<img width="914" alt="image" src="https://github.com/user-attachments/assets/438497f1-45c1-4bcb-858c-d2fc2f3738b8" />

- They suggested that we look around, we then inspected the code
  
<img width="238" alt="image" src="https://github.com/user-attachments/assets/0a7b637f-c7d9-45c8-b3a1-675620812c8f" />

- We then inspected style.css based on the hint

- This was all the CSS provided
  
<img width="277" alt="image" src="https://github.com/user-attachments/assets/47c803a3-a264-4179-b308-420b8b07437c" />

- We then proceed to inspect the remaining 2 files, robot.txt and flag.html
- robot.txt is a file used by websites to tell web crawlers (robots) like Googlebot which parts of the site they are allowed or not allowed to access.

<img width="138" alt="image" src="https://github.com/user-attachments/assets/dcd3bf73-223f-4044-888c-9aee4b9778e3" />

    User-agent: *
means the rule applies to all web crawlers. "*" is a wildcard symbol that represents any bot

    Disallow: /flag.html/
This tells the bots not to access any URLs that start with /flag.html/.

- robot.txt hints that the flag is in flag.html
- flag.html hints "Maybe you can write a robot to find the flag for you"
- The file just contains a long string, and we can therefore write a [script](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/flag.py) that searches for "NYP"
- This script might not be the best
- At the end of the output, it shows the flag
  
<img width="318" alt="image" src="https://github.com/user-attachments/assets/9b908fb0-85ff-418b-95a4-b41b0f64c182" />

- Not sure if this is the intended method of solving 

### Flag
    NYP{r0b0ts_ar3_sc4ry}
