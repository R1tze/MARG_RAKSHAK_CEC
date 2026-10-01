import random
from sensors.airflow_processing import pressure_to_airflow


class AirflowSimulator:

    def read_pressure(self):
        # Simulate a breath sample most of the time
        if random.random() < 0.7:
            return random.uniform(0.5, 2.0)

        # Simulate no-breath condition
        return random.uniform(-0.05, 0.05)