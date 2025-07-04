# message from the stars

Category: Forensics

## Challenge Difficulty

medium

## Challenge Description
Bob's gone missing. There's some browser history from Edge. We're still running the investigation but could you take a look at this?

Flag format is the manufacturer of the computer and the last time he went to his most visited website in GMT+8. Eg NYP{Apple,25/02/2014/3:58:09PM}

[Download Bookmarks](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/Bookmarks)


## Solution
- From a quick analysis of the file, we find out his most visited website is **Transient Luminous Events – Backyardastronomy.net**
  
![image](https://github.com/user-attachments/assets/9d9f947c-8ea0-43ba-a3a6-6c9fb8a102b2)

- We can also find the last time he went to his most visited website. Do note that the time is in WebKit timestamps and needs to be converted to human-readable
  
![image](https://github.com/user-attachments/assets/8bdffa4d-1cf7-4e88-b61a-d177db03e1cf)

- After conversion, we know the time is **31/05/2025/17:57:55**; however, the flag uses 12-hour clock, so it becomes **31/05/2025/5:57:55PM**
- The file also shows that he visited 3 laptop support websites. We can therefore understand that his laptop has to be one of the manufacturers and we can guess it

![image](https://github.com/user-attachments/assets/3726a07d-9902-4f9b-b341-0ef374248f27)

- Upon guessing, we find out that Lenovo is the correct match 


### Flag
    NYP{Lenovo,31/05/2025/5:57:55PM}
