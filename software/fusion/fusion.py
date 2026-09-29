def fuse_results(dpv_decision, voc_signal):
    """
    Combine DPV and VOC results.

    voc_signal:
        True  = VOC sensors show a supporting response
        False = VOC sensors do not show a supporting response

    This is demo fusion logic.
    It is not a validated drug-identification model.
    """

    if dpv_decision == "PRESUMPTIVE POSITIVE" and voc_signal:
        return "PRESUMPTIVE POSITIVE"

    if dpv_decision == "NEGATIVE" and not voc_signal:
        return "NEGATIVE"

    return "INCONCLUSIVE"


if __name__ == "__main__":

    print("MARG RAKSHAK - FUSION TEST")
    print("--------------------------")

    result = fuse_results(
        "PRESUMPTIVE POSITIVE",
        True
    )

    print(f"Final result: {result}")