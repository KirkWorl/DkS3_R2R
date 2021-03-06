################################################################################
#                                                                              # 
#                       DARK SOULS 3 - RAGS TO RICHES                          # 
#                               DEVELOPED BY:                                  # 
#                              KIRK C. WORLEY                                  # 
#                                (c) 2016.                                     # 
#                        Licensed under GNU GPL 3.0                            # 
#                For more information about this license, see:                 # 
#               http://www.gnu.org/licenses/quick-guide-gplv3.html             # 
#                                                                              #
################################################################################
#                            SPECIAL THANKS:                                   # 
#                KYLE W., TYLER C., KAI D., BRANDON A.                         #
#                           AUSTIN (@NE_austin)                                #
#               for being an amazing person and always finding                 # 
#           a way to brighten my day with inspiration. Thank you.              # 
#                                  AND                                         # 
#               everyone who encouraged me to attempt this,                    # 
#       and put up with my constant questions about design choices.            # 
################################################################################
#                                                                              # 
#                   Welcome to Dark Souls 3 Rags to Riches!                    # 
#   You are currently viewing the source code to DkS 3 Rags to Riches. This    # 
#   code was made open source by GitHub and Cloud9 IDE. This program is        # 
#   written in Python 2.7.9 with the use of PyGame 1.9.1.                      # 
#   Check out the official pages below:                                        # 
#   ===================================                                        # 
#   Python:                                                                    # 
#   https://www.python.org/                                                    # 
#   ===================================                                        # 
#   PyGame 1.9.1:                                                              # 
#   http://www.pygame.org/hifi.html                                            # 
#   ===================================                                        # 
#                                                                              # 
#   This code is licensed under the General Public License 3.0. For more       # 
#   information about this license, please see the following link:             # 
#   http://www.gnu.org/licenses/quick-guide-gplv3.html                         # 
#                                                                              # 
#   Feel free to tweet serious (or not serious) questions/feedback to me       # 
#   at the following twitter handle:                                           # 
#   ==================================                                         # 
#   Twitter Handle:                                                            # 
#   @Kirk_CW                                                                   # 
#   https://twitter.com/Kirk_CW                                                # 
#   ==================================                                         #
#                                                                              # 
#   Special thanks to DreadedCone, Oroboro, and LobosJR for inspiring me.      #
#   ==================================                                         # 
#   Dreaded Cone: https://www.youtube.com/user/DreadedCone                     # 
#   ==================================                                         # 
#   Oroboro: https://www.youtube.com/user/OroboroTheNinja                      # 
#   ==================================                                         # 
#   Lobos Jr: https://www.youtube.com/user/LobosjrGaming                       #
#                                                                              # 
#   As a side note to any programmer viewing this: I have purposefully         # 
#   chosen to not take an object-oriented style of programming while making    # 
#   this. While creating objects would be beneficial here, I am leaving that   # 
#   up to those who wish to alter the code for their own purposes.             #
#                                                                              # 
#   Authors note: Even if you are big and respected, it's nice to interact     # 
#   with your fans and followers. I wish I had a little bit more help from     # 
#   some of the people I reached out to, but they have lives and things to     # 
#   take care of. A note to any of you reading this: Never feel like you're    # 
#   too important to help people who reach out to you. I appreciate it.        # 
#   Thank you.                                                                 # 
#                                                                              #
################################################################################
#                                                                              #
#                   !! EASY EDITABLE PARTS FOR PROGRAMMERS !!                  # 
#                                                                              #
################################################################################

#==============================================================================#
#               == USER SPECIFIED LOOT TABLES ==                               #
#==============================================================================#
# Set ENABLE_USER_LOOT to True if you would like to use your own loot tables.  # 
# you can edit the loot tables below.                                          # 
# The format for loot tables is as follows:                                    # 
#------------------------------------------------------------------------------#

ENABLE_USER_LOOT = False

#------------------------------------------------------------------------------#
# USR_LOOT_[CATEGORY] = {}                                                     # 
#           This is the category of loot.                                      # 
#                                                                              # 
# { <- This begins the dictionary. Do not remove it.                           # 
# } <- This ends the dictionary. Do not remove it.                             # 
#                                                                              # 
#------------------------------------------------------------------------------#
#               == HOW TO WRITE THE LOOT ENTRIES ==                            #
#------------------------------------------------------------------------------#
# Loot structure: If you know Python, this is simply a dictionary. The values  # 
# that the keys are assigned to are image files from an OBJ dictionary.        # 
# The dictionaries that exist are listed below in ** Location.                 # 
# The structure is subject to change with the implementation of weighted loot. # 
#                                                                              # 
# Name*, followed by a :, Location**, [Name of Loot item***]                   # 
# "Weapon Name":          WPN_OBJ["Loot Item Name"]                            # 
#                                                                              # 
#   * Name must be in quotes. What you type here will show up in the           # 
#       current item bar.                                                      # 
#                                                                              # 
#   ** Location is one of six dictionaries:                                    # 
#       Weapons:        WPN_OBJ[]                                              # 
#       Shields:        SHIELD_OBJ[]                                           # 
#       Pyro:           SPELL_OBJ[]                                            # 
#       Armor:          ARMOR_OBJ[]                                            # 
#       Misfortunes:    MISF_OBJ[]                                             #         
#       Consumables:    CONS_OBJ[]                                             # 
#                                                                              # 
#   *** Name of loot item must be encased in brackets.                         # 
#           Name should also be in quotes.                                     # 
#                                                                              # 
#   If the loot is NOT the last in the list, add a comma after the ]           # 
#   If you need more help, see the commented example below.                    # 
#------------------------------------------------------------------------------#            
#               == BEGIN USER LOOT ==                                          #
#------------------------------------------------------------------------------#

def enableUserLoot():
#------------------------------------------------------------------------------#
#               !! DO NOT REMOVE GLOBAL DECLARATIONS !!                        #
#------------------------------------------------------------------------------#
    global LOOT_CMN; global LOOT_RARE; global LOOT_ULTRA; global LOOT_MISF;
    global WPN_OBJ; global ARMOR_OBJ; global MISF_OBJ; global SHIELD_OBJ;
    global SPELL_OBJ; global CONS_OBJ
    
#------------------------------------------------------------------------------#
#               EDITABLE LOOT TABLES                                           #
#------------------------------------------------------------------------------#
#                                                                              # 
#   Example Loot Entry:                                                        # 
#   USR_LOOT_EXAMPLE    = {"User Weapon":   WPN_OBJ["Longsword"]}              # 
#                          "Weapon name":   Location ["Object name"],          # 
#                                                                              # 
#------COMMON------------------------------------------------------------------#
    USR_LOOT_COMMON     = { #Don't touch this.
                        #"User Weapon 1":        WPN_OBJ["Longsword"],
        
                        } #Don't touch this.
#------RARE--------------------------------------------------------------------#
    USR_LOOT_RARE       = { #Don't touch this.
        
                        } #Don't touch this.
#------ULTRA-------------------------------------------------------------------#
    USR_LOOT_ULTRA      = { #Don't touch this.
        
                        } #Don't touch this.
#------MISFORTUNE--------------------------------------------------------------#
    USR_LOOT_MISFORTUNE = { #Don't touch this.
        
                        } #Don't touch this.
    
#------------------------------------------------------------------------------#
#               !! FAILSAFE SYSTEMS - DO NOT EDIT !!                           #
#------------------------------------------------------------------------------#
    if(bool(USR_LOOT_COMMON)):
        LOOT_CMN = USR_LOOT_COMMON
    if(bool(USR_LOOT_RARE)):
        LOOT_RARE = USR_LOOT_RARE
    if(bool(USR_LOOT_ULTRA)):
        LOOT_ULTRA = USR_LOOT_ULTRA
    if(bool(USR_LOOT_MISFORTUNE)):
       LOOT_MISF = USR_LOOT_MISFORTUNE
       
#==============================================================================#
#               == END USER SPECIFIED LOOT TABLES ==                           #
#==============================================================================#
################################################################################
#                                                                              #
#                   !! END OF EASY EDITABLE PARTS FOR PROGRAMMERS !!           # 
#                                                                              #
################################################################################
#==============================================================================#
#                   BEGIN PROGRAM                                              # 
#==============================================================================#            
#                   BEGIN IMPORTS                                              # 
#==============================================================================#
# This section is for importing modules used in Rags to Riches.                #
#------------------------------------------------------------------------------#
#!/usr/bin/env python
import pygame as dks
import webbrowser as wb
import sys
import random as rnd

# Create a PRNG seed.
rnd.seed(None)

#==============================================================================#
#                   INITIALIZE ELEMENTS                                        # 
#==============================================================================#
# This section is to create most of the global variables used throughout       #
# Rags to Riches. It also contains versioning information.                     #
#------------------------------------------------------------------------------#
# Create mixer pre initialize calls to optimize playback.
dks.mixer.pre_init(44200, -16, 8, 1024)
dks.mixer.init()

# Initialize PyGame itself, aliased as 'dks' from here on out.
dks.init()
dks.font.init()

#------------------------------------------------------------------------------#
#               !! FOR VERSIONING PURPOSES, DO NOT EDIT !!                     #
#------------------------------------------------------------------------------#
# Version number string, along with internal BETA flag.
# Current Ver. No: 1.0
# VERSION LAST UPDATED: 7/7/2016
#------------------------------------------------------------------------------#
VERSION_NO  = "v1.0"
BETA        = True

# Add BETA to the caption according to internal flag.
if(BETA):
    VERSION_NO += " BETA"

# Create the caption to be displayed on the window and the "About" screen.  
CAPTION     = ("Rags to Riches " + str(VERSION_NO))

#------------------------------------------------------------------------------#
# Create the caption for the window.
dks.display.set_caption(CAPTION)

#------------------------------------------------------------------------------#
#               !! SCREEN DIMENSIONS - CAUTION !!                              #
#------------------------------------------------------------------------------#
# Width, Height of Screen in pixels. If this is changed, the background images #
# will also need to be rescaled to fit the new sizes.                          # 
# Location: <<images/system/intro1.png>>, <<images/system/intro1_1.png>>, etc. # 
# This will mean the loot-images will be off place as well. Be careful when    #
# adjusting these values. Editing them will cause a big mess.                  # 
#------------------------------------------------------------------------------#
#               !! Changing this is NOT recommended. !!                        #
#------------------------------------------------------------------------------#
WIDTH       = 950
HEIGHT      = 600
DISP        = (WIDTH, HEIGHT)

#------------------------------------------------------------------------------#
# Create the icon used in the corner of the window, as well as system tray.
ICON        =   dks.image.load("images/system/icon.png")
dks.display.set_icon(ICON)

# Create a PyGame screen object with the aforementioned dimensions.
# Initialize a Clock object.
screen      =   dks.display.set_mode(DISP)
CL          =   dks.time.Clock()

# Set the state of the program as RUNNING. When set to false the
# program stops its main loop.
RUNNING     =   True

# Set of Booleans to use as switches for animations and whether or not there
# is an active loot item being displayed.
LOOT_CLICK1 =   False;  LOOT_CLICK2 =   False;  LOOT_CLICK3 =   False
LOOT_CLICK4 =   False;  LOOT_CLICK5 =   False;  LOOT_CLICK6 =   False
LOOT_1ON    =   False;  LOOT_2ON    =   False;  LOOT_3ON    =   False
LOOT_4ON    =   False;  LOOT_5ON    =   False;  LOOT_6ON    =   False

# Set of variables which will hold the names of items that are currently
# displayed.
currentLoot1 =  None;   currentLoot2 =  None;   currentLoot3 =  None;
currentLoot4 =  None;   currentLoot5 =  None;   currentLoot6 =  None;

# Initialize variable to determine the current "Loot roll".
# Boolean to determine whether or not to draw the current roll to the screen.
currentRoll =   ""
lootRoll_ON =   False

# Boolean switch to indicate whether or not the Text Changer is being used.
# Boolean switches to indicate if the help screens are being drawn.
TXT_CHANGER =   False
MAIN_HELP   =   False;  DHELP       =   False

# Tutorial Arrow switch, when set to false it will not be drawn.
# Variable indicating which frame of animation should be played.
TUT_ARROW   =   True
ARROW_FRAME =   0

# Boolean to Mute/Unmute sounds played.
MUTE_FX     =   False

# Switch to include or exclude pyromancies in the game.
# Difficulty setting: 1 = Easy, 2 = Hard. Default: 1
INCL_PYRO   =   False
DIFF        =   1

# State of the intro screen:
# 1 = Title Screen.
# 2 = Introduction + Recommended build.
# 3 = Difficulty Selection.
# 4 = Rules + Default Equipment.
# 5 = Main Game Screen.
INTRO       =   1

# Font defined for the program. Do not edit.
# FNT = Size 30. FNT2 =  Size 23.
FONT        =   "fonts/OptimusPrinceps.ttf"
FNT         =   dks.font.Font(FONT, 30)
FNT2        =   dks.font.Font(FONT, 23)

#------------------------------------------------------------------------------#
#               -- Custom Drawn Arrow Icon --                                  #
#------------------------------------------------------------------------------#
# Custom cursor. Can edit if you wish but keep the positioning.
#        ("                        ",  Line up at these two " marks.
arrow =  ("          x             ",
          "         X.X            ",
          "        X...X           ",
          "       X..X..X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "       X.X.X.X          ",
          "  X.X  X.X.X.X  X.X     ",
          "  X.XXXX.....XXXX.X     ",
          "   X.............X      ",
          "    X...X...X...X       ",
          "        X..XX           ",
          "        X.X.X           ",
          "        X...X           ",
          "        X...X           ",
          "         X.X            ",
          "                        ",
          "                        ",
          "                        ")

