



import time
import os

# Define the cycle as ASCII art with two states for pedal movement
# Larger cycle (ahead), with the message "I will win gulk" at the top
cycle_art_state_1_1 = [
    "  I will win  ",
    "   gulk!     ",
    "     __o     ",
    "   _  \<_    ",
    "  (_)/(_)   "
]

cycle_art_state_1_2 = [
    "  I will win  ",
    "   gulk!     ",
    "     __o     ",
    "   _ /<\\    ",
    "  (_)/(_)   "
]

# Smaller cycle (following), with pedal movement
cycle_art_state_2_1 = [
    "cmon    __o    ",
    "no!   _ \<_    ",
    "     (_)/(_)   "
]

cycle_art_state_2_2 = [
    "cmon    __o    ",
    "no!   _ /<\\   ",
    "     (_)/(_)   "
]

# Function to clear the screen
def clear():
    os.system('clear')

# Function to animate the two cycles with pedal movement
def animate():
    terminal_width = os.get_terminal_size().columns
    position_1 = -len(cycle_art_state_1_1[0])  # Start the first cycle outside the screen
    position_2 = -len(cycle_art_state_2_1[0]) - 20  # Start the second cycle behind by 20 spaces (larger distance)
    pedal_state_1 = 0  # 0 for state 1, 1 for state 2 (pedal forward/backward)
    pedal_state_2 = 0  # Same pedal state for both cycles initially

    while True:
        clear()

        # Move the cycles across the screen
        position_1 += 1
        position_2 += 1

        # Check if both cycles reached the end of the terminal
        if position_1 > terminal_width and position_2 > terminal_width:
            break

        # Print empty lines to move the cycle down
        print("\n" * (len(cycle_art_state_1_1) + 2))

        # Alternate the pedal states for animation
        cycle_art_1 = cycle_art_state_1_1 if pedal_state_1 == 0 else cycle_art_state_1_2
        cycle_art_2 = cycle_art_state_2_1 if pedal_state_2 == 0 else cycle_art_state_2_2

        # Print the first cycle with the current position (larger cycle with message)
        for line in cycle_art_1:  # Only print the first cycle with message
            print(" " * position_1 + line)

        # Print the second cycle with the current position (smaller cycle without message)
        for line in cycle_art_2:  # Only print the smaller cycle without message
            print(" " * position_2 + line)

        # Toggle pedal states for next frame
        pedal_state_1 = 1 - pedal_state_1
        pedal_state_2 = 1 - pedal_state_2

        time.sleep(0.1)  # Delay to control the speed of the animation

# The main function which runs the program
def main():
    animate()  # Start the animation

# Only call main() if the script is run directly (not imported)
if __name__ == "__main__":
    main()

