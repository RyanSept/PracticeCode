lsongs= ["http://50.30.37.49/yt/1/aa/august_alsina_make_it_home_explicit_ft._jeezy_mp3_57142.mp3",
"http://199.189.84.110/yt/2/8d/trevor_jackson_new_thang_official_music_video_mp3_57377.mp3",
         "http://188.138.124.217/yt/b/7e/jacob_latimore_what_are_you_waiting_for_mp3_57482.mp3",
         "http://173.224.125.217/yt/c/66/ciara_speechless_mp3_57529.mp3",
         "http://50.30.32.147/yt/c/05/alessia_cara_here_mp3_57617.mp3",
         "http://199.189.84.110/yt/8/75/korede_bello_ft._tiwa_savage_romantic_official_music_video_mp3_57703.mp3"]

import urllib2
import urllib
import os

for song in lsongs:
    data = urllib2.urlopen(song).read()
    fname = urllib.unquote(os.path.basename(song))
    print fname
    f = open("D:/ryan music/Music/"+fname,"w")
    f.write(data)
    f.close()