#==============================================================================#
#                   FUNCTION DEFINITIONS                                       # 
#==============================================================================#
# This large section is devoted completely to functions that are utilized in   #
# Rags to Riches. Please do not edit these unless you know what you are doing. #
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#               -- Grab Resources From Path --                                 #
#------------------------------------------------------------------------------#
# This function is necessary to build a OneFile version of Rags to Riches.
# This was retrieved from:
# http://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741
# To be utilized in a future update.
def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller.
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#               -- Create A Custom Cursor --                                   #
#------------------------------------------------------------------------------#
# Creates a new cursor using PyGame's method of bitmapped cursors.
def newCursor(arrow):
    hotspot = None
    for y in range(len(arrow)):
        for x in range(len(arrow[y])):
            if arrow[y][x] in ['x', ',', 'O']:
                hotspot = x,y
                break
        if hotspot != None:
            break
    if hotspot == None:
        raise Exception("No hotspot specified for cursor 'Arrow'!")
    s2 = []
    for line in arrow:
        s2.append(line.replace('x', 'X').replace(',', '.').replace('O','o'))
    cursor, mask = dks.cursors.compile(s2, 'X', '.', 'o')
    size = len(arrow[0]), len(arrow)
    dks.mouse.set_cursor(size, hotspot, cursor, mask)
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#               -- Include Pyromancies --                                      #
#------------------------------------------------------------------------------#
# Adds Pyromancies to the loot tables. By default they are not included.
def includePyro():

    # Do not remove global declarations.
    global LOOT_CMN; global LOOT_RARE; global LOOT_ULTRA;

    # Update the COMMON loot tables.
    LOOT_CMN.update(  {"Black Fire Orb":        SPELL_OBJ["BlackFireOrb"],
                       "Boulder Heave":         SPELL_OBJ["BoulderHeave"],
                       "Bursting Fireball":     SPELL_OBJ["BurstingFireball"],
                       "Fireball":              SPELL_OBJ["Fireball"],
                       "Fire Orb":              SPELL_OBJ["FireOrb"],
                       "Fire Surge":            SPELL_OBJ["FireSurge"],
                       "Profaned Flame":        SPELL_OBJ["ProfanedFlame"],
                       "Toxic Mist":            SPELL_OBJ["ToxicMist"],
                       "Carthus Beacon":        SPELL_OBJ["CarthusBeacon"],
                       "Iron Flesh":            SPELL_OBJ["IronFlesh"]})

    # Update the RARE loot tables.
    LOOT_RARE.update( {"Great Combustion":      SPELL_OBJ["GreatCombustion"],
                       "Chaos Storm":           SPELL_OBJ["ChaosStorm"],
                       "Black Flame":           SPELL_OBJ["BlackFlame"],
                       "Fire Whip":             SPELL_OBJ["FireWhip"],
                       "Power Within":          SPELL_OBJ["PowerWithin"],
                       "Sacred Flame":          SPELL_OBJ["SacredFlame"]})
    
    # Update the ULTRA RARE loot tables.
    LOOT_ULTRA.update({"Black Serpent":         SPELL_OBJ["BlackSerpent"],
                       "Carthus Flame Arc":     SPELL_OBJ["CarthusFlameArc"],
                       "Chaos Bed Vestiges":    SPELL_OBJ["ChaosBedVestiges"],
                       "Great Chaos Fire Orb":  SPELL_OBJ["GreatChaosFireOrb"],
                       "Warmth":                SPELL_OBJ["Warmth"]})
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#               -- Set A New Text Color --                                     #
#------------------------------------------------------------------------------#
# Simple check to set a new Text color. Verifies that the passed color is a
# tuple before setting. When I am not so lazy I can foolproof this by creating
# a datatype called RGBTuple, and check if it is that.
def setTxtColor(color):

    # Do not remove global declarations.
    global TXT_COLOR

    # Check if passed color is a tuple. Flawed, but works for now.
    if(isinstance(color, tuple)):
        TXT_COLOR = color
    else:
        # Error if it is not a tuple.
        raise ValueError("Passed Color was not RGB tuple!")
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#               -- Draw A Help Screen #1 --                                    #
#------------------------------------------------------------------------------#
# This is used to draw a help screen on the main program and also controls
# whether or not the Tutorial Arrow stays on after the first time it is called.
def helpScreen():

    # Do not remove global declarations.
    global TUT_ARROW; global MAIN_HELP; global MUTE_FX

    # Rectangle hitbox of the "X" icon to close the screen.
    inCLOSE     =   dks.Rect((724, 120), (29, 31))

    # Main HELP loop.
    while(MAIN_HELP == True):

        # Update Mouse position. Clock tick for FPS and call limit.
        pos = dks.mouse.get_pos()
        CL.tick(60)

        # Draw the Pre-Made Help Screen onto the screen.
        # Update the display.
        screen.blit(MN_HELPSCREEN, (187, 112))
        dks.display.update()

        # Event Handler:
        for event in dks.event.get():

            # The close button is clicked:
            if event.type == (dks.MOUSEBUTTONUP) and (inCLOSE.collidepoint(pos) == 1):

                # Check if sounds are muted.
                if not (MUTE_FX):
                    # Play switch SFX.
                    switch_fx.play()
                # Main Help window is no longer open.
                MAIN_HELP = False

            # Entire Window is closed:
            elif event.type == dks.QUIT:
                    # Internal flag to false and quit all processes.
                    RUNNING = False
                    dks.quit()
                    sys.exit()
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#               -- Tutorial Arrow Animations --                                #
#------------------------------------------------------------------------------#
# This function is a handmade animation consisting of 14 looping frames.
# It moves the arrow back and forth in a painstakingly CPU consuming way.
# It forces the user to click on the Help screen or suffer laggy performance!
# Muahaha!
def updateArrow():

    # Do not remove global declarations.
    global ARROW_FRAME

    # Determine what frame the animation should be on, draw the arrow at
    # its correct place. Reset the count on frame 14.
    if(ARROW_FRAME == 0):
        blitAlpha(screen, G_ARROW, (789, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 1):
        blitAlpha(screen, G_ARROW, (788, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 2):
        blitAlpha(screen, G_ARROW, (787, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 3):
        blitAlpha(screen, G_ARROW, (786, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 4):
        blitAlpha(screen, G_ARROW, (785, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 5):
        blitAlpha(screen, G_ARROW, (784, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 6):
        blitAlpha(screen, G_ARROW, (783, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 7):
        blitAlpha(screen, G_ARROW, (782, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 8):
        blitAlpha(screen, G_ARROW, (783, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 9):
        blitAlpha(screen, G_ARROW, (784, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 10):
        blitAlpha(screen, G_ARROW, (785, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 11):
        blitAlpha(screen, G_ARROW, (786, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 12):
        blitAlpha(screen, G_ARROW, (787, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 13):
        blitAlpha(screen, G_ARROW, (788, 23), 255)
        dks.display.update()
    elif(ARROW_FRAME == 14):
        blitAlpha(screen, G_ARROW, (789, 23), 255)
        dks.display.update()
        ARROW_FRAME = 0

    # Increment the frame number up to 14, where it resets.
    if(ARROW_FRAME < 14):
        ARROW_FRAME += 1
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#               -- Text Color Changer: Mini Module --                          #
#------------------------------------------------------------------------------#
# Function which creates a screen allowing the user to click on a colored gem
# and change the text color to the same color of the gem.
def textChanger():

    # Do not remove global declarations.
    global TXT_COLOR; global TXT_CHANGER;
    global RED; global ORANGE; global YELLOW; global GREEN;
    global BLUE; global PURPLE; global CYAN; global WHITE

    # Set the color chosen to the default text color.
    tempColor   = TXT_COLOR

    # Rectangular hitboxes for various things:
    # 1: Inside the Finished box.
    # 2: Inside the Red gem.
    # 3: Inside the Orange gem.
    # 4: Inside the Yellow gem.
    # 5: Inside the Green gem.
    # 6: Inside the Blue gem.
    # 7: Inside the Purple gem.
    # 8: Inside the Cyan gem.
    # 9: Inside the White gem.
    inDONE      = dks.Rect((368, 0), (32, 32))
    inRED       = dks.Rect((24, 43), (60, 64))
    inORANGE    = dks.Rect((119, 43), (60, 64))
    inYELLOW    = dks.Rect((217, 43), (60, 64))
    inGREEN     = dks.Rect((313, 43), (60, 64))
    inBLUE      = dks.Rect((24, 118), (60, 64))
    inPURPLE    = dks.Rect((119, 118), (60, 64))
    inCYAN      = dks.Rect((217, 118), (60, 64))
    inWHITE     = dks.Rect((313, 118), (60, 64))

    # While the text changer is open, main loop:
    while(TXT_CHANGER):

        # Update the mouse position, clock tick for FPS and call limit.
        pos = dks.mouse.get_pos()
        CL.tick(60)

        # Draw the Text Color changer picture.
        screen.blit(CHNGR_MAIN, (0, 0))

        # Set of conditional statements: The statements light up
        # the gem the user has selected based on the temporary color.
        if(tempColor == RED):
            screen.blit(CHNGR_RED, (0, 0))
        elif(tempColor == ORANGE):
            screen.blit(CHNGR_ORANGE, (0, 0))
        elif(tempColor == YELLOW):
            screen.blit(CHNGR_YELLOW, (0, 0))
        elif(tempColor == GREEN):
            screen.blit(CHNGR_GREEN, (0, 0))
        elif(tempColor == BLUE):
            screen.blit(CHNGR_BLUE, (0, 0))
        elif(tempColor == PURPLE):
            screen.blit(CHNGR_PURPLE, (0, 0))
        elif(tempColor == CYAN):
            screen.blit(CHNGR_CYAN, (0, 0))
        elif(tempColor == WHITE):
            screen.blit(CHNGR_WHITE, (0, 0))

        # If the user mouses over the DONE box, light up the check mark.
        if(inDONE.collidepoint(pos) == 1):
            screen.blit(CHNGR_CONFIRM, (368, 0))

        # Upate the display.
        dks.display.update()

        # Event handler:
        for event in dks.event.get():

            # Set of conditional statements to set the temp color if the user clicks on a gem.
            if event.type == dks.MOUSEBUTTONUP and (inRED.collidepoint(pos) == 1):
                tempColor = RED
            elif event.type == dks.MOUSEBUTTONUP and (inORANGE.collidepoint(pos) == 1):
                tempColor = ORANGE
            elif event.type == dks.MOUSEBUTTONUP and (inYELLOW.collidepoint(pos) == 1):
                tempColor = YELLOW
            elif event.type == dks.MOUSEBUTTONUP and (inGREEN.collidepoint(pos) == 1):
                tempColor = GREEN
            elif event.type == dks.MOUSEBUTTONUP and (inBLUE.collidepoint(pos) == 1):
                tempColor = BLUE
            elif event.type == dks.MOUSEBUTTONUP and (inPURPLE.collidepoint(pos) == 1):
                tempColor = PURPLE
            elif event.type == dks.MOUSEBUTTONUP and (inCYAN.collidepoint(pos) == 1):
                tempColor = CYAN
            elif event.type == dks.MOUSEBUTTONUP and (inWHITE.collidepoint(pos) == 1):
                tempColor = WHITE

            # If the DONE button is clicked:
            elif event.type == dks.MOUSEBUTTONUP and (inDONE.collidepoint(pos) == 1):
                # Check if sounds are muted.
                if not (MUTE_FX):
                    switch2_fx.play()
                # Call the set text color function, which will update the text color to the user's choice.
                # Set the text changer as no longer in use.
                setTxtColor(tempColor)
                TXT_CHANGER = False
                
            #If the program is closed, exit:
            elif event.type == dks.QUIT:
                RUNNING = False
                dks.quit()
                sys.exit()
#------------------------------------------------------------------------------#
            
#------------------------------------------------------------------------------#
#               -- Reset Loot --                                               #
#------------------------------------------------------------------------------#
# This function resets all active loot. Thus, clearing the main screen.
def resetLoot():

    # Do not remove global defintions.
    global currentLoot1; global currentLoot2; global currentLoot3
    global currentLoot4; global currentLoot5; global currentLoot6
    
    global LOOT_1ON; global LOOT_2ON; global LOOT_3ON
    global LOOT_4ON; global LOOT_5ON; global LOOT_6ON

    global currentRoll; global lootRoll_ON

    # Reset all the loot on states.
    LOOT_1ON = False; LOOT_2ON = False;
    LOOT_3ON = False; LOOT_4ON = False;
    LOOT_5ON = False; LOOT_6ON = False;

    # Reset the current loot states.
    currentLoot1 = None; currentLoot2 = None;
    currentLoot3 = None; currentLoot4 = None;
    currentLoot5 = None; currentLoot6 = None;

    # Reset the current roll.
    currentRoll = ""; lootRoll_ON = False
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#               -- Blit An Image With Alpha Values --                          #
#------------------------------------------------------------------------------#
# !! Credit to Blake for this workaround. !!
# This function blits an image that still has alpha values onto a surface that
# does not.
# http://www.nerdparadise.com/tech/python/pygame/blitopacity/
def blitAlpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = dks.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#               -- Update Hard Mode Loot Tables --                             #
#------------------------------------------------------------------------------#
# This function updates the loot tables to remove a couple items while in      #
# hard mode. Can be modified in the future.
def updateHLoot():

    # Do not remove global definitions.
    global LOOT_CMN; global LOOT_RARE; global LOOT_ULTRA; global LOOT_MISF

    del LOOT_RARE["Black Knight Sword"]
    del LOOT_RARE["Avelyn"]
    del LOOT_CMN["Eleonora"]
    del LOOT_CMN["Firebomb +5"]
    del LOOT_CMN["Halberd"]
    del LOOT_RARE["Greatshield of Glory"]

#------------------------------------------------------------------------------#
    
#------------------------------------------------------------------------------#
#               -- Generate A Loot Roll (Easy)--                               #
#------------------------------------------------------------------------------#
# This function generates a string that displays what kind of loot the user
# receives. Ex: 1 Common, 1 Rare, 0 Ultra, 0 Misfortune.
# This function rolls for the <EASY> difficulty.
def generateRoll():

    # Do not remove global definitions.
    global currentRoll; global lootRoll_ON

    # Reset current roll.
    currentRoll = ""

    # Pick a random number from 0 to 1000 to determine the loot roll.
    cmn_rand    = rnd.randint(0, 1000)
    rare_rand   = rnd.randint(0, 1000)
    ultra_rand  = rnd.randint(0, 1000)
    misf_rand   = rnd.randint(0, 1000)

#---COMMON---------------------------------------------------------------------#
    # 10% Chance: 0 Common
    if(cmn_rand < 100):
        currentRoll += "0 Common"
        
    # 65.5% Chance: 1 Common
    elif((cmn_rand >= 100) & (cmn_rand < 755)): 
        currentRoll += "1 Common"
        
    # 24.5% Chance: 2 Common
    elif(cmn_rand >= 755): 
        currentRoll += "2 Common"
        
    #print("COMMON ROLL: ", cmn_rand)   // Debugging Purposes

    # Add a comma and a space for next word.
    currentRoll += ", "

#---RARE-----------------------------------------------------------------------#
    # 66% Chance: 0 Rare
    if(rare_rand < 660): 
        currentRoll += "0 Rare"

    # 24% Chance: 1 Rare   
    elif((rare_rand >= 660) & (rare_rand < 900)): 
        currentRoll += "1 Rare"

    # 10% Chance: 2 Rare
    elif(rare_rand >= 900):
        currentRoll += "2 Rare"

    # Add a comma and space for the next word.
    currentRoll += ", "

#---ULTRA----------------------------------------------------------------------#
    # 97.5% Chance: 0 Ultra
    if(ultra_rand < 975): 
        currentRoll += "0 Ultra"

    # 2.5% Chance: 1 Ultra
    elif(ultra_rand >= 975):
        currentRoll += "1 Ultra"

    # Add a comma and space for next word.
    currentRoll += ", "

#---MISFORTUNES----------------------------------------------------------------#
    # 95% Chance: 0 Misfortune
    if(misf_rand < 950): 
        currentRoll += "0 Misfortune"

    # 5% Chance: 1 Misfortune
    elif(misf_rand >= 950):
        currentRoll += "1 Misfortune"

#---DEFAULT--------------------------------------------------------------------#
    # If you get nothing, 70% chance for 1 common, 30% chance for 1 rare.
    if((cmn_rand < 100) & (rare_rand < 720) & (ultra_rand < 975)):
        staleRand = rnd.randint(0, 9)
        if(staleRand < 7):
            currentRoll = "1 Common, 0 Rare, 0 Ultra, 0 Misfortune"
        elif(staleRand >= 7):
            currentRoll = "0 Common, 1 Rare, 0 Ultra, 0 Misfortune" 

    # Set the roll switch to True.
    lootRoll_ON = True
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#               -- Generate A Loot Roll (Hard) --                              #
#------------------------------------------------------------------------------#
# This function generates a string that displays what kind of loot the user
# receives. Ex: 1 Common, 1 Rare, 0 Ultra, 0 Misfortune.
# This function rolls for the <HARD> difficulty.
def generateHardRoll():

    # Do not remove global declarations.
    global currentRoll; global lootRoll_ON

    # Reset the curent roll.
    currentRoll = ""

    # Pick a random number from 0 to 1000.
    cmn_rand    = rnd.randint(0, 1000)
    rare_rand   = rnd.randint(0, 1000)
    ultra_rand  = rnd.randint(0, 1000)
    misf_rand   = rnd.randint(0, 1000)

#---COMMON---------------------------------------------------------------------#
    # 15% Chance: 0 Common
    if(cmn_rand < 150): 
        currentRoll += "0 Common"

    # 70% Chance: 1 Common  
    elif((cmn_rand >= 150) & (cmn_rand < 850)): 
        currentRoll += "1 Common"

    # 15% Chance: 2 Common 
    elif(cmn_rand >= 850): 
        currentRoll += "2 Common"
        
    # Add a space and a comma for next word.
    currentRoll += ", "

#---RARE-----------------------------------------------------------------------#
    # 80% Chance: 0 Rare
    if(rare_rand < 800):
        currentRoll += "0 Rare"

    # 14% Chance: 1 Rare
    elif((rare_rand >= 800) & (rare_rand < 940)):
        currentRoll += "1 Rare"
        
    # 6% Chance: 2 Rare 
    elif(rare_rand >= 940): 
        currentRoll += "2 Rare"

    # Add a comma and space for the next word.
    currentRoll += ", "

#---ULTRA----------------------------------------------------------------------#
    # 98.3% Chance: 0 Ultra
    if(ultra_rand < 983):
        currentRoll += "0 Ultra"

    # 1.7% Chance: 1 Ultra
    elif(ultra_rand >= 983): 
        currentRoll += "1 Ultra"

    # Add a comma and space for the next word.
    currentRoll += ", "

#---MISFORTUNES----------------------------------------------------------------#
    # 91% Chance: 0 Misfortune
    if(misf_rand < 910): 
        currentRoll += "0 Misfortune"

    # 9% Chance: 1 Misfortune
    elif(misf_rand >= 910): 
        currentRoll += "1 Misfortune"

#---DEFAULT--------------------------------------------------------------------#
    # If you get nothing, 85% chance for 1 common, 15% chance for 1 rare.
    if((cmn_rand < 150) & (rare_rand < 800) & (ultra_rand < 983)):
        staleRand = rnd.randint(1, 100)
        if(staleRand < 85):
            currentRoll = "1 Common, 0 Rare, 0 Ultra, 0 Misfortune"
        elif(staleRand >= 85):
            currentRoll = "0 Common, 1 Rare, 0 Ultra, 0 Misfortune" 

    # Turn the loot switch on.
    lootRoll_ON = True
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#               -- Grab A Loot Tile --                                         #
#------------------------------------------------------------------------------#
# This function is used to actually obtain a piece of loot from the tables.
# The argument passed is a string, and is the category of loot you want to grab.
def grabLoot(category):

    # Determine which category was passed and return a pseudo random key from the dictionary.
    if(category.lower() == "common"):
        return LOOT_CMN.keys()[rnd.randint(0, len(LOOT_CMN)-1)]

    elif(category.lower() == "rare"):
        return LOOT_RARE.keys()[rnd.randint(0, len(LOOT_RARE)-1)]

    elif(category.lower() == "ultra"):
        return LOOT_ULTRA.keys()[rnd.randint(0, len(LOOT_ULTRA)-1)]

    elif(category.lower() == "misfortune"):
        return LOOT_MISF.keys()[rnd.randint(0, len(LOOT_MISF)-1)]
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#               -- Draw A Loot Coin --                                         #
#------------------------------------------------------------------------------#
# This funtion is used to draw a loot coin onto the screen. It carries out
# a simple animation and then calls the "grabLoot" function to actually draw
# loot onto the screen. Passed arguments are the Category (string) of loot, and
# the spot (1 or 2). 1 being the left spot, 2 being the right spot if applicable.
def lootCoin(category, spot):

    # Do not remove global declarations.
    global currentLoot1; global currentLoot2; global currentLoot3
    global currentLoot4; global currentLoot5; global currentLoot6
    
    global LOOT_1ON; global LOOT_2ON; global LOOT_3ON
    global LOOT_4ON; global LOOT_5ON; global LOOT_6ON

#---COMMON COIN DRAW-----------------------------------------------------------#
    if(category.lower() == "common"):

        # COMMON LOOT SPOT 1
        if(spot == 1):

            # Use the grabLoot() function to get a loot tile to be drawn.
            currentLoot1 = grabLoot("common")

            # Animate the common coin being drawn. This is a fade in.
            for i in range(255):
                screen.blit(MN_MAIN, (0, 0)) 

                # Draw other loot and the current roll if it is active.
                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))

                # Use the blit alpha function to draw the Common coin.    
                blitAlpha(screen, CMN_COIN, (10, 258), i)

                # Draw the mute icon as well.
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))

                # Update the screen, lock FPS at 300.
                dks.display.update()
                CL.tick(300)

            # One second delay before fading out the coin.
            dks.time.delay(1000)

            # Animate the common coin being drawn. This is a fade out.
            for i in range(255):
                screen.blit(MN_MAIN, (0, 0))

                # Draw other loot and the current roll on the screen if it is active.
                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))

                # Use the blitAlpha function to decrease the coin's opacity,
                # while increasing the loot's opactity.    
                blitAlpha(screen, CMN_COIN, (10, 258), 255-i)
                blitAlpha(screen, LOOT_CMN[currentLoot1], (20, 230), i)

                # Draw the mute icon as well.
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))

                # Update the display, lock the FPS at 600.
                dks.display.update()
                CL.tick(600)

            # Loot 1 is now active.
            LOOT_1ON = True

        # COMMON LOOT SPOT 2
        elif(spot == 2):

            # Use the grabLoot() function to obtain a loot tile to be drawn.
            currentLoot2 = grabLoot("common")

            # Animate the common coin being drawn. This is a fade in.
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                # Draw other loot and the current roll if it is active.
                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))

                # Use the blitAlpha function to draw the coin, increasing opacity.    
                blitAlpha(screen, CMN_COIN, (166, 258), i)

                # Draw the mute icon as well.
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))

                # Update the display and cap FPS at 300.
                dks.display.update()
                CL.tick(300)

            # One second delay between fading out the coin.
            dks.time.delay(1000)

            # Animate the common coin being drawn. This is a fade out.
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                # Draw other loot and the current roll if it is active.
                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))
                    
                # Use the blitAlpha function to decrease the coin's opacity,
                # while increasing the loot's opacity.
                blitAlpha(screen, CMN_COIN, (166, 258), 255-i)
                blitAlpha(screen, LOOT_CMN[currentLoot2], (176, 230), i)

                # Draw the mute icon as well.
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))

                # Update the display and cap FPS at 600.
                dks.display.update()
                CL.tick(600)

            # Loot 2 is now active.
            LOOT_2ON = True

