def classify_score(score):
    '''
    Given a score, classify it into one of four categories.
    
    "Poor" if score is between 0 to 50 (exclusive)
    "Average" if score is between 50 to 70 (exclusive)
    "Good" if score is between 70 to 90 (exclusive)
    "Excellent" if score is between 90 to 100 (inclusive)
    
    Example:
        classify_score(35) == "Poor"
        classify_score(55) == "Average"
        classify_score(75) == "Good"
        classify_score(95) == "Excellent"
    '''

    if score < 50:
        return "Poor"
    elif score < 70:
        return "Average"
    elif score < 90:
        return "Good"
    else:
        return "Excellent"
def classify_scores(scores):
    categories = {'Poor': 0, 'Average': 0, 'Good': 0, 'Excellent': 0}
    for score in scores:
        categories[classify_score(score)] += 1
    return categories