import numpy as np

class PDController:
    def __init__(self, Kp=0.15, Kd=0.6):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0.0

    def compute_control(self, reference, output):
        # Calculate current error
        error = reference - output

        # PD control law
        u = self.Kp * error + self.Kd * (error - self.previous_error)

        # Update previous error for next step
        self.previous_error = error

        return u
