# -*- coding: utf-8 -*-

from plone.dexterity.content import Item
from zope.interface import implementer
from zope.interface import Interface


class ILinkedArticle(Interface):
        """Explicit marker interface for Grid Page."""


@implementer(ILinkedArticle)
class LinkedArticle(Item):
        """Convenience Item subclass for ``LinkedArticle`` portal type
        """

