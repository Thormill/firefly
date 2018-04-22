# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = Character("Me")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg meadow

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show madam blush

    # These display lines of dialogue.

    me "You've created a new Ren'Py game."

    me "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
      "Go left":
        $dir = 'left'
      "Go right":
        $dir = 'right'
    
    if dir == 'left':
      show madam angry at left
      me "on my left"
    else:
      me "on my right"
    # This ends the game.

    return
