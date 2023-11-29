### DISCOVER
<img width="371" alt="dscv" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/a82e6d08-dd75-43ae-b93e-05daf31af24c">

### Solution
From the description, we understand that she posted a picture on social media taken with a flycam, and your task is to locate it and identify the name of the tall building across from that location. When exploring her Threads account, you may encounter some fake flags and even a rickroll, so feel free to experience those if you're interested 😛. 
However, we should focus on the two posts she made:

<img width="349" alt="Screenshot 2023-10-15 205948" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/73770ad9-2e65-45a7-89ae-f8ef217fc636">

Looking at it, you will understand that it's a portion of a Facebook and Twitter URL. For Facebook, you can simply enter it like this:

<img width="255" alt="Screenshot 2023-10-15 210203" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/d3d407d4-8890-4e65-9436-aba4c5bb885b">

The link will lead to the video of Rick Astley's "Never Gonna Give You Up" song 🙃

<img width="1246" alt="rr" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/2a8d6238-b975-4192-92bb-2a015810643a">

Next, with the Twitter ID , you may need to combine it with some additional conditions, like this:

``https://twitter.com/randomusername/status/id_in_her_post``

So, by putting it together, you will be able to access it as follows:

https://twitter.com/randomusername/status/1706752419806560656

<img width="673" alt="Screenshot 2023-10-15 211048" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/9d8404b5-80ef-47a2-a490-2bd937eef18c">

Visiting her personal page doesn't reveal much useful information, so we'll use the username to search. You'll find another account of hers on Mastodon. Additionally, there will be some archived content on her Twitter account:

<img width="1270" alt="Screenshot 2023-10-15 211327" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/c225b564-1d91-4e9d-b1c4-cbeb4bc47acf">

Access to her Mastodon account:

<img width="438" alt="Screenshot 2023-10-15 211641" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/a0edb31a-944d-461b-a7b3-a5851ae0332e">

You will have a picture, use Google Lens to search for it:

<img width="1275" alt="Screenshot 2023-10-14 195237" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/b2d74413-e5d4-4d54-8fba-ff14f2a83dbc">

Combining it with the title of her post on Mastodon: ``"I watched a quite interesting video, and I captured this picture"``. She took a picture from a video, so we will begin the search on YouTube.

<img width="1280" alt="Screenshot 2023-10-15 212823" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/dc4f0f33-3b4e-4610-a3d9-faf36a8cff56">

By watching the videos one by one, you'll eventually find a scene that matches the picture she captured in the second video according to the search results:

<img width="939" alt="Screenshot 2023-10-15 213036" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/59fd94f1-80ca-4969-bc7e-f58e350dfdbd">

And by watching the video, you'll also recognize the tallest building across from this bicycle graveyard:
<img width="1280" alt="Screenshot 2023-10-15 213821" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/c61030cc-9a06-4029-81b7-dbcfd344032d">

Now, we'll need to find the location of this building. Looking to the side, you can easily spot a building named HITIME.
A Google search reveals the address:

![Screenshot 2023-10-15 214528](https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/41eb50a9-6bcb-411e-a3e4-b7cfdfddcc1a)

Use Baidu Maps to search for the address and you'll see it:

<img width="862" alt="Screenshot 2023-10-15 215319" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/ae5d8885-b108-4299-883c-2627115c0c80">

Get a bit closer to see the name of the tallest building on the other side: > CHINA CITIC BANK

<img width="902" alt="Screenshot 2023-10-15 215606" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/e471f862-7bf5-4e27-be85-30e68537f229">

Next, access the website of China Citic Bank: https://www.citicbank.com/common/fwwd/. You'll find a list of their branches. Search for the word CITIC, and you'll get the result:

<img width="1214" alt="Screenshot 2023-10-15 220036" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/056fad4d-a4f0-4005-9ecf-6c65dbd108ee">

Based on the flag format, we have the flag:

**FLAG: ISITDTU{shanghai_citic_plaza}**
