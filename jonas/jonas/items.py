# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.contrib.loader.processor import Join, MapCompose
from w3lib.html import remove_tags, replace_entities, replace_escape_chars

extract_text = MapCompose(remove_tags, replace_entities, replace_escape_chars)

class JonasAuthorItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = Field()
    permalink = Field()
    born_before = Field()
    born_after = Field()
    dead_before = Field()
    dead_after = Field()
    
    #OEuvres associees
    oeuvres_link_detailed_works = Field()
    incipit = Field()
    oeuvres_title = Field()
    editorial_note = Field()
    #note_on_work = Field() # is indistinguishable from incipit at this level
    #shape = Field() # is indistinguishable from author at this level

    associated_link_detailed_works = Field()
    associated_manuscripts = Field(
            input_processor=extract_text,
            #output_processor=Join()
    )
    
    #Bibliographie
    bibliography_link_detailed_works = Field()
    author_date = Field()
    complete_name = Field()
    bibliography_title = Field()
    in_work = Field()
    pages = Field()
    topic = Field()

    signature = Field()