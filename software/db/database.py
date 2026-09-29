import sqlite3
from datetime import datetime


class DatabaseLogger:
    """
    SQLite logger for MARG RAKSHAK test results.
    """

    def __init__(self, database_path="marg_rakshak.db"):
        self.database_path = database_path
        self.connection = sqlite3.connect(self.database_path)

        self.create_table()

    def create_table(self):
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS test_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                co2_ppm REAL,
                airflow REAL,
                peak_potential REAL,
                peak_current REAL,
                dpv_decision TEXT,
                final_result TEXT
            )
        """)

        self.connection.commit()

    def log_result(
        self,
        co2,
        airflow,
        peak_potential,
        peak_current,
        dpv_decision,
        final_result
    ):
        timestamp = datetime.now().isoformat(timespec="seconds")

        self.connection.execute("""
            INSERT INTO test_results (
                timestamp,
                co2_ppm,
                airflow,
                peak_potential,
                peak_current,
                dpv_decision,
                final_result
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            timestamp,
            co2,
            airflow,
            peak_potential,
            peak_current,
            dpv_decision,
            final_result
        ))

        self.connection.commit()

    def close(self):
        self.connection.close()


if __name__ == "__main__":

    print("MARG RAKSHAK - DATABASE TEST")
    print("----------------------------")

    database = DatabaseLogger()

    database.log_result(
        co2=3000,
        airflow=2.0,
        peak_potential=0.250,
        peak_current=0.1469,
        dpv_decision="PRESUMPTIVE POSITIVE",
        final_result="PRESUMPTIVE POSITIVE"
    )

    print("Test result saved successfully.")

    database.close()