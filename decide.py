GO_THRESHOLD = 85
REVIEW_THRESHOLD = 60


def decide(scored_matches):
    eligible = [m for m in scored_matches if m["mandatory_met"]]

    if eligible and eligible[0]["score"] >= GO_THRESHOLD:
        status = "GO"
    elif eligible and eligible[0]["score"] >= REVIEW_THRESHOLD:
        status = "REVIEW"
    else:
        status = "NO-GO"

    return {
        "status": status,
        "top_candidate": eligible[0] if eligible else None,
        "ranked": scored_matches,
    }
