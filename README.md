
# Tracking class activity behavior
![activity tracker](https://s23.picofile.com/file/8448317118/activity.png)
                     

# Lazy Chatter Detector
**It can detect Lazy Chatters** 
based on [Daan platform](https://daan.ir/) chats:  , You can see chat samples in the `./chat-samples` directory.
# Bar plot
![Bar Plot](https://s22.picofile.com/file/8447995900/tebar.png)
# Pie plot
![Pie Plot](https://s23.picofile.com/file/8447995918/tepie.png)

# Quick Start
0. [Watch the guide on YouTube](https://youtu.be/pPJ-NBAdNGA)
1. Install script dependencies: `pip install -r requirements.txt`
2. Put **chat files (or a chat)** in `lazy_chatter_detector` directory (next to other `.py` files)
3. Run `MainScript.py`

# Usage

**Plots:** After executing `MainScript.py`, script will show you a **pie** and a **bar** plots in a row (with matplotlib GUI).

**Student Chats:** All student chats store in `./std_chats` in `.txt` format.

# DO NOT...

1. change name of the chats that you download from daan platform
2. put different types of chat file together, this does not cause any error, but it is not logically correct

   `bbb-تاریخ امامت[public-chat]_2022-2-23_17-52.txt`

   `bbb-تاریخ امامت[public-chat]_2022-2-30_17-52.txt`

   `bbb-تاریخ امامت[public-chat]_2022-3-6_17-52.txt`

   `bbb-سیستم عامل[public-chat]_2022-3-13_17-52.txt`

   **script:** !??? تاریخ امامت + سیستم عامل
