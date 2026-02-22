# spam_detector.py
# Spam Detection Application

# List of 30 common spam words/phrases
SPAM_KEYWORDS = [
    'free',
    'winner',
    'congratulations',
    'click here',
    'limited time',
    'act now',
    'urgent',
    'guaranteed',
    'risk free',
    'prize',
    'claim now',
    'lottery',
    'cash',
    'earn money',
    'work from home',
    'no credit check',
    'credit card',
    'investment',
    'double your',
    'miracle',
    'weight loss',
    'viagra',
    'luxury',
    'offer expires',
    'buy now',
    'cheap',
    'exclusive deal',
    '100% free',
    'this is not spam',
    'winner selected'
]


def calculate_spam_score(message):
    '''
    Scans message for spam keywords and calculates spam score.
    Returns score and list of detected spam words.
    '''
    score = 0
    found_words = []

    message_lower = message.lower()

    for keyword in SPAM_KEYWORDS:
        count = message_lower.count(keyword)
        if count > 0:
            score += count
            found_words.append((keyword, count))

    return score, found_words


def rate_spam(score):
    '''
    Rates likelihood of spam based on score.
    '''
    if score == 0:
        return 'Very unlikely to be spam.'
    elif score <= 3:
        return 'Low likelihood of spam.'
    elif score <= 6:
        return 'Moderate likelihood of spam.'
    elif score <= 10:
        return 'High likelihood of spam.'
    else:
        return 'Very high likelihood of spam.'


def main():
    print('==== Spam Detection Application ====\n')

    user_message = input('Enter the email message to scan:\n')

    score, found_words = calculate_spam_score(user_message)
    likelihood = rate_spam(score)

    print('\n===== RESULTS =====')
    print(f'Spam Score: {score}')
    print(f'Spam Likelihood: {likelihood}')

    if found_words:
        print('\nWords/Phrases Found:')
        for word, count in found_words:
            print(f'- \'{word}\' found {count} time(s)')
    else:
        print('\nNo spam keywords detected.')


if __name__ == '__main__':
    main()