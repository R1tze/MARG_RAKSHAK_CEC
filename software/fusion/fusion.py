def fuse_results(dpv_decision, voc_signal, sample_valid=True):
    """
    Combine DPV and VOC results.

    This is development/demo fusion logic.
    It is NOT a validated drug-identification model.

    sample_valid:
        True  = breath/sample passed validity checks
        False = sample is invalid or insufficient
    """

    # Never classify an invalid sample as negative.
    if not sample_valid:
        return "INCONCLUSIVE"

    # Both channels support the result.
    if dpv_decision == "PRESUMPTIVE POSITIVE" and voc_signal:
        return "POSITIVE"

    # Both channels support a negative result.
    if dpv_decision == "NEGATIVE" and not voc_signal:
        return "NEGATIVE"

    # Any disagreement between channels.
    return "INCONCLUSIVE"


if __name__ == "__main__":

    print("MARG RAKSHAK - FUSION TEST")
    print("--------------------------")

    result = fuse_results(
        dpv_decision="PRESUMPTIVE POSITIVE",
        voc_signal=True,
        sample_valid=True
    )

    print(f"Final result: {result}")