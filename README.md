# Auto ZingMp3
Author: QuocManh<br>
Description: Project automated web browser and do ZingMp3 tasks like play music,
skip, volume, download, get information of the song.

# Installation
- virtual enviroment

# Usages
- usages

# References
macos: verify chromedriver
- copy chromedriver: cp [path] /usr/local/bin
- xattr -d com.apple.quarantine chromedriver

Get api zing mp3:
https://mp3.zing.vn/xhr/media/get-source?type=audio&key=kmJHTZHNCVaSmSuymyFHLH
tìm theo keyword data-xml nha bạn, vd link này, chỉ cần Ctrl + F là thấy.
view-source:https://mp3.zing.vn/bai-hat/Cho-Toi-Lang-Thang-Ngot-Den/ZW79DF7C.html
=> data-xml="/media/get-source?type=audio&key=kHcnyZGspxapQJHyHTbnZHyZCDzHVmzZH" data-id="ZW79DF7C"
lưu ý nhỏ là view source bằng mp3.zing.vn mới thấy đc data-xml nha, zingmp3.vn ko ra đâu.