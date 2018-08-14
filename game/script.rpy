# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
  define me = Character("Я", what_italic = True)
  define ma = Character(_("Маша"), color="#db1717")
  define ba = Character(_("Бабушка"), color="#db1717")
  define sis = Character(_("Сестра"), color="#008080")
  define ss = Character(_("Медсестра"), color="#20B2AA", what_color ="#20B2AA", what_italic = True)  
  define doc = Character(_("Доктор"), color="#4682B4", what_color ="#4682B4", what_italic = True)  
  
  define shade = Character(_("Девушка"), color="#008000", what_color ="#006400", what_italic = True)  
  
  define dog = Character(_("Некто"), color="#db1717")
  define dd1 = Character(_("Незнакомка"), color="#800080", what_color ="#800080", what_italic = True)
  define dd = Character(_("Смерть"), color="#800080", what_color ="#800080", what_italic = True)
  

##glass-smash

# The game starts here.


label start:
  #call intro
  call hospital_start from _call_hospital_start
  call hospital_next from _call_hospital_next 
  call room from _call_room 
  call tram_start from _call_tram_start
  call tram_fin from _call_tram_fin
  #call summer
  #call tram_after_summer
