# playground-diceware
A Reinhold’s “Diceware” password generator, for the upcomming Playground compatible with Micropython

## Why this?

The author is among other things a security researcher and educator. A difficult challange to teach is how to use secure passwords and password gerators, and Reinhold's Diceware seems to be an easy way to generate and remember passwords.

## Description

The project will use a word list, and the random() funcion to emulate a dice, and create a password using Reinhold's Diceware technique.

## Goals

- [x] Convert a Diceware wordlist to JSON
- [x] Upload a Diceware wordlist, initially to an ESP8266 and later or to the (in development by Adafruit) Playground with SAMD21. With the ESP8266 and the ampy-adafruit command it took slightly less than 5 minutes to upload the JSON file.
- [ ] Convert Json data to array
- [ ] Use the leds as "dice" indicator
- [ ] Use randomize() properly
- [ ] Generate a password and upload it in a password vault
- [ ] If the chipset supports it, use it as a HID keyboard to write the passwords, like John Parks' Adafruit project.
- [ ] Aldo not a primary objective, later on we can revisit the project to upload the list in a more efficient manner
