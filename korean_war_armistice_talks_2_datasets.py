# -*- coding: utf-8 -*-
"""Korean_War_Armistice_talks_2_datasets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tA0HcIX1WhwBzKVzC18aYuX6XiCTSrKa

# Classification of utterances in Korean War Armistice Talk documents

e.g.
An utterance is said by whom?

## Prepare datasets for classification task training
"""
'''
!gdown '15UhUBr__vE6X-hlu11uDwqt-KRQYVz5o'
!gdown '1usM2qqG-106AloZa3V27JWSnaBIjoIFu'

!unzip vol_1.zip
!unzip vol_2.zip

!gdown '1-AGVlteiIE5z6RkGXc2_BQtcKkchIt7W'
!gdown '17lVN70B4JsL5dK_bK70wLnWqTL4vyb6J'

!unzip vol_7.zip
!unzip vol_8.zip

!cat 'Cleaned_data_1/0100.txt'

"""**Speakers**

INTERPRETER (HGU):

UNITED NATIONS:

NORTH KOREA:

===

*Their utterances*

UNITED NATIONS: *In other words you mean there is only ....*

NORTH KOREA: *That is our opinion, and the opinion of the other party ...*

### make directories for datasets
"""
'''
import os

#make dataset directories
train_dir = 'armistice_talk/train'
if not os.path.exists(train_dir):
    os.makedirs(train_dir)
    if not os.path.exists(train_dir + 'un'):
        os.makedirs(train_dir+'/un')
    if not os.path.exists(train_dir + 'nk'):
        os.makedirs(train_dir+'/nk')

test_dir = 'armistice_talk/test'
if not os.path.exists(test_dir ):
    os.makedirs(test_dir )
    if not os.path.exists(test_dir  + 'un'):
        os.makedirs(test_dir +'/un')
    if not os.path.exists(test_dir  + 'nk'):
        os.makedirs(test_dir +'/nk')


"""### Convert all speakers(both sides) and their utterances

into every single file under dataset directories
"""

UN_speakings = []
NK_speakings = []

"""#### vol.1 & 2"""

import glob

fn1_list = glob.glob('Cleaned_data_1/*.txt')
fn2_list = glob.glob('Cleaned_data_2/*.txt')

def make_files(fn_list, vol):

    for fn in fn_list:
        #print(fn)
        ofn = os.path.basename(fn) #filename without directory name
        cnt = 0
        lines = open(fn).readlines()
        for line in lines:
            cnt += 1
            pos = line.find(':')
            if pos != -1:
                speaker = line[:pos].lower()
                utterance = line[pos+1:]

                if ('united nations' or 'un ' or 'col murray' or 'col butler') in speaker:
                    #input(line)
                    occur = (vol, ofn, cnt, utterance)
                    UN_speakings.append(occur)

                if ('north korea' or 'nk' 'capt kim') in speaker:
                    #input(line)
                    occur = (vol, ofn, cnt, utterance)
                    NK_speakings.append(occur)

    return (len(UN_speakings), len(NK_speakings))

print(make_files(fn1_list, 'vol1'))
print(make_files(fn2_list, 'vol2'))

print(UN_speakings[0])
print(NK_speakings[0])

"""#### vol.7 & vol.8"""

def load_nk_un_names():
    nk_names = "COL TSAI, COL WANG, COL LEE, COL PU, COL CHANG, COL JU,  COL WANG, COL O, COL HUANG,  MAJOR WU"
    un_names = "COL CAIRNS, COL CARLOCK, COL DARROW, COL SOMERVILL, COL MCCARTHY,  COL MURRAY, COL AUSTIN"
    nk_names = {name.strip().lower() for name in nk_names.split(',')}
    un_names = {name.strip().lower() for name in un_names.split(',')}
    return nk_names, un_names

n_names, u_names = load_nk_un_names()

print(n_names)
print(u_names)

fn1_list = glob.glob('Cleaned_data_7/*.txt')
fn2_list = glob.glob('Cleaned_data_8/*.txt')

def make_files(fn_list, vol):
    for fn in fn_list:
        #print(fn)
        ofn = os.path.basename(fn)
        cnt = 0
        lines = open(fn).readlines()
        for line in lines:
            cnt += 1
            pos = line.find(':')
            if pos != -1:
                speaker = line[:pos].lower()
                utterance = line[pos+1:]
                name_is = '0'
                for name in u_names:
                    if name in speaker: name_is = 'un'
                for name in n_names:
                    if name in speaker: name_is = 'nk'
                if name_is == 'un':
                    #input(line)
                    occur = (vol, ofn, cnt, utterance)
                    UN_speakings.append(occur)
                if name_is == 'nk':
                    #input(line)
                    occur = (vol, ofn, cnt, utterance)
                    NK_speakings.append(occur)

    return (len(UN_speakings), len(NK_speakings))

print(make_files(fn1_list, 'vol7' ))
print(make_files(fn2_list, 'vol8' ))

len(UN_speakings), len(NK_speakings)

"""## Write files"""

def write_files(speakings, speaker):
    fcnt = 0
    import random
    random.shuffle(speakings)
    data_dir = 'armistice_talk'
    train_idx = int(len(speakings)*0.8)
    for vol, ofn, cnt, utterance in speakings[:train_idx]:
        filename = f"{data_dir}/train/{speaker}/{vol}_{cnt}_{ofn}"
        print(filename)
        ofile = open(filename, 'w')
        ofile.write(utterance)
        ofile.close()
        fcnt += 1
    for vol, ofn, cnt, utterance in speakings[train_idx:]:
        filename = f"{data_dir}/test/{speaker}/{vol}_{cnt}_{ofn}"
        ofile = open(filename, 'w')
        ofile.write(utterance)
        ofile.close()
        fcnt += 1
    return fcnt

write_files(UN_speakings, 'un')

write_files(NK_speakings, 'nk')

print(len(UN_speakings), len(NK_speakings))
