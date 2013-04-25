__author__ = 'robertv'

import nltk, datetime
from models import ItemForSale, HuntEntry

def extract_nouns( sentence):

    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    nouns = []
    for (word, tag) in tagged:
        if tag == 'NN':
            nouns.append(word)

    return nouns

def add_a_listing(listingTitle, listingDescription, listingPrice):
    item = ItemForSale(title = listingTitle,
                       description = listingDescription,
                       price = listingPrice,
                       listing_date = datetime.datetime.now())

    nouns = extract_nouns(item.title)
    for noun in nouns:
        notices = HuntEntry.objects.filter(search_text__icontains=noun)
        for notice in notices:
            email = notice.email
            print "Sent email notification to " + email

def get_emails_to_notify(description):
    words = description.split()
    emails = []
    for word in words:
    #        nn = NoticeRequest.objects.filter(search_text__icontains=word)
        nn = HuntEntry.objects.filter(search_text__icontains=word)
        for n in nn:
            emails.append(n.email)
    return emails
