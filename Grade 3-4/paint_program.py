import raylibpy as rl

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    rl.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Magic Paint Brush!")
    rl.set_target_fps(60)

    painted_circles = []  # List to store all the circles we paint
    current_color = rl.BLUE  # Start with blue color
    circle_size = 20        # Start with size 20

    while not rl.window_should_close():
        # Change color with keys: R, G, B
        if rl.is_key_pressed(rl.KEY_R):
            current_color = rl.RED
        elif rl.is_key_pressed(rl.KEY_G):
            current_color = rl.GREEN
        elif rl.is_key_pressed(rl.KEY_B):
            current_color = rl.BLUE

        # Change circle size with UP and DOWN arrows
        if rl.is_key_down(rl.KEY_UP):
            circle_size += 1
        elif rl.is_key_down(rl.KEY_DOWN) and circle_size > 1:
            circle_size -= 1

        # Clear all painted circles when spacebar is pressed
        if rl.is_key_pressed(rl.KEY_SPACE):
            painted_circles.clear()

        # Add a new circle when the left mouse button is clicked
        if rl.is_mouse_button_pressed(rl.MOUSE_BUTTON_LEFT):
            mouse_x = rl.get_mouse_x()
            mouse_y = rl.get_mouse_y()
            painted_circles.append((mouse_x, mouse_y, circle_size, current_color))

        rl.begin_drawing()
        rl.clear_background(rl.WHITE)

        # Draw all the circles we have painted
        for circle in painted_circles:
            x, y, size, color = circle
            rl.draw_circle(x, y, size, color)

        # Instructions for the kids
        rl.draw_text("Click to paint circles!", 10, 10, 20, rl.BLACK)
        rl.draw_text("Press R, G, B to change colors", 10, 40, 20, rl.BLACK)
        rl.draw_text("Use UP/DOWN arrows to change size", 10, 70, 20, rl.BLACK)
        rl.draw_text("Press SPACE to clear the screen", 10, 100, 20, rl.BLACK)
        rl.draw_text(f"Current size: {circle_size}", 10, 130, 20, rl.BLACK)

        rl.end_drawing()

    rl.close_window()

if __name__ == "__main__":
    main()
