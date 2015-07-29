#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
import goslate

def trans(word):
    gs = goslate.Goslate()
    ro = gs.translate(word, 'or')
    if ro == "":
        ro = word
    return ro

i = 3
while i != 100000:
    ArtName = raw_input('\n\ntype the name of article from english wikipedia: ')
    
    urls = "\n\nhttps://en.wikipedia.org/wiki/" + ArtName
    print urls
    request = urllib2.Request(urls)
    handle = urllib2.urlopen(request)
    content = handle.read()
    if '<table class="infobox' in content:
        print '\n\ndata about ' + ArtName + ' found... working...\n\n'
        splitted_page = content.split('<p>', 1);
        splitted_page = splitted_page[1].split('<span class="mw-headline" id="References">References</span>', 1)
        art = splitted_page[0]
        art = " ".join(art.splitlines())
        art = art.replace('</p>', '\n')
        art = art.replace('&#160;', '')
        art = re.sub('\<.*?\>','', art)
        art = re.sub('\[.*?\]','', art)
        art = re.sub('\ox .*?\em">','', art)
        print "'''" + ArtName + "'''\n"
        #print art.decode('utf-8') #prints the original text
        print trans(art.decode('utf-8')) #translate the text in to Odia
    else:
        print 'escape', i+1

    i+=1
