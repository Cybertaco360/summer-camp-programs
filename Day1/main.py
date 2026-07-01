# This is what you would get if you buy Cookie Clicker off of Temu
# Cookie Clicker is free btw so I don't know why you would spend money for it

from pyray import *
import time

COOKIE_X = 170
COOKIE_Y = 280
COOKIE_HITBOX_RADIUS = 134

UPGRADE_FONT_SIZE = 25

upgrades = {
    "cursor": {
        "name": "Cursor",
        "cost": 10,
        "cps": 0.2,
        "owned": 0,
        "pos": (750, 50),
        "scale": 0.5,
    },
    "grandma": {
        "name": "Grandma",
        "cost": 50,
        "cps": 2,
        "owned": 0,
        "pos": (760, 340),
        "scale": 0.3,
    },
    "farm": {
        "name": "Farm",
        "cost": 500,
        "cps": 12,
        "owned": 0,
        "pos": (760, 575),
        "scale": 0.38,
    },
    "mine": {
        "name": "Mine",
        "cost": 2400,
        "cps": 60,
        "owned": 0,
        "pos": (970, 60),
        "scale": 0.3,
    },
    "factory": {
        "name": "Factory",
        "cost": 10000,
        "cps": 360,
        "owned": 0,
        "pos": (980, 330),
        "scale": 0.3,
    },
}


def mouse_over_cookie() -> bool:
    mouse = get_mouse_position()

    dx = mouse.x - COOKIE_X
    dy = mouse.y - COOKIE_Y

    return dx * dx + dy * dy <= COOKIE_HITBOX_RADIUS * COOKIE_HITBOX_RADIUS


def main() -> None:
    init_window(1200, 900, "Cookie Clicker (from Temu)")
    set_target_fps(60)

    textures = {
        "cookie": load_texture(r"assets\cookie.png"),
        "cursor": load_texture(r"assets\cursor.png"),
        "grandma": load_texture(r"assets\grandma.png"),
        "farm": load_texture(r"assets\farm.png"),
        "mine": load_texture(r"assets\mine.png"),
        "factory": load_texture(r"assets\factory.png"),
    }

    cookies = 0.0
    cookie_held = False

    last_time = time.time()

    while not window_should_close():

        # ================= TIME + CPS =================

        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        cps = 0.0
        for upgrade in upgrades.values():
            cps += upgrade["cps"] * upgrade["owned"]

        cookies += cps * dt

        # ================= CLICK COOKIE =================

        if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT) and mouse_over_cookie():
            cookie_held = True

        if cookie_held and is_mouse_button_released(MouseButton.MOUSE_BUTTON_LEFT):
            cookies += 1
            cookie_held = False

        # ================= BUY UPGRADES =================

        if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
            mouse = get_mouse_position()

            for key, upgrade in upgrades.items():

                texture = textures[key]
                scale = upgrade["scale"]
                x, y = upgrade["pos"]

                rect = Rectangle(
                    x,
                    y,
                    texture.width * scale,
                    texture.height * scale,
                )

                if check_collision_point_rec(mouse, rect):

                    if cookies >= upgrade["cost"]:
                        cookies -= upgrade["cost"]
                        upgrade["owned"] += 1

        # ================= DRAW =================

        begin_drawing()
        clear_background((112, 125, 185, 255))

        draw_text(f"Cookies: {int(cookies)}", 40, 30, 40, RAYWHITE)
        draw_text(f"CPS: {round(cps, 1)}", 55, 90, 28, RAYWHITE)

        cookie_scale = 0.9 if cookie_held else 1.0
        cookie_texture = textures["cookie"]

        draw_texture_ex(
            cookie_texture,
            (
                COOKIE_X - (cookie_texture.width * cookie_scale) / 2,
                COOKIE_Y - (cookie_texture.height * cookie_scale) / 2,
            ),
            0,
            cookie_scale,
            WHITE,
        )

        for key, upgrade in upgrades.items():
            texture = textures[key]
            scale = upgrade["scale"]
            x, y = upgrade["pos"]

            draw_texture_ex(texture, (x, y), 0, scale, WHITE)

            text_y = int(y + texture.height * scale + 5)

            draw_text(upgrade["name"], x, text_y, UPGRADE_FONT_SIZE, RAYWHITE)
            draw_text(
                f"Cost: {upgrade['cost']}",
                x,
                text_y + 30,
                UPGRADE_FONT_SIZE,
                RAYWHITE,
            )
            draw_text(
                f"Owned: {upgrade['owned']}",
                x,
                text_y + 60,
                UPGRADE_FONT_SIZE,
                RAYWHITE,
            )

        end_drawing()

    close_window()


if __name__ == "__main__":
    main()