from django import template

register=template.library()

def cut(value,arg): #this takes value cuts out all values of arg
    return value.replace(arg,'')

register.filter('cut',cut)
