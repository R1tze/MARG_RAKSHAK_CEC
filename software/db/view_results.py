import sqlite3


DATABASE = "marg_rakshak.db"


def view_results():
    connection = sqlite3.connect(DATABASE)

    cursor = connection.execute("""
        SELECT
            id,
            timestamp,
            co2_ppm,
            airflow,
            peak_potential,
            peak_current,
            dpv_decision,
            final_result
        FROM test_results
        ORDER BY id
    """)

    rows = cursor.fetchall()

    print("MARG RAKSHAK - TEST RESULTS")
    print("=" * 90)

    if not rows:
        print("No test results found.")
        connection.close()
        return

    for row in rows:
        print(f"Test ID:          {row[0]}")
        print(f"Timestamp:         {row[1]}")
        print(f"CO2:               {row[2]} ppm")
        print(f"Airflow:           {row[3]:.2f}")
        print(f"DPV peak potential:{row[4]:.3f} V")
        print(f"DPV peak current:  {row[5]:.4f}")
        print(f"DPV decision:      {row[6]}")
        print(f"Final result:      {row[7]}")
        print("-" * 90)

    connection.close()


if __name__ == "__main__":
    view_results()