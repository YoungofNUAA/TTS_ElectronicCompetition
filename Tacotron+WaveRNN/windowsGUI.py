import sys
import PySimpleGUI as sg
import os
import GUI.app_audio as app
import GUI.playAudio as pl

sg.ChangeLookAndFeel('SandyBeach')
layout = [[sg.Text('我是大白(●—●)，我在听呢:',size=(150,1),justification='left',font=("Terminal",10),auto_size_text=True)],
          [sg.Input(do_not_clear=False,size=(54,1),key='_IN_')],
          [sg.Button('开始合成语音（中文）',key='ShowChina'),sg.Button('开始合成语音（英文）',key='ShowEnglish'),sg.Button('退出系统',key='Exit')],
          [sg.Text('采样速率:',size=(10,1),auto_size_text=True),sg.Text('    ',size=(10,1),key='_OUTPUTFREQ_',auto_size_text=True)],
          [sg.Text('通道数量:',size=(10,1),auto_size_text=True),sg.Text('    ',size=(10,1),key='_OUTPUTCHAN_',auto_size_text=True)],
          [sg.Text('采样宽度:',size=(10,1),auto_size_text=True),sg.Text('    ',size=(10,1),key='_OUTPUTSAMP_',auto_size_text=True)],
          [sg.Text('帧速率:',size=(10,1),auto_size_text=True),sg.Text('    ',size=(10,1),key='_OUTPUTFRAM_',auto_size_text=True)],
          [sg.Text('总帧数:',size=(10,1),auto_size_text=True),sg.Text('   ',size=(10,1),key='_OUTPUTNFRAM_',auto_size_text=True)],
          [sg.Text('时长（s）:',size=(10,1),auto_size_text=True),sg.Text('   ',size=(10,1),key='_OUTPUTSECOND_',auto_size_text=True)],
          [sg.Text('-----------------Loading------------------------->',size=(36,1)),
           sg.Button('想听我说话？中文',key='SpeakChina'),sg.Button('想听我说话？英文',key='SpeakEnglish')],
          [sg.Graph(canvas_size=(620,470),graph_bottom_left=(-100,-100),background_color='white',graph_top_right=(100,100),key='graph'),
           sg.Graph(canvas_size=(650,470),graph_bottom_left=(-100,-100),background_color='white',graph_top_right=(100,100),key='graph1')]
          ]

window = sg.Window('大白(●—●)',layout,resizable=True,size=(1300,800),location=(100,100)).Finalize()
graph = window.Element('graph')
graph1 = window.Element('graph1')

while True:
    event,values = window.Read()
    if event is None or event == 'Exit':
        break
    if event == 'ShowChina':
        isEnglish = 1;
        root = './quick_start'
        words = values['_IN_']
        os.system("python quick_start.py --input_text "+'\"'+words+'\"'+' '+'--batched')
        # sampling_freq,audio_ori,nchannels,sampwidth,framerate,nframes,f = app.get_params(root,isEnglish)
        # Second = round(audio_ori.shape[0] / float(sampling_freq), 3)
        # app.plot_time(root)
        # app.plot_freq(root)
        # window.Element('_OUTPUTFREQ_').Update(sampling_freq)
        # window.Element('_OUTPUTCHAN_').Update(nchannels)
        # window.Element('_OUTPUTSAMP_').Update(sampwidth)
        # window.Element('_OUTPUTFRAM_').Update(framerate)
        # window.Element('_OUTPUTNFRAM_').Update(nframes)
        # window.Element('_OUTPUTSECOND_').Update(Second)
        graph.DrawImage(root+'/sayhello.png',color='red',location=(-100,100))
        graph1.DrawImage(root + '/sayhello_spec.png', color='red', location=(-100, 100))
    if event == 'SpeakChina':
        pl.playmusicChina()

    if event == 'ShowEnglish':
        isEnglish = 1
        root = './quick_start'
        words = values['_IN_']
        os.system("python quick_start.py --input_text "+'\"'+words+'\"'+' '+'--batched')
        # sampling_freq,audio_ori,nchannels,sampwidth,framerate,nframes,f = app.get_params(root,isEnglish)
        # Second = round(audio_ori.shape[0] / float(sampling_freq), 3)
        # app.plot_time(root)
        # app.plot_freq(root)
        # window.Element('_OUTPUTFREQ_').Update(sampling_freq)
        # window.Element('_OUTPUTCHAN_').Update(nchannels)
        # window.Element('_OUTPUTSAMP_').Update(sampwidth)
        # window.Element('_OUTPUTFRAM_').Update(framerate)
        # window.Element('_OUTPUTNFRAM_').Update(nframes)
        # window.Element('_OUTPUTSECOND_').Update(Second)
        graph.DrawImage(root+'/sayhello.png',color='red',location=(-100,100))
        graph1.DrawImage(root + '/sayhello_spec.png', color='red', location=(-100, 100))
    if event == 'SpeakEnglish':
        pl.playmusicEnglish()
window.Close()