#---RARE COIN DRAW-------------------------------------------------------------#
    elif(category.lower() == "rare"):

        # RARE LOOT SPOT 1
        if(spot == 1):

            # Use the grabLoot() function to obtain a loot tile to be drawn.
            currentLoot3 = grabLoot("rare")

            # Animate the rare coin being drawn. This is a fade in.
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                # Draw the other loot and current roll if active.
                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))

                # Use the blitAlpha function to draw the rare coin to the screen.
                blitAlpha(screen, RARE_COIN, (323, 258), i)

                # Draw the mute icon as well.
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))

                # Update the display and cap FPS at 300.
                dks.display.update()
                CL.tick(300)

            # One second delay before fading out the coin.
            dks.time.delay(1000)

            # Animate the rare coin on the screen. This is a fade out.
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                # Draw other loot and current roll if active.
                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))

                # Use the blitAlpha function to decrease the coin's opacity,
                # while increasing the loot tile's opacity.
                blitAlpha(screen, RARE_COIN, (323, 258), 255-i)
                blitAlpha(screen, LOOT_RARE[currentLoot3], (333, 230), i)

                # Draw the mute icon as well.
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))

                # Update the display and cap the FPS at 600.
                dks.display.update()
                CL.tick(600)

            # Loot 3 is now active.
            LOOT_3ON = True

        # RARE LOOT SPOT 2
        elif(spot == 2):

            # Use the grabLoot() function to obtain a loot tile to be drawn.
            currentLoot4 = grabLoot("rare")

            # Animate the coin being drawn on the screen. This is a fade in.
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                # Draw the other loot and current roll if active.
                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))

                # Use the blitAlpha function to draw the coin on the screen.
                blitAlpha(screen, RARE_COIN, (480, 258), i)

                # Draw the mute icon as well.
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))

                # Update the display and cap the FPS at 300.
                dks.display.update()
                CL.tick(300)

            # One second delay before fading out the coin.
            dks.time.delay(1000)

            # Animate the coin being drawn. This is a fade out.
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                # Draw other loot and current roll if active.
                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))

                # Use the blitAlpha function to decrease the coin's opacity,
                # while increasing the loot tile's opacity.
                blitAlpha(screen, RARE_COIN, (480, 258), 255-i)
                blitAlpha(screen, LOOT_RARE[currentLoot4], (490, 230), i)

                # Draw the mute icon as well.
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))

                # Update the display and cap FPS at 600.
                dks.display.update()
                CL.tick(600)

            # Loot 4 is now active.
            LOOT_4ON = True
            
#---ULTRA COIN DRAW------------------------------------------------------------#
    elif(category.lower() == "ultra"):

        # ULTRA LOOT SPOT 1
        if(spot == 1):

            # Use the grabLoot() function to grab a loot tile to be drawn.
            currentLoot5 = grabLoot("ultra")

            # Animate the ultra coin being drawn on the screen. This is a fade in.
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                # Draw the other loot and current roll if active.
                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))  
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))

                # Use the blitAlpha function to draw the coin on the screen.
                blitAlpha(screen, ULTRA_COIN, (636, 258), i)

                # Draw the mute icon as well.
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))

                # Update the display and cap FPS at 300.
                dks.display.update()
                CL.tick(300)

            # One second delay between fading out the coin.
            dks.time.delay(1000)

            # Animate the ultra coin being drawn on screen. This is a fade out.
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                # Draw other loot and current roll if active.
                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_6ON):
                    screen.blit(LOOT_MISF[currentLoot6], (805, 230))

                # Use the blitAlpha function to decrease the coin's opacity,
                # while increasing the loot tile's opacity.
                blitAlpha(screen, ULTRA_COIN, (636, 258), 255-i)
                blitAlpha(screen, LOOT_ULTRA[currentLoot5], (648, 230), i)

                # Draw the mute icon as well.
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))

                # Update the display and cap FPS at 600.
                dks.display.update()
                CL.tick(600)
                
            # Loot 5 is now active.
            LOOT_5ON = True
            
#---MISFORTUNE COIN DRAW-------------------------------------------------------#
    elif(category.lower() == "misfortune"):

        # MISFORTUNE LOOT SPOT 1
        if(spot == 1):

            # Use the grabLoot() function to get a misfortune to be drawn.
            currentLoot6 = grabLoot("misfortune")

            # Animate the misfortune coin on the screen. This is a fade in.
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                # Draw the other loot and current roll if active.
                if(lootRoll_ON):
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))  
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))

                # Use the blitAlpha function to draw the coin to the screen.
                blitAlpha(screen, MISF_COIN, (795, 258), i)

                # Draw the mute icon as well.
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))

                # Update the display and cap FPS at 300.
                dks.display.update()
                CL.tick(300)

            # One second delay before fading out the coin.
            dks.time.delay(1000)

            # Animate the misfortune coin on screen. This is a fade out.
            for i in range(255): 
                screen.blit(MN_MAIN, (0, 0))

                # Draw the other loot and the current roll if active.
                if(lootRoll_ON):    
                    screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))
                if(LOOT_1ON):
                    screen.blit(LOOT_CMN[currentLoot1], (20, 230))
                if(LOOT_2ON):
                    screen.blit(LOOT_CMN[currentLoot2], (176, 230))
                if(LOOT_3ON):
                    screen.blit(LOOT_RARE[currentLoot3], (333, 230))
                if(LOOT_4ON):
                    screen.blit(LOOT_RARE[currentLoot4], (490, 230))
                if(LOOT_5ON):
                    screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))

                # Use the blitAlpha function to decrease the coin's opacity,
                # while increasing the misfortune's opacity.
                blitAlpha(screen, MISF_COIN, (795, 258), 255-i)
                blitAlpha(screen, LOOT_MISF[currentLoot6], (805, 230), i)

                # Draw the mute icon again.
                if(MUTE_FX):
                    screen.blit(MUTE_ICON, (20, 517))
                elif(not MUTE_FX):
                    screen.blit(UNMUTE_ICON, (20, 517))

                # Update the display for each iteration, cap FPS at 600.
                dks.display.update()
                CL.tick(600)

            # Loot 6 is now active.
            LOOT_6ON = True
#------------------------------------------------------------------------------#


#==============================================================================#
#                   LOAD IMAGES AND SOUND FILES                                # 
#==============================================================================#
# This section is devoted to creating sound objects and large image objects    #
# utilized in Rags to Riches like background images, help screens, etc.        # 
#------------------------------------------------------------------------------#
#                   SOUND OBJECTS                                              # 
#------------------------------------------------------------------------------#
start_fx        =   dks.mixer.Sound("sounds/start.wav"); start_fx.set_volume(0.25)
mtheme          =   dks.mixer.Sound("sounds/MainMenu_Theme.wav"); mtheme.set_volume(0.08)
select_fx       =   dks.mixer.Sound("sounds/$draw.wav"); select_fx.set_volume(0.75)
challenge_fx    =   dks.mixer.Sound("sounds/challenge.ogg")
switch_fx       =   dks.mixer.Sound("sounds/switch1.ogg")
switch2_fx      =   dks.mixer.Sound("sounds/switch2.ogg")
accept_fx       =   dks.mixer.Sound("sounds/confirm1.ogg")
coin_fx         =   dks.mixer.Sound("sounds/coin.ogg")
reset_fx        =   dks.mixer.Sound("sounds/cancel1.ogg")

