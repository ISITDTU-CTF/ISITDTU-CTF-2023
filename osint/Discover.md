### DISCOVER
<img width="371" alt="dscv" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/67baa614-2023-4c00-a0e7-86198a2e7d4d">

### Solution
From the description, we understand that she posted a picture on social media taken with a flycam, and your task is to locate it and identify the name of the tall building across from that location. When exploring her Threads account, you may encounter some fake flags and even a rickroll, so feel free to experience those if you're interested 😛. 
However, we should focus on the two posts she made:
<img width="349" alt="Screenshot 2023-10-15 205948" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/9ca72548-0e88-4fad-8020-c8056efc2621">

Looking at it, you will understand that it's a portion of a Facebook and Twitter URL. For Facebook, you can simply enter it like this:
<img width="255" alt="Screenshot 2023-10-15 210203" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/7093d5dd-77ab-4614-8f4d-11c82ff06f9a">

The link will lead to the video of Rick Astley's "Never Gonna Give You Up" song 🙃
<img width="1246" alt="rr" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/3fbb65c9-d736-4e02-91ae-36322064ce24">

Next, with the Twitter ID , you may need to combine it with some additional conditions, like this:

``https://twitter.com/randomusername/status/id_in_her_post``

So, by putting it together, you will be able to access it as follows:

https://twitter.com/randomusername/status/1706752419806560656
<img width="673" alt="Screenshot 2023-10-15 211048" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/26ea68cf-ee1f-4728-84cd-46e3f5a52713">

Visiting her personal page doesn't reveal much useful information, so we'll use the username to search. You'll find another account of hers on Mastodon. Additionally, there will be some archived content on her Twitter account:
<img width="1270" alt="Screenshot 2023-10-15 211327" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/ca90b755-66fd-406f-9d85-a0cda170022e">

Access to her Mastodon account:

<img width="438" alt="Screenshot 2023-10-15 211641" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/c7d93f9a-41e7-4aa7-ae88-e9be3e4efa2f">

You will have a picture, use Google Lens to search for it:
<img width="1275" alt="Screenshot 2023-10-14 195237" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/c2c46d94-3658-4a4a-8951-34534f8a01ca">

Combining it with the title of her post on Mastodon: ``"I watched a quite interesting video, and I captured this picture"``. She took a picture from a video, so we will begin the search on YouTube.
<img width="1280" alt="Screenshot 2023-10-15 212823" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/67af5ae3-f96d-466d-8309-1ad098feac31">

By watching the videos one by one, you'll eventually find a scene that matches the picture she captured in the second video according to the search results:
<img width="939" alt="Screenshot 2023-10-15 213036" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/00056cc4-d85b-42a5-aa51-060b4b9a65f0">

And by watching the video, you'll also recognize the tallest building across from this bicycle graveyard:

<img width="1280" alt="Screenshot 2023-10-15 213821" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/a11814e7-aee3-4574-9cf0-15351347e4f3">

Now, we'll need to find the location of this building. Looking to the side, you can easily spot a building named HITIME.
A Google search reveals the address:

![Screenshot 2023-10-15 214528](https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/12a55d2e-c651-4965-9376-8bbbdd6452a8)


Use Baidu Maps to search for the address and you'll see it:
<img width="862" alt="Screenshot 2023-10-15 215319" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/f24b5adb-c10e-4314-9538-0e19c6e681ed">

Get a bit closer to see the name of the tallest building on the other side: >CHINA CITIC BANK
<img width="902" alt="Screenshot 2023-10-15 215606" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/06dc2cc5-4165-4256-9492-134ee7e90718">

Next, access the website of China Citic Bank: https://www.citicbank.com/common/fwwd/. You'll find a list of their branches. Search for the word CITIC, and you'll get the result:
<img width="1214" alt="Screenshot 2023-10-15 220036" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/f11db8d8-777f-4177-91bc-b2f0c6e580d2">

Based on the flag format, we have the flag:

**FLAG: ISITDTU{shanghai_citic_plaza}**
