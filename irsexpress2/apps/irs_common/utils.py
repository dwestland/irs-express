# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET


def get_tree_attrs(obj, *tree):
    value = obj
    for a in tree:
        value = getattr(value, a, None)
    return value


def generate_xfdf(fdf_data):
    prefix = '<?xml version="1.0" encoding="UTF-8"?>'
    root = ET.Element('xfdf')
    fields = ET.SubElement(root, 'fields', attrib={'xmlns': "http://ns.adobe.com/xfdf/", 'xml:space': "preserve"})
    for ename, evalue in fdf_data:
        xfield = ET.SubElement(fields, 'field', attrib={'name': ename})
        xvalue = ET.SubElement(xfield, 'value')
        xvalue.text = str(evalue)
    xml = bytearray(prefix, 'utf-8') + ET.tostring(root, encoding="utf-8", method="xml")
    return xml


def make_address(**kwargs):
    rvset = []
    wrap = kwargs.pop('wrap', 3)
    name_address_fields_order = ['name', 'street', 'apt', 'city', 'state', 'zip', 'county']
    for key in name_address_fields_order:
        value = kwargs.get(key, None)
        if value:
            if key == 'street' and not kwargs.get('apt') and wrap > 2:
                value = "%s\\n" % value
            elif key == 'apt':
                value = "#%s\\n" % value
            elif key == 'name':
                value = "%s\\n" % value
            elif key == 'zip' and wrap > 2:
                value = "%s\\n" % value
            else:
                value = "%s, " % value
            rvset.append(str(value))
    address = ''.join(rvset)
    if address.endswith(', '):
        address = address[:-2]
    return address
