import pyray as rl
import random

def main():
    # Initialize window
    screen_width = 800
    screen_height = 600
    rl.init_window(screen_width, screen_height, "Dodge the Falling Objects!")
    rl.set_target_fps(60)

    # Player properties
    player_width = 50
    player_height = 50
    player_pos_x = screen_width // 2 - player_width // 2
    player_pos_y = screen_height - 70
    player_speed = 7
    player_color = rl.BLUE

    # Enemy properties
    enemy_width = 40
    enemy_height = 40
    enemy_speed = 5
    enemy_colors = [rl.RED, rl.GREEN, rl.PURPLE, rl.ORANGE, rl.GOLD, rl.MAROON]
    enemies = [] # List of [x, y, color]
    spawn_timer = 0

    score = 0
    game_over = False

    while not rl.window_should_close():
        # --- Update ---
        if not game_over:
            # Player movement
            if rl.is_key_down(rl.KEY_LEFT) and player_pos_x > 0:
                player_pos_x -= player_speed
            if rl.is_key_down(rl.KEY_RIGHT) and player_pos_x < screen_width - player_width:
                player_pos_x += player_speed

            # Enemy spawning
            spawn_timer += 1
            if spawn_timer >= 30: # Spawn every 30 frames
                enemy_x = random.randint(0, screen_width - enemy_width)
                enemy_color = random.choice(enemy_colors)
                enemies.append([enemy_x, -enemy_height, enemy_color])
                spawn_timer = 0

            # Enemy movement and collision
            for enemy in enemies[:]:
                enemy[1] += enemy_speed
                
                # Collision detection
                if (player_pos_x < enemy[0] + enemy_width and
                    player_pos_x + player_width > enemy[0] and
                    player_pos_y < enemy[1] + enemy_height and
                    player_pos_y + player_height > enemy[1]):
                    game_over = True

                # Remove off-screen enemies and increase score
                if enemy[1] > screen_height:
                    enemies.remove(enemy)
                    score += 1
                    # Increase difficulty
                    if score % 10 == 0:
                        enemy_speed += 0.2

        else:
            # Restart game
            if rl.is_key_pressed(rl.KEY_R):
                player_pos_x = screen_width // 2 - player_width // 2
                enemies = []
                score = 0
                enemy_speed = 5
                game_over = False

        # --- Draw ---
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)

        # Draw Player
        rl.draw_rectangle(int(player_pos_x), int(player_pos_y), player_width, player_height, player_color)

        # Draw Enemies
        for enemy in enemies:
            rl.draw_rectangle(int(enemy[0]), int(enemy[1]), enemy_width, enemy_height, enemy[2])

        # Draw Score
        rl.draw_text(f"Score: {score}", 10, 10, 20, rl.DARKGRAY)

        if game_over:
            rl.draw_text("GAME OVER!", screen_width // 2 - 100, screen_height // 2 - 20, 40, rl.RED)
            rl.draw_text("Press 'R' to Restart", screen_width // 2 - 110, screen_height // 2 + 30, 20, rl.DARKGRAY)

        rl.end_drawing()

    rl.close_window()

if __name__ == "__main__":
    main()
