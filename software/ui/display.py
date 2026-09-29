def show_result(
    breath_status,
    sample_status,
    peak_potential=None,
    peak_current=None,
    dpv_decision=None,
    final_result=None
):
    print()
    print("=" * 40)
    print("          MARG RAKSHAK")
    print("=" * 40)

    print(f"BREATH : {breath_status}")
    print(f"SAMPLE : {sample_status}")

    if peak_potential is not None:
        print(f"DPV PEAK : {peak_potential:.3f} V")

    if peak_current is not None:
        print(f"CURRENT  : {peak_current:.4f}")

    if dpv_decision is not None:
        print(f"DPV DECISION : {dpv_decision}")

    if final_result is not None:
        print()
        print("RESULT")
        print("-" * 40)
        print(final_result)

    print("=" * 40)
    print()


if __name__ == "__main__":

    show_result(
        breath_status="VALID",
        sample_status="READY",
        peak_potential=0.250,
        peak_current=0.1469,
        dpv_decision="PRESUMPTIVE POSITIVE",
        final_result="PRESUMPTIVE POSITIVE"
    )