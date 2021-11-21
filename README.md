## OpenRandonaut
![Python](https://img.shields.io/badge/built%20with-Python3-red.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

### Open-source QRNG coordinate bot
<img align="left" src="https://i.imgur.com/KFueJRM.png" width="150">

I couldn't find any attempt at an open-source version of the [Fatum Project bot](https://github.com/anonyhoney/fatum-en), so I decided to try and make one myself.
<br><br> The script uses [quantumrandom](https://github.com/lmacken/quantumrandom) to interface with the [ANU Quantum Random Number Generator](https://qrng.anu.edu.au/), where it gets a list of [truly random](https://en.wikipedia.org/wiki/Hardware_random_number_generator#Quantum_random_properties) numbers, converts them to coordinates and then uses [SciPy](https://github.com/scipy/scipy) to compute the gaussian kernel density estimate of those coordinates. As far as I have understood, this should be equivalent of an Attractor point in the Fatum bot/Randonautica. The script can be interacted with through a Telegram-bot (made using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)).
<br><br>
If you're unfamiliar with The Fatum Project and the concepts of Probability Blind-Spots and Quantum Randomness, I recommend reading [fatum_theory.txt](https://github.com/anonyhoney/fatum-en/blob/master/docs/fatum_theory.txt) which shipped with the original Fatum bot. [This video](https://www.youtube.com/watch?v=6C6aXta3m1M) gives a lot of great background info too. If you have no idea what any of this is about, watch [this video](https://www.youtube.com/watch?v=nDX81AUm8yE) and/or read [this article](https://medium.com/swlh/randonauts-how-a-random-number-generator-can-set-you-free-dfc2a2413e15).

Contributions would be greatly appreciated!

#### To-do:
- [x] Get coordinate generation working
- [x] Get Telegram-bot working
- [ ] Make heatmap generation more stable
- [ ] Get people excited about the project!
- [ ] Turn the coordinate logic into a module for use in other projects? :thinking:


## Table of contents
- [Introduction](#openrandonaut)
- [Examples](#examples)
- [Installation](#installation)
- [Getting started](#getting-started)

## Examples
A few images for your pleasure:
<table border="0">
 <tr>
    <td><b style="font-size:30px">Telegram bot preview:</b></td>
    <td><b style="font-size:30px">Kernel density estimate visualization:</b></td>
 </tr>
 <tr>
    <td><img src="https://media4.giphy.com/media/JkrKss7cEpusD0yLzJ/giphy.gif">[1]</td>
    <td><img src="https://i.imgur.com/BxxxddF.png" width="500">[2]</td>
 </tr>
</table>

**Fig. 1:** A very shitty GIF demonstrating the functionality of the Telegram bot.<br>
**Fig. 2:** A visualization of how the Attractor coordinate is calculated. The blue dots are quantum random coordinates. The heat map shows the density of those coordinates. The darker, the denser. The red X marks the point with the highest density. Made using [seaborn](https://github.com/mwaskom/seaborn) and [this script](https://github.com/openrandonaut/openrandonaut/blob/main/kdeplot_heatmap.py) (BETA!).
<br>

## Installation
1. I you don't already have: [Install Python](https://wiki.python.org/moin/BeginnersGuide/Download). OpenRandonaut needs at least version 3.9 of Python to run.
2. Install [poetry]() (OpenRandonaut uses it for package management):<br>
`curl -sSL https://install.python-poetry.org/ | python3 -`

3. Clone the repository:<br>
`git clone https://github.com/openrandonaut/openrandonaut.git`

4. Go to the openrandonaut directory and run `poetry install`.
This will install all dependencies.
<br>

## Getting started
1. Test out the coordinate generation by editing `openrandonaut.py` and uncommenting the lines at the bottom of the file. Save it and run `python openrandonaut.py`

2. Test out the Telegram bot, by [registering a new Telegram bot](https://core.telegram.org/bots#6-botfather) and putting your token in `bot.py` where it says
```python
updater = Updater(token="TELEGRAM_TOKEN_HERE", use_context=True)
```
Then run `python bot.py` and try sharing your location with your new bot in the Telegram app. (see Fig. 1 in [Examples](#examples))
