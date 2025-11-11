# Consoling
Category: web

## Challenge Difficulty

very easy

## Challenge Description
What is the definition of consoling? | Hmm…. | To console?
<img width="948" alt="image" src="https://github.com/user-attachments/assets/453c28b8-6268-4341-b814-9888e3397120" />

## Solution
- Website has 3 buttons, only "PAGE WITH THE REAL FLAG" leads us to the right website, the other 2 are misleading
- This is the page upon clicking
<img width="933" alt="image" src="https://github.com/user-attachments/assets/c6c13297-c4f9-4a6c-8f98-71d24c7ec8ba" />

- Based on the clue, we realise that we need to inspect the website 
- Source Code as shown hints at the function we have to use, and the flag could be hidden in "script.js" or "trash.js"
- It also hints that encryption is involved 
<img width="500" alt="image" src="https://github.com/user-attachments/assets/f1052243-88e2-4d5e-bbfe-0fcb2b91bb8a" />

    listfunctions()
- Gives us different commands 
<img width="482" alt="image" src="https://github.com/user-attachments/assets/b839eb6a-efd4-4144-ba88-00649a75fab8" />

- Using the commands, we can find the encrypted string and the key 
<img width="578" alt="image" src="https://github.com/user-attachments/assets/56ce7385-67a4-4233-99d4-f7181594aa13" />

- Input AES Decryption script to reveal flag
```bash
    var encrypted = "U2FsdGVkX1/+BlAURUP5Pk6eQ6vCjySgoCCE/ZJyDESLlrlqfy5ibbzAVg+pdjPH";
    var passkey = "98D2B27"; // your passkey
    var decrypted = CryptoJS.AES.decrypt(encrypted, passkey).toString(CryptoJS.enc.Utf8);
    console.log(decrypted);
```


### Flag
      NYP{PC_0r_c0ns0le}



