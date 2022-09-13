# Microsoft-Teams-GIFShell

Press:

https://www.bleepingcomputer.com/news/security/gifshell-attack-creates-reverse-shell-using-microsoft-teams-gifs/

Technical Blogs:

https://medium.com/me/stats/post/1618c4e64ed7

https://medium.com/me/stats/post/458aea1826c5


**Replication Steps:**

There are a few prerequisites required to replicate the attack chain above:

* The GIFShell Python script, which should be executed on the attacker’s machine

* The GIFShell Powershell stager, executed on the victim’s machine

* Two Microsoft Azure Organizations or Tenants. The attacker organization or tenant should have at least 2 users, and the victim organization should have at least 1 user. This is for testing the Microsoft Teams Work Edition
* Two Microsoft Teams users for personal use. This is for testing the Microsoft Teams Home Edition
* A Teams channel with a publicly available webhook 
* A GIF of your choice 
* A public facing IP which can be used as a listener for incoming web requests

**<span style="text-decoration:underline;">Steps:</span>**

1) Open the Python script, and edit instances of the `token` variable with the `skypetoken_asm` cookie value from your authenticated browser session running Microsoft Teams as the attacker

2) Open Microsoft Teams as an attacker, and create a new chat with the victim. Look at the network traffic, and extract the Teams URL of this conversation. The URL should be in the form 
`“https://amer.ng.msg.teams.microsoft.com/v1/users/ME/conversations/<unique-identifier>@unq.gbl.spaces/messages”`

3) Open the GIFShell Python script, and edit instances of the `burp_url` variable with the URL from Step #2

4) Open the Microsoft Teams chat associated with the webhook created by the attacker, in the authenticated browser session running Microsoft Teams as the attacker

5) Run the GIFShell Python script on the attacking machine - this will create a prompt to enter desired commands to be run on the victim’s machine. 

6) Open the GIFShell Powershell stager script, and edit the $originalendpoint and $gifendpoint variables, changing the domain to the public IP address of the attacking machine

7) Open The GIFShell Powershell stager script, and edit the $response variable, changing the webhook, to the value of the attacker’s publicly available webhook

8) Run the Powershell stager script on the victim’s machine

9) Execute the desired commands in the GIFShell Python script prompt

10)  Ensure that while the desired commands are being executed, the Teams application is open to the chat associated with the publicly available webhook.
