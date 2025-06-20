# Travelling Intern

Category: osint

## Challenge Difficulty

medium

## Challenge Description
While we're dealing with the aftermath of the cyberattack, one of our lead investigators has taken the liberty to go on a vacation without informing anyone. We need to track down their whereabouts and ensure they are safe. Can you help us find them?

Flag format: NYP{location_they_are_at} (lowercase separated by underscore)

[Download travelling_intern2](https://github.com/Diablo2912/CTF-Writeups/blob/main/NYP%20InfoSec%20June%20CTF%202025/.files/travelling_intern2.HEIC)

## Solution
- We find out that the image contains metadata
  
![image](https://github.com/user-attachments/assets/c0b11bd7-1e54-47b4-acb6-b7865dca5a40)

- From further investigation, we find out that the location is on a street **Matsubara dori**, so we use Google Maps to find out more
    
![image](https://github.com/user-attachments/assets/9c241196-0cb8-4b23-bd94-74e53426d122)

- We can also see the Japanese name of the location, which is **朝日陶庵**. From a quick search in Google Maps, we can find the location

![image](https://github.com/user-attachments/assets/1d1a2a89-dcdd-459a-bb15-7eb301ed32c2)
 
![image](https://github.com/user-attachments/assets/97b6cc1a-3fc6-4673-bd88-81dbf124b1c7)

- From the Google Maps image and the metadata location, we can see that the outline and surroundings of the shop are similar
- The flag is therefore **ASAHI Tou'an Craft Shop**


### Flag
    NYP{asahi_tou'an_craft_shop}

