
# HardcoreRhythmGame
This was made in the span of 8 Hours... **STRIGHT!**
This is a `Python` project where you are a cube and you gotta survive the laser beams that go to with the music.
If you just want to know how to play the game, you can [click here](#playing-the-game)

# How It Works?
``` mermaid
stateDiagram-v2

Start --> GiveSong

GiveSong --> DownloadsSong

DownloadsSong --> GeneratesBeatMap

GeneratesBeatMap --> SelectDifficulty

SelectDifficulty --> CreatesGameScreen

CreatesGameScreen --> StartsGame

  

onGameStart --> ClearScreen

ClearScreen --> UpdatePlayerState

UpdatePlayerState --> UpdateLasersState

UpdateLasersState --> UpdateScore

UpdateScore --> DrawFrame

DrawFrame --> ClearScreen

  

onGameStart --> WaitForGameLoss

WaitForGameLoss --> ResetScore

ResetScore --> ResetSong

ResetSong --> ResetPlayer
```
When the `main.py` file is opened, the game will ask for a link to a youtube video to play as the song. Then it will download the video and convert to `mp3` using **FFMPEG** and converts the audio to a beatmap with timing for each laser to be spawned.
After the file generation, the game will ask for a diffuculty:
1. Easy
2. Medium
3. Hard

and will spawn the lasers based on the diffuculty
IE: Easy will spawn 1 per beat and medium spawns 2 and hard spawns 3.
After x ammount of lasers spawned, it will spawn a special laser that will lock onto the players position to reduce 'camping' stratergy.


# Playing The Game
## Downloading The Project
Inside [GitHub](https://github.com/ChezyName/HardcoreRhythmGame), download the project of the code or [click here](https://github.com/ChezyName/HardcoreRhythmGame/archive/refs/heads/main.zip).
Once you extract the files, open `main.py`, If it closes as soon as it opens, you need to download the packages.
## Downloading Python + Packages
### Downloading Python
You can download `Python` from the **Windows Store** or from the [Python website](https://www.python.org/), Either way download and install Python to make the project run.

### Downloading Packages
<s>
Open up the `terminal` or `cmd` to where the project folder is located. Run `pip install -r requirements.txt`. This will download every package inside the requirements.txt file.

> No Longer Required, Packages Installed In Repo


## How To Play
Its very simple, you just open `main.py`, and find a song that you want to play on youtube. Paste the link and select your diffuculty
> The terminal might not let you paste links so use `ctrl + shift + v` 


# Future Updates?
Well this was just a fun project before the end of the year so perhaps?
If I would update this in the future I would add the following
1. Convert the menu from command promt to pygame,
2. Highscore system
3. Python &rarr; C++?
