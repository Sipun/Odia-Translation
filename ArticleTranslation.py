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
    urls2 = "https://en.wikipedia.org/w/index.php?title=" + ArtName + "&action=edit"
    print urls
    request = urllib2.Request(urls)
    handle = urllib2.urlopen(request)
    content = handle.read()
    if '<table class="infobox' in content:
        print '\n\ndata about ' + ArtName + ' found... working...\n\n'
        splitted_page = content.split('<p>', 1);
        splitted_page = splitted_page[1].split('<span class="mw-headline" id="References">References</span>', 1)
        art = splitted_page[0]
        art = art.replace('</p>', '\n')
        art = art.replace('&#160;', '')
        art = art.replace('<span class="mw-headline"', '\n==<')
        art = re.sub('\<.*?\>','', art)
        art = re.sub('\ox .*?\em">','', art)

        to_print = trans(art.decode('utf-8')) #translate the text in to Odia
        
        # to write reference --BEGIN
        request2 = urllib2.Request(urls2)
        handle2 = urllib2.urlopen(request2)
        content2 = handle2.read()
        content2 = content2.split('name="wpTextbox1">', 1)
        content2 = content2[1].split('</textarea>', 1)
        content2 = content2[0]
        content2 = content2.replace('&lt;', '<')
        content3 = content2
        ref = input('entre the no. of references: ')
        i = 0
        while i != ref:
            if '<ref' in content2:
                ref_dataa = content2.split('<ref', 1)
                if '</ref>' in ref_dataa[1]: 
                    ref_data = ref_dataa[1].split('</ref>', 1)
                    ref_data = ref_data[0]
                else:
                    ref_data = ''
                ref_data = '<ref' + ref_data + '</ref>'
                if '/>' in ref_data:
                    ref_data = ref_dataa[1].split('/>', 1)
                    ref_data = '<ref' + ref_data[0] + '/>'
                content2 = content2.replace(ref_data, '')
                ref_no = '[' + str(i+1) + ']'
                to_print = to_print.replace(ref_no.decode('utf-8'), ref_data.decode('utf-8'))
            i+=1
        # to write reference -- END
        print "'''" + ArtName + "'''\n"
        to_print = to_print.replace('[ସମ୍ପାଦନା]'.decode('utf-8'), '==\n')
        print to_print

        #to print text after reference as it is -- BEGIN
        as_it_is = content3.split('==References==', 1)
        as_it_is = as_it_is[1]
        as_it_is = as_it_is.replace('</p>', '\n')
        as_it_is = as_it_is.replace('&#160;', '')
        print '\n==References==\n', as_it_is
        #to print text after reference as it is -- END
    else:
        print 'escape', i+1

    i+=1
