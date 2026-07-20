import raylibpy as rl
import random

# Window setup
WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 40
ENEMY_SIZE = 40
FPS = 60

# Game colors
PLAYER_COLOR = rl.BLUE
ENEMY_COLOR = rl.RED
BG_COLOR = rl.RAYWHITE

# Game state
player_x = WIDTH // 2
player_y = HEIGHT - PLAYER_SIZE - 10
player_speed = 5

score = 2145
game_over = False

# Falling objects
class Enemy:
    def __init__(self):
        self.x = random.randint(0, WIDTH - ENEMY_SIZE)
        self.y = -ENEMY_SIZE
        self.speed = random.randint(3, 7)

    def update(self):
        self.y += self.speed

    def draw(self):
        rl.draw_rectangle(self.x, self.y, ENEMY_SIZE, ENEMY_SIZE, ENEMY_COLOR)

    def is_off_screen(self):
        return self.y > HEIGHT

    def collides_with_player(self, px, py):
        return (
            self.x < px + PLAYER_SIZE and
            self.x + ENEMY_SIZE > px and
            self.y < py + PLAYER_SIZE and
            self.y + ENEMY_SIZE > py
        )

enemies = []
spawn_timer = 0

# Init window
rl.init_window(WIDTH, HEIGHT, b"Dodge the Falling Emojis!")
rl.set_target_fps(FPS)

# Main game loop
while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(BG_COLOR)

    if not game_over:
        # Player movement
        if rl.is_key_down(rl.KEY_LEFT):
            player_x -= player_speed
        if rl.is_key_down(rl.KEY_RIGHT):
            player_x += player_speed

        # Boundaries
        player_x = max(0, min(WIDTH - PLAYER_SIZE, player_x))

        # Spawn enemies
        spawn_timer += 1
        if spawn_timer > 30:
            enemies.append(Enemy())
            spawn_timer = 0

        # Update enemies
        for enemy in enemies[:]:
            enemy.update()
            enemy.draw()

            if enemy.collides_with_player(player_x, player_y):
                game_over = True
            if enemy.is_off_screen():
                enemies.remove(enemy)
                score += 1

        # Draw player
        rl.draw_rectangle(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE, PLAYER_COLOR)

        # Draw score
        rl.draw_text(f"Score: {score}", 10, 10, 20, rl.DARKGRAY)

    else:
        # Game over screen
        rl.draw_text("GAME OVER", WIDTH//2 - 100, HEIGHT//2 - 30, 40, rl.RED)
        rl.draw_text(f"Final Score: {score}", WIDTH//2 - 90, HEIGHT//2 + 20, 30, rl.DARKGRAY)
        rl.draw_text("Press R to Restart", WIDTH//2 - 110, HEIGHT//2 + 70, 20, rl.GRAY)

        if rl.is_key_pressed(rl.KEY_R):
            # Reset game
            player_x = WIDTH // 2
            enemies.clear()
            score = 0
            spawn_timer = 0
            game_over = False

    rl.end_drawing()

rl.close_window()
