from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('CURTE O SOM!')
mixer.music.pause()
