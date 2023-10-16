# python-packages directory
import os,sys
import_dir = os.path.abspath('python-packages')
sys.path.append(import_dir)

import shutil
from pytube import YouTube
import aubio
import generate_beatmap
import subprocess
import game
from AudioDbAdjuster import AudioDbAdjuster

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

def get_value_from_file(search_item):
    with open('tmp.txt', 'r') as file:
        for line in file:
            if line.startswith(f'{search_item}:'):
                value_str = line.split(': ')[1]
                value = tuple(map(int, value_str.strip('()\n').split(', ')))
                return value
def get_value_from_file_str(search_item):
    with open('tmp.txt', 'r') as file:
        for line in file:
            if line.startswith(f'{search_item}:'):
                value = line.split(': ')[1].strip()
                return value

selected_preset = "youtube_url"
youtube_url = get_value_from_file_str(selected_preset)
print("Paste Song Link From YouTube")
yt = YouTube(youtube_url)
#
#YouTube(
    #str(input("Enter the URL of the video you want to download: \n>> ")))

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

print("\n\n\n")
print("Select Diffuculty\n")
print("Press Enter Only for easy mode")
print("1.) Easy")
print("2.) Medium")
print("3.) Hard")
print("4.) Insane")
print("5.) Nightmare")
print("6.) Endless")
#d = input("> ")

difficulty = "difficulty"
d = get_value_from_file(difficulty)


try:
    d = int(d[0])
    # Now d is an integer
    if d >= 1 and d <= 6:
        game.playGame(d)
    else:
        d = 1
        game.playGame(d)
except (ValueError, IndexError):
    e = 1
    game.playGame(e)



# presets for minimum and maximum dB levels
db_presets = {
    '1': {'min_db': -50, 'max_db': -40},
    '2': {'min_db': -50, 'max_db': -30},
    '3': {'min_db': -50, 'max_db': -20},
    '4': {'min_db': -50, 'max_db': -10},
    '5': {'min_db': -5, 'max_db': 5},
    '6': {'min_db': -20, 'max_db': 10},
    '7': {'min_db': -20, 'max_db': 20},
    '8': {'min_db': -20, 'max_db': 40},
    '9': {'min_db': -20, 'max_db': 50}
}
print("DB Presets:")
for key, values in db_presets.items():
    print(f"Preset {key}: Min dB = {values['min_db']}, Max dB = {values['max_db']}")
print ("\n")
print("Lets select volume. Note the less volume you set the game will become more easy")
print("Select a preset (1 to 9) or press 0 for custom or Enter to skip: ")

selected_presett = "selected_preset"
selected_preset = get_value_from_file(selected_presett)
if not selected_preset:
    print("Skipping preset selection.")

else:
    if selected_preset == '0':
        pass

            # Custom dB level input
        #min_db = int(input("Enter custom minimum dB level: "))
        #max_db = int(input("Enter custom maximum dB level: "))

    elif selected_preset in db_presets:
        preset = db_presets[selected_preset]
        min_db = preset['min_db']
        max_db = preset['max_db']
    else:
        selected_preset = 0
if 'min_db' in locals() and 'max_db' in locals():
    AudioDbAdjuster(min_db, max_db)
else:
    pass
'''
def store_value():
    window_background_color = (0, 0, 0)
    shape_color = (255, 0, 255)
    warning_zone = (0, 255, 0)
    red_zone = (255, 0, 0)
    Mouse_mode = "False"
    #diffuculty(d, window_background_color, shape_color, warning_zone, red_zone)
    with open('tmp.txt', 'w') as file:

        file.write(f'difficulty: {difficulty}\n')
        file.write(f'd: {d}\n')
        file.write(f'window_background_color: {window_background_color}\n')
        file.write(f'shape_color: {shape_color}\n')
        file.write(f'warning_zone: {warning_zone}\n')
        file.write(f'red_zone: {red_zone}\n')
        file.write(f'Mouse_mode: {Mouse_mode}\n')

store_value()
'''



difficulty(d)
