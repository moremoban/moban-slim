# flake8: noqa
import moban.constants as constants
from lml.plugin import PluginInfo, PluginInfoChain

from moban_slim._version import __author__, __version__

PluginInfoChain(__name__).add_a_plugin_instance(
    PluginInfo(
        constants.TEMPLATE_ENGINE_EXTENSION,
        "%s.engine.EngineSlim" % __name__,
        tags=["slim"],
    )
)
