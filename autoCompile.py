import sys
from datetime import datetime
import subprocess
import json
import shutil
import os

def delete_all_files_in_directory(directory_path):
    # List all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        # Check if it is a file (not a directory)
        if os.path.isfile(file_path):
            os.remove(file_path)  # Delete the file
            print(f"Deleted file: {file_path}")







# Get Time
startTime = datetime.now()

version = "1.0"

# Get the arguments
arguments = sys.argv[1:]  # Exclude the script name

help_txt = f"Choc1024's Unified Blocklist\nVersion: {version}\nHelp Manual:\n          --help, -h        Displays this help text\n          --version, -v     Displays the version\n          --config, -c      Manually input the location to the config file, default is latest/config.json\n          --temp, -t        Manually input the temporary directory\n          --release, -r     Tells the script that this will be a release build, and you must specify the version (e.g., --release v4.6)\n          --not-latest      (NOT RECOMMENDED), (DEPRECATED, WILL NOT WORK) Does not update the list in the latest folder, but will instead put it in the 'dev' folder (it will create it if it does not exist). The script will automatically delete the 'dev' folder if the argument is not specified."

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

        
if argConfig:
    print("Config argument detected. Using config from " + argConfigValue)
else:
    print("Using config from latest/config.json")
if argTemp:
    print("Temp argument detected. Using folder " + argTempValue)
else:
    print("Using folder TEMP as temporary storage folder.")
if argRelease:
    print("Release argument detected. This will be release " + argReleaseVer)
else:
    print("No release argument detected, this will be a snapshot.")

if argConfig:
    try:
        print(argConfigValue)
        with open(argConfigValue, 'r') as file:
            print("cnfig opened")
            configFile = json.load(file)
            print("config loaded")
        print("Provided Config File Path is valid")

        if argTemp:
            try:
                srcConfig = argConfigValue
                destConfigDir = argTempValue

                os.makedirs(destConfigDir, exist_ok=True)

                destConfig = os.path.join(destConfigDir, os.path.basename(srcConfig))

                shutil.copy(srcConfig, destConfig)

                print("Copied Config file to Temp Folder Sucsessfully!")

            except:
                print("ERROR WHILE COPYING")
        else:
            try:
                srcConfig = argConfigValue
                destConfigDir = "TEMP"

                os.makedirs(destConfigDir, exist_ok=True)

                destConfig = os.path.join(destConfigDir, os.path.basename(srcConfig))
                
                shutil.copy(srcConfig, destConfig)

                print("Copied Config file to Temp Folder Sucsessfully!")

            except:
                print("ERROR WHILE COPYING")
        
    except:
        print("ERROR: Provided Config FIle Path Invalid!")
        exit()
else:
    try:
        with open('latest/config.json', 'r') as file:
            data = json.load(file)
        print("Default config.json is Accessible!")

        if argTemp:
            try:
                srcConfig = "latest/config.json"
                destConfigDir = argTempValue

                os.makedirs(destConfigDir, exist_ok=True)

                destConfig = os.path.join(destConfigDir, os.path.basename(srcConfig))

                shutil.copy(srcConfig, destConfig)

                print("Copied Config file to Temp Folder Sucsessfully!")

            except:
                print("ERROR WHILE COPYING")
        else:
            try:
                srcConfig = "latest/config.json"
                destConfigDir = "TEMP"
                
                os.makedirs(destConfigDir, exist_ok=True)

                destConfig = os.path.join(destConfigDir, os.path.basename(srcConfig))
                
                shutil.copy(srcConfig, destConfig)

                print("Copied Config file to Temp Folder Sucsessfully!")

            except:
                print("ERROR WHILE COPYING")


    except:
        print("ERROR: Couldn't access the config.json! Make sure to cd into the project directory, otherwise specify the config.json file path with --config")
        exit()

print(str(datetime.now()) + ": OK, Copied Config to temporary folder:")
print(destConfigDir)
print("Now: Using Subprocess to run hostlist-compiler to compile.")
print("This WILL take up to 1 hour, so please be patient. If this is still stuck after 1 hour, check for errors.")
print("Running...")

last_compiledtm = datetime.now()



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
    print(f"Error return code: {run.returncode}")



print("OK: Editting Lists...")

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

print("Original Comments Removed!")
print("OK, adding New Comments")

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

print("OK, Generation of blocklist complete!")


if argRelease:
    releaseDir = os.path.join("src/versions", argReleaseVer)

    os.makedirs(releaseDir, exist_ok=True)

    releaseOutput = os.path.join(releaseDir, "output.txt")

    #destConfig, destCOnfigDIr

    shutil.copy(os.path.join(destConfigDir, "output.txt"), releaseOutput)

    configOutput = os.path.join(releaseDir, os.path.basename(destConfig))

    shutil.copy(destConfig, configOutput)

    os.rename(configOutput, os.path.join(releaseDir, "config.json"))

    os.rename(releaseOutput, os.path.join(releaseDir, "blocklist.txt"))

    blocklistDir = os.path.join(releaseDir, "blocklist.txt")

    configDir = os.path.join(releaseDir, "config.json")

    delete_all_files_in_directory("latest")

    listLatest = os.path.join("latest", os.path.basename(blocklistDir))
    configLatest = os.path.join("latest", "config.json")
    
    shutil.copy(blocklistDir, listLatest)
    shutil.copy(configDir, configLatest)

    os.rename(listLatest, os.path.join("latest", "latest.txt"))
    
elif not argRelease:
    print(destConfig)

    configOrigin = destConfig
    listOrigin = os.path.join(destConfigDir, "output.txt")

    print(listOrigin)

    snapshotDir = str(os.path.join("src/snapshots", str(last_compiledtm)))
    snapshotDir = snapshotDir.replace(" ", "_")

    print(snapshotDir)
    
    os.makedirs(snapshotDir, exist_ok=True)

    snapshotConfig = os.path.join(snapshotDir, os.path.basename(configOrigin))
    snapshotList = os.path.join(snapshotDir, "output.txt")

    shutil.copy(configOrigin, snapshotDir)
    shutil.copy(listOrigin, snapshotDir)

    os.rename(snapshotList, os.path.join(snapshotDir, "blocklist.txt"))
    snapshotList = os.path.join(snapshotDir, "blocklist.txt")

    shutil.copy(snapshotList, os.path.join("latest", "blocklist.txt"))
    shutil.copy(snapshotConfig, os.path.join("latest", os.path.basename(snapshotConfig)))

    os.rename(os.path.join("latest", "blocklist.txt"), os.path.join("latest", "latest.txt"))


print("All Fine, congrats!")
print("Now: Running 'git add .' ...")

gitAdd = subprocess.run(["git", "add", "."])

print(gitAdd.stdout)
print("OK.")
print("Now: Running 'git push' ... Please make sure that you have the credentials for the repository.")
print("Please enter the URL for the repo,")
print("or press enter if it has already been set: ")

repUrl = input()
repUrl = repUrl.replace("\n", "")

if "http" in repUrl:
    gitRemote = subprocess.run("git remote set-url origin " + repUrl)
    print(gitRemote.stdout)
    gitPush = subprocess.run(["git", "push"])
    print(gitPush.stdout)
if repUrl == "":
    gitPush = subprocess.run(["git", "push"])
    print(gitPush.stdout)

print("Operations completed with succssess")

if argNotLatest:
    print("--not-latest has been set in arguments, but is deprecated. Not doing anything.")
