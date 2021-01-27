import sys
import os


"""
Make sure that you are inside script folder when using the follow commands
How to use:
    python script_rcc [.qrc file name]
        "this way the script will create .py relate to the .qrc file specified"
    python script_rcc
        "this way the script will create all .py for all .qrc files"
"""


def update_rc(arguments):
    # sys.argv[0] is always our file 'script_rcc.py'
    if len(arguments) > 1:
        files = arguments[1:]
        for file in files:
            command(file)
    else:
        print(
            """
*** All .py files related to .qrc files are gonna be create/update ***
            """)
        files = os.listdir("../assets/")
        for file in files:
            command(file)


def command(file_name):
    if file_name.endswith(".qrc"):
        output_name = file_name[:-4] + "_rc.py"

        cmd = f'pyside2-rcc "../assets/{file_name}" '
        cmd += f'-o "../src/ui/{output_name}"'

        print(f"-> {cmd}")
        os.system(cmd)
    else:
        print(f"{file_name} is not valid")


if __name__ == '__main__':
    update_rc(sys.argv)
