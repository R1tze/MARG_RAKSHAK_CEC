def classify_signal(peak_current, lod=0.05, loq=0.10):
    """
    Demo DPV decision logic.

    lod = Limit of Detection
    loq = Limit of Quantification
    """

    if peak_current is None:
        return "INCONCLUSIVE"

    if peak_current < lod:
        return "NEGATIVE"

    if peak_current < loq:
        return "INCONCLUSIVE"

    return "PRESUMPTIVE POSITIVE"
