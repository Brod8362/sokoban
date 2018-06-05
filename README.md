How To Run
==========

Linux
-----
First, if you're on linux you have two options- You can run the game in PyGame, or you can run it in a terminal.
To run it on pygame, you just need the pygame library and you should be good to go. If you're going to run it 
in a terminal, you need two extra things - blessings and urwid. The terminal UI will automatically be used if
the pygame UI is not available for whatever reason. You can install libraries like this:

`python3 -m pip install {library}`

Once you have your libraries setup, all you need to do is run skb.py

Windows
-------
For windows users you only have one choice, and that's to run it in pygame. This is due to the libraries used in
the terminal UI being unavailable for windows. An alternative may be implemented at a later date. Either way, in
order to install pygmae via pip just do

`pygame -m pip install pygame`

Then run skb.py and you should be good to go.
