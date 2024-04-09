import sys
import settings
from utils.audio_player import AudioPlayer
from utils.draw import Draw
from utils.system import Terminal


def main(ap: AudioPlayer, t: Terminal, nd: Draw):

    number_extracted = nd.number_draw()
    if not number_extracted:
        ap.audio_start(audio_file=settings.AUDIO_FILE_END)
        sys.exit()
    ap.audio_start(audio_file=settings.AUDIO_FILE_COUNTDOWN)
    ap.audio_start(audio_file=settings.AUDIO_FILE_NUM_ENTRY)
    ap.audio_create(text=str(number_extracted), audio_file=settings.AUDIO_FILE_NUM)
    ap.audio_start(audio_file=settings.AUDIO_FILE_NUM)

    t.clear()
    t.print_center(f"*** NUMERO ESTRATTO: {number_extracted} ***")

    last_n_extraxted = nd.number_get_lasts()
    t.print_center(f"*** ULTIMI ESTRATTI {last_n_extraxted} ***")

    t.tabellone_print(nd.number_get_drawn())


if __name__ == "__main__":
    ap = AudioPlayer()
    t = Terminal()
    nd = Draw(
        settings.NUMBERS,
        settings.NUMBERS_EXTRACTED_FILE,
        print_last_n_drawn=settings.SHOW_LAST_N_DRAWN,
    )

    t.clear()
    t.print_line()
    t.print_center("Benvenuto nella Tombola Automatica!")
    t.print_line()
    while True:
        main(ap, t, nd)
        t.print_loading_bar()
