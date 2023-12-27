#!/bin/bash
#install gdown to download google drive's shared file
pip install gdown

# download them (vol.1,2,7,8) with their file ids
gdown '15UhUBr__vE6X-hlu11uDwqt-KRQYVz5o'
gdown '1usM2qqG-106AloZa3V27JWSnaBIjoIFu'
gdown '1-AGVlteiIE5z6RkGXc2_BQtcKkchIt7W'
gdown '17lVN70B4JsL5dK_bK70wLnWqTL4vyb6J'

unzip vol_1.zip
unzip vol_2.zip
unzip vol_7.zip
unzip vol_8.zip
