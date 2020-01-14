import configparser
import re
import os


class CustomHTML(object):
    def legend(self, html):
        """Remove legend from html"""
        html_lines = re.split('\n', html)
        for line in html_lines:
            if re.match(".*<table.*\"Legends\">$", line):
                idx = html_lines.index(line)
                for i in range(idx, idx + 15):
                    html_lines.pop(idx)
                return '\n'.join(html_lines)

    def layout_default(self, html, args):
        """Change page layout"""
        app_path = '/'.join(os.path.realpath(__file__).split('/')[0:-1])
        cfg = configparser.ConfigParser()
        cfg.read(app_path + '/config/config_html.ini')
        style = cfg['STYLE']

        regex = (r"(?P<style>.*<style.*/css.*)\n"
                 r"(?P<table_diff>.*)(?P<c1>font.*;).\n"
                 r"(?P<_diff_header>.*)(?P<c2>background.*\b).\n"
                 r"(?P<td_diff_header>.*)(?P<c3>text.*\b).\n"
                 r"(?P<_diff_next>.*)(?P<c4>background.*\b).\n"
                 r"(?P<_diff_add>.*)(?P<c5>background.*\b).\n"
                 r"(?P<_diff_chg>.*)(?P<c6>background.*\b).\n"
                 r"(?P<_diff_sub>.*)(?P<c7>background.*\b).\n"
                 r"(?P<end_style>.*)")

        subst = ["\\g<style>\\n",
                 "\\g<table_diff>%s}\\n" % style['table.diff'].format(
                     str(args.font_size) + "pt"),
                 "\\g<_diff_header>%s}\\n" % style['.diff_header'],
                 "\\g<td_diff_header>%s}\\n" % style['tab.diff_header'],
                 "\\g<_diff_next>%s}\\n" % style['.diff_next'],
                 "\\g<_diff_add>\\g<c5>}\\n",
                 "\\g<_diff_chg>\\g<c6>}\\n",
                 "\\g<_diff_sub>\\g<c7>}\\n",
                 "%s" % ''.join([style['td'], style['th'],
                                 style['th.diff_header'], style['a']]),
                 "\\g<end_style>"]

        return re.sub(pattern=regex, repl=''.join(subst), string=html)

    def new_html(self, html, args):
        if not args.legend:
            html = self.legend(html)
        html = self.layout_default(html, args)
        return html
