﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = Character("Я")
define ma = Character(_("Маша"), color="#db1717")


##glass-smash

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg meadow
    
    play music "sound/summer01.ogg"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show madam blush

    # These display lines of dialogue.
  
    me "Маша я предлагаю тебе свою руку, сердце и прочие  органы!"
    ma "Наверняка обманешь."
    me "Нет! Ты будешь моим Цветочком, а я твоим Андрейкой!"

    menu:
      "Наебать и пойти на лево":
        $dir = 'left'
      "Честность и преданность":
        $dir = 'right'
    
    if dir == 'left': 
    ##play sound "sound/glass-smash.ogg"   
     show madam angry at left
     ma "Ну ты и мудак!"
   
        
      
    else:
      ma "Дай поцелую."
    # This ends the game.

    return
