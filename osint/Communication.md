### COMMUNICATION
<img width="370" alt="commu" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/c43a865e-1db8-4da2-8798-0891d541306a">

### Solution
When using a tool to search for her name, we also found an "Archived" section on Twitter.
According to her Twitter post, she mentioned using something to manage her accounts, but the image was blurred, so we can't identify what that is.
Checking the archived versions on the website https://web.archive.org/, and pointing to the "URLs" section, we have a saved status:

<img width="1258" alt="Screenshot 2023-10-15 222106" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/1dbb8f99-d437-4560-9f48-61d2ea84602c">

Download the image and check the metadata to find the Linktr.ee link: https://linktr.ee/cithrelwynhice

<img width="776" alt="Screenshot 2023-10-15 222406" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/319bb417-5516-4396-823f-c64f76695143">

Accessing it, you will get an invitation link to her Discord server and a very hot video 😍

<img width="749" alt="Screenshot 2023-10-15 222615" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/48720127-e503-4b83-8f38-8f24c534ed85">

In Discord, we need to pay attention to a channel named ``Secret`` where there are many similar links, and we'll need to find the exact link:

<img width="1048" alt="Screenshot 2023-10-15 223222" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/726ce597-d34c-4e02-81cc-e7df2b405c6e">

Returning to the Twitter archive page and checking the saved versions, there will be an archived version with a difference in the cover photo section:

<img width="1277" alt="Screenshot 2023-10-15 224237" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/6a01f512-f4ec-43d4-8731-b6ece291d381">

We have an ID: 1156305669700460695. Add this ID to the link leading to the "Secret" channel:
https://discord.com/channels/1154636986448085032/1154669336645083166/1156305669700460695
This is the link to a message, and this message is different from the others:

<img width="626" alt="Screenshot 2023-10-15 224911" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/5d75842f-2cf6-47d7-9085-5f92f8272a3e">

Accessing it will provide you with the ``flag.bmp`` file. Now, you'll need to find a way to extract the flag from this file:

<img width="1279" alt="Screenshot 2023-10-15 225141" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/779510a6-9fd1-4bb7-9245-ab635fc41be4">

**METHOD 1:**
For Windows, you can use ``Xiao Steganography`` to extract the file:

<img width="349" alt="Screenshot 2023-10-15 225554" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/22f30ab2-bcc9-48de-921d-41e8f3e73ccf">

There will be an embedded XLS file that you need to extract. Simply extract it and save the file with the ".xls" extension. Afterward, open the file, and you will have a blank spreadsheet like this:

<img width="1277" alt="Screenshot 2023-10-15 225919" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/c4630be9-8e3e-4710-a6da-85a627f75bcc">

Select all and press Ctrl + Shift+ ~ 
You will get the Flag:

<img width="1280" alt="Screenshot 2023-10-15 230406" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/bd8be42c-990d-4ad8-a037-7c213990ca68">

**METHOD 2:**
That's using the "zsteg" tool.
First, use the command: ```zsteg -a flag.bmp``` and you will notice something unusual: "TAG:Int21"

<img width="407" alt="Screenshot 2023-10-15 231024" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/a674dc1f-417b-47ab-84b5-e04a6ca18416">

Next, use the command: ```zsteg -E b1,lsb,bY flag.bmp > data_file``` to extract the data to a file named "data_file." Open "data_file" with Excel and search for "ISITDTU" to find the flag.

<img width="1280" alt="Screenshot 2023-10-15 231710" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/ce129225-024c-478c-8329-f1b9e5aa4caf">

**FLAG: ISITDTU{3xc3l_trjck_t0_hjd3_t3xt}**
