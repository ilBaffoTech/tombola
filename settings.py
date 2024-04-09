from os.path import join

# Consts
DRAWN_RATE = 180  # each n seconds
NUMBERS = 90
SHOW_LAST_N_DRAWN = 5

# Filenames
AUDIO_FOLDER = "audio"
AUDIO_FILE_NUM = join(AUDIO_FOLDER, "tmp.number.mp3")
AUDIO_FILE_NUM_ENTRY = join(AUDIO_FOLDER, "number_entry.mp3")
AUDIO_FILE_COUNTDOWN = join(AUDIO_FOLDER, "countdown.mp3")
AUDIO_FILE_END = join(AUDIO_FOLDER, "end.mp3")

NUMBERS_EXTRACTED_FILE = "tmp.numbers.txt"
