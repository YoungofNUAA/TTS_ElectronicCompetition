import winsound

ppp = winsound.PlaySound(None,winsound.SND_NODEFAULT)
wav = r'E:\PycharmWorkspace\WaveRNN\quick_start\quick_start.wav'

def playmusic(wav):
    global ppp
    print('播放')
    ppp = winsound.PlaySound(wav,winsound.SND_ALIAS)

def stopmusic():
    global ppp
    winsound.PlaySound(ppp,winsound.SND_PURGE)