#------------------------------------------------------------------------------#
#                   IMAGE OBJECTS                                              # 
#------------------------------------------------------------------------------#
IN_1            =   dks.image.load("images/system/intro1.png").convert()
IN_1ON          =   dks.image.load("images/system/intro1_1.png").convert()
IN_1T           =   dks.image.load("images/system/intro1_2.png").convert()
IN_1G           =   dks.image.load("images/system/intro1_3.png").convert()
IN_2            =   dks.image.load("images/system/intro2.png").convert()
IN_2ON          =   dks.image.load("images/system/intro2_1.png").convert()
IN_3            =   dks.image.load("images/system/intro3.png").convert()
IN_3ON          =   dks.image.load("images/system/intro3_1.png").convert()
DIFF_E          =   dks.image.load("images/system/Difficulty_E.png").convert()
DIFF_E2         =   dks.image.load("images/system/Difficulty_E2.png").convert()
DIFF_H          =   dks.image.load("images/system/Difficulty_H.png").convert()
DIFF_H2         =   dks.image.load("images/system/Difficulty_H2.png").convert()
PYRO_ON         =   dks.image.load("images/system/PyroSwitch_ON.png").convert()
PYRO_OFF        =   dks.image.load("images/system/PyroSwitch_OFF.png").convert()
PYRO_DISABLE    =   dks.image.load("images/system/PyroSwitch_DISABLED.png").convert()
MN_MAIN         =   dks.image.load("images/system/main1.png").convert()
MN_L            =   dks.image.load("images/system/main1_L.png").convert()
MN_R            =   dks.image.load("images/system/main1_R.png").convert()
MN_I            =   dks.image.load("images/system/main1_I.png").convert()
ABOUT_SCREEN    =   dks.image.load("images/system/aboutScreen.png").convert()
MN_HELPSCREEN   =   dks.image.load("images/system/help_screen.png").convert()
DIFF_HELP       =   dks.image.load("images/system/difficulty_help.png").convert()
MUTE_ICON       =   dks.image.load("images/system/muted.png").convert()
UNMUTE_ICON     =   dks.image.load("images/system/unmuted.png").convert()
G_ARROW         =   dks.image.load("images/system/GreenArrow.png").convert_alpha()
CHNGR_MAIN      =   dks.image.load("images/system/clr/clr_changer.png").convert()
CHNGR_RED       =   dks.image.load("images/system/clr/changer_Red.png").convert()
CHNGR_ORANGE    =   dks.image.load("images/system/clr/changer_Orange.png").convert()
CHNGR_YELLOW    =   dks.image.load("images/system/clr/changer_Yellow.png").convert()
CHNGR_GREEN     =   dks.image.load("images/system/clr/changer_Green.png").convert()
CHNGR_BLUE      =   dks.image.load("images/system/clr/changer_Blue.png").convert()
CHNGR_PURPLE    =   dks.image.load("images/system/clr/changer_Purple.png").convert()
CHNGR_CYAN      =   dks.image.load("images/system/clr/changer_Cyan.png").convert()
CHNGR_WHITE     =   dks.image.load("images/system/clr/changer_White.png").convert()
CHNGR_CONFIRM   =   dks.image.load("images/system/clr/clr_confirm.png").convert()
CMN_COIN        =   dks.image.load("images/system/coin/cmn_coin.png").convert_alpha()
RARE_COIN       =   dks.image.load("images/system/coin/rare_coin.png").convert_alpha()
ULTRA_COIN      =   dks.image.load("images/system/coin/ultra_coin.png").convert_alpha()
MISF_COIN       =   dks.image.load("images/system/coin/misf_coin.png").convert_alpha()

#==============================================================================#
#                   BEGIN CREATING LOOT TILES: PART 1                          # 
#==============================================================================#
# This section is devoted to creating lists of names. These names are of all   #
# the items in Dark Souls 3. Not all of these items are used in Rags to Riches #
# but they are all created and loaded in case other programmers want to make   #
# their own loot tables.                                                       # 
#------------------------------------------------------------------------------#
#                   WEAPON NAMES                                               # 
#------------------------------------------------------------------------------#
WPN_IMG_NAMES       =   ["AnriSword", "ArstorsSpear", "AstoraGreatsword",
                         "AstoraStraightSword", "Avelyn", "BanditsKnife",
                         "BarbedSword", "BastardSword", "BattleAxe",
                         "BlackBlade", "BlackKnightGA", "BlackKnightGS",
                         "BlackKnightHalberd", "BlackKnightSword", "Bloodlust",
                         "BrigandAxe", "BrigandDaggers", "Broadsword",
                         "BrokenSword", "ButchersKnife", "Caestus",
                         "CandleDagger", "CarthusCurvedGS", "CarthusCurvedSword",
                         "CarthusShotel", "CathedralGreatsword", "ChaosBlade",
                         "Claw", "Claymore", "ClericCandle",
                         "Club", "CompositeBow", "CorvianDagger",                
                         "CrescentAxe", "CrescentShotel", "CrystalSageRapier",
                         "Dagger", "DancersTwinswords", "Darkdrift",
                         "DarkHand", "DarkSword", "DemonFist",
                         "DemonGreataxe", "DragonslayerAxe", "DragonslayerCross",
                         "DragonslayerGA", "DragonslayerSpear", "DragonTooth",
                         "DrakebloodSword", "DrangHammers", "DrangTwinspears",
                         "Eleonora", "Estoc", "ExecutionerSword",
                         "ExileGreatsword", "Falchion", "FarronGreatsword",
                         "FirelinkGreatsword", "Flamberge", "FourProngedPlow",
                         "FumeUltraGS", "GargoyleFlameHammer", "GargoyleFlameSpear",
                         "GhruCurvedSword", "GhruDagger", "GhruSpear",
                         "Glaive", "GoldenRitualSpear", "GotthardKatanas",
                         "GotthardTwinswords", "Greataxe", "GreatClub",
                         "CorvianGreatScythe", "Greatlance", "GreatMace",
                         "GreatMachete", "GreatScythe", "Greatsword",
                         "GreatswordJudgement", "GundyrHalberd", "Halberd",
                         "HandAxe", "HandmaidDagger", "Harpe",
                         "HeyselPick", "HollowslayerSword", "ImmolationTinder",
                         "IrithyllRapier", "IrithyllSword", "LargeClub",
                         "Longsword", "LoriansSword", "LothricGreatsword",
                         "LothricHolySword", "LothricSpear", "LothricStraightSword",
                         "Lucerne", "Mace", "MailBreaker",
                         "ManikinClaw", "ManSerpentAxe", "MoonlightGreatsword",
                         "MorionBlade", "MornesHammer", "MorningStar",
                         "Murakumo", "NotchedWhip", "OldKingHammer",
                         "PaintingCurvedSword", "ParryDagger", "Partizan",
                         "Pickaxe", "Pike", "PontiffCurvedSword",
                         "PontiffGreatScythe", "ProfanedGreatsword", "Rapier",
                         "RedHalberd", "ReinforcedClub", "RicardsRapier",
                         "SaintBident", "Scimitar", "SellswordTwinblades",
                         "Shortsword", "Shotel", "SmithHammer",
                         "SmoughsHammer", "SolderingIron", "Spear",
                         "SpikedMace", "SpottedWhip", "StormCurvedSword",
                         "Stormruler", "SunlightSword", "TailboneDagger",
                         "TailboneSpear", "ThrallAxe", "TwinPrinceSword",
                         "Uchigatana", "VordtsHammer", "WardenTwinblades",
                         "Warpick", "WashingPole", "Whip",
                         "WingedKnightHalberd", "WingedKnightTwinaxes", "WingedSpear",
                         "WitchLocks", "WolfCurvedGS", "WolfGreatsword",
                         "WolnirsHolyBlade", "WoodenHammer", "YhormsMachete",
                         "YorshkasSpear", "Zweihander"]

#------------------------------------------------------------------------------#
#                   ARMOR NAMES                                                # 
#------------------------------------------------------------------------------#
ARMOR_IMG_NAMES     =   ["Alva", "Alva_F", "Antiquated", "Antiquated_F",
                         "Archdeacon", "Archdeacon_F", "Assassin", "Assassin_F",
                         "BlackDress", "BlackDress_F", "BlackHand", "BlackHand_F",
                         "BlackIron", "BlackIron_F", "BlackKnight", "BlackKnight_F",
                         "BlackLeather", "BlackLeather_F", "Brass", "Brass_F",
                         "Brigand", "Brigand_F", "Catarina", "Catarina_F",
                         "Cathedral", "Cathedral_F", "Chain", "Chain_F",
                         "Clandestine", "Clandestine_F", "ClericBlue", "ClericBlue_F",
                         "Conjurator", "Conjurator_F", "Cornyx", "Cornyx_F",
                         "CourtSorcerer", "CourtSorcerer_F", "Dancers", "Dancers_F",
                         "Dark", "Dark_F", "Deacon", "Deacon_F",
                         "Deserter", "Deserter_F", "Dragonscale", "Dragonscale_F",
                         "Dragonslayer", "Dragonslayer_F", "Drakeblood", "Drakeblood_F",
                         "Drang", "Drang_F", "Eastern", "Eastern_F",
                         "EliteKnight", "EliteKnight_F", "Evangelist", "Evangelist_F",
                         "Executioner", "Executioner_F", "Exile", "Exile_F",
                         "FallenKnight", "FallenKnight_F", "Faraam", "Faraam_F",
                         "Favor", "Favor_F", "Firekeeper", "Firekeeper_F",
                         "Firelink", "Firelink_F", "FireWitch", "FireWitch_F",
                         "Gundyr", "Gundyr_F", "HardLeather", "HardLeather_F",
                         "Havel", "Havel_F", "Herald", "Herald_F",
                         "Jailer", "Jailer_F", "Karla", "Karla_F",
                         "Knight", "Knight_F", "Leather", "Leather_F",
                         "Legion", "Legion_F", "Leonhard", "Leonhard_F",
                         "Lorian", "Lorian_F", "Lothric", "Lothric_F",
                         "Maiden", "Maiden_F", "Masters", "Masters_F",
                         "Mirrah", "Mirrah_F", "MirrahChain", "MirrahChain_F",
                         "Morne", "Morne_F", "NamelessKnight", "NamelessKnight_F",
                         "Northern", "Northern_F", "OldSorcerer", "OldSorcerer_F",
                         "Outrider", "Outrider_F", "Painting", "Painting_F",
                         "PaleShade", "PaleShade_F", "PontiffKnight", "PontiffKnight_F",
                         "Prayer", "Prayer_F", "Pyromancer", "Pyromancer_F",
                         "Sellsword", "Sellsword_F", "Shadow", "Shadow_F",
                         "SilverKnight", "SilverKnight_F", "Smough", "Smough_F",
                         "Sorcerer", "Sorcerer_F", "SunArmor", "SunArmor_F",
                         "Sunless", "Sunless_F", "Sunset", "Sunset_F",
                         "Thorns", "Thorns_F", "Warden", "Warden_F",
                         "WingedKnight", "WingedKnight_F", "WolfKnight", "WolfKnight_F",
                         "Worker", "Worker_F", "Xanthous", "Xanthous_F"]

#------------------------------------------------------------------------------#
#                   SHIELD NAMES                                               # 
#------------------------------------------------------------------------------#
SHIELD_IMG_NAMES    =   ["AncientDragon", "BlackIron", "BlackKnight", "BlueWooden",
                         "Bonewheel", "Buckler", "CaduceusRound", "Carthus",
                         "CathedralKnight", "Crest", "Crimson", "CurseWard",
                         "DragonCrest", "Dragonslayer", "EasternIron", "EastWest",
                         "ElkhornRound", "GhruRotshield", "GoldenFalcon", "GoldenWingCrest",
                         "GrassCrest", "GreatshieldOfGlory", "Havels", "Hawkwoods",
                         "IronRound", "Kite", "Knight", "LargeLeather",
                         "Leather", "Llewellyn", "LothricGreatshield", "LothricKnight",
                         "Moaning", "Pierce", "Plank", "PontiffKnight",
                         "Porcine", "Round", "SacredBloom", "ShieldOfWant",
                         "SilverEagleKite", "SilverKnight", "SmallLeather", "Spiked",
                         "SpiritTreeCrest", "Stone", "StoneParma", "Sunlight",
                         "Sunset", "Target", "TwinDragon", "WarriorsRound", "WolfKnights",
                         "Wooden"]

#------------------------------------------------------------------------------#
#                   PYROMANCY NAMES                                            # 
#------------------------------------------------------------------------------#
SPELL_IMG_NAMES     =   ["AcidSurge", "BlackFireOrb", "BlackFlame", "BlackSerpent",
                         "BoulderHeave", "BurstingFireball", "CarthusBeacon", "CarthusFlameArc",
                         "ChaosBedVestiges", "ChaosStorm", "Fireball", "FireOrb",
                         "Firestorm", "FireSurge", "FireWhip", "FlashSweat",
                         "GreatChaosFireOrb", "GreatCombustion", "IronFlesh", "PoisonMist",
                         "PowerWithin", "ProfanedFlame", "ProfuseSweat", "Rapport",
                         "SacredFlame", "ToxicMist", "Warmth"]

#------------------------------------------------------------------------------#
#                   MISFORTUNE NAMES                                           # 
#------------------------------------------------------------------------------#
MISF_IMG_NAMES      =   ["Chest", "Confused", "Cursed", "Hand", "Head",
                         "Leg", "LH1", "LH2", "LH3", "Lucky",
                         "RH1", "RH2", "RH3", "Ring1", "Ring2",
                         "Ring3", "Ring4", "Spell", "Tripped"]

#------------------------------------------------------------------------------#
#                   CONSUMABLE NAMES                                           # 
#------------------------------------------------------------------------------#
CONS_IMG_NAMES      =   ["BlackFirebomb_5", "BlackFirebomb_10", "CarthusRouge_5",
                         "CarthusRouge_10", "CharcoalBundle_5", "CharcoalBundle_10",
                         "CharcoalResin_5", "CharcoalResin_10", "DuelCharm_5",
                         "Firebomb_5", "Firebomb_10", "GoldBundle_5",
                         "GoldBundle_10", "GoldResin_5", "GoldResin_10",
                         "GoldResin_20", "GreenBlossom_5", "GreenBlossom_10",
                         "HumanResin_5", "HumanResin_10", "Kukri_5",
                         "Kukri_10", "LightningUrn_5", "LightningUrn_10",
                         "PaleResin_5", "PaleResin_10", "PoisonThrowingKnife_5",
                         "PoisonThrowingKnife_10", "RopeBlackFirebomb_5", "RopeBlackFirebomb_10",
                         "RopeFirebomb_5", "RopeFirebomb_10", "RottenResin_5",
                         "RottenResin_10", "ThrowingKnife_5", "ThrowingKnife_10",
                         "Repaired"]

