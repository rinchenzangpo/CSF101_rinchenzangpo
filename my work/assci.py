#-------------------------------------------------------------------------------
# Name:        assci
# Purpose:     To create all the assci art and graphic tools for the game:
#              "you wake up..."
#
# Author:      William Bryant
#
# Created:     15/12/2013
# Copyright:   (c) William 2013
#-------------------------------------------------------------------------------

import time
import os

WOODEN_DOOR = """ ______________________________
/_____/_____/_____/_____/_____/
 ._.                    ._.
 | |                    | |
 |_|   ______   ______  |_|
 |-|  /_____/  /_____/  |-|
 | |                    | |
 |_|                    |_|
 ._.                    ._.
 | |                    | |
 |_|   ______           |_|
 |-|  /_____/           |-|
 | |              /\    | |
 |_|              \/    |_|
 ._.                    ._.
 | |                    | |
 |_|   ______   ______  |_|
 |-|  /_____/  /_____/  |-|
 | |                    | |
 |_|                    |_|

  ______   ______   ______   ______   ______   ______   ______   ______
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/"""

#Error message if user executes the wrong file.
if __name__ == '__main__':
    print("[ERROR]: Do not run this file. Run main.py - this file should not be executed!")
    time.sleep(4)
    exit()

#Clear function
def clear():
    """
    Clears the console screen using the built in commands on a operating
    system (here linux and windows)
    """
    os.system(['clear','cls', "^L"][os.name == 'nt'])

#"Wake up..." title/banner at the start
def ywu_banner(num_of_times):
    """
    Prints You wake up...(the game name) in ascii code big letters into a
    console and clears the screen using the clear function above and reprints
    the message to make the dots at the end appear to be moving.
    """
    print("__     __                         _")
    time.sleep(0.25)
    print("\ \   / /                        | |")
    time.sleep(0.25)
    print(" \ \_/ /__  _   _  __      ____ _| | _____   _   _ _ __")
    time.sleep(0.25)
    print("  \   / _ \| | | | \ \ /\ / / _` | |/ / _ \ | | | | '_ \ ")
    time.sleep(0.25)
    print("   | | (_) | |_| |  \ V  V / (_| |   <  __/ | |_| | |_) | _ _ ")
    time.sleep(0.25)
    print("   |_|\___/ \__,_|   \_/\_/ \__,_|_|\_\___|  \__,_| .__(_|_|_)")
    time.sleep(0.25)
    print("                                                  | |    ")
    time.sleep(0.25)
    print("                                                  |_| ")
    time.sleep(0.25)
    clear()

    for foo in range(num_of_times):
        print("__     __                         _")
        print("\ \   / /                        | |")
        print(" \ \_/ /__  _   _  __      ____ _| | _____   _   _ _ __")
        print("  \   / _ \| | | | \ \ /\ / / _` | |/ / _ \ | | | | '_ \ ")
        print("   | | (_) | |_| |  \ V  V / (_| |   <  __/ | |_| | |_) | _  ")
        print("   |_|\___/ \__,_|   \_/\_/ \__,_|_|\_\___|  \__,_| .__(_|_)")
        print("                                                  | |    ")
        print("                                                  |_| ")
        time.sleep(0.7)
        clear()

        print("__     __                         _")
        print("\ \   / /                        | |")
        print(" \ \_/ /__  _   _  __      ____ _| | _____   _   _ _ __")
        print("  \   / _ \| | | | \ \ /\ / / _` | |/ / _ \ | | | | '_ \ ")
        print("   | | (_) | |_| |  \ V  V / (_| |   <  __/ | |_| | |_) |  ")
        print("   |_|\___/ \__,_|   \_/\_/ \__,_|_|\_\___|  \__,_| .__(_)")
        print("                                                  | |    ")
        print("                                                  |_| ")
        time.sleep(0.7)
        clear()

        print("__     __                         _")
        print("\ \   / /                        | |")
        print(" \ \_/ /__  _   _  __      ____ _| | _____   _   _ _ __")
        print("  \   / _ \| | | | \ \ /\ / / _` | |/ / _ \ | | | | '_ \ ")
        print("   | | (_) | |_| |  \ V  V / (_| |   <  __/ | |_| | |_) |  ")
        print("   |_|\___/ \__,_|   \_/\_/ \__,_|_|\_\___|  \__,_| .___/")
        print("                                                  | |    ")
        print("                                                  |_| ")
        time.sleep(0.7)
        clear()

        print("__     __                         _")
        print("\ \   / /                        | |")
        print(" \ \_/ /__  _   _  __      ____ _| | _____   _   _ _ __")
        print("  \   / _ \| | | | \ \ /\ / / _` | |/ / _ \ | | | | '_ \ ")
        print("   | | (_) | |_| |  \ V  V / (_| |   <  __/ | |_| | |_) | _ _ ")
        print("   |_|\___/ \__,_|   \_/\_/ \__,_|_|\_\___|  \__,_| .__(_|_|_)")
        print("                                                  | |    ")
        print("                                                  |_| ")
        time.sleep(0.7)
        clear()

    START = input("Press ENTER/RETURN on your keyboard to start the game")
    time.sleep(0.7)
    clear()