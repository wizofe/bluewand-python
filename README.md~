# **caution: experimental** code::blueWand

## What is this?

Code project bluewand was started in order to become a Tiny Open Source API to speak with the KANO Wand. It is a layer over
the `bluepy` library which itself utilises `bluez`. All that it means is that practically that currently it only supports
Linux (tested on Raspberry Pi3/3b on Stretch Raspbian and the latest KANO OS v4.1).

There are plans to create a cross platform Open Source API that will utilise its full functionality.

### OK, but what can I do with it?

Currently not much.

It started as a internal experimental approach, to find out whether we can interface the KANO Wand by having as little information as
possible (so that's mostly a Reverse Engineered approach).

There most important part is the example program, that gets you started by interfacing the Wand! You can connect to the Wand automatically
 (it detects a Wand based on it's name but that can be extended easily to detect the closest Wand; feel free to take this and create a PR) :)
It also outputs the quaternions in real time! Now, that sounds fun.

The structure is there though to implement an OO wand  and be able to do a `make install` and from inside your
 REPL `from magic import wand`!

### OK, now tell me now how do I run it

If you are comfortable with `virtualenv` feel free to experiment with your own environment. Otherwise it should be as easy as:

```bash
sudo apt update && sudo apt install python3-pip -y
sudo pip3 install bluepy

git clone https://github.com/wizofe/bluewand-python
cd bluewand-python

# Run the demo program
(sudo) python3 magic/bluewand.py
```

A `Piplock` and `pipenv` is also on plans.

## Can I contribute to this project?

Absolutely! Feel free to impelement new features, experiment with the KANO Wand LED's, Vibration Motor, etc. Also a lot of work needs to be done
in order to make sense of the quaternions or the other movement sensors (including accelerometer etc).

Just send your issue or your PR in! The idea should be very similar to the `thingy52.py` from the `bluepy` library (Hint hint!)

## Can you help me hacking it?

Sure. Here are some fine details:

- The protocol is BLE
- Sensor Service `64A70011-F691-4B93-A6F4-0968F5B648F8`
- Quaternions Characteristic `64A70002-F691-4B93-A6F4-0968F5B648F8`
- Format: `4 x int16`
- Minimum Value: `-1000`
- Maximum Value: `1000`
- Attributes: `Notify`, `Read`
- Details: Returns the orientation values in `quaternions * 1000`

Thanks to Gabriel for those details.

## What about Copyright?

The whole thing is Copyrighted under the GNU GPLv3.0.
