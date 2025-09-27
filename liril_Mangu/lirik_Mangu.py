
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
        ("\nJangan salahkan faham ku kini tertuju oh", 0.15),
        ("Siapa yang tau", 0.11),
        ("Siapa yang mau", 0.11),
        ("Kau di sana", 0.10),
        ("Aku diseberangmu\n", 0.11),

    ("Cerita kita sulit dicerna", 0.1),
        ("Tak lagi sama", 0.10),
        ("Cara berdo'a\n", 0.10),

    ("Cerita kita sulit diterka", 0.11),
        ("Tak lagi sama", 0.10),
        ("Arah kiblatnya ohh\n", 0.10),

    ("Cerita kita sulit dicerna", 0.1),
        ("Tak lagi sama", 0.10),
        ("Cara berdo'a\n", 0.10),

    ("Cerita kita sulit diterka", 0.11),
        ("Tak lagi sama", 0.10),
        ("Arah kiblatnya\n", 0.10),
]
    
    delays = [0.1, 9.6, 12.5, 15.0,17.2,
               20.0, 24.0,27.5,
                 30.0, 34.0, 37.3,
                40.5, 44.7, 48.0,
                 50.5, 55.5, 58.0 

              ]

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
























