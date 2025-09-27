import time
from threading import Thread, Lock
import sys
from colorama import Fore, Style, init
init(autoreset=True)
lock = Lock()
def animate_text(text, delay=0.1, color=Fore.CYAN):
    with lock:
        for char in text:
            sys.stdout.write(color + char + Style.RESET_ALL)
            sys.stdout.flush() 
            time.sleep(delay)
        print()
def sing_lyric(lyric, delay, speed, color):
    time.sleep(delay)
    animate_text(lyric, speed, color)
def sing_song():
    lyrics = [("\nI saw her in the rightest way", 0.1),
        ("Looking like Anne Hathaway", 0.12),
        ("Laughing while she hit her pen", 0.11),
        ("And coughed, and coughed", 0.10),

        ("\nAnd then, she came up to my knees", 0.10),
        ("Begging, Baby, would you please?", 0.10),
        ("Do the things you said you'd do to me, to me?", 0.15),

        ("\nOh, won't you kiss me on the mouth and love me like a sailor?", 0.08),
        ("And when you get a taste, can you tell me what's my flavor?", 0.08),
        ("I don't believe in God, but I believe that you're my savior", 0.08),
        ("My mom says that she's worried, but I'm covered in His favor\n", 0.08)]
    delays = [0.3, 4.5, 9.3, 14.5, 
            19.3, 24.3, 29.1, 
            39.3, 45.0, 50.0, 54.0]
    colors = [Fore.MAGENTA, Fore.MAGENTA, Fore.MAGENTA, Fore.MAGENTA, 
        Fore.BLUE, Fore.BLUE, Fore.BLUE, 
        Fore.MAGENTA, Fore.MAGENTA, Fore.MAGENTA, Fore.MAGENTA]
    
    threads = []
    min_len = min(len(lyrics), len(delays), len(colors))

    for i in range(min_len):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed, colors[i]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
if __name__ == "__main__":
    sing_song()











