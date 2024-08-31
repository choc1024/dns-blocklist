'''
Import Necessary Libraries

Because I want the highest compatibility and ease of use, I made sure
to only import libraries that already come bundled with Python 3.

PLEASE do not use Python 2.

Sys: Used to know the arguments
Datetime: Get the current time, for logging.
Subprocess: For running commands, e.g., hostlist-compiler, git push, git commit, etc.
Json: JSON files handling
shutil: Copying files
os: Path handling
'''

import sys
from datetime import datetime
import subprocess
import json
import shutil
import os



'''
Define Functions.

'''

# ANSI Code to Log with color
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))

# tp is for Type, but that can cause conflicts with Python
def log(tp, text, terminate = None):

    # Get the time of the log
    logTime = datetime.now()

    # Log Types
    if tp.lower() == "info":
        print("[" + str(logTime) + " | INFO]: " + str(text))
    elif tp.lower() == "ok":
        prGreen("[" + str(logTime) + " | SUCCESS]: " + str(text))
    elif tp.lower() == "warn":
        prYellow("[" + str(logTime) + " | WARNING]: " + str(text))
    elif tp.lower() == "error":
        prRed("[" + str(logTime) + " | ERROR]: " + str(text))
    elif tp.lower() == "fatal":
        prPurple("[" + str(logTime) + " | FATAL]: " + str(text))
    elif tp.lower() == "try":
        prCyan("[" + str(logTime) + " | Trying]: " + str(text))

    # Terminate Process; e.g., a fatal error occured
    if terminate == True:
        temp = datetime.now()
        prPurple("[" + str(temp) + " | TERMINATION ORDER REIVED]: Terminating Process...")
        exit()

# Self-Explainable
def delete_all_files_in_directory(directory_path):
    # List all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        # Check if it is a file (not a directory)
        if os.path.isfile(file_path):
            os.remove(file_path)  # Delete the file
            print(f"Deleted file: {file_path}")

log("ok", "Libraries Imported, Functions Defined. Everything is OK.")



'''
Gets the time as of running the script

'''

# Get Time
startTime = datetime.now()

version = "2.5"

log("info", "Starting time: " + str(startTime) + ", version: " + version)


# Get the arguments
arguments = sys.argv[1:]  # Exclude the script name


# Help Text to display for instructions
help_txt = f"Choc1024's Unified Blocklist\nVersion: {version}\nHelp Manual:\n          --help, -h        Displays this help text\n          --version, -v     Displays the version\n          --config, -c      Manually input the location to the config file, default is latest/config.json\n          --temp, -t        Manually input the temporary directory\n          --release, -r     Tells the script that this will be a release build, and you must specify the version (e.g., --release v4.6)\n          --not-latest     (NOT RECOMMENDED), (DEPRECATED, WILL NOT WORK) Does not update the list in the latest folder, but will instead put it in the 'dev' folder (it will create it if it does not exist). The script will automatically delete the 'dev' folder if the argument is not specified.\n          --change 'changes'     Specifies the changes to add to the CHANGELOG.md."

log("ok", "Help Text is OK")


# Check if either the help flag or version flags are used
if "--help" in arguments or "-h" in arguments:
    print(help_txt)
    exit()

if "--version" in arguments or "-v" in arguments:
    print("Version: " + version)
    exit()

# Define argument variables
argConfig = False
argConfigValue = ""
argTemp = False
argTempValue = ""
argRelease = False
argReleaseVer = ""
argNotLatest = False
argChange = False
argChangeText = ""




'''
This part is used to detect which arguments are used.
If an argument is detected, it flags the respective variable value.

'''
# Argument Check
n = 0

