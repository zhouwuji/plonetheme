# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ploneconf.theme1


class PloneconfTheme1Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ploneconf.theme1)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ploneconf.theme1:default')


PLONECONF_THEME1_FIXTURE = PloneconfTheme1Layer()


PLONECONF_THEME1_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONECONF_THEME1_FIXTURE,),
    name='PloneconfTheme1Layer:IntegrationTesting'
)


PLONECONF_THEME1_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONECONF_THEME1_FIXTURE,),
    name='PloneconfTheme1Layer:FunctionalTesting'
)


PLONECONF_THEME1_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONECONF_THEME1_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PloneconfTheme1Layer:AcceptanceTesting'
)
