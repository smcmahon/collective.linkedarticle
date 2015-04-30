# -*- coding: utf-8 -*-

from plone.dexterity.content import Item
from zope.interface import implementer
from zope.interface import Interface
from Products.Five.browser import BrowserView


class ILinkedArticle(Interface):
        """Explicit marker interface for Grid Page."""


@implementer(ILinkedArticle)
class LinkedArticle(Item):
        """Convenience Item subclass for ``LinkedArticle`` portal type
        """


class LinkedArticleView(BrowserView):
    """ Default view for grid pages.
    """