#------------------------------------------------------------------------------#
#                   ABOUT THE PROGRAM TEXT BLOCK                               # 
#------------------------------------------------------------------------------#
ABOUT_TXT           =   ["Thanks for trying out DkS III: Rags to Riches.",
                         "Credits:",
                         "Art and Programming: Myself.",
                         "Game Images themselves: Dark Souls 3 Wiki",
                         "(www.darksouls3.wikidot.com).",
                         "Difficulty Screenshots: Myself.",
                         "Main Theme: Dark Souls 3 Main Theme.",
                         "Other misc. images used under Creative Commons.",
                         "To report a bug, please tweet at me (@Kirk _ CW).",
                         "Or, I guess you could e-mail me. It's on the screen",
                         "somewhere, unless I forgot.",
                         "Thank you, so much."]

#==============================================================================#
#                   CREATE LOOT TILES: PART 2                                  # 
#==============================================================================#
# This section is for creating dictionaries that contain all the loot tiles.   #
# The loot tile names are taken from the IMG_NAME lists, and from there the    #
# loot tiles are then generated from the images/loot/ folders.                 #
#------------------------------------------------------------------------------#

#-------WEAPONS----------------------------------------------------------------#
WPN_OBJ	    =   {name: dks.image.load("images/loot/weapons/{}.png".format(name)).convert_alpha()
			for name in WPN_IMG_NAMES}

#-------MISFORTUNES------------------------------------------------------------#
MISF_OBJ    =   {name: dks.image.load("images/loot/misfortunes/{}.png".format(name)).convert_alpha()
			for name in MISF_IMG_NAMES}

#-------ARMOR------------------------------------------------------------------#
ARMOR_OBJ   =   {name: dks.image.load("images/loot/armor/{}.png".format(name)).convert_alpha()
			for name in ARMOR_IMG_NAMES}

#-------SHIELDS----------------------------------------------------------------#
SHIELD_OBJ  =   {name: dks.image.load("images/loot/shields/{}.png".format(name)).convert_alpha()
			for name in SHIELD_IMG_NAMES}

#-------PYROMANCIES------------------------------------------------------------#
SPELL_OBJ   =   {name: dks.image.load("images/loot/spells/{}.png".format(name)).convert_alpha()
			for name in SPELL_IMG_NAMES}

#-------CONSUMABLES------------------------------------------------------------#
CONS_OBJ    =   {name: dks.image.load("images/loot/consumables/{}.png".format(name)).convert_alpha()
			for name in CONS_IMG_NAMES}

#==============================================================================#
#                   LOOT TABLES                                                # 
#==============================================================================#
# This section is used for defining the actual loot tables that will be used.  #
# It is possible to edit this, but there is a similar module at the top that   #
# will yield the same results without messing with the default loot tables.    #
# As of v1.0 the loot is all equal chance of being selected.                   #
#------------------------------------------------------------------------------#
#      !! NOTE !!                                                              #     
# Place a space after a FULL armor set key, so dictionaries make it a new key. #
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
#                   DEFAULT COMMON LOOT TABLE                                  # 
#------------------------------------------------------------------------------#
LOOT_CMN    =   {"Longsword":                   WPN_OBJ["Longsword"],
                 "Astora Straight Sword":       WPN_OBJ["AstoraStraightSword"],
                 "Bandit's Knife":              WPN_OBJ["BanditsKnife"],
                 "Bastard Sword":               WPN_OBJ["BastardSword"],
                 "Brigand Axe":                 WPN_OBJ["BrigandAxe"],
                 "Brigand Twindaggers":         WPN_OBJ["BrigandDaggers"],
                 "Broadsword":                  WPN_OBJ["Broadsword"],
                 "Caestus":                     WPN_OBJ["Caestus"],
                 "Claws":                       WPN_OBJ["Claw"],
                 "Claymore":                    WPN_OBJ["Claymore"],
                 "Cleric's Candlestick":        WPN_OBJ["ClericCandle"],
                 "Club":                        WPN_OBJ["Club"],
                 "Crescent Moon Sword":         WPN_OBJ["CrescentShotel"],
                 "Dagger":                      WPN_OBJ["Dagger"],
                 "Executioner's Sword":         WPN_OBJ["ExecutionerSword"],
                 "Four Pronged Plow":           WPN_OBJ["FourProngedPlow"],
                 "Rotten Ghru Curved Sword":    WPN_OBJ["GhruCurvedSword"],
                 "Glaive":                      WPN_OBJ["Glaive"],
                 "Greatlance":                  WPN_OBJ["Greatlance"],
                 "Great Mace":                  WPN_OBJ["GreatMace"],
                 "Flamberge":                   WPN_OBJ["Flamberge"],
                 "Rotten Ghru Spear":           WPN_OBJ["GhruSpear"],
                 "Halberd":                     WPN_OBJ["Halberd"],
                 "Hand Axe":                    WPN_OBJ["HandAxe"],
                 "Harpe":                       WPN_OBJ["Harpe"],
                 "Irithyll Rapier":             WPN_OBJ["IrithyllRapier"],
                 "Lothric Knight Long Spear":   WPN_OBJ["LothricSpear"],
                 "Lucerne":                     WPN_OBJ["Lucerne"],
                 "Mace":                        WPN_OBJ["Mace"],
                 "Lothric Knight S. Sword":     WPN_OBJ["LothricStraightSword"],
                 "Morning Star":                WPN_OBJ["MorningStar"],
                 "Partizan":                    WPN_OBJ["Partizan"],
                 "Pickaxe":                     WPN_OBJ["Pickaxe"],
                 "Scimitar":                    WPN_OBJ["Scimitar"],
                 "Saint's Bident":              WPN_OBJ["SaintBident"],
                 "Soldering Iron":              WPN_OBJ["SolderingIron"],
                 "Spear":                       WPN_OBJ["Spear"],
                 "Thrall Axe":                  WPN_OBJ["ThrallAxe"],
                 "Tailbone Dagger":             WPN_OBJ["TailboneDagger"],
                 "Vordt's Great Hammer":        WPN_OBJ["VordtsHammer"],
                 "Warpick":                     WPN_OBJ["Warpick"],
                 "Winged Spear":                WPN_OBJ["WingedSpear"],
                 "Wolnir's Holy Sword":         WPN_OBJ["WolnirsHolyBlade"],
                 "Great Wooden Hammer":         WPN_OBJ["WoodenHammer"],
                 "Eleonora":                    WPN_OBJ["Eleonora"],
                 "Arstor's Spear":              WPN_OBJ["ArstorsSpear"],
                 "Blue Wooden Shield":          SHIELD_OBJ["BlueWooden"],
                 "Caduceus Round Shield":       SHIELD_OBJ["CaduceusRound"],
                 "Crimson Parma":               SHIELD_OBJ["Crimson"],
                 "Iron Round Shield":           SHIELD_OBJ["IronRound"],
                 "Large Leather Shield":        SHIELD_OBJ["LargeLeather"],
                 "Plank Shield":                SHIELD_OBJ["Plank"],
                 "Silver Eagle Kite Shield":    SHIELD_OBJ["SilverEagleKite"],
                 "Wooden Shield":               SHIELD_OBJ["Wooden"],
                 "Kite Shield":                 SHIELD_OBJ["Kite"],
                 "Hawkwood's Shield":           SHIELD_OBJ["Hawkwoods"],
                 "Twin Dragon Greatshield":     SHIELD_OBJ["TwinDragon"],
                 "Carthus Rouge +5":            CONS_OBJ["CarthusRouge_5"],
                 "Charcoal Pine Bundle +5":     CONS_OBJ["CharcoalBundle_5"],
                 "Charcoal Pine Bundle +10":    CONS_OBJ["CharcoalBundle_10"],
                 "Charcoal Pine Resin +5":      CONS_OBJ["CharcoalResin_5"],
                 "Firebomb +5":                 CONS_OBJ["Firebomb_5"],
                 "Firebomb +10":                CONS_OBJ["Firebomb_10"],
                 "Green Blossom +5":            CONS_OBJ["GreenBlossom_5"],
                 "Human Pine Resin +5":         CONS_OBJ["HumanResin_5"],
                 "Kukri +10":                   CONS_OBJ["Kukri_10"],
                 "Lightning Urn +5":            CONS_OBJ["LightningUrn_5"],
                 "Pale Pine Resin +5":          CONS_OBJ["PaleResin_5"],
                 "Rope Firebomb +5":            CONS_OBJ["RopeFirebomb_5"],
                 "Rope Firebomb +10":           CONS_OBJ["RopeFirebomb_10"],
                 "Rotten Pine Resin +5":        CONS_OBJ["RottenResin_5"],
                 "Throwing Knife +10":          CONS_OBJ["ThrowingKnife_10"],
                 "Antiquated Set":              ARMOR_OBJ["Antiquated_F"],
                 "Archdeacon Set":              ARMOR_OBJ["Archdeacon"],
                 "Assassin Set":                ARMOR_OBJ["Assassin"],
                 "Assassin Set ":               ARMOR_OBJ["Assassin_F"],
                 "Black Set":                   ARMOR_OBJ["BlackDress"],
                 "Black Iron Set":              ARMOR_OBJ["BlackIron"],
                 "Black Leather Set":           ARMOR_OBJ["BlackLeather"],
                 "Black Leather Set ":          ARMOR_OBJ["BlackLeather_F"],
                 "Brass Set":                   ARMOR_OBJ["Brass"],
                 "Brigand Set":                 ARMOR_OBJ["Brigand_F"],
                 "Chain Set":                   ARMOR_OBJ["Chain_F"],
                 "Clandestine Set":             ARMOR_OBJ["Clandestine"],
                 "Cleric Blue Set":             ARMOR_OBJ["ClericBlue"],
                 "Cleric Blue Set ":            ARMOR_OBJ["ClericBlue_F"],
                 "Conjurator Set":              ARMOR_OBJ["Conjurator"],
                 "Cornyx's Set":                ARMOR_OBJ["Cornyx"],
                 "Deacon Set":                  ARMOR_OBJ["Deacon_F"],
                 "Eastern Set":                 ARMOR_OBJ["Eastern"],
                 "Evangelist Set":              ARMOR_OBJ["Evangelist"],
                 "Executioner Set":             ARMOR_OBJ["Executioner"],
                 "Embraced Favor Set":          ARMOR_OBJ["Favor"],
                 "Fire Witch Set":              ARMOR_OBJ["FireWitch"],
                 "Hard Leather Set":            ARMOR_OBJ["HardLeather"],
                 "Hard Leather Set ":           ARMOR_OBJ["HardLeather_F"],
                 "Jailer Set":                  ARMOR_OBJ["Jailer"],
                 "Karla's Set":                 ARMOR_OBJ["Karla"],
                 "Knight Set":                  ARMOR_OBJ["Knight"],
                 "Mirrah Set":                  ARMOR_OBJ["Mirrah"],
                 "Old Sorcerer Set":            ARMOR_OBJ["OldSorcerer"],
                 "Outrider Set":                ARMOR_OBJ["Outrider"],
                 "Pontiff Knight Set":          ARMOR_OBJ["PontiffKnight"],
                 "Sellsword Set":               ARMOR_OBJ["Sellsword"],
                 "Shadow Set":                  ARMOR_OBJ["Shadow_F"],
                 "Sunset Set":                  ARMOR_OBJ["Sunset"],
                 "Xanthous Set":                ARMOR_OBJ["Xanthous"]
                 }

