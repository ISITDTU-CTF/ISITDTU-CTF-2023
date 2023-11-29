### FAMOUS GIRL

<img width="367" alt="fmgirl" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/c8a8f3d6-6f31-4d53-ac0c-8c0d6038ccf7">

### Solution

Now we have a girl named Cithrel Wynhice who is quite famous on the internet. Now, we surely need to find her social media accounts. Search for her on social media platforms using her name. You might wonder why you can't find her because I changed one character, which is the lowercase ``L`` and the uppercase ``I`` in her name on social media: 
``Cithrel Wynhice --> CithreI Wynhice`` 
And we will find her on Instagram: 

<img width="344" alt="Screenshot 2023-10-15 202456" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/e3091899-8933-4971-8ee4-6c3b9aa416a2">

Another way to find Cithrel Wynhice on Instagram is by searching for just "Wynhice." You might also obtain similar results this way:

<img width="350" alt="Screenshot 2023-10-15 202741" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/3dde1eab-36ca-45e0-a644-277a818eac5a">

Okay, when you access her profile, you'll find a binary string and her username is also encoded with a Caesar Cipher: (And both of these are troll 👀)

<img width="1021" alt="Screenshot 2023-10-15 202941" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/a7c8b5dd-e426-44bc-b3c6-58f85f0e14a7">
<img width="654" alt="Screenshot 2023-10-15 203101" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/05a6844c-af7d-40ea-a4a6-ccd72b8f1534">


The new social media platform called Threads, recently announced by Meta, has gained popularity, and Cithrel has also registered an account to use it. Threads is registered by directly transferring from Instagram, so we will use her Instagram username to search for her on Threads:

<img width="925" alt="Screenshot 2023-10-15 203925" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/5e51b05b-d9b8-46c2-8d51-48cc28100f19">

Accessing her account, we notice a difference in the binary code mentioned in the bio:

<img width="1280" alt="Screenshot 2023-10-15 204116" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/c4b56ed1-84ee-459b-a540-07daa6926529">

When decoding the binary code on Threads, we obtain a link:

<img width="520" alt="binary threads" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/1901b0b7-c859-49ce-b729-13de3d2247ee">

Accessing the hyperlink will take you to the Anotepad page:

<img width="1279" alt="anote" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/08067884-4e34-4b91-8ce6-770956d26f01">

Looking at it, there's something unusual here 😉. There's only one line of text, but there are many spaces below it. When you select it, you'll realize it's in Whitespace Language. Decoding it reveals the flag:

<img width="665" alt="flag1" src="https://github.com/ISITDTU-CTF/ISITDTU-CTF-2023/assets/83077449/81cc8ada-1311-4e29-b00d-9a624b8b2872">

### **FLAG: ISITDTU{4_n3w_w4Y_t0_5hAr3_wjtH_t3xt}**
