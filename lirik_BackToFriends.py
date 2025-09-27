import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush() 
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("How can we go back to being friends", 0.1),
        ("When we just shared a bed?", 0.12),
        ("How can you look at me and pretend", 0.11),
        ("I'm someone you've never met?", 0.10),
        ("It was last December", 0.10),
        ("You were layin' on my chest", 0.10),
        ("I still remember", 0.1),
        ("I was scared to take a breath, didn't want you to move your head", 0.1)
        ("How can we go back to being friends", 0.1),
        ("When we just shared a bed? (Yeah)", 0.12),
        ("How can you look at me and pretend", 0.11),
        ("I'm someone you've never met?", 0.10),
    ]
    delays = [0.3, 4.5, 9.3, 14.1, 18.8, 23.0, 28.0, 34.5]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__== "__main__":
    sing_song()









