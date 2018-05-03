# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
  define me = Character("Я")
  define ma = Character(_("Маша"), color="#db1717")
  define ba = Character(_("Бабушка"), color="#db1717")
  define sis = Character(_("Сестра"), color="#008080")
  # $ g = Character("Celeste", color = "#ffffff", window_background="GUI/girl-text-box.png", what_xpos=0, what_ypos=5, who_xpos=2, who_ypos=0.0, show_two_window=True, show_who_window_style="say_who_window2")
  # $ mc = Character("Me", color = "#ffffff", show_two_window=True, show_who_window_style="say_who_window1")


##glass-smash

# The game starts here.


label start:
  call tram_start
  call summer
  call tram_after_summer
