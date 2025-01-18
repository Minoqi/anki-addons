from ..shige_pop.patreon_list import PATRONS_LIST

ADDON_NAME = "" #🟢

def clink(name, text,url=None):
    if not url:
        return f'{name} : {text}<br>'
    return f'{name} : <a href="{url}">{text}</a><br>'

credits = """
<br><br><br>
<b>[ CREDIT ]</b>
<br><br><br>
""".replace('\n', '<br>')

patreon = f"""
Special Thanks
<b>[ PATRONS ]</b>
{PATRONS_LIST}


""".replace('\n', '<br>').replace(",","<br>")

sound =("<b>[ SOUNDS & BGM ]</b><br>"+
clink("Sound Effect", "Koukaon lab","https://soundeffect-lab.info/",)+
clink("Music" , "MaouDamashii","https://maou.audio/",)+
clink("Catgirl Voice","Cici Fyre","https://cicifyre.itch.io/")+
clink("Robot Voice","Charlie Pennell Productions©","https://www.charliepennellproductions.com/")+
clink("classical music"," Bernd Krueger","http://www.piano-midi.de/")
)


caractor = ("<b>[ IMAGE&3D MATERIALS ]</b><br>" +
clink("Knight","rvros","https://rvros.itch.io/") +
clink("Hooded","Penzilla","https://penzilla.itch.io/")+
clink("CatGirl","(Unity-chan)Kanbayashi Yuko<br>© Unity Technologies Japan/UCL","https://unity-chan.com/contents/guideline/")+
clink("Monsters","RPG dot(R-do) monta!","http://rpgdot3319.g1.xrea.com/")+
clink("Sushi","Ichika","https://www.ac-illust.com/main/profile.php?id=23341701&area=1")+
clink("Textures","PiiiXL","https://piiixl.itch.io/")+
clink("Banner Materials,Lock on cursor<br>","Nanamiyuki's Atelier","https://nanamiyuki.com/")+
clink("Sniper animated","DJMaesen","https://sketchfab.com/3d-models/sniper-animated-eae1ba5b43ae4bc89b0647fb5d8a2d27")+
clink("Parasite Zombie","Mixamo","https://www.mixamo.com/")+
clink("MiniZombie&RedHat","Fkgcluster","https://fkgcluster.itch.io/survivaltowerdefense")+
clink("BloodEffect","XYEzawr","https://xyezawr.itch.io/gif-free-pixel-effects-pack-5-blood-effects")+
clink("Cats","girlypixels","https://girlypixels.itch.io/")+
clink("Terminator-Core","Fred Drabble","https://sketchfab.com/3d-models/fusion-core-f717683d5502496d9e1ef1f1e1d1cb45" )+
clink("Terminator-Robo","Threedee","https://www.threedee.design/cartoon-robot")+
clink("Meowknight","9E0", "https://9e0.itch.io/")+
clink("Vegetable","Butter Milk","https://butterymilk.itch.io/")+
clink("Flower","kathychow","https://kathychow.itch.io/")+
clink("Crops", "bluecarrot16, Daniel Eddeland (daneeklu),<br> Joshua Taylor, Richard Kettering (Jetrel).<br> Commissioned by castelonia", "https://opengameart.org/content/lpc-crops")+
clink("Farmer","Butter Milk","https://butterymilk.itch.io/")

            )


addons = ("<b>[ Original Add-on ]</b><br>"+
clink ("Enhance main window","Arthur Milchior","https://github.com/Arthur-Milchior/anki-enhance-main-window")+
clink ("Based on" ,"Anki code by Damien Elmes", "https://github.com/dae")+
clink ("Based on" ,"Helen Foster's code in add-on Deck counts now later", "https://github.com/HelenFoster")+
clink ("Original idea", "Juda Kaleta")+
clink ("Somme CSS","Some idea from cjdduarte")+
clink ("Bug correction","telotortium on Github")+
clink ("Percent bar","Idea and partial realization by Kyle Khonkhortisan Mills")+
clink ("Contributor","Kyle Mills","https://github.com/khonkhortisan")+
clink ("Contributor","ngirard","https://github.com/ngirard")+
clink ("Contributor","grac-zh","https://github.com/grac-zh")+
clink ("Contributor","Aleksej","https://github.com/aleksejrs")+
clink ("Contributor","Robert Irelan","https://github.com/telotortium")+
clink ("Contributor","Scott Noyes","https://github.com/snoyes")+
clink ("Contributor","Guillem Palau","https://github.com/guillempalau")+
clink ("Contributor","Sam Bradshaw","https://github.com/roxgib")+
clink ("Contributor","Jeffrey Ying","https://github.com/Jefftree")+
clink ("Contributor","Gustaf-C","https://github.com/Gustaf-C")
)

budle = ("<b>[ BUNDLE SOURCE CODE ]</b><br>"+
clink ("BGM","Pyglet","https://pyglet.readthedocs.io/en/latest/index.html")+
clink ("webp","dwebp","https://developers.google.com/speed/webp/download")+
clink ("midi","FluidSynth","https://www.fluidsynth.org/")

)

thankYou = ("""
<br><br><br>
<h3>%s</h3><br>""" % ADDON_NAME +
clink("Customized  by", "Shigeyuki","https://www.patreon.com/Shigeyuki")+
"""
<br>
Thank you very much!
<br><br><br><br>
""")