while n != len(arguments):
    if arguments[n] == "--config" or arguments[n] == "-c":
        if argConfig == True:
            print("Error: argument cannot be used twice: '" + arguments[n] + "''")
            exit()
        elif argConfig == False:
            argConfig = True
            n += 1
            continue
        else:
            print("Unknown Error. Quitting.")
            exit()

            
    elif arguments[n] == "--temp" or arguments[n] == "-t":
        if argTemp == True:
            print("Error: argument cannot be used twice: '" + arguments[n] + "''")
            exit()
        elif argTemp == False:
            argTemp = True
            n += 1
            continue
        else:
            print("Unknown Error. Quitting.")
            exit()


    elif arguments[n] == "--release" or arguments[n] == "-r":
        if argRelease == True:
            print("Error: argument cannot be used twice: '" + arguments[n] + "''")
            exit()
        elif argRelease == False:
            argRelease = True
            n += 1
            continue
        else:
            print("Unknown Error. Quitting.")
            exit()


    elif arguments[n] == "--not-latest":
        if argNotLatest == True:
            print("Error: argument cannot be used twice: '" + arguments[n] + "''")
            exit()
        elif argNotLatest == False:
            print("WARNING: This argument is NOT RECOMMENDED.")
            print("Are you sure to proceed? (y/n): ")
            tmp = input()
            if n.lower() == y:
                argConfig = True
                n += 1
                continue
            else:
                print("Abborting.")
                exit()
        else:
            print("Unknown Error. Quitting.")
            exit()

    elif arguments[n-1] == "--config" or arguments[n-1] == "-c":
        argConfigValue = arguments[n]
        n += 1
        continue

    elif arguments[n-1] == "--change":
        argChangeText = arguments[n]
        n += 1
        continue
        
    elif arguments[n] == "--change":
        if argChange == True:
            print("Error: argument cannot be used twice: '" + arguments[n] + "'")
            exit()
        elif argChange == False:
            argChange = True
            n += 1
            continue
        else:
            print("Unknown Error. Quitting.")
            exit()

    elif arguments[n-1] == "--temp" or arguments[n-1] == "-t":
        argTempValue = arguments[n]
        n += 1
        continue

    elif arguments[n-1] == "--release" or arguments[n-1] == "-r":
        argReleaseVer = arguments[n]
        n += 1
        continue

    else:
        print("Unknown argument: '" + arguments[n] + "', use the '--help' or '-h' argument to view instructions.")
        exit()

        
'''

Now this will basically check and log which arguments are used.

'''

if argConfig:
    log("info", "Config argument detected. Using config from " + argConfigValue)
else:
    log("info", "Using config from latest/config.json")
if argTemp:
    log("info", "Temp argument detected. Using folder " + argTempValue)
else:
    log("info", "Using folder TEMP as temporary storage folder.")
if argRelease:
    log("info", "Release argument detected. This will be release " + argReleaseVer)
else:
    log("info", "No release argument detected, this will be a snapshot.")


'''

Now it will copy the config.json file to a temporary folder

'''

if argConfig:
    log("try", "Trying to open the custom config file to test if it is valid")
    try:
        log("info", "Custom config file is " + argConfigValue)
        with open(argConfigValue, 'r') as file:
            log("ok", "Custom config path is valid!")
            log("try", "Now verifying if it is a valid json...")
            configFile = json.load(file)
        log("ok", "Config file is valid!")


        if argTemp:
            log("try", "Now copying the config file to the custom temporary folder " + argTempValue)
            try:

                srcConfig = argConfigValue
                destConfigDir = argTempValue

                try:
                    os.makedirs(destConfigDir, exist_ok=False)
                    log("ok", "Made the temporary directory!")                    
                except:
                    log("error", "The temporary folder alrady exists. A fatal error may occur if it has contents.")


                destConfig = os.path.join(destConfigDir, os.path.basename(srcConfig))

                
                shutil.copy(srcConfig, destConfig)

                log("ok", "Copied Config file successfully to destination!")

            except:
                print("fatal", "The provided temp folder is invalid, requires higher permission, or an unknown error occured.", True)
        else:
            log("try", "Now copying the config file to the TEMP folder...")
            try:
                srcConfig = argConfigValue
                destConfigDir = "TEMP"

                try:
                    os.makedirs(destConfigDir, exist_ok=False)
                    log("ok", "Made the temporary directory!")
                except:
                    log("error", "The temporary folder alrady exists. A fatal error may occur if it has contents.")


                                 
                destConfig = os.path.join(destConfigDir, os.path.basename(srcConfig))
                
                shutil.copy(srcConfig, destConfig)

                log("ok", "Config copied to destination!")

            except:
                log("fatal", "Error when trying to copy config to destination.", True)
        
    except:
        log("fatal", "Provided config path is either invalid, or the config is not a valid json")
