### FAMOUS GIRL
<img width="367" alt="fmgirl" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/5e7bedae-1a91-436d-9251-5f645f6c10b7">

### Solution

Now we have a girl named Cithrel Wynhice who is quite famous on the internet. Now, we surely need to find her social media accounts. Search for her on social media platforms using her name. You might wonder why you can't find her because I changed one character, which is the lowercase ``L`` and the uppercase ``I`` in her name on social media: 
``Cithrel Wynhice --> CithreI Wynhice`` 
And we will find her on Instagram: 

<img width="344" alt="Screenshot 2023-10-15 202456" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/8506e579-5fdd-4ac5-8fa0-418f806c0942">

Another way to find Cithrel Wynhice on Instagram is by searching for just "Wynhice." You might also obtain similar results this way:

<img width="350" alt="Screenshot 2023-10-15 202741" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/31dd6542-6ed6-424a-b18e-5891a93487dc">

Okay, when you access her profile, you'll find a binary string and her username is also encoded with a Caesar Cipher: (And both of these are troll 👀)
<img width="1021" alt="Screenshot 2023-10-15 202941" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/72d97e99-c3df-413f-b52f-7cfee3206b05">
<img width="654" alt="Screenshot 2023-10-15 203101" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/3ed864a5-a729-48f2-bf31-289dd977f48b">

The new social media platform called Threads, recently announced by Meta, has gained popularity, and Cithrel has also registered an account to use it. Threads is registered by directly transferring from Instagram, so we will use her Instagram username to search for her on Threads:

<img width="925" alt="Screenshot 2023-10-15 203925" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/3f7d904f-70cc-416f-849b-d8cffcb42d9c">

Accessing her account, we notice a difference in the binary code mentioned in the bio:

<img width="1280" alt="Screenshot 2023-10-15 204116" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/a71b55ec-2f2f-429c-9f79-843b5b39c7ce">

When decoding the binary code on Threads, we obtain a link:

<img width="520" alt="binary threads" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/12160f67-4d3b-40cc-a5cc-5b48aadf9c02">

Accessing the hyperlink will take you to the Anotepad page:

<img width="1279" alt="anote" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/9e29f06c-ca5e-4ce7-b378-09a70893e0b0">

Looking at it, there's something unusual here 😉. There's only one line of text, but there are many spaces below it. When you select it, you'll realize it's in Whitespace Language. Decoding it reveals the flag:

<img width="665" alt="flag1" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/9a889be9-ee00-4b91-ab6a-a4ebb4ec4d0c">


### **FLAG: ISITDTU{4_n3w_w4Y_t0_5hAr3_wjtH_t3xt}**
