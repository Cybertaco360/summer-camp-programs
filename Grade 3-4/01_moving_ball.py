import raylibpy as rl

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    rl.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Bouncy Balls are fun!")
    rl.set_target_fps(60)
    
    # Ball starting position and size
    ball_x = 400  # Middle of screen
    ball_y = 300
    ball_2x = 300  # Middle of screen
    ball_2y = 200  # Middle of screen  
    ball_size = 40
    ball_size = 40
    
    # Ball speed (how fast it moves)
    ball_speed_x = 10               
      # Moving right
    ball_speed_y = 10

    ball_speed_2x = 10              
      # Moving right
    ball_speed_2y = 10
    
    # Ball colorb
    ball_color = rl.RED
    
    while not rl.window_should_close():
        
        # Move the ball
        ball_x = ball_x + ball_speed_x
        ball_y = ball_y + ball_speed_y
        ball_2x = ball_2x + ball_speed_2x
        ball_2y = ball_2y + ball_speed_2y

        # Bounce off left and right walls
        if ball_x <= ball_size or ball_x >= SCREEN_WIDTH - ball_size:
            ball_speed_x = -ball_speed_x  # Reverse direction
            ball_color = rl.GREEN
      # Change color when bouncing
        if ball_2x <= ball_size or ball_2x >= SCREEN_WIDTH - ball_size:
            ball_speed_2x = -ball_speed_2x  # Reverse direction
            ball_color = rl.RED
       
        
        # Bounce off top and bottom walls
        if ball_y <= ball_size or ball_y >= SCREEN_HEIGHT - ball_size:
            ball_speed_y = -ball_speed_y  # Reverse direction
            ball_color = rl.GREEN  # Change color when bouncing
        
        if ball_2y <= ball_size or ball_2y >= SCREEN_HEIGHT - ball_size:
            ball_speed_2y = -ball_speed_2y  # Reverse direction
            ball_color = rl.PURPLE  # Change color when bouncing
        
        rl.begin_drawing()
        rl.clear_background(rl.WHITE)
        
        # Draw the bouncing ball
        rl.draw_circle(int(ball_x), int(ball_y), ball_size, ball_color)
        rl.draw_circle(int(ball_2x), int(ball_2y), ball_size, ball_color)
        
        # Draw some helpful text
        rl.draw_text("Watch the ball bounce! 🏀", 250, 50, 30, rl.DARKBLUE)
        rl.draw_text(f"Ball position: ({int(ball_x)}, {int(ball_y)})", 10, 10, 20, rl.BLACK)
        
        rl.end_drawing()
    
    rl.close_window()

if __name__ == "__main__":
    main()

"""
🌟 WHAT'S HAPPENING?
1. We store the ball's position in variables (ball_x, ball_y)
2. Every frame, we add speed to position (this creates movement)
3. When the ball hits a wall, we reverse its speed direction
4. The ball changes color each time it bounces

🎮 TRY CHANGING:
- Make the ball move faster (bigger speed numbers)
- Make the ball bigger or smaller
- Try different colors
- Add more balls (you'll need more variables!)

🧮 MOVEMENT MATH:
position = position + speed
If speed is positive, object moves right/down
If speed is negative, object moves left/up
"""
