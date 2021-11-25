# Create QrCode on Siemens NX

This project made for [Sibernetik M&A Applications](https://sibernetik.com.tr) firm.

## Installation

To use the program, please review the steps below.

First of all, you need [Python](https://www.python.org) to use this code. If you have NX10 or higher version, recommended [Python 3.7.5](https://www.python.org/downloads/release/python-375/) version. Don't forget to check which python version your NX is using.

### **Install Python**


```bash
pip install qrcode
pip install pillow
```
or
```bash
Start sys.bat
```


Find `ugii_env_ug.bat` in NX path. **C:/Program Files/Siemens/NX/UGII** the file probably in there.
Open with notepad.
You must get administrator permission from properties->security tab for change texts in file.

In the file: **Find `UGII_PYTHONPATH`**. Add your **Python Path** at the end of the line.
Do same with `PYTHONPATH`
```
UGII_PYTHONPATH=${UGII_PYTHON_HOME};${UGII_PYTHON_HOME}\Python37.zip;${UGCHECKMATE_DIR}\python;%UserProfile%\AppData\Local\Programs\Python\Python37\Lib\site-packages;%UserProfile%\AppData\Local\Programs\Python\Python37
```
```
PYTHONPATH=${UGII_PYTHONPATH};${JK_KIT}\lib;${JK_KIT}\library\script;%UserProfile%\AppData\Local\Programs\Python\Python37\Lib\site-packages;%UserProfile%\AppData\Local\Programs\Python\Python37
```


## Usage

<pre>
  <center>
    <img src=".\\img\\img1.png" width="500">
    <figcaption>Fig.1 - select File->Preferences->User Interface.</figcaption>
  </center>                  
</pre>

or press "<kbd>Ctrl</kbd> + 2" on keyboard shortcut.

<pre>
  <center>
    <img src=".\\img\\img2.png" width="500">
    <figcaption>Fig.2 - Change the journal language to Python.</figcaption>
  </center>                  
</pre>

After that, you need to press <kbd>Alt</kbd> <kbd>F11</kbd> for open journal editor.

<pre>
  <center>
    <img src=".\\img\\img3.png" width="500">
    <figcaption>Fig.3 - Open File->NxQrCode.py and RUN </figcaption>
  </center>                  
</pre>

> If you had an error about NX or the code. Please contact with me. Telegram: **sefaeren0** E-Mail: **sefa.eren000@gmail.com**

## License
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
