## -*- coding: utf-8 -*-
import telebot


class Table:
    dict_categories = {}

    def __init__(self):
        self.dict_categories = {} ## maps the name of the category to the object of type 'Category'


class Category:
    name = ''
    dict_subcategories = {}

    def __init__(self, name):
        self.name = name
        self.dict_subcategories = {}  ## maps the name of the subcategory to the object of type 'Subcategory'


class Subcategory:
    name = ''
    dict_blocks = {}

    def __init__(self, name):
        self.name = name
        self.dict_blocks = {}  ## maps name of the organization to the object of type 'Block' (organization)


class Block:
    name = ''
    category = ''
    subcategory = ''
    description = ''
    address = ''
    phone = ''
    schedule = ''
    link = ''

    def __init__(self,
                 name,
                 category,
                 subcategory=None,
                 description=None,
                 address=None,
                 phone=None,
                 schedule=None,
                 link=None):
        self.name = name
        self.category = category
        self.subcategory = subcategory
        self.description = description
        self.address = address
        self.phone = phone
        self.schedule = schedule
        self.link = link