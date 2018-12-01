# flake8: noqa
from moban_slim._version import __version__
from moban_slim._version import __author__

from lml.plugin import PluginInfo, PluginInfoChain
import moban.constants as constants


PluginInfoChain(__name__).add_a_plugin_instance(
    PluginInfo(
        constants.TEMPLATE_ENGINE_EXTENSION,
        "%s.engine.EngineSlim" % __name__,
        tags=["slim"],
    )
)
