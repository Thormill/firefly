define selesta = Character(_("???"), color="ffffff", window_background="gui/tram_text_box.png", name_xpos=25, name_ypos=275, text_xpos=2, text_ypos=1.0) #, show_two_window=True, show_who_window_style="say_who_window2")

label tram_start:
  scene bg tram
  with dissolve
  "Странное место"
  selesta "Очнулся? Ну ты и соня"
  return

label tram_after_summer:
  scene bg tram
  with fade
  selesta "Понравилось снова чувствовать себя молодым?"
  if sis_points > 0:
    selesta "Помнишь, как сестра тебя любила? Хоть ты и делал кислую рожу, но вам всегда было чем заняться вдвоём"
  elif sis_points < 0:
    selesta "Тебе не кажется, что если бы ты уделял сестре больше времени, то её судьба сложилась бы иначе?"

  pause(2)
  return

# return
