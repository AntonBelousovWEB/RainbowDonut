# RainbowDonut
A fork created from the donut shaped c code that produces a donut output that does nothing else but to print that donut but with **special rainbow color stuff thingys**

## Credits

This project is a frankenstein like merge of two existing project. First of course the existing code to produce a spinning donut. The source for this project can be found [here](https://www.a1k0n.net/2006/09/15/obfuscated-c-donut.html).  
The second project I used was an implementation in C of the popular **useful** comando-line tool `lolcat`. The original project (at least I think) was [this] (https://github.com/busyloop/lolcat) written in ruby.
I first changed this implementation a little and just adjusted it so it can do the trick. But what I had to find out was that it had a poor performance and the donut was laggy. **UNACCEPTABLE**!!!1eleven!

A new solution had to be found for this urgent project! It was 6 o'clock in the morning and I found just what I was looking for. A fast and efficient implementation of `lolcat` written in C. The git repositroy can be found [here](https://github.com/IchMageBaume/clolcat).  
This was perfect as I no longer had to use a pipe to get the output of donut.c and let lolcat *change* the color. I could just use the existing implementation to change the color of the output directly within the donut.c file.

This also meant I had to somehow make sense of the donut.c file or at least I had to get a basic understanding which print did what and then 'add' the 'color characters'.
I encountered the problem that the 'output buffer' does not contain new line characters and those were printed via a ternary expression within the putchar. This at first made it harder for me and I changed it so the output buffer also contains the new line characters. 
What I had to realize after a lot of work is that this was unnecessary. My brain - now at a functinal level of maybe 2%, my body desperate for sleep but my determination still strong just couldn't let this go. So I just smashed my head on the keyboard until the compiled program did what I wanted it to do.

This leaves us at where we are right now. A weird useless programm that produces a somewhat pleasent output with unnecessary superficial changes to the original projects.

## Running/Compiling the programm
To compile the program the original donut.c `gcc` call has not changed.
Simply call the following to compile and run the programm
```sh
gcc donut.c -o donut -lm && ./donut
```
Note that I removed the includes (which I had included while working on the project). But in a sense I felt I should remove them to at least somewhat keep in the spirit of the original source :) 

## Special thanx
Special thanx to [this](https://www.youtube.com/watch?v=9xDtwYJx7yc) for keeping me sane and generally keeping the mood up through out the knight.