else:
    log("try", "Checking if the config file in the default path is valid...")
    try:
        with open('latest/config.json', 'r') as file:
            log("ok", "The config file exists.")
            log("try", "Now checking if the default config file is a valid json")
            data = json.load(file)
        log("ok", "The default config file is valid and accessible!")

        if argTemp:
            log("try", "Now copying the config file to the custom temporary folder " + argTempValue)
            try:

                srcConfig = "latest/config.json"
                destConfigDir = argTempValue

                try:
                    os.makedirs(destConfigDir, exist_ok=False)
                    log("ok", "Made the temporary directory!")                    
                except:
                    log("error", "The temporary folder alrady exists. A fatal error may occur if it has contents.")


                destConfig = os.path.join(destConfigDir, os.path.basename(srcConfig))

                
                shutil.copy(srcConfig, destConfig)

                log("ok", "Copied Config file successfully to destination!")

            except:
                print("fatal", "The provided temp folder is invalid, requires higher permission, or an unknown error occured.", True)


        else:
            log("try", "Now copying the config file to the TEMP folder...")
            try:
                srcConfig = "latest/config.json"
                destConfigDir = "TEMP"

                try:
                    os.makedirs(destConfigDir, exist_ok=False)
                    log("ok", "Made the temporary directory!")
                except:
                    log("error", "The temporary folder alrady exists. A fatal error may occur if it has contents.")


                                 
                destConfig = os.path.join(destConfigDir, os.path.basename(srcConfig))
                
                shutil.copy(srcConfig, destConfig)

                log("ok", "Config copied to destination!")

            except:
                log("fatal", "Error when trying to copy config to destination.", True)


    except:
        log("fatal", "Provided config path is either invalid, or the config is not a valid json")

        

log("ok", "Preparations complete.")







'''
The Preparations are now complete.
We here will first use datetime to set the last compilation time, 
and then use subprocess to use the hostlist-compiler tool made by the AdGuard team and
installable via NPM to compile the blocklists.
'''



last_compiledtm = datetime.now()

log("info", "Compilation start time is " + str(last_compiledtm))

log("try", "Using subprocess to run hostlist-compiler. If this returns an error, it is probably because it is not installed correctly.")
log("info", "This will take some time, about 40 minutes minimum.")
run = subprocess.Popen(
    ["hostlist-compiler", "-v", "-c", destConfig, "-o", os.path.join(destConfigDir, "output.txt")],
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE,
    universal_newlines=True, 
    text=True, 
    bufsize=1
)


for line in run.stdout:
    print(line, end='')

run.stdout.close()
run.wait()

if run.returncode != 0:
    log("fatal", "Hostlist-compiler crashed, returncode is: " + str(run.returncode), True)
elif run.returncode == 0:
    log("ok", "Hostlist-compiler compiled successfully.")




log("try", "Removing the comments from the start of the file...")


'''
IMPORTANT

This part of the code is ChatGPT-made
'''

# File paths
input_file_path = os.path.join(destConfigDir, "output.txt")
output_file_path = os.path.join(destConfigDir, "temp.txt")

# Open the input file for reading and a temporary output file for writing
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    skip = True

    for line in input_file:
        # Check if we should skip lines
        if skip:
            if not line.startswith('!'):
                skip = False  # Stop skipping when a non-`!` line is found

        # If we're not skipping, write the line to the output file
        if not skip:
            output_file.write(line)

# Replace the original file with the modified file
os.replace(output_file_path, input_file_path)

log("ok", "Comments removed!")
log("try", "Now adding new custom comments")

