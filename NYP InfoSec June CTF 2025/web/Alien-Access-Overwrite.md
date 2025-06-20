# Alien Access Overwrite

Category: web

## Challenge Difficulty

very easy

## Challenge Description
The alien attackers have compromised the Nova Sentinel's main control panel web interface. As a cybersecurity specialist, you need to find vulnerabilities in the control panel and gain administrative access to restore control of the ship's systems. You've managed to access a backup copy of the control panel's login page. Your task is to bypass the authentication and gain access to the admin panel where you can restore the ship's defense systems.

<img width="950" alt="image" src="https://github.com/user-attachments/assets/b41a1297-09b5-4d62-a4af-ee43372fbd85" />


## Solution

- We initially tried to log in with a random account "test" "test"
- It just prompts us this message
  
<img width="351" alt="image" src="https://github.com/user-attachments/assets/d6842a7c-3401-4906-a929-3a1df4d6082b" />

- We then proceed to inspect the code

<img width="490" alt="image" src="https://github.com/user-attachments/assets/19601da3-3033-4872-b276-90091d65e9c4" />

    const SECRET_TOKEN = 'ALIEN_ACCESS_GRANTED_42';

This declares a constant string variable, likely used as a fake access token. Hardcoded, meaning anyone who reads the source can see it.

    document.getElementById('loginForm').addEventListener('submit', function (e) {
        e.preventDefault();
        alert('Login disabled.');
    });

This disables the login form. Even if you try to submit the form, it will just alert "Login disabled." and do nothing. So, you can’t log in using normal means.

    function accessAdminPanel() {
    localStorage.setItem('accessToken', SECRET_TOKEN);
    window.location.href = "admin_panel.html?access=granted";
    }
- Stores the secret token into localStorage as accessToken.
- Redirects the browser to admin_panel.html?access=granted.

- **This is a client-side authentication bypass.**
- We then go into console and run the script to access admin panel:
  
      localStorage.setItem('accessToken', 'ALIEN_ACCESS_GRANTED_42');
      window.location.href = "admin_panel.html?access=granted";

- After running the script it leads us to this page

<img width="824" alt="image" src="https://github.com/user-attachments/assets/5ea1f6b0-ef4c-4bd8-8a8a-7139e6b66762" />

- We then proceed to click the restore the "Restore All Systems" button
- Which then prompts us this

<img width="334" alt="image" src="https://github.com/user-attachments/assets/476eb147-06e6-46f8-852d-116e7a930e88" />

- Flag is then revealed

<img width="278" alt="image" src="https://github.com/user-attachments/assets/61625731-88f4-4268-9601-ea23db6dd0b2" />



### Flag
    NYP{4L13N_4CC355_6R4N73D_kTwJRxwKhg}

