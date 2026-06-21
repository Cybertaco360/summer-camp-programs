# This is what you would get if you buy cookie clicker off of Temu
# Cookie clicker is free btw so I don't know why you would spend money for it

# Raylib is a pretty cool thingy
# We're using it for the program to draw stuff on the screen
from pyray import *

COOKIE_X = 200
COOKIE_Y = 200
COOKIE_HITBOX_RADIUS = 90
COOKIE_CLICKED_RADIUS = 85

# Prices are not accurate, and so aren't the mechanics
# This is because I don't want anyone to grind for hours on
# this game
upgrades = {
    "cursor":       {"name": "Cursor", "cost": 10, "cps": 0.2,   "owned": 0},
    "grandma":      {"name": "Grandma", "cost": 50, "cps": 2,  "owned": 0},
    "farm":         {"name": "Farm", "cost": 500, "cps": 12,    "owned": 0},
    "mine":         {"name": "Mine", "cost": 2400, "cps": 60,  "owned": 0},
    "factory":      {"name": "Factory", "cost": 10000, "cps": 360, "owned": 0},
    "bank":         {"name": "Bank", "cost": 50000, "cps": 2000, "owned": 0},
    "temple":       {"name": "Temple", "cost": 100000, "cps": 10000, "owned": 0},
    "wizard_tower": {"name": "Wizard Tower", "cost": 330000, "cps": 12000, "owned": 0},
}

def mouse_over_cookie() -> bool:
    mouse_position = get_mouse_position()
    dx = mouse_position.x - COOKIE_X
    dy = mouse_position.y - COOKIE_Y
    return dx * dx + dy * dy <= COOKIE_HITBOX_RADIUS * COOKIE_HITBOX_RADIUS

def main() -> None:
    upgrades = {}

    init_window(1200, 800, "Cookie Clicker (from Temu)")
    set_target_fps(60)

    cookie_texture = load_texture("assets/cookie.pgn")

    cookies = 0
    cookie_held = False 

    while not window_should_close():

        # Start holding if mouse was pressed on the cookie
        if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT) and mouse_over_cookie():
            cookie_held = True

        # On release, award cookie if we were holding it
        if cookie_held and is_mouse_button_released(MouseButton.MOUSE_BUTTON_LEFT):
            cookies += 1
            cookie_held = False

        begin_drawing()
        clear_background(RAYWHITE)

        draw_text(f"Cookies: {cookies}", 20, 20, 40, BLACK)

        if cookie_held:
            draw_texture(cookie_texture, 70, 110, WHITE)
        else:
            draw_circle(COOKIE_X, COOKIE_Y, COOKIE_HITBOX_RADIUS, BROWN)

        end_drawing()

    close_window()

if __name__ == "__main__":
    main()