# Define file paths
original_file_path = input_file_path
temp_file_path = output_file_path

# Define lines to insert at the beginning
if argRelease:
    new_lines = [
        "! Choco's Combined List\n",
        "! By choc1024, hosted on GitHub and GitLab: \n",
        "! (sources)\n",
        "! \n",
        "! Version: " + argReleaseVer + "\n",
        "! Last Compiled: " + str(last_compiledtm) + "\n",
        "! \n",
        "! Compiled with @adguard/hostlist-compiler v1.0.26\n",
        " "
    ]
else:
    new_lines = [
        "! Choco's Combined List\n",
        "! By choc1024, hosted on GitHub and GitLab: \n",
        "! (sources)\n",
        "! \n",
        "! Snapshot Version: " + str(last_compiledtm) + "\n",
        "! \n",
        "! Compiled with @adguard/hostlist-compiler v1.0.26\n",
        " \n"
    ]


# Open the original file for reading and a temporary file for writing
with open(original_file_path, 'r') as original_file, open(temp_file_path, 'w') as temp_file:
    # Write the new lines to the temporary file
    temp_file.writelines(new_lines)
    
    # Write the existing content of the original file to the temporary file
    for line in original_file:
        temp_file.write(line)

# Replace the original file with the temporary file
os.replace(temp_file_path, original_file_path)

log("ok", "Done! The blocklist generation process is complete.")


if argRelease:
    try:
        releaseDir = os.path.join("src/versions", argReleaseVer)
        
        os.makedirs(releaseDir, exist_ok=True)
        log("ok", "The release directory is available")
        
        releaseOutput = os.path.join(releaseDir, "output.txt")

        #destConfig, destCOnfigDIr

        log("try", "Copying the blocklist output.txt to the release folder...")
        shutil.copy(os.path.join(destConfigDir, "output.txt"), releaseOutput)
        log("ok", "Success!")

        configOutput = os.path.join(releaseDir, os.path.basename(destConfig))

        log("try", "Copying the config file to the release folder...")
        shutil.copy(destConfig, configOutput)
        log("ok", "Success!")

        log("try", "Renaming the config file to config.json (if not already)...")
        os.rename(configOutput, os.path.join(releaseDir, "config.json"))
        log("ok", "Success!")
        log("try", "Renaming the output.txt blocklist to blocklist.txt...")

        os.rename(releaseOutput, os.path.join(releaseDir, "blocklist.txt"))
        log("ok", "Success!")

        blocklistDir = os.path.join(releaseDir, "blocklist.txt")

        configDir = os.path.join(releaseDir, "config.json")

        log("try", "Deleting all outdated files in the 'latest' folder to replace them with updated ones...")
        delete_all_files_in_directory("latest")
        log("ok", "Success!")

        listLatest = os.path.join("latest", os.path.basename(blocklistDir))
        configLatest = os.path.join("latest", "config.json")

        log("try", "Copying the new files to destination...")
        shutil.copy(blocklistDir, listLatest)
        shutil.copy(configDir, configLatest)
        log("ok", "Success!")
        log("try", "Renaming blocklist.txt to latest.txt in the 'latest' folder...")
        
        os.rename(listLatest, os.path.join("latest", "latest.txt"))
        log("ok", "Success!")
    except:
        log("error", "A non-fatal error occured. The blocklist was generated, but not copied to its destination(s). Please check the previous logs and post this on GitHub/GitLab issues for support.")
    
