#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Andre Staltz
# Copyright (c) 2014 Andre Staltz
#
# License: MIT
#

"""This module exports the Xtendlint plugin class."""

from SublimeLinter.lint import Linter, util


class Xtendlint(Linter):
    """Provides an interface to xtendlint."""

    syntax = 'xtend'
    cmd = 'xtendlint @'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.1.0'
    regex = r'^L(?P<line>\d+): (?P<message>.+)'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None
