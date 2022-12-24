import os, shutil
from pytube import YouTube
import aubio
import generate_beatmap
import subprocess
import game
    
#Create Temp Folder
Path = os.path.join(os.getcwd(),"Music")
if not os.path.exists(Path): os.makedirs(Path)

for filename in os.listdir(Path):
    file_path = os.path.join(Path, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))




print("Paste Song Link From YouTube")
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))
  
# extract only audio
video = yt.streams.filter(only_audio=True).first()
  
# check for destination to save file
destination = Path
  
# download the file
out_file = video.download(output_path=destination)
  
print(yt.title + " has been successfully downloaded.")
print("\n\n")

# save the file
subprocess.run([
    'ffmpeg',
    '-i', os.path.join(Path, out_file),
    os.path.join(Path, 'song.wav')
])

os.remove(out_file)

# result of success
print("Generating Beatmap...")

generate_beatmap.generateBeatmap(os.path.join(Path,'song.wav'))
game.playGame()