elif not argRelease:

    try:
        configOrigin = destConfig
        listOrigin = os.path.join(destConfigDir, "output.txt")


        log("info", "Configuring Snapshot Directory...")
        snapshotDir = str(os.path.join("src/snapshots", str(last_compiledtm)))
        snapshotDir = snapshotDir.replace(" ", "_")
        log("ok", "Success!")
        log("info", "Snapshot Directory is at " + str(snapshotDir))
        log("try", "Making snapshot directory...")
        
        os.makedirs(snapshotDir, exist_ok=True)
        log("ok", "Success!")

        snapshotConfig = os.path.join(snapshotDir, os.path.basename(configOrigin))
        snapshotList = os.path.join(snapshotDir, "output.txt")

        log("try", "Copying files to destination...")
        shutil.copy(configOrigin, snapshotDir)
        shutil.copy(listOrigin, snapshotDir)
        log("ok", "Success!")

        log("try", "Renaming 'output.txt' to 'blocklist.txt'...")
        os.rename(snapshotList, os.path.join(snapshotDir, "blocklist.txt"))
        snapshotList = os.path.join(snapshotDir, "blocklist.txt")
        log("ok", "Success!")

        log("try", "Copying blocklist.txt and latest.txt to the 'latest' folder...")
        shutil.copy(snapshotList, os.path.join("latest", "blocklist.txt"))
        shutil.copy(snapshotConfig, os.path.join("latest", os.path.basename(snapshotConfig)))
        log("ok", "Success!")
        
        log("try", "Renaming blocklist.txt to latest.txt")
        os.rename(os.path.join("latest", "blocklist.txt"), os.path.join("latest", "latest.txt"))
        log("ok", "Success!")

    except:
        log("error", "A non-fatal error occured, the blocklist was generated but couldn't be copied to the destination.")
    


log("ok", "Everything seems to be OK")
log("try", "Running 'git add .'")

gitAdd = subprocess.run(["git", "add", "."])
log("ok", "Ran 'git add .'")

log("info", "The output is ''" + str(gitAdd.stdout) + "'. If it is none, then the command was successful. Otherwise, check the git installation and repository files.")


log("try", "Running 'git commit -m \"Automatic Compilation Update\"'...")

gitCom = subprocess.run(["git", "commit", "-m", "'Automatic Compilation Update'"])
log("OK", "Success!")
log("info", "The output is: " + str(gitCom.stdout))


log("ok", "Everything seems to be in place.")

log("try", "Pushing to GitHub.")
log("info", "Please make sure that you have GitHub credentials cached, if not, login with 'gh auth login'.")
ghPush = subprocess.run(["git", "push", "https://github.com/choc1024/dns-blocklist.git", "main"])
log("info", "Output: " + str(ghPush.stdout))

log("try", "Pushing to GitLab.")
log("info", "Please make sure that you have GitLab credentials cached, if not, login with 'glab auth login'.")

glabPush = subprocess.run(["git", "push", "https://gitlab.com/choc1024/dns-blocklist.git", "main"])

log("info", "Output: " + str(ghPush.stdout))

if argNotLatest:
    log("warning", "--not-latest is set, but is deprecated. Nothing will be done regards that.")



'''
Time to update the CHANGELOG.md

Again, I am not good with file handling so this is ChatGPT made
'''



if True:

    if argChangeText == "":
        argChangeText = "No changelog information provided"
    else:
        argChangeText = argChangeText.replace("'", "")
        argChangeText = argChangeText.replace("\"", "")

    if argRelease:
        compileType = argReleaseVer
    else:
        compileType = "Snapshot " + str(last_compiledtm)
    
    log("try", "Modifying CHANGELOG.md")
    # List of new lines to add at the beginning
    new_lines = [
        "# CHANGELOG\n",
        " \n",
        " \n",
        "## " + compileType + "\n",
        " \n",
        "Time of Compilation: " + str(last_compiledtm) + "\n",
        "Time Elapsed: " + str(datetime.now() - last_compiledtm) + "\n",
        " \n",
        argChangeText + "\n",
        " \n"
    ]



    # Open the file, read all lines, and close the file
    with open("CHANGELOG.md", "r") as file:
        log("ok", "Opened CHANGELOG.md")
        lines = file.readlines()

    # Remove the first line
    lines = lines[1:]

    # Insert the new lines at the beginning
    lines = new_lines + lines

    # Write the updated content back to the file
    with open("CHANGELOG.md", "w") as file:
        file.writelines(lines)
        log("ok", "Wrote changes to CHANGELOG.md")

    log("ok", "All operations completed!")

















