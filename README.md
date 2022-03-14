
# Lazy Chatter Detector
**It can detect Lazy Chatters** 
based on [Daan platform](https://daan.ir/) chats
# Treacking Students activity (students of a class)
![activity tracker](https://s23.picofile.com/file/8448378034/students_activity_detail.png)
# Tracking class activity behavior
![activity tracker](https://s23.picofile.com/file/8448317118/activity.png)
# acceptable vs non acceptable (with detail)
![good](https://s22.picofile.com/file/8448341534/goodact.png)
![bad](https://s22.picofile.com/file/8448341426/badactivity.png)
                     


# Bar plot
![Bar Plot](https://s22.picofile.com/file/8447995900/tebar.png)
# Pie plot
![Pie Plot](https://s23.picofile.com/file/8447995918/tepie.png)

# Quick Start
0. [Watch the guide on YouTube](https://youtu.be/pPJ-NBAdNGA)
1. Install script dependencies: `pip install -r requirements.txt`
2. Put **chat files (or a chat)** next to other `.py` files (you can use `./chat-samples` chats)
3. Run `main-script.py`

# Features

**Plots:** After executing `main-script.py`, script will show you a **pie** ,a **bar** plots in a row (with matplotlib GUI). PDF-export option is available for best quality.

**Class activity behavoir:** After closing plot windows, you will see  pictures that describe class activity behavior(detailed and non-detailed). The pictures will be saved automatically as `activity.png`, `activity-detail.png`

`dark red ----> incresing activity ----> light red`

**Student Chats:** All student chats will be store in `./std_chats` in `.txt` format.

# DO NOT...

1. change name of the chats that you download from daan platform
2. put different types of chat file together, this does not cause any error, but it is not logically correct

   `bbb-تاریخ امامت[public-chat]_2022-2-23_17-52.txt`

   `bbb-تاریخ امامت[public-chat]_2022-2-30_17-52.txt`

   `bbb-تاریخ امامت[public-chat]_2022-3-6_17-52.txt`

   `bbb-سیستم عامل[public-chat]_2022-3-13_17-52.txt`

   **script:** !??? تاریخ امامت + سیستم عامل
