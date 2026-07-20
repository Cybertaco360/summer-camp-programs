import raylibpy as rl
from dataclasses import dataclass
import time

# --- Customizable Configs ---
GARDEN_WIDTH = 10
GARDEN_HEIGHT = 6
TILE_SIZE = 64

SCREEN_WIDTH = GARDEN_WIDTH * TILE_SIZE + 200
SCREEN_HEIGHT = GARDEN_HEIGHT * TILE_SIZE + 100  # Space for UI

PLANT_TYPES = {
    "Carrot": {
        "growth_time": 5.0,
        "cost": 2,
        "harvest_income": 5,
        "color": rl.ORANGE,       # Fully grown
        "young_color": rl.BEIGE   # Before grown
    },
    "Tomato": {
        "growth_time": 10.0,
        "cost": 5,
        "harvest_income": 10,
        "color": rl.RED,          # Fully grown
        "young_color": rl.LIME    # Before grown
    },
    "Yay": {
        "growth_time": 1.0,
        "cost": 1,
        "harvest_income": 15,
        "color": rl.LIME,          # Fully grown
        "young_color": rl.LIME    # Before grown
    }
}


KEY_TO_SEED = {}
SEED_KEY_HINTS = []

for index, seed in enumerate(PLANT_TYPES.keys()):
    key_code = rl.KEY_ONE + index  # KEY_ONE == 49 ('1'), KEY_TWO == 50 ('2'), etc.
    KEY_TO_SEED[key_code] = seed
    SEED_KEY_HINTS.append(f"{index + 1}-{seed}")


STARTING_MONEY = 20


# --- Classes ---
@dataclass
class Plant:
    type_name: str
    planted_time: float

    def is_grown(self):
        return time.time() - self.planted_time >= PLANT_TYPES[self.type_name]["growth_time"]


@dataclass
class Plot:
    x: int
    y: int
    plant: Plant = None

    def plant_seed(self, plant_type):
        self.plant = Plant(plant_type, time.time())

    def harvest(self):
        if self.plant and self.plant.is_grown():
            income = PLANT_TYPES[self.plant.type_name]["harvest_income"]
            self.plant = None
            return income
        return 0

    def draw(self):
        rect = rl.Rectangle(self.x, self.y, TILE_SIZE, TILE_SIZE)
        rl.draw_rectangle_rec(rect, rl.DARKGREEN)
        rl.draw_rectangle_lines_ex(rect, 2, rl.BLACK)

        if self.plant:
            plant_info = PLANT_TYPES[self.plant.type_name]
            if self.plant.is_grown():
                rl.draw_circle(self.x + TILE_SIZE // 2, self.y + TILE_SIZE // 2, 10, plant_info["color"])
            else:
                rl.draw_circle(self.x + TILE_SIZE // 2, self.y + TILE_SIZE // 2, 6, plant_info["young_color"])


# --- Game State ---
plots = []
money = STARTING_MONEY
selected_seed = "Carrot"

def init_game():
    global plots
    for row in range(GARDEN_HEIGHT):
        for col in range(GARDEN_WIDTH):
            plots.append(Plot(col * TILE_SIZE, row * TILE_SIZE))


def get_plot_at_mouse():
    mouse_pos = rl.get_mouse_position()
    for plot in plots:
        rect = rl.Rectangle(plot.x, plot.y, TILE_SIZE, TILE_SIZE)
        if rl.check_collision_point_rec(mouse_pos, rect):
            return plot
    return None



# --- Main Game ---
def main():
    global money, selected_seed

    rl.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, b"Grow-a-Garden Tycoon")
    rl.set_target_fps(60)
    init_game()

    while not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)

        # Input
        if rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            plot = get_plot_at_mouse()
            if plot:
                if not plot.plant and money >= PLANT_TYPES[selected_seed]["cost"]:
                    plot.plant_seed(selected_seed)
                    money -= PLANT_TYPES[selected_seed]["cost"]
                elif plot.plant and plot.plant.is_grown():
                    money += plot.harvest()

        for key_code, seed in KEY_TO_SEED.items():
            if rl.is_key_pressed(key_code):
                selected_seed = seed
                break


        # Draw Plots
        for plot in plots:
            plot.draw()

        # UI
        rl.draw_text(f"Money: ${money}", 10, SCREEN_HEIGHT - 90, 20, rl.BLACK)
        keybinds_text = ", ".join(SEED_KEY_HINTS)
        rl.draw_text(f"Selected: {selected_seed} ({keybinds_text})", 10, SCREEN_HEIGHT - 60, 20, rl.DARKGRAY)

        rl.end_drawing()

    rl.close_window()


if __name__ == "__main__":
    main()
