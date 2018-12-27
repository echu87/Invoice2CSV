Requirements:
This project has only been tested on Windows
Use of Python 3.6 is recommended
Having visual studio ide is probably good as well
Tensor flow (gpu support)
CUDA® Toolkit 9.0.


pip install AWSCLI
pip install BOTO3
pip install wand
https://legacy.imagemagick.org/script/binary-releases.php#windows x86-64 version
pip install Pillow
install ghostscript; 32 bit version https://www.ghostscript.com/download/gsdnld.html (WE NEED TO LICENSE THIS)

Install tensorflow using these instructions, https://www.tensorflow.org/install/install_windows. Tried to install GPU support, however nvidia cuda toolkit is very finicky. 
I DID A THING, it works now. Make sure you add these paths to your SYSTEM PATH not user variables. (E:\Documents\Nvidia\cudnn-8.0-windows10-x64-v7\cuda\bin, C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\extras\CUPTI, C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\libnvvp, C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin)

GO OVER LICENSING BEFORE PUBLISHING
