import play
frames = 48
step = 10
player = play.new_circle(color='red', x=-10, y=-270, radius=10,border_color='light_red')
player2 = play.new_circle(color='green', x=10, y=-270, radius=10,border_color='light_green')
object_1 = play.new_box(color='black', x=-290, y=-300, width=1500, height=5)
object_2 = play.new_box(color='black', x=-400, y=270, width=5, height=1500)
object_3 = play.new_box(color='black', x=290, y=300, width=1500, height=5)
object_4 = play.new_box(color='black', x=400, y=-270, width=5, height=1500)

finish = play.new_text(words='finish', x=0, y=270, font=None, font_size=30)
@play.when_program_starts
def start():
    player.start_physics(bounciness=0.2)
    player2.start_physics(bounciness=0.2)
    object_1.start_physics(can_move=False)
    object_2.start_physics(can_move=False)
    object_3.start_physics(can_move=False)
    object_4.start_physics(can_move=False)
@play.repeat_forever
async def game():
    player.physics.x_speed = 0
    player.physics.y_speed = 0

    if play.key_is_pressed('w'):
        player.physics.y_speed = step
    if play.key_is_pressed('s'):
        player.physics.y_speed = -1 * step
    if play.key_is_pressed('a'):
        player.physics.x_speed = -1 * step
    if play.key_is_pressed('d'):
        player.physics.x_speed = step

    if play.key_is_pressed('up'):
        player2.physics.y_speed = step
    if play.key_is_pressed('down'):
        player2.physics.y_speed = -1 * step
    if play.key_is_pressed('left'):
        player2.physics.x_speed = -1 * step
    if play.key_is_pressed('right'):
        player2.physics.x_speed = step       

    if player.is_touching(finish):
        play.new_text(words='RED WIN!', x=0, y=0, font=None, font_size=100, color='red')
        object_1.hide()
    if player2.is_touching(finish):
        play.new_text(words='GREEN WIN!', x=0, y=0, font=None, font_size=100, color='green')
        object_1.hide()

    await play.timer(seconds=1/frames)



play.start_program()