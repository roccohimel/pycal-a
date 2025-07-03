# Pycal-A beta version 0.2
Pycal-A is a free, Python based, Advanced calculator for Linux, Mac, and Windows. Pycal-A lets you:
- Evaluate basic equations
- Calulate the area and circumfrance of a circle using diameter
- View date and time
- Use a stopwatch
- Set a timer
- Update direcly from the program
- Gain access to developer options

More feaures will be comming soon!
# Updates
Vist: https://github.com/roccohimel/pycal-a/releases   for all versio

Current support for: Beta versions 0 (BR0)

**Beta version 0.1 (BR0V1)**: https://github.com/roccohimel/pycal-a/releases/tag/pycal-a-bv0.1

July 1, 2025:
  - Released Pycal-A beta version 0.1 (BR0V1)
  - Currently working on support for Windows
  - Currently working on Pycal-A beta version 0.1.1

**Beta version 0.1.1 (BR0V1X1)**: https://github.com/roccohimel/pycal-a/releases/tag/pycal-a-bv0.1.1

July 2, 2025:
  - Fixed output repeating after chosen option
  - Added "clear" command to a Python definition: "clear()"
  - Added "python3 pycal-a.py" to a Python definition: "open()"
  - Added the start input to a Python definition: "startpmt()"
  - Added new start input choice: "Update Pycal-A"
  - Makes sure you have FireFox, then takes you to the GitHub repo to update Pycal-A.

**Beta version 0.1.2 (BR0V1X2)**: https://github.com/roccohimel/pycal-a/releases/tag/pycal-a-bv0.1.2

July 2, 2025:
- Added support for updating on the spot:
  This allows you to choose your operating system, then run script that re-installs Pycal-A from GitHub.

**Beta version 0.2 (BROV2)**: https://github.com/roccohimel/pycal-a/releases/tag/pycal-a-bv0.2

July 2 2025:
- Added clocks!!!
- Added date and time clock
- Added stopwatch
- Added timer

# Install support
Pycal-A beta version 0.2 (BR0V2) is supported on:
- Debian GNU/Linux 6.0 or newer
- Debian GNU/Linux 6.0 based distros or newer
- MacOS 10.13 or newer
- Windows 10 or newer
# Install newest version of Pycal-A: For Debian GNU/Linux
**DO NOT MOVE PYCAL-A OUT OF HOME FOLDER**
Run this bash script:
```
#!/bin/bash/
sudo apt update
sudo apt install python3
sudo apt upgrade python3
sudo apt install wget
sudo apt upgrade 
sudo rm pycal-a.py
wget https://raw.githubusercontent.com/roccohimel/pycal-a/refs/heads/main/pycal-a.py
```
Run Pycal-A using:
```
python3 pycal-a.py
```
# Install newest version of Pycal-A: For MacOS
**DO NOT MOVE PYCAL-A OUT OF HOME FOLDER**
Paste this bash script into the MacOS terminal:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update
brew install python@3.9
brew install wget
sudo rm pycal-a.py
wget https://raw.githubusercontent.com/roccohimel/pycal-a/refs/heads/main/pycal-a.py
```
Run Pycal-A using:
```
python3 pycal-a.py
```
# Install newest version of Pycal-A For Windows
Paste this script into the Windows command prompt:
```
winget install -e --id Python.Python.3.11
winget install -e --id JernejSimoncic.Wget
del /f /q "pycal-a.py"
wget https://raw.githubusercontent.com/roccohimel/pycal-a/refs/heads/main/pycal-a.py
```
