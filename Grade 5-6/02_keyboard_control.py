import raylibpy as rl
EN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
   rl.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "I Control the Drawing!")
rl.set_target_fps(60)
    
    # Character starting position
player_x = 400  # Middle of screen
player_y = 300
player_size = 30
    
    # How fast the player moves
move_speed = 99
    
    while not rl.window_should_close():
        
        # Check which keys are being pressed
        if rl.is_key_down(rl.KEY_RIGHT):
            player_x = player_x + move_speed
        
        if rl.is_key_down(rl.KEY_LEFT):
            player_x = player_x - move_speed
            
        if rl.is_key_down(rl.KEY_DOWN):
            player_y = player_y + move_speed
            
        if rl.is_key_down(rl.KEY_UP):
            player_y = player_y - move_speed
        
        # Keep player on screen (don't let them disappear!)
        if player_x < player_size:
            player_x = player_size
        if player_x > SCREEN_WIDTH - player_size:
            player_x = SCREEN_WIDTH - player_size
        if player_y < player_size:
            player_y = player_size
        if player_y > SCREEN_HEIGHT - player_size:
            player_y = SCREEN_HEIGHT - player_size
        
    rl.begin_drawing()
    rl.clear_background(rl.LIGHTGRAY)
        
        # Draw the player as a happy circle
    rl.draw_circle(int(player_x), int(player_y), player_size, rl.ORANGE)
        
     # Draw eyes on the character
     rl.draw_circle(int(player_x - 10), int(player_y - 8), 4, rl.BLACK)
        rl.draw_circle(int(player_x + 10), int(player_y - 8), 4, rl.BLACK)
        
        # Draw a smile
        rl.draw_circle(int(player_x), int(player_y + 5), 8, rl.BLACK)
        rl.draw_circle(int(player_x), int(player_y + 3), 6, rl.ORANGE)
        
        # Instructions
        rl.draw_text("Use ARROW KEYS to move!", 200, 50, 25, rl.DARKGREEN)
        rl.draw_text(f"Character position: ({int(player_x)}, {int(player_y)})", 10, 10, 20, rl.BLACK)
        
        rl.end_drawing()
    
    rl.close_window()

if __name__ == "__main__":
    main()

"""
🌟 WHAT'S HAPPENING?
1. We check if arrow keys are pressed each frame
2. If a key is pressed, we move the character in that direction
3. We keep the character on screen with boundary checking
4. We draw a happy face so it looks like a character

🎮 TRY CHANGING:
- Make the character move faster or slower
- Use WASD keys instead of arrows (W=up, A=left, S=down, D=right)
- Change the character color or make it bigger
- Draw a different shape (square, triangle)

⌨️ OTHER KEYS TO TRY:
- rl.KEY_SPACE for spacebar
- rl.KEY_A, rl.KEY_B, etc. for letter keys
- rl.is_key_pressed() detects single presses instead of holding
"""
