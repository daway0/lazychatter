# Lazy Chatter Detector

It can detect Lazy Chatters.
!(Bar Plot)[https://s23.picofile.com/file/8447934734/tarikh_e_emamat_barplot.png]
!(Pie Plot)[https://s23.picofile.com/file/8447934750/tarikh_e_emamat_pieplot.png]

# Quick Start

1. Install script dependencies: `pip install -r requirements.txt`
2. Put **chat files (or just 1 one chat file)** in `lazy_chatter_detector` directory (next to other .py files)
3. Run `MainScript.py`

# Usage

**Plots:** After executing MainScript.py, script will show you **pie** and **bar** plots in a row (with matplotlib GUI).

**Student Chats:** All student chats store in `./std_chats` in `.txt` format.

# Do NOT...

1. change name of chats that you download from daan plattrom
2. put different types of chat file together, this does not cause error, but it is not logically justified

   `bbb-تاریخ امامت[public-chat]_2022-2-23_17-52.txt`

   `bbb-تاریخ امامت[public-chat]_2022-2-30_17-52.txt`

   `bbb-تاریخ امامت[public-chat]_2022-3-6_17-52.txt`

   `bbb-سیستم عامل[public-chat]_2022-3-13_17-52.txt`

   **script:** !??? تاریخ امامت + سیستم عامل
