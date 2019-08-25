# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from ploneconf.theme1.testing import PLONECONF_THEME1_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ploneconf.theme1 is properly installed."""

    layer = PLONECONF_THEME1_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneconf.theme1 is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ploneconf.theme1'))

    def test_browserlayer(self):
        """Test that IPloneconfTheme1Layer is registered."""
        from ploneconf.theme1.interfaces import (
            IPloneconfTheme1Layer)
        from plone.browserlayer import utils
        self.assertIn(IPloneconfTheme1Layer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONECONF_THEME1_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(username=TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['ploneconf.theme1'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if ploneconf.theme1 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ploneconf.theme1'))

    def test_browserlayer_removed(self):
        """Test that IPloneconfTheme1Layer is removed."""
        from ploneconf.theme1.interfaces import \
            IPloneconfTheme1Layer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPloneconfTheme1Layer,
            utils.registered_layers(),
        )
