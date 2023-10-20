### COMMUNICATION
<img width="370" alt="commu" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/d00b8e69-13e2-4ab9-9fcd-39dcea825252">

### Solution
When using a tool to search for her name, we also found an "Archived" section on Twitter.
According to her Twitter post, she mentioned using something to manage her accounts, but the image was blurred, so we can't identify what that is.
Checking the archived versions on the website https://web.archive.org/, and pointing to the "URLs" section, we have a saved status:

<img width="1258" alt="Screenshot 2023-10-15 222106" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/a12b3f30-f854-4e16-9ee0-8b348c9adbe5">

Download the image and check the metadata to find the Linktr.ee link: https://linktr.ee/cithrelwynhice

<img width="776" alt="Screenshot 2023-10-15 222406" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/9025a3c4-8061-4bc9-9b56-df970e78df56">

Accessing it, you will get an invitation link to her Discord server and a very hot video 😍

<img width="749" alt="Screenshot 2023-10-15 222615" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/8f0f63cf-6cc8-4d05-9b12-f8ed651f13b4">

In Discord, we need to pay attention to a channel named ``Secret`` where there are many similar links, and we'll need to find the exact link:

<img width="1048" alt="Screenshot 2023-10-15 223222" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/2cf192c9-a7ba-47c8-a144-ed02aa4932c4">

Returning to the Twitter archive page and checking the saved versions, there will be an archived version with a difference in the cover photo section:

<img width="1277" alt="Screenshot 2023-10-15 224237" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/1e81675f-2fd7-4572-a187-7bcff85bc01f">

We have an ID: 1156305669700460695. Add this ID to the link leading to the "Secret" channel:
https://discord.com/channels/1154636986448085032/1154669336645083166/1156305669700460695
This is the link to a message, and this message is different from the others:

<img width="626" alt="Screenshot 2023-10-15 224911" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/3edc16e5-f5d4-4579-baac-38e37f43752a">

Accessing it will provide you with the ``flag.bmp`` file. Now, you'll need to find a way to extract the flag from this file:

<img width="1279" alt="Screenshot 2023-10-15 225141" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/d84bf1e6-fc5c-4da6-921a-a430ff0d3559">

**METHOD 1:**
For Windows, you can use ``Xiao Steganography`` to extract the file:

<img width="349" alt="Screenshot 2023-10-15 225554" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/b1b8a1b7-22c3-4ef3-95ca-d325fcb19a1d">

There will be an embedded XLS file that you need to extract. Simply extract it and save the file with the ".xls" extension. Afterward, open the file, and you will have a blank spreadsheet like this:

<img width="1277" alt="Screenshot 2023-10-15 225919" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/c7a5f191-ca23-4e37-b194-8bce3ce72119">

Select all and press Ctrl + Shift+ ~ 
You will get the Flag:

<img width="1280" alt="Screenshot 2023-10-15 230406" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/6301e78c-2711-4490-a268-176f1736e327">

**METHOD 2:**
That's using the "zsteg" tool.
First, use the command: ```zsteg -a flag.bmp``` and you will notice something unusual: "TAG:Int21"

<img width="407" alt="Screenshot 2023-10-15 231024" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/e058fb5c-05c1-4c23-96b9-0d8714397fb8">

Next, use the command: ```zsteg -E b1,lsb,bY flag.bmp > data_file``` to extract the data to a file named "data_file." Open "data_file" with Excel and search for "ISITDTU" to find the flag.

<img width="1280" alt="Screenshot 2023-10-15 231710" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/453a0018-29d7-4a42-a0a3-393ca7ecabdf">

**FLAG: ISITDTU{3xc3l_trjck_t0_hjd3_t3xt}**