#------------------------------------------------------------------------------#
#                   DEFAULT RARE LOOT TABLE                                    # 
#------------------------------------------------------------------------------#
LOOT_RARE   =   {"Astora Greatsword":           WPN_OBJ["AstoraGreatsword"],
                 "Avelyn":                      WPN_OBJ["Avelyn"],
                 "Anri's Straight Sword":       WPN_OBJ["AnriSword"],
                 "Bloodlust":                   WPN_OBJ["Bloodlust"],
                 "Carthus Curved Sword":        WPN_OBJ["CarthusCurvedSword"],
                 "Chaos Blade":                 WPN_OBJ["ChaosBlade"],
                 "Black Knight Greatsword":     WPN_OBJ["BlackKnightGS"],
                 "Black Knight Sword":          WPN_OBJ["BlackKnightSword"],
                 "Cathedral Knight Greatsword": WPN_OBJ["CathedralGreatsword"],
                 "Composite Bow":               WPN_OBJ["CompositeBow"],
                 "Corvian Greatknife":          WPN_OBJ["CorvianDagger"],
                 "Demon's Fist":                WPN_OBJ["DemonFist"],
                 "Dragonslayer's Axe":          WPN_OBJ["DragonslayerAxe"],
                 "Dragonslayer Spear":          WPN_OBJ["DragonslayerSpear"],
                 "Drang Hammers":               WPN_OBJ["DrangHammers"],
                 "Firelink Greatsword":         WPN_OBJ["FirelinkGreatsword"],
                 "Falchion":                    WPN_OBJ["Falchion"],
                 "Gargoyle Flame Spear":        WPN_OBJ["GargoyleFlameSpear"],
                 "Onikiri and Ubadachi":        WPN_OBJ["GotthardKatanas"],
                 "Large Club":                  WPN_OBJ["LargeClub"],
                 "Great Machete":               WPN_OBJ["GreatMachete"],
                 "Great Scythe":                WPN_OBJ["GreatScythe"],
                 "Greataxe":                    WPN_OBJ["Greataxe"],
                 "Greatsword":                  WPN_OBJ["Greatsword"],
                 "Hollowslayer Greatsword":     WPN_OBJ["HollowslayerSword"],
                 "Manikin Claws":               WPN_OBJ["ManikinClaw"],
                 "Man Serpent Hatchet":         WPN_OBJ["ManSerpentAxe"],
                 "Moonlight Greatsword":        WPN_OBJ["MoonlightGreatsword"],
                 "Morion Blade":                WPN_OBJ["MorionBlade"],
                 "Murakumo":                    WPN_OBJ["Murakumo"],
                 "Painting G. Curved Sword":    WPN_OBJ["PaintingCurvedSword"],
                 "Rapier":                      WPN_OBJ["Rapier"],
                 "Ricard's Rapier":             WPN_OBJ["RicardsRapier"],
                 "Sellsword Twinblades":        WPN_OBJ["SellswordTwinblades"],
                 "Shotel":                      WPN_OBJ["Shotel"],
                 "Spiked Mace":                 WPN_OBJ["SpikedMace"],
                 "Uchigatana":                  WPN_OBJ["Uchigatana"],
                 "Winged Knight Halberd":       WPN_OBJ["WingedKnightHalberd"],
                 "Winged Knight Twinaxes":      WPN_OBJ["WingedKnightTwinaxes"],
                 "Old Wolf Curved Sword":       WPN_OBJ["WolfCurvedGS"],
                 "Zweihander":                  WPN_OBJ["Zweihander"],
                 "Crest Shield":                SHIELD_OBJ["Crest"],
                 "Grass Crest Shield":          SHIELD_OBJ["GrassCrest"],
                 "Pierce Shield":               SHIELD_OBJ["Pierce"],
                 "Shield of Want":              SHIELD_OBJ["ShieldOfWant"],
                 "Greatshield of Glory":        SHIELD_OBJ["GreatshieldOfGlory"],
                 "Sunset Shield":               SHIELD_OBJ["Sunset"],
                 "Dragon Crest Shield":         SHIELD_OBJ["DragonCrest"],
                 "Ancient Dragon Greatshield":  SHIELD_OBJ["AncientDragon"],
                 "Black Firebomb +5":           CONS_OBJ["BlackFirebomb_5"],
                 "Black Firebomb +10":          CONS_OBJ["BlackFirebomb_10"],
                 "Charcoal Pine Resin +10":     CONS_OBJ["CharcoalResin_10"],
                 "Duel Charm +5":               CONS_OBJ["DuelCharm_5"],
                 "Gold Pine Bundle +10":        CONS_OBJ["GoldBundle_10"],
                 "Gold Pine Resin +5":          CONS_OBJ["GoldResin_5"],
                 "Lightning Urn +10":           CONS_OBJ["LightningUrn_10"],
                 "Poison Throwing Knife +10":   CONS_OBJ["PoisonThrowingKnife_10"],
                 "Rope Black Firebomb +10":     CONS_OBJ["RopeBlackFirebomb_10"],
                 "Alva Set":                    ARMOR_OBJ["Alva"],
                 "Archdeacon Set":              ARMOR_OBJ["Archdeacon_F"],
                 "Black Set":                   ARMOR_OBJ["BlackDress_F"],
                 "Black Hand Set":              ARMOR_OBJ["BlackHand_F"],
                 "Black Knight Set":            ARMOR_OBJ["BlackKnight"],
                 "Catarina Set":                ARMOR_OBJ["Catarina"],
                 "Cornyx's Set":                ARMOR_OBJ["Cornyx_F"],
                 "Court Sorcerer Set":          ARMOR_OBJ["CourtSorcerer_F"],
                 "Dancer's Set":                ARMOR_OBJ["Dancers"],
                 "Dancer's Set ":               ARMOR_OBJ["Dancers_F"],
                 "Drakeblood Set":              ARMOR_OBJ["Drakeblood"],
                 "Eastern Set":                 ARMOR_OBJ["Eastern_F"],
                 "Exile Set":                   ARMOR_OBJ["Exile"],
                 "Embraced Favor Set":          ARMOR_OBJ["Favor_F"],
                 "Firelink Set":                ARMOR_OBJ["Firelink"],
                 "Gundyr's Set":                ARMOR_OBJ["Gundyr"],
                 "Herald Set":                  ARMOR_OBJ["Herald_F"],
                 "Leonhard's Set":              ARMOR_OBJ["Leonhard"],
                 "Mirrah Set":                  ARMOR_OBJ["Mirrah_F"],
                 "Nameless Knight Set":         ARMOR_OBJ["NamelessKnight_F"],
                 "Lothric Knight Set":          ARMOR_OBJ["Lothric"],
                 "Sunlight Set":                ARMOR_OBJ["SunArmor"],
                 "Sunless Set":                 ARMOR_OBJ["Sunless_F"],
                 "Wolf Knight Set":             ARMOR_OBJ["WolfKnight"]
                 }

#------------------------------------------------------------------------------#
#                   DEFAULT ULTRA RARE LOOT TABLE                              # 
#------------------------------------------------------------------------------#
LOOT_ULTRA  =   {"Black Knight Greataxe":       WPN_OBJ["BlackKnightGA"],
                 "Black Knight Glaive":         WPN_OBJ["BlackKnightHalberd"],
                 "Butchers Knife":              WPN_OBJ["ButchersKnife"],
                 "Dancer's Enchanted Swords":   WPN_OBJ["DancersTwinswords"],
                 "Dark Sword":                  WPN_OBJ["DarkSword"],
                 "Dragonslayer Swordspear":     WPN_OBJ["DragonslayerCross"],
                 "Dragonslayer Greataxe":       WPN_OBJ["DragonslayerGA"],
                 "Estoc":                       WPN_OBJ["Estoc"],
                 "Exile Greatsword":            WPN_OBJ["ExileGreatsword"],
                 "Farron Greatsword":           WPN_OBJ["FarronGreatsword"],
                 "Fume Ultra Greatsword":       WPN_OBJ["FumeUltraGS"],
                 "Gotthard Twinswords":         WPN_OBJ["GotthardTwinswords"],
                 "Gundyr's Halberd":            WPN_OBJ["GundyrHalberd"],
                 "Lothric's Holy Sword":        WPN_OBJ["LothricHolySword"],
                 "Morne's Great Hammer":        WPN_OBJ["MornesHammer"],
                 "Profaned Greatsword":         WPN_OBJ["ProfanedGreatsword"],
                 "Smough's Great Hammer":       WPN_OBJ["SmoughsHammer"],
                 "Sunlight Straight Sword":     WPN_OBJ["SunlightSword"],
                 "Twin Princes' Sword":         WPN_OBJ["TwinPrinceSword"],
                 "Washing Pole":                WPN_OBJ["WashingPole"],
                 "Witch's Locks":               WPN_OBJ["WitchLocks"],
                 "Wolf Knight Greatsword":      WPN_OBJ["WolfGreatsword"],
                 "Yhorm's Great Machete":       WPN_OBJ["YhormsMachete"],
                 "Alva Set":                    ARMOR_OBJ["Alva_F"],
                 "Catarina Set":                ARMOR_OBJ["Catarina_F"],
                 "Cathedral Knight Set":        ARMOR_OBJ["Cathedral_F"],
                 "Dark Set":                    ARMOR_OBJ["Dark_F"],
                 "Dragonscale Set":             ARMOR_OBJ["Dragonscale_F"],
                 "Dragonslayer Set":            ARMOR_OBJ["Dragonslayer_F"],
                 "Drang Set":                   ARMOR_OBJ["Drang_F"],
                 "Elite Knight Set":            ARMOR_OBJ["EliteKnight_F"],
                 "Fallen Knight Set":           ARMOR_OBJ["FallenKnight_F"],
                 "Faraam Set":                  ARMOR_OBJ["Faraam_F"],
                 "Firekeeper Set":              ARMOR_OBJ["Firekeeper_F"],
                 "Havel's Set":                 ARMOR_OBJ["Havel_F"],
                 "Undead Legion Set":           ARMOR_OBJ["Legion_F"],
                 "Lorian's Set":                ARMOR_OBJ["Lorian_F"],
                 "Painting Guardian Set":       ARMOR_OBJ["Painting_F"],
                 "Silver Knight Set":           ARMOR_OBJ["SilverKnight_F"],
                 "Thorns Set":                  ARMOR_OBJ["Thorns_F"],
                 "Winged Knight Set":           ARMOR_OBJ["WingedKnight_F"],
                 "Wolf Knight Set":             ARMOR_OBJ["WolfKnight_F"],
                 "Bonewheel Shield":            SHIELD_OBJ["Bonewheel"],
                 "Dragonslayer Greatshield":    SHIELD_OBJ["Dragonslayer"],
                 "Golden Wing Crest Shield":    SHIELD_OBJ["GoldenWingCrest"],
                 "Havel's Shield":              SHIELD_OBJ["Havels"],
                 "Llewellyn Shield":            SHIELD_OBJ["Llewellyn"],
                 "Silver Knight Shield":        SHIELD_OBJ["SilverKnight"],
                 "Target Shield":               SHIELD_OBJ["Target"],
                 "Gold Pine Resin +20":         CONS_OBJ["GoldResin_20"],
                 "Repaired a Ring!":            CONS_OBJ["Repaired"]
                 }

#------------------------------------------------------------------------------#
#                   DEFAULT MISFORTUNE LOOT TABLE                              # 
#------------------------------------------------------------------------------#
LOOT_MISF   =   {"Chest Broken":                MISF_OBJ["Chest"],
                 "Chest Broken":                MISF_OBJ["Chest"],
                 "Confused!":                   MISF_OBJ["Confused"],
                 "Cursed!":                     MISF_OBJ["Cursed"],
                 "Guantlets Broken":            MISF_OBJ["Hand"],
                 "Helm Broken":                 MISF_OBJ["Head"],
                 "Leggings Broken":             MISF_OBJ["Leg"],
                 "Left Hand 1 Broken":          MISF_OBJ["LH1"],
                 "Left Hand 1 Broken ":         MISF_OBJ["LH1"],
                 "Left Hand 2 Broken":          MISF_OBJ["LH2"],
                 "Left Hand 3 Broken":          MISF_OBJ["LH3"],
                 "Lucked Out!":                 MISF_OBJ["Lucky"],
                 "Right Hand 1 Broken":         MISF_OBJ["RH1"],
                 "Right Hand 1 Broken ":        MISF_OBJ["RH1"],
                 "Right Hand 2 Broken":         MISF_OBJ["RH2"],
                 "Right Hand 3 Broken":         MISF_OBJ["RH3"],
                 "Ring 1 Broken":               MISF_OBJ["Ring1"],
                 "Ring 2 Broken":               MISF_OBJ["Ring2"],
                 "Ring 3 Broken":               MISF_OBJ["Ring3"],
                 "Ring 4 Broken":               MISF_OBJ["Ring4"],
                 "Spell Forgotten":             MISF_OBJ["Spell"],
                 "Tripped!":                    MISF_OBJ["Tripped"]
                 }

#------------------------------------------------------------------------------#
#                   USER LOOT CHECK                                            # 
#------------------------------------------------------------------------------#
# If the switch to enable user loot is True, replace the current dictionaries
# with the users dictionaries. If the dictionary is blank, it will not be
# changed from the default dictionary.
if(ENABLE_USER_LOOT):
    enableUserLoot()

#==============================================================================#
#                   COLORS DEFINITIONS                                         # 
#==============================================================================#
# This section is simply for color definitions. The reason it is not in the    #
# editable parts for programmers is because the color changer module is        #
# pre-defined. The only thing a programmer can do here is to change the        #
# default text color to something of their choice, and not click on the        #
# text changer icon.                                                           #
#------------------------------------------------------------------------------#
# Color Defs.   =       (R,   G,   B)
RED 	        =       (237, 28,  36)
ORANGE          =       (255, 69,  0)
YELLOW 	        =       (241, 255, 0)
GREEN 	        =       (78,  255, 87)
BLUE 	        =       (25,  25,  112)
PURPLE 	        =       (240, 0,   255)
CYAN            =       (0,   255, 255)
WHITE           =       (255, 255, 255)
BLACK           =       (0,   0,   0)

#------------------------------------------------------------------------------#
#       Authors note:                                                          # 
# I flipped a coin to determine what the default color would be. I wanted      #     
# to leave it Purple, but Purple is somewhat difficult to see. Cyan is my      # 
# next favorite color, but everyone insisted I keep it a plain white           # 
# and let the user decide.                                                     # 
#------------------------------------------------------------------------------#

# Initial, Default text color.
TXT_COLOR = WHITE

#==============================================================================#
#                   INTRO INDEX 1: TITLE SCREEN                                # 
#==============================================================================#
# This section is all about the user being on the title screen.                #
#------------------------------------------------------------------------------#

# Use the newCursor function to create the bitmapped cursor.
newCursor(arrow)

# Play the Title Screen music on infinite loop. 3 second fade in time.
mtheme.play(loops=-1, fade_ms=3000)

# Rectangular coordinates for hitboxes:
# 1: Inside the BEGIN button.
# 2: Inside the twitter link.
# 3: Inside the github link.
#                        (X,    Y),  (Width, Height)
inBEGIN     =   dks.Rect((304, 312), (340, 123))
inTWITTER   =   dks.Rect((545, 478), (394, 33))
inGITHUB    =   dks.Rect((281, 549), (658, 34))

# Screen set and updated. Changed from a fade in due to unresponsiveness.
# It's less pleasing to the eye but generally a lot more efficient.
screen.blit(IN_1, (0,0))
dks.display.update()

# Clear all queued events to prevent double registering.
dks.event.clear()

# Main Loop for while user is at the title screen. 
while(INTRO == 1):

    # Update the mouse position.
    # Cap FPS via clock.tick @60; Then update the display.
    pos = dks.mouse.get_pos()
    CL.tick(60)
    dks.display.update()

    # If the mouse is in the BEGIN button, draw a highlighted version of it.
    if(inBEGIN.collidepoint(pos) == 1):
        screen.blit(IN_1ON, (0, 0))
        dks.display.update()

    # If the mouse is in the Twitter link, draw a highlighted version of it.
    elif(inTWITTER.collidepoint(pos) == 1):
        screen.blit(IN_1T, (0, 0))
        dks.display.update()

    # If the mouse is inside the Github link, draw a highlighted version of it.
    elif(inGITHUB.collidepoint(pos) == 1):
        screen.blit(IN_1G, (0, 0))
        dks.display.update()

    # If nothing, re-draw the title screen.
    else:
        screen.blit(IN_1, (0, 0))

    # Event Handler:
    for event in dks.event.get():

        # Mouse is pressed inside the BEGIN button:
        if event.type == dks.MOUSEBUTTONUP and (inBEGIN.collidepoint(pos) == 1):
            # Check if sounds are muted: Future update to mute @ Title Screen.
            if not(MUTE_FX):
                start_fx.play()
                
            # Fadeout the title theme, and set the Intro state to 2.
            mtheme.fadeout(2000)
            INTRO = 2

        # Mouse is pressed inisde the Twitter link:
        elif event.type == dks.MOUSEBUTTONUP and (inTWITTER.collidepoint(pos) == 1):
            # Check if sounds are muted: Future update.
            if not(MUTE_FX):
                select_fx.play()
                
            # Use the WebBrowser module to open a new page with twitter link. Uses the user's default browser.
            wb.open("https://twitter.com/Kirk_CW", 0, True)

        # Mouse is pressed inside the Github link:
        elif event.type == dks.MOUSEBUTTONUP and (inGITHUB.collidepoint(pos) == 1):
            # Check if sounds are muted: Future update.
            if not(MUTE_FX):
                select_fx.play()
                
            # Use the WebBrowser module to open a new pge with Github repo. Uses the user's defauly browser.
            wb.open("https://github.com/KirkWorl/DarkSouls3_R2R", 0, True)

        ##---------------------------------------------------------------------#
        ##    !! DEV. SHORTCUT TO MAIN SCREEN !!                               #
        ##---------------------------------------------------------------------#
        ##elif event.type == dks.KEYDOWN:
        ##
        ##    if event.key == dks.K_SPACE:
        ##        mtheme.fadeout(1000)
        ##        INTRO = 5
        ##---------------------------------------------------------------------#
            
        # If the program is closed, exit all and reset states:
        elif event.type == dks.QUIT:
            RUNNING = False
            dks.quit()
            sys.exit()
            
