## OpenRandonaut - Open-source QRNG coordinate bot
<img align="left" src="https://i.imgur.com/KFueJRM.png" width="150">

I couldn't find any attempt at an open-source version of The Fatum Project bot, so I decided to try and make it myself.
I'm not sure how The Fatum Project bot/Randonautica does it's calculations, and I'm not sure I'm doing it correctly here, but I think so.
Fork away, friends!<br><br><br> The script uses [quantumrandom](https://github.com/lmacken/quantumrandom) to interface with the [ANU Quantum Random Number Generator](https://qrng.anu.edu.au/), where it gets a list of [truly random](https://en.wikipedia.org/wiki/Hardware_random_number_generator#Quantum_random_properties) numbers, converts them to coordinates and then uses [SciPy](https://github.com/scipy/scipy) to compute the gaussian kernel density estimate of those coordinates. The script can be interacted with through a Telegram-bot (using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)). 
<br><br><br>

#### Telegram bot preview:
![](https://media4.giphy.com/media/JkrKss7cEpusD0yLzJ/giphy.gif)
