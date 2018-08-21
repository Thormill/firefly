# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

   
    label splashscreen:
    scene black
    play sound "sound/intro.mp3"
    with Pause(1)
    show text "{color=#FFFFFF}Когда гнев богов постигает человека, то прежде всего божество отнимает у него здравый смысл и дает превратное направление его мыслям, чтобы он не сознавал своих ошибок.     Ликург{/color}" with dissolve
    with Pause(8)
    show text "{color=#FFFFFF}{size=+20}ДЕМО 0.02 beta{/size}{/color}" with dissolve
    with Pause(2)
    hide text with dissolve
   
    stop sound 
    
    #$ renpy.movie_cutscene('webm.webm')

    return