#==============================================================================#
#                   INTRO INDEX 2: WELCOME SCREEN                              # 
#==============================================================================#
# This screen is all about introducing the user to Rags to Riches and what     # 
# kind of build they will need for it.                                         #
#------------------------------------------------------------------------------#

# Initial Check before creating elements.
if(INTRO == 2):

    # Rectangular coordinates, hitbox for the NEXT button.
    inNEXT      =   dks.Rect((614, 477), (336, 123))

    # Fade the screen out from the Title Screen.
    for i in range(255): 
        screen.fill((0, 0, 0))
        IN_1.set_alpha(255-i)
        screen.blit(IN_1, (0, 0))
        dks.display.update()
        CL.tick(120)

    # 250 mSecond delay before fading back in.
    dks.time.delay(250)

    # Fade in the Welcome Screen.
    for i in range(255): 
        screen.fill((0, 0, 0))
        IN_2.set_alpha(i)
        screen.blit(IN_2, (0, 0))
        dks.display.update()
        CL.tick(120)

# Clear events to ensure no event was registered twice while fading in.
dks.event.clear()

# Intro Index 2: Main Loop.
while(INTRO == 2):

    # Update the mouse position. Lock FPS at 60.
    # Update the display every iteration.
    pos = dks.mouse.get_pos()
    CL.tick(60)
    dks.display.update()

    # If the mouse is inside the NEXT button, draw a highlighted version of it.
    if(inNEXT.collidepoint(pos) == 1):
        screen.blit(IN_2ON, (0, 0))
        dks.display.update()

    # If nothing, draw the Welcome Screen normally.
    else:
        screen.blit(IN_2, (0, 0))
    
    # Event Handler:
    for event in dks.event.get():

        # NEXT button is clicked:
        if event.type == dks.MOUSEBUTTONUP and (inNEXT.collidepoint(pos) == 1):
            # Check for muted sounds; future update.
            if not(MUTE_FX):
                select_fx.play()
                
            # Set the Intro index to 3.
            INTRO = 3

        # If the program is closed, exit and reset states:
        elif event.type == dks.QUIT:
            RUNNING = False
            dks.quit()
            sys.exit()
            
#==============================================================================#
#                   INTRO INDEX 3: DIFFICULTY SELECT                           # 
#==============================================================================#
# This section allows the user to pick what difficulty they would like to play #
# Rags to Riches on. It also allows them to select whether or not they want    #
# to include pyromancies in the loot tables via a switch at the bottom of the  #
# screen.                                                                      #
#------------------------------------------------------------------------------#

# Initial Check before creating elements.
if(INTRO == 3):
    
    # Rectangular hitbox coordinates for several things:
    # 1: Continue button to go to next screen.
    # 2: Easy Mode box.
    # 3: Hard Mode box.
    # 4: Pyromancy Switch.
    # 5: Difficulty Help Box.
    # 6: Difficulty Help Box Close.
    inCONTINUE      =   dks.Rect((659, 516), (255, 73))
    inEASY          =   dks.Rect((39, 55),  (415, 444))
    inHARD          =   dks.Rect((496, 55), (415, 444))
    inPYRO          =   dks.Rect((465, 525), (150, 65))
    inDHELP     =   dks.Rect((455, 7),   (41, 37))
    inDCLOSE    =   dks.Rect((724, 120), (29, 31))
    
    # Fade out Welcome Screen each iteration.
    for i in range(255): 
        screen.fill((0, 0, 0))
        IN_2.set_alpha(255-i)
        screen.blit(IN_2, (0, 0))
        dks.display.update()
        CL.tick(120)

    # 250 mSecond delay before fading in Difficulty Select screen.
    dks.time.delay(250)

    # Fade in the Difficulty Select screen from black as well as the Pyromancy switch.
    for i in range(255): 
        screen.fill((0, 0, 0))
        PYRO_OFF.set_alpha(i)
        DIFF_E.set_alpha(i)
        screen.blit(DIFF_E, (0, 0))
        screen.blit(PYRO_OFF, (465, 525))
        dks.display.update()
        CL.tick(120)

# Clear events in case of double registering and other clicks.
dks.event.clear()

# Difficulty Screen Main loop:
while(INTRO == 3):

    # Update the mouse position and cap FPS at 60.
    # Update the display every iteration.
    pos = dks.mouse.get_pos()
    CL.tick(60)
    dks.display.update()

    # If the chosen difficulty is Easy, draw the Easy Selected screen.
    if(DIFF == 1):
        screen.blit(DIFF_E, (0, 0))

    # If the chosen difficulty is Hard, draw the Hard Selected screen.
    elif(DIFF == 2):
        # Automatically exclude pyromancies, and draw a "Disabled" version of the Pyromancy switch.
        INCL_PYRO = False
        screen.blit(DIFF_H, (0, 0))
        screen.blit(PYRO_DISABLE, (465, 525))

    # If the mouse is inside the CONTINUE button and the help screen is not active:
    if((inCONTINUE.collidepoint(pos) == 1) and (not DHELP)):

        # Based on the difficulty draw the correct lit up continue screen.
        # EASY:
        if(DIFF == 1):

            # If Pyromancies are included as well, draw the switch on and the lit continue.            
            if(INCL_PYRO):
                screen.blit(DIFF_E2, (0, 0))
                screen.blit(PYRO_ON, (465, 525))
                dks.display.update()

            # If Pyromancies are excluded, draw the switch off and the lit continue.
            if not (INCL_PYRO):
                screen.blit(DIFF_E2, (0, 0))
                screen.blit(PYRO_OFF, (465, 525))
                dks.display.update()

        # HARD:
        elif(DIFF == 2):
            # Draw the disabled Pyromancy switch and the lit continue.
            screen.blit(DIFF_H2, (0, 0))
            screen.blit(PYRO_DISABLE, (465, 525))
            dks.display.update()

    # After the previous screens have been drawn, check the Pyromancy switch.
    # If Pyro Switch is set to On and the difficulty is Easy, draw the switch in the on position.
    # Mostly for failsafe purposes.
    if((INCL_PYRO) and (DIFF == 1)):
        screen.blit(PYRO_ON, (465, 525))
    elif ((not (INCL_PYRO)) and (DIFF == 1)):
        screen.blit(PYRO_OFF, (465, 525))

    # If the difficulty help screen flag is true, continue to draw it.
    if(DHELP):
        screen.blit(DIFF_HELP, (187, 112))
        dks.display.update()
            
    # Event Handler:
    for event in dks.event.get():
        
        # CONTINUE Button was pressed and help screen is not active:
        if event.type == dks.MOUSEBUTTONUP and (inCONTINUE.collidepoint(pos) == 1) and (not DHELP):
            # Check for muted sounds; future update.
            if not(MUTE_FX):
                select_fx.play()
            # Set the Intro index to 4.
            INTRO = 4

        # EASY Box was pressed and help screen is not active:
        elif event.type == dks.MOUSEBUTTONUP and (inEASY.collidepoint(pos) == 1) and (not DHELP):

            # If the Difficulty is on Hard:
            if(DIFF == 2):
                # Check for muted sounds; future update.
                if not(MUTE_FX):
                    switch2_fx.play()
                    
                # Set the difficulty back to Easy.
                DIFF = 1

        # HARD Box was pressed and help screen is not active:
        elif event.type == dks.MOUSEBUTTONUP and (inHARD.collidepoint(pos) == 1) and (not DHELP):

            # If the Difficulty is on Easy:
            if(DIFF == 1):
                # Check for muted sounds; future update.
                if not(MUTE_FX):
                    switch2_fx.play()

                # Set the difficulty back to Hard.
                DIFF = 2

        # Pyromancy Switch clicked and help screen is not active:
        elif event.type == dks.MOUSEBUTTONUP and (inPYRO.collidepoint(pos) == 1) and (not DHELP):

            # Initial check if Difficulty is on Easy:
            if(DIFF == 1):
                # Check for muted sounds; future update.
                if not(MUTE_FX):
                    switch_fx.play()

                # Basic switch: If include is true, set to false and vice versa.
                if(INCL_PYRO):
                    INCL_PYRO = False
                else:
                    INCL_PYRO = True

        # HELP Button pressed and help screen wasn't already set to active:
        elif event.type == dks.MOUSEBUTTONUP and (inDHELP.collidepoint(pos) == 1) and (not DHELP):
            # Check for muted sounds; future update.
            if not(MUTE_FX):
                switch2_fx.play()
            # Set the Help screen switch to True.
            DHELP = True

        # HELP Close Button pressed and help screen HAS to be active:
        elif event.type == dks.MOUSEBUTTONUP and (inDCLOSE.collidepoint(pos) == 1) and (DHELP):
            #Check for muted sounds; future update.
            if not(MUTE_FX):
                switch_fx.play()
            # Set the Help screen switch to False.
            DHELP = False
                
        # If the program is closed, exit and reset states:
        elif event.type == dks.QUIT:
            RUNNING = False
            dks.quit()
            sys.exit()    

# Check the user's choice: If the user has chosen to include Pyromancies
# and the difficulty is set to easy, call the function to add them to the loot tables.
if((INCL_PYRO == True) and (DIFF == 1)):
    includePyro()
    
#==============================================================================#
#                   INTRO INDEX 4: RULES OF RAGS TO RICHES                     # 
#==============================================================================#
# This section is for the Rules screen of Rags to Riches. This screen is       #
# all about what default equipment the user receives and the general rules.    #
#------------------------------------------------------------------------------#

# Initial check before creating elements:
if(INTRO == 4):

    # Rectangular coordinate hitboxes:
    # START button.
    inSTART     =   dks.Rect((129, 531), (166, 60))
    
    # Fade out the Difficulty screen:
    for i in range(255): 
        screen.fill((0, 0, 0))

        # If the difficulty is Easy, fade out the Easy Selected screen.
        if(DIFF == 1):

            # Based on the user's input, fade out the correct screen:
            # If pyromancies are included, fade out Easy with Pyromancy switch on.
            if(INCL_PYRO):
                PYRO_ON.set_alpha(255-i)
                DIFF_E2.set_alpha(255-i)
                screen.blit(DIFF_E2, (0, 0))
                screen.blit(PYRO_ON, (465, 525))

            # If pyromancies are excluded, fade out Easy with Pyromancy switch off.
            elif(INCL_PYRO == False):
                PYRO_OFF.set_alpha(255-i)
                DIFF_E2.set_alpha(255-i)
                screen.blit(DIFF_E2, (0, 0))
                screen.blit(PYRO_OFF, (465, 525))

        # If the difficulty is Hard, fade out the Hard Selected screen.
        elif(DIFF == 2):
            PYRO_DISABLE.set_alpha(255-i)
            DIFF_H2.set_alpha(255-i)
            screen.blit(DIFF_H2, (0, 0))
            screen.blit(PYRO_DISABLE, (465, 525))

        # Update the display each iteration of the loop, limit frames at 120.
        dks.display.update()
        CL.tick(120)

    # 250 mSecond delay before fading in the Rules screen.
    dks.time.delay(250)

    # Fade in the rules screen.
    for i in range(255): 
        screen.fill((0, 0, 0))
        IN_3.set_alpha(i)
        screen.blit(IN_3, (0, 0))
        dks.display.update()
        CL.tick(120)

# Clear event queue so nothing was double registered.
dks.event.clear()

# Rules Screen Main loop:
while(INTRO == 4):

    # Update mouse positions, set FPS cap at 60.
    # Update the display each iteration.
    pos = dks.mouse.get_pos()
    CL.tick(60)
    dks.display.update()

    # If the mouse is inside the Start button, draw a highlighted version of it.
    if(inSTART.collidepoint(pos) == 1):
        screen.blit(IN_3ON, (0, 0))
        dks.display.update()

    # If nothing, draw the regular Rules screen.
    else:
        screen.blit(IN_3, (0, 0))
    
    # Event Handler:
    for event in dks.event.get():

        # START button clicked:
        if event.type == dks.MOUSEBUTTONUP and (inSTART.collidepoint(pos) == 1):
            # Check for muted sounds; future update.
            if not(MUTE_FX):
                select_fx.play()
            # Set the Intro index to 5: This is the Main screen.
            INTRO = 5
                
        # If the program is closed, exit and reset states:
        elif event.type == dks.QUIT:
            RUNNING = False
            dks.quit()
            sys.exit()

# If difficulty is Hard, update the loot tables via function.
if(DIFF == 2):
    updateHLoot()
    
#==============================================================================#
#                   INTRO INDEX 5: MAIN PROGRAM SCREEN / RAGS TO RICHES        # 
#==============================================================================#
# This section is dedicated to the main program. This is the actual Rags to    #
# Riches minigame, and the Intro Index does not progress further from here.    #
#------------------------------------------------------------------------------#

# Initial Check before creating elements:
if(INTRO == 5):
    
    # Rectangular coordinates, hitboxes for several thing:
    # 1:  Green Loot Gem
    # 2:  Reset Loot Button
    # 3:  Common Loot 1
    # 4:  Common Loot 2
    # 5:  Rare Loot 1
    # 6:  Rare Loot 2
    # 7:  Ultra Loot
    # 8:  Misfortune
    # 9:  Text Changer Module
    # 10: About Module
    # 11: Mute Button
    # 12: Help Box
    inGEM       =   dks.Rect((109, 73),  (108, 108))
    inRESET     =   dks.Rect((358, 497), (248, 60))
    inCOMM1     =   dks.Rect((20,  230), (125, 216))
    inCOMM2     =   dks.Rect((176, 230), (125, 216))
    inRARE1     =   dks.Rect((333, 230), (125, 216))
    inRARE2     =   dks.Rect((490, 230), (125, 216))
    inULTRA     =   dks.Rect((648, 230), (125, 216))
    inMISF      =   dks.Rect((802, 230), (125, 216))
    inTXTC      =   dks.Rect((890, 22),  (42, 41))
    inABT       =   dks.Rect((890, 68),  (40, 40))
    inMUTE      =   dks.Rect((20, 517),  (29, 25))
    inHELP      =   dks.Rect((845, 21),  (41, 41))
    
    # Fade out the Rules Screen.
    for i in range(255): 
        screen.fill((0, 0, 0))
        IN_3.set_alpha(255-i)
        screen.blit(IN_3, (0, 0))
        dks.display.update()
        CL.tick(120)

    # 250 mSecond delay between fade in.
    dks.time.delay(250)

    # Fade in the Main Screen.
    for i in range(255): 
        screen.fill((0, 0, 0))
        MN_MAIN.set_alpha(i)
        UNMUTE_ICON.set_alpha(i)
        screen.blit(MN_MAIN, (0, 0))
        screen.blit(UNMUTE_ICON, (20, 517)) 
        dks.display.update()
        CL.tick(120)

