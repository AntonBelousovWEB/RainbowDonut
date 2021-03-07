# RainbowDonut
A fork created from the donut shaped c code that produces a donut output that does nothing else but to print that donut but with **special rainbow color stuff thingys**

## Credits

This project is a frankenstein like merge of two existing project. First of course the existing code to produce a spinning donut. The source for this project can be found [here](https://www.a1k0n.net/2006/09/15/obfuscated-c-donut.html)  
The second project I used template if you will is a implementation in c of the popular **useful** comando-line tool `lolcat`. The original project (at least I think) was [this] (https://github.com/busyloop/lolcat) written with ruby.
I first changing this implementation a little and just adjust it so it can do the trick. But what I had to find out that it had a poor performance and the donut was laggy. **UNACCEPTABLE**!!!1eleven!

A new solution must be found for this urgent project! It was 6 o'clock in the morning and I found just what I was looking for. A fast and efficient implementation of `lolcat` written in C. The git repositroy can be found [here](https://github.com/IchMageBaume/clolcat).  
This was perfect as I no longer had to use a pipe to get the output of donut.c and let lolcat *change* the color. I could now use a good implementation to change the color of the output directly within the donut.c file.

This also meant I had to somehow make sense of the donut.c file. Well at least I had to get a basic understanding which print did what and then 'add' the 'color characters' that.
But after that was doen and I made some superficial changes to the program to fit my problem better it was up and running.

