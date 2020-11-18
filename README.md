## OpenRandonaut
### Open-source QRNG coordinate bot
<img align="left" src="https://i.imgur.com/KFueJRM.png" width="150">

I couldn't find any attempt at an open-source version of The Fatum Project bot, so I decided to try and make one myself.
I'm not sure how The Fatum Project bot/Randonautica does it's calculations, and I'm not sure I'm doing it correctly here, but I think so.
Fork away, friends!<br><br><br> The script uses [quantumrandom](https://github.com/lmacken/quantumrandom) to interface with the [ANU Quantum Random Number Generator](https://qrng.anu.edu.au/), where it gets a list of [truly random](https://en.wikipedia.org/wiki/Hardware_random_number_generator#Quantum_random_properties) numbers, converts them to coordinates and then uses [SciPy](https://github.com/scipy/scipy) to compute the gaussian kernel density estimate of those coordinates. As far as I have understood, this should be equivalent of an Attractor point in Randonautica. The script can be interacted with through a Telegram-bot (made using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)).
<br><br>

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
**Fig. 2:** A visualization of how the Attractor coordinate is calculated. The blue dots are quantum random coordinates. The heat map shows the density of those coordinates. The darker, the denser. The red X marks the point with the highest density.
<br>

## Installation
1. I you don't already have: [Install Python](https://wiki.python.org/moin/BeginnersGuide/Download)
2. Install [poetry]() (OpenRandonaut uses it for package management):<br>
`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

3. Glone the repository:<br>
`git clone https://github.com/openrandonaut/openrandonaut.git`

4. Go to the openrandonaut directory and run `poetry install`.
This will install all dependencies.
<br>

## Getting started
1. Test out the coordinate generation by editing openrandonaut.py and uncommenting the lines at the bottom of the file. Save it and run `python openrandonaut.py`

2. Test out the Telegram bot, by [registering a new Telegram bot](https://core.telegram.org/bots#creating-a-new-bot) and putting your token in bot.py where it says
```python
updater = Updater(token="TELEGRAM_TOKEN_HERE", use_context=True)
```
Then run `python bot.py` and try sharing your location with your new bot in the Telegram app. (see Fig. 1 in [Examples](#examples))