# Clear event queue for double registering events.
dks.event.clear()

# Main Program Loop for Rags to Riches:
while((RUNNING) and (INTRO == 5)):

    # Reset these switches: After each iteration, no loot tile is being clicked on.
    LOOT_CLICK1 = False;    LOOT_CLICK2 = False
    LOOT_CLICK3 = False;    LOOT_CLICK4 = False
    LOOT_CLICK5 = False;    LOOT_CLICK6 = False
    
    # Update the mouse position, cap FPS framerate.
    pos = dks.mouse.get_pos()
    CL.tick(60)

    # If the mouse is over the Loot Gem, and the Text Changer is not active,
    # draw a highlighted version of the Gem.
    if((inGEM.collidepoint(pos) == 1) & (TXT_CHANGER == False)):
        screen.blit(MN_L, (0, 0))

    # If the mouse is over the Reset Button, and the Text Changer is not active,
    # draw a highlighted version of the Reset button.
    elif((inRESET.collidepoint(pos) == 1) & (TXT_CHANGER == False)):
        screen.blit(MN_R, (0, 0))

    # If nothing else, draw the regular Rags to Riches screen.
    else:
        screen.blit(MN_MAIN, (0, 0))

    # If the mouse is over Common Loot Spot 1 and there is a loot tile active,
    # draw the items name (Loot dictionary key) in the "Current Item" spot.
    if((inCOMM1.collidepoint(pos) == 1) & (LOOT_1ON == True)):
        screen.blit(MN_I, (0, 0))
        screen.blit(FNT2.render(currentLoot1, 1, (TXT_COLOR)), (612, 178))

    # If the mouse is over Common Loot Spot 2 and there is a loot tile active,
    # draw the items name (Loot dictionary key) in the "Current Item" spot.
    if((inCOMM2.collidepoint(pos) == 1) & (LOOT_2ON == True)):
        screen.blit(MN_I, (0, 0))
        screen.blit(FNT2.render(currentLoot2, 1, (TXT_COLOR)), (612, 178))

    # If the mouse is over Rare Loot Spot 1 and there is a loot tile active,
    # draw the items name (Loot dictionary key) in the "Current Item" spot.
    if((inRARE1.collidepoint(pos) == 1) & (LOOT_3ON == True)):
        screen.blit(MN_I, (0, 0))
        screen.blit(FNT2.render(currentLoot3, 1, (TXT_COLOR)), (612, 178))

    # If the mouse is over Rare Loot Spot 2 and there is a loot tile active,
    # draw the items name (Loot dictionary key) in the "Current Item" spot.
    if((inRARE2.collidepoint(pos) == 1) & (LOOT_4ON == True)):
        screen.blit(MN_I, (0, 0))
        screen.blit(FNT2.render(currentLoot4, 1, (TXT_COLOR)), (612, 178))

    # If the mouse is over Ultra Loot Spot 1 and there is a loot tile active,
    # draw the items name (Loot dictionary key) in the "Current Item" spot.
    if((inULTRA.collidepoint(pos) == 1) & (LOOT_5ON == True)):
        screen.blit(MN_I, (0, 0))
        screen.blit(FNT2.render(currentLoot5, 1, (TXT_COLOR)), (612, 178))

    # If the mouse is over Misfortune Spot 1 and there is a loot tile active,
    # draw the misfortune name (Loot dictionary key) in the "Current Item" spot.
    if((inMISF.collidepoint(pos) == 1) & (LOOT_6ON == True)):
        screen.blit(MN_I, (0, 0))
        screen.blit(FNT2.render(currentLoot6, 1, (TXT_COLOR)), (612, 178)) 

    # If there is a generated roll (#Common, #Rare, #Ultra, etc.)
    # continue to draw it on screen.
    if(lootRoll_ON):
        screen.blit(FNT.render(currentRoll, 1, (TXT_COLOR)), (225, 113))

    # If there is a loot tile active at Common spot 1, draw it each iteration.
    if(LOOT_1ON):
        screen.blit(LOOT_CMN[currentLoot1], (20, 230))

    # If there is a loot tile active at Common spot 2, draw it each iteration.
    if(LOOT_2ON):
        screen.blit(LOOT_CMN[currentLoot2], (176, 230))

    # If there is a loot tile active at Rare spot 1, draw it each iteration.
    if(LOOT_3ON):
        screen.blit(LOOT_RARE[currentLoot3], (333, 230))

    # If there is a loot tile active at Rare spot 2, draw it each iteration.
    if(LOOT_4ON):
        screen.blit(LOOT_RARE[currentLoot4], (490, 230))

    # If there is a loot tile active at Ultra spot 1, draw it each iteration.
    if(LOOT_5ON):
        screen.blit(LOOT_ULTRA[currentLoot5], (648, 230))

    # If there is a loot tile active at Misfortune spot 1, draw it each iteration.
    if(LOOT_6ON):
        screen.blit(LOOT_MISF[currentLoot6], (805, 230))

    # Draw the correct mute/unmuted icon each iteration.
    if(MUTE_FX):
        screen.blit(MUTE_ICON, (20, 517))
    elif(not MUTE_FX):
        screen.blit(UNMUTE_ICON, (20, 517))

    # When the mouse is inside of the About square, draw a background and
    # dynamic text blocks. These text blocks are in program credits of a sort.
    # As well as the current version at the bottom. This can only be displayed
    # if the Tutorial Arrow switch is off.
    if((inABT.collidepoint(pos) == 1) and (not TUT_ARROW)):
        screen.blit(ABOUT_SCREEN, (187, 112))
        screen.blit(FNT2.render(ABOUT_TXT[0], 1, (TXT_COLOR)), (230, 140))
        screen.blit(FNT2.render(ABOUT_TXT[1], 1, (TXT_COLOR)), (200, 180))
        screen.blit(FNT2.render(ABOUT_TXT[2], 1, (TXT_COLOR)), (200, 204))
        screen.blit(FNT2.render(ABOUT_TXT[3], 1, (TXT_COLOR)), (200, 228))
        screen.blit(FNT2.render(ABOUT_TXT[4], 1, (TXT_COLOR)), (200, 252))
        screen.blit(FNT2.render(ABOUT_TXT[5], 1, (TXT_COLOR)), (200, 276))
        screen.blit(FNT2.render(ABOUT_TXT[6], 1, (TXT_COLOR)), (200, 300))
        screen.blit(FNT2.render(ABOUT_TXT[7], 1, (TXT_COLOR)), (200, 324))
        screen.blit(FNT2.render(ABOUT_TXT[8], 1, (TXT_COLOR)), (200, 348))
        screen.blit(FNT2.render(ABOUT_TXT[9], 1, (TXT_COLOR)), (200, 372))
        screen.blit(FNT2.render(ABOUT_TXT[10], 1, (TXT_COLOR)), (200, 396))
        screen.blit(FNT2.render(ABOUT_TXT[11], 1, (TXT_COLOR)), (200, 420))
        screen.blit(FNT.render(CAPTION, 1, (TXT_COLOR)), (324, 445))
        dks.display.update()

    # If the tutorial arrow switch is active: Update the arrow's frames
    # and lock FPS at 20.
    if(TUT_ARROW):
        CL.tick(20)
        updateArrow()

    # Finally, update the display before moving to the event handler.
    dks.display.update()
    
    # Event Handler:
    for event in dks.event.get():

        # If the program is closed, exit and reset states:
        if event.type == dks.QUIT:
            RUNNING = False
            dks.quit()
            sys.exit()

        # Reset Button is clicked, Text changer is not active:
        elif event.type == (dks.MOUSEBUTTONUP) and (inRESET.collidepoint(pos) == 1) and (TXT_CHANGER == False):
            # Check for muted sounds: Complete.
            if not (MUTE_FX):
                switch2_fx.play()

            # Call the reset loot function and remove all other MOUSE UP events queued.
            resetLoot()
            dks.event.clear(dks.MOUSEBUTTONUP)

        # Green Loot Gem is clicked, Text changer is not active:
        elif event.type == (dks.MOUSEBUTTONUP) and (inGEM.collidepoint(pos) == 1) and (TXT_CHANGER == False):
            # Check for muted sounds: Complete.
            if not (MUTE_FX):
                coin_fx.play()

            # Based on difficulty, call the correct Roll Generation method:
            if(DIFF == 1):
                generateRoll()
            elif(DIFF == 2):
                generateHardRoll()
            # Clear all other MOUSE UP events queued to prevent double registering.
            dks.event.clear(dks.MOUSEBUTTONUP)

        # Common Loot Spot 1 is clicked, Failsafe measure for double clicks must be false, and Text Changer must not be active:
        elif event.type == (dks.MOUSEBUTTONUP) and (inCOMM1.collidepoint(pos) == 1) and (LOOT_CLICK1 == False) and (TXT_CHANGER == False):

            # Turn on a temporary switch so the loot tile can't be clicked rapidly. The animations must finish.
            LOOT_CLICK1 = True

            # Call the lootCoin() function to draw a common loot coin at spot one, as well as
            # grab the loot to be displayed. Then, clear all MOUSE UP events to prevent double registering.
            lootCoin("common", 1)
            dks.event.clear(dks.MOUSEBUTTONUP)

        # Common Loot Spot 2 is clicked, Failsafe measures for double clicks must be false, and Text Changer must not be active:
        elif event.type == (dks.MOUSEBUTTONUP) and (inCOMM2.collidepoint(pos) == 1) and (LOOT_CLICK2 == False) and (TXT_CHANGER == False):

            # Turn on a temporary switch so the loot tile can't be clicked rapidly. The animations must finish.
            LOOT_CLICK2 = True

            # Call the lootCoin() function to draw a common loot coin at spot two, as well as
            # grab the loot to be displayed. Then, clear all MOUSE UP events to prevent double registering.
            lootCoin("common", 2)
            dks.event.clear(dks.MOUSEBUTTONUP)

        # Rare Loot Spot 1 is clicked, Failsafe measures for double clicks must be false, and Text Changer must not be active:
        elif event.type == (dks.MOUSEBUTTONUP) and (inRARE1.collidepoint(pos) == 1) and (LOOT_CLICK3 == False) and (TXT_CHANGER == False):

            # Turn on a temporary switch so the loot tiles can't be clicked rapidly. The animations must finish.
            LOOT_CLICK3 = True

            # Call the lootCoin() function to draw a rare loot coin at spot one, as well as
            # grab the loot to be displayed. Then, clear all MOUSE UP events to prevent double registering.
            lootCoin("rare", 1)
            dks.event.clear(dks.MOUSEBUTTONUP)

        # Rare Loot Spot 2 is clicked, Failsafe measures for double clicks must be false, and Text Changer must not be active:
        elif event.type == (dks.MOUSEBUTTONUP) and (inRARE2.collidepoint(pos) == 1) and (LOOT_CLICK4 == False) and (TXT_CHANGER == False):

            # Turn on a temporary switch so the loot tiles can't be clicked rapidly. This allows the animations to finish.
            LOOT_CLICK4 = True

            # Call the lootCoin() function to draw a rare loot coin at spot two, as well as
            # grab the loot to be displayed. Then, clear all MOUSE UP events to prevent double registering.
            lootCoin("rare", 2)
            dks.event.clear(dks.MOUSEBUTTONUP)

        # Ultra Rare Loot Spot 1 is clicked, Failsafe measures for double clicks must be false, and Text Changer must not be active:
        elif event.type == (dks.MOUSEBUTTONUP) and (inULTRA.collidepoint(pos) == 1) and (LOOT_CLICK5 == False) and (TXT_CHANGER == False):

            # Turn on a temporary switch so the loot tiles can't be clicked rapidly. This allows animations to finish.
            LOOT_CLICK5 = True

            # Call the lootCoin() function to draw an ultra rare loot coin at spot one, as well as
            # grab the loot to be displayed. Then, clear all MOUSE UP events to prevent double registering.
            lootCoin("ultra", 1)
            dks.event.clear(dks.MOUSEBUTTONUP)
            
        # Misfortune Spot 1 is clickd, Failsafe measures for double clicks must be false, and Text Changer must not be active:
        elif event.type == (dks.MOUSEBUTTONUP) and (inMISF.collidepoint(pos) == 1) and (LOOT_CLICK6 == False) and (TXT_CHANGER == False):

            # Turn on a temporary switch so the loot tiles can't be clicked rapidly. This allows animations to finish.
            LOOT_CLICK6 = True

            # Call the lootCoin() function to draw a misfortune coin at spot one, as well as
            # grab the loot to be displayed. Then, clear all MOUSE UP events to prevent double registering.
            lootCoin("misfortune", 1)
            dks.event.clear(dks.MOUSEBUTTONUP)

        # Mute Button is clicked, Text Changer must not be active:
        elif event.type == (dks.MOUSEBUTTONUP) and (inMUTE.collidepoint(pos) == 1) and (TXT_CHANGER == False):

            # If sounds were previously muted, play a sound to indicate they are no longer muted, and set switch to false.
            if(MUTE_FX):
                switch2_fx.play()
                MUTE_FX = False

            # All other cases: Set switch to true, and clear all other MOUSE UP events to prevent double registering.
            else:
                MUTE_FX = True
            dks.event.clear(dks.MOUSEBUTTONUP)

        # Rags to Riches Help button is clicked, Text Changer must not be active, and the Help Screen must not already be displayed.
        elif event.type == (dks.MOUSEBUTTONUP) and (inHELP.collidepoint(pos) == 1) and (TXT_CHANGER == False) and (MAIN_HELP == False):
            # Check for muted sounds: Complete.
            if not (MUTE_FX):
                switch_fx.play()

            # If the Tutorial Arrow is still on, turn it off after they click the help button the first time.
            if(TUT_ARROW):
                TUT_ARROW = False

            # Set the Help screen switch to True and run the Help Screen function, this will keep the user on the help screen until
            # the close box is clicked. Clear all other MOUSE UP events to prevent double registering.
            MAIN_HELP = True
            helpScreen()
            dks.event.clear(dks.MOUSEBUTTONUP)

        # Text Changer Module is clicked, the module can not already be active:
        elif event.type == (dks.MOUSEBUTTONUP) and (inTXTC.collidepoint(pos) == 1) and (TXT_CHANGER == False):
            # Check for muted sounds: Complete.
            if not (MUTE_FX):
                switch_fx.play()

            # Text Changer is now active, run the Text Changer function. This will keep the user on the text changer until
            # the done check mark is clicked. Clear all other MOUSE UP events to prevent double registering.
            TXT_CHANGER = True
            textChanger()
            dks.event.clear(dks.MOUSEBUTTONUP)
    
#==============================================================================#
#                   END OF MAIN PROGRAM LOOP                                   # 
#==============================================================================#
#------------------------------------------------------------------------------#

#==============================================================================#
#                   END OF PROGRAM                                             # 
#==============================================================================#
