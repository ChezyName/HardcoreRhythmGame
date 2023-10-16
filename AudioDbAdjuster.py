from pydub import AudioSegment
def AudioDbAdjuster(min_db, max_db):
    # Load file
    audio = AudioSegment.from_file("Music/song.wav")
    # Calculate the current dB level
    current_db = audio.dBFS

    # Adjust the volume to stay within the specified range
    if current_db < min_db:
        db_change = min_db - current_db
        adjusted_audio = audio + db_change
    elif current_db > max_db:
        db_change = max_db - current_db
        adjusted_audio = audio + db_change
    else:
        adjusted_audio = audio

    print("min_db = ", min_db ,"max_db = ", max_db )

    # Export the adjusted audio to a new file
    adjusted_audio.export("Music/song.wav", format="wav")
    print("done")
    print("Exit sound_db.py")

