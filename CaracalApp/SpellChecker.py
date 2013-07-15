__author__ = 'robertv'

import re, collections

CORPUS = '../../Corpora/LargeWordCorpus.txt'
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def words(text):
    """
        Convert input text to lower case and parse out (using regex) into words
    :param text:
    :return:
    """
    return re.findall('[a-z]+', text.lower())

def train(list_of_words):
    """
        Return smoothed training set
        i.e.,  hash of word counts, with a smoother of 1 for rare words
    :param features: collection of words, in lower case
    :return:
    """
    counts = collections.defaultdict(lambda: 1)
    for w in list_of_words:
        counts[w] += 1
    return counts

# TODO:  The training set should be saved and reused rather than calculated every time
NWORDS = train(words(file(CORPUS).read()))


def words_of_distance1(word):
   """
        Construct 'corrected' words from various permutations of original word
        These all have edit distance '1' from the original word
   :param word:
   :return:
   """
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def words_of_distance2(word):
    """
        Construct 'corrected' words from repeated application of distance1 mutation
        except, only return words in the corpus
        NOTE:  this means rare words may get misclassified.
    :param word:
    :return:
    """
    return set(e2 for e1 in words_of_distance1(word) for e2 in words_of_distance1(e1) if e2 in NWORDS)

def known(words_to_check):
    """
        return only words in words_to_check that are 'real' words.  i.e., in the corpus
    :param words_to_check:
    :return:
    """
    return set(w for w in words_to_check if w in NWORDS)

def get_correct_spelling(word):
    """
        Find c with maximum P(c|w)
        P(c|w) = P(w|c) * P(c) / P(w)   -- Since w is constant, so is P(w) and it can be ignored
        P(c) = count(c)/count(all)      -- Since count(all) is also constant, it can be ignored
        maximize P(w|c) * count(c)
        For this simple checker, let
            P1(w|c)  is the probability for edit_distance=1
            P2(w|c)  is the probability for edit_distance=2
        Assume P1 >>> P2,  that is, if we can find a word distance 1,use it.  if not, try distance 2
    :param word:
    :return:
    """
    candidates = known([word]) or known(words_of_distance1(word)) or words_of_distance2(word) or [word]
    return max(candidates, key=NWORDS.get)

