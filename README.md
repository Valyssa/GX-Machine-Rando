# GX Machine Rando
## Introduction
This program generates a random list of 26 out of the 41 GX Machines and puts them in order to match the 26 tracks. The idea is that you have to complete all tracks in order with the given machine. I recommend using this with GX Unleashed or GXtreme, as the base machines are a lot more interesting in those mods than in vanilla.
Currently this program only runs in cmd. I started working on a GUI but just wanted to get a working version up first. GUI version might still come later. Also if you have ideas for more features let me know.

## Usage
The program also spits out some instructions when you start it, but here's some explanation anyway:

- Press the "enter" key to go to the next track
- Type "r" to reset the run and generate a new random list of machines
- Type "p" to go back to the previous track
- Type "m" to use a mulligan

You still have to confirm your "r", "p" or "m" with an enter press. Any other letters aren't recognized and won't do anything.

### About mulligans
When the 26 random machines are generated, the leftover 15 machines are kept in a backup list. When you use a mulligan, you replace the current machine with one from this list. Don't wanna do Slim-line Slits with Super Piranha? Just mulligan! Super Piranha gets discarded and you get a replacement machine. Given that there are 15 machines in this backup list, you can use at most 15 mulligans. However I recommend you try to just roll with what you get. The program tracks how many mulligans you've used in the run. If you wanna do a speedrun with this program, you could add a time penalty, or donate x amount of money to charity for every mulligan used. It's all up to you.

## Possible future features
- GUI
- Add 4 or 8 custom machines into the mix
- Banning certain machines
- Different track sets so it's not just for all time attack tracks