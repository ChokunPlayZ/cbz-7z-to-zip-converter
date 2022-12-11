# CBZ 7z to Zip Converter

## What is this?

CBZ ebook file is just a zip file underneth but it is possible to use 7z, so there will be people out there package their book using 7z format which is not supported by most ebook management software like "Komga" due to limited libary and the format being old, this tool will help you convert that CBZ 7z to zip, it can even do batches of it in case you get a lot of 7z file you want to convert!

## How Does it works?

1. scans all the files in input directroy
2. extracts the file into the temp folder
3. repackage the files in temp folder as a cbz file again using zip format instead of 7z
4. clean up data in temp dicretory

## How To Use

1. Git clone this repo or use the download button
2. extract the files if you use the "download as zip" option
3. ensure that in the folder with the main.py file there is an `input` `output` and `temp` directory if not exist create them, the script will not run properly without these directories
4. install the require packages using

```bash
pip3 install -r requirements.txt
```

5. drop the files you want to convert inside `input` folder
6. run the python script

```bash
python3 main.py
```

7. wait till it finishes
8. Enjoy your Books!

the converted files will be in the `output` folder

## If you have problems read here!

Here's are some problems I encounter during development you might find helpful

### 1. PAtool not found

Error:

```bash
ValueError: patool not found! Please install patool!
```

this error was caused by patool not being installed properly make sure you install python and add it to PATH

here's a quick fix for macos users!

print out your `PATH` varible

```shell
echo $PATH
```

make sure there is a python directory in there it should looks somthing like this

```bash
╭─chokun@Chokuns-MacBook-Pro.local ~/Projects/cbz 7z to zip converter  
╰─➤  echo $PATH
/Users/chokun/Library/Python/3.9/bin/:
```

if it isn't there find where your python bin location is

(this varies from machine to mahine so I wont be providing copy n place script here it might break your stuff)

```bash
echo 'export PATH=<YOUR PYTHON BIN DIR>:$PATH' >> $HOME/.zshrc
```

change the bin directroy and run it and you should be ready to go!

just as a check restart terminal and try to run

```bash
patool
```

there should be an output if not then you might got other problems

---



### 2. could not find an executable program to extract format 7z

Error:

```bash
patool error: error extracting book.cbz: could not find an executable program to extract format 7z; candidates are (7z,7za,7zr),
```

this should be easy to fix in windows just install 7zip

for macos/linux install [homebrew](https://brew.sh/) and run this

```bash
 brew install p7zip
```

this should make it work

---



if there is any other problems feel free to open an issue, I'll answer ASAP

or just message me on discord `winword.zip#0036` If I dont answer then your message is caught in the "message request" section and discord failed to send push noti

# Like what I do and want to support my work?

Buy me a coffee: [buymeacoffee/chokunplayz](http://buymeacoffee.com/chokunplayz)
