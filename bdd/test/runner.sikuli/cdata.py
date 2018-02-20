"""
Module:  cdata

Author:  arjs.net

License: http://opensource.org/licenses/mit-license.html; year=2013,2014; copyright holders=arjs.net

Module for the cdata extension
"""
import xml.etree.cElementTree as elementTree


class ElementTreeCDATA(elementTree.ElementTree):
    """ElementTreeCDATA: Extension to write a cdata section to a xml file"""

    def _write(self, xmlfile, node, encoding, namespaces):
        """
        :param xmlfile: xml file to write
        :type xmlfile: file
        :param node: Node element to write
        :type node: Element
        :param encoding: Encoding type
        :type encoding: str
        :param namespaces: Namespace to use
        :type namespaces: str
        :rtype: None

        Write the xml data extended with cdata block(s)
        """
        if node.tag is cdata:
            text = node.text.encode(encoding)
            xmlfile.write("\n<![CDATA[%s]]>\n" % text)
        else:
            elementTree.ElementTree._write(self, xmlfile, node, encoding, namespaces)


def cdata(text=None):
    """
    :param text: cdata content
    :type text: str
    :return:
    :rtype: Element

    Create a cdata element
    """
    element = elementTree.Element(cdata)
    element.text = text
    return element
