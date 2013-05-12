__author__ = 'robertv'

import nltk, datetime
from models import ItemForSale, HuntEntry, Seller

def extract_nouns( sentence):

    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    nouns = []
    for (word, tag) in tagged:
        if tag == 'NN':
            nouns.append(word)

    return nouns

def add_a_listing(listingTitle, listingDescription, listingPrice, seller):
    item = ItemForSale(title=listingTitle,
                       description=listingDescription,
                       price = listingPrice,
                       listing_date = datetime.datetime.now(),
                       seller = seller)
    item.save()

    nouns = extract_nouns(item.title + item.description)
    count = 0
    emails = {}
    for noun in nouns:
        notices = HuntEntry.objects.filter(search_text__icontains=noun)
        for notice in notices:
            email = notice.email
            if not emails.has_key(email):
                emails[email] = listingDescription
            print "Saved item " + item.title + " notified " + email
            count += 1
    return count
