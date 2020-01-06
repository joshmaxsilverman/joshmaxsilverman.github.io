from urllib.request import urlopen


def get_words(url) -> list:
    """Download and return a list of valid words"""
    source = urlopen(url)
    words = (word.strip().decode("utf-8").lower() for word in source)

    # filter the full list of words to remove words that contain the
    # letter "s", words with fewer than 4 total letters, and words
    # with more than 7 unique letters
    words = (w for w in words if "s" not in w)
    words = (w for w in words if len(w) >= 4)
    words = (w for w in words if len(set(w)) <= 7)
    return list(words)


def word_score(word: str) -> int:
    """
    A word's score is based on the length of the word:
    1 point for 4-letter words, 5 points for 5-letter words,
    6 points for 6-letter words, etc., plus a bonus of
    7 points if the word contains 7 unique letters
    """
    if len(word) == 4:
        return 1
    return len(word) + 7 * (len(set(word)) == 7)


class Puzzle(set):
    """
    A puzzle is a collection of letters that we can use to 
    make words. A word may use letters any number of times.
    """

    word_list = get_words("https://norvig.com/ngrams/enable1.txt")

    def score(self, center_letter: str) -> int:
        """
        A puzzle's score is the score of all the words that can be created
        from its letters, provided that the center letter is included
        """
        words = (w for w in self.word_list if center_letter in w)
        return sum(word_score(w) for w in words if set(w) <= self)

    def max_score(self) -> int:
        """Returns the max puzzle score by finding the best center letter"""
        return max(self.score(center) for center in self)

    def max_center(self) -> str:
        """Returns the center letter that maximizes the Puzzle's score"""
        scores = ((self.score(center), center) for center in self)
        return sorted(scores, reverse=True)[0][1]


if __name__ == "__main__":

    # create a list of candidates: seven-letter pool
    # that we can identify from the word list
    candidates = set()
    for word in Puzzle.word_list:
        uniques = set(word)
        if len(uniques) == 7:
            candidates.add("".join(sorted(uniques)))

    # calculate the maximum score we can achieve from
    # each candidate pool, and store as a dictionary
    # use tqdm as a progress bar; takes ~10 minutes.
    results = {c: Puzzle(c).max_score() for c in candidates}

    # print the top-10 seven letter combinations with scores
    print(sorted(results.items(), key=lambda x: x[1], reverse=True)[:10])
