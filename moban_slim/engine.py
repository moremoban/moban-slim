import codecs

from jinja2 import Environment, FileSystemLoader
from slimish_jinja import SlimishExtension
import moban.utils as utils


class EngineSlim(object):
    def __init__(self, template_dirs):
        self.template_dirs = template_dirs
        self.jj2_env = Environment(
            loader=FileSystemLoader(template_dirs),
            extensions=[SlimishExtension]
        )
        self.jj2_env.slim_debug = True

    def get_template(self, template_file):
        template = self.jj2_env.get_template(template_file)
        return template

    def apply_template(self, template, data, _):
        rendered_content = template.render(**data)
        return rendered_content
