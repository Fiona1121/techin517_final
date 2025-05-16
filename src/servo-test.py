from adafruit_servokit import ServoKit
import time
import sys

class LidController:
    def __init__(self, channel_left=0, channel_right=1, closed_angle=0, open_angle=90, step_delay=0.01, step_size=1):
        try:
            self.kit = ServoKit(channels=16)
        except ValueError as e:
            print(f"ERROR initializing ServoKit: {e}")
            sys.exit(1)

        print("ServoKit initialized")
        self.left = channel_left
        self.right = channel_right
        self.closed_angle = closed_angle
        self.open_angle = open_angle
        self.step_delay = step_delay
        self.step_size = step_size
        self.current_angle = closed_angle  # track current angle
        self.initialize()

    def initialize(self):
        self.set_angle(self.closed_angle)

    def set_angle(self, target_angle):
        try:
            start = self.current_angle
            step = self.step_size if target_angle > start else -self.step_size
            for angle in range(start, target_angle + step, step):
                self.kit.servo[self.left].angle = angle
                self.kit.servo[self.right].angle = 180 - angle
                time.sleep(self.step_delay)
            self.current_angle = target_angle
        except Exception as e:
            print(f"Failed to set angle: {e}")


    def open_lid(self):
        print("Opening lid...")
        self.set_angle(self.open_angle)

    def close_lid(self):
        print("Closing lid...")
        self.set_angle(self.closed_angle)


def main():
    lid = LidController(closed_angle=10, open_angle=135)

    lid.open_lid()
    time.sleep(2)
    lid.close_lid()

if __name__ == '__main__':
    main()