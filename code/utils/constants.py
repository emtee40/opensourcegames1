"""
Paths, properties.
"""

import os
import configparser

# paths
root_path = os.path.realpath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))
code_path = os.path.join(root_path, 'code')
web_template_path = os.path.join(code_path, 'html')
entries_path = os.path.join(root_path, 'entries')
tocs_path = os.path.join(entries_path, 'tocs')
screenshots_path = os.path.join(entries_path, 'screenshots')

web_path = os.path.join(root_path, 'docs')
web_css_path = os.path.join(web_path, 'css')
web_js_path = os.path.join(web_path, 'js')
web_screenshots_path = os.path.join(web_path, 'screenshots')
web_data_path = os.path.join(web_path, 'data')

private_properties_file = os.path.join(root_path, 'private.properties')
inspirations_file = os.path.join(root_path, 'inspirations.md')
developer_file = os.path.join(root_path, 'developers.md')

backlog_file = os.path.join(code_path, 'backlog.txt')
rejected_file = os.path.join(code_path, 'rejected.txt')
statistics_file = os.path.join(root_path, 'statistics.md')
screenshots_file = os.path.join(screenshots_path, 'README.md')
json_db_file = os.path.join(root_path, 'docs', 'data.json')

# local config
local_config_file = os.path.join(root_path, 'local-config.ini')

config = configparser.ConfigParser()
config.read(local_config_file)


def get_config(key):
    """

    :param key:
    :return:
    """
    return config['general'][key]

# database entry constants
generic_comment_string = '[comment]: # (partly autogenerated content, edit with care, read the manual before)'

# these fields have to be present in each entry (in this order)
essential_fields = ('File', 'Title', 'Home', 'State', 'Keyword', 'Code language', 'Code license')

# only these fields can be used currently (in this order)
valid_properties = ('Home', 'Media', 'Inspiration', 'State', 'Play', 'Download', 'Platform', 'Keyword', 'Code repository', 'Code language',
    'Code license', 'Code dependency', 'Assets license', 'Developer')

valid_fields = ('File', 'Title') + valid_properties + ('Note', 'Building')

url_fields = ('Home', 'Media', 'Play', 'Download', 'Code repository')

valid_url_prefixes = ('http://', 'https://', 'git://', 'svn://', 'ftp://', 'bzr://')

valid_building_properties = ('Build system', 'Build instruction')
valid_building_fields = valid_building_properties + ('Note',)

# these are the only valid platforms currently (and must be given in this order)
valid_platforms = ('Windows', 'Linux', 'macOS', 'Android', 'iOS', 'Web')

# these fields are not allowed to have comments
fields_without_comments = ('Inspiration', 'Play', 'Download', 'Platform', 'Code dependency')

# at least one of these must be used for every entry, this gives the principal categories and the order of the categories
recommended_keywords = (
    'action', 'arcade', 'adventure', 'visual novel', 'sports', 'platform', 'puzzle', 'role playing', 'simulation',
    'strategy', 'cards', 'board', 'music', 'educational', 'tool', 'game engine', 'framework', 'library', 'remake')
# TODO unmake remake a recommended keyword (should be the same as clone maybe), i.e. add another recommended keyword if only remake is in there

# entries where we do not want to show developers (because these lists are too long and too general)
entries_without_developers = ('Box2D', 'Dear ImGui', 'DirectPython', 'FreeType', 'Horde3D', 'ncurses', 'Penumbra', 'Simple and Fast Multimedia Library',
                              'Simple DirectMedia Layer', 'Allegro', 'Crystal Space 3D SDK', 'Dash Engine', 'Delta Engine', 'libGDX', 'MonoGame', 'OGRE',
                              'Panda3D', 'Phaser', 'Qt', 'raylib', 'ScummVM', 'Urho3D')

# interesting keywords = recommend keywords + some popular keywords
interesting_keywords = recommended_keywords + ('2D', '3D', 'clone', 'first-person', 'real-time', 'roguelike', 'shooter', 'space', 'turn-based', 'for kids', 'for adults')

# non game keywords take precedence over other (game) recommended keywords, at most one of them per entry
non_game_keywords = ('framework', 'game engine', 'library', 'tool')

# known programming languages, anything else will result in a warning during a maintenance operation
# only these will be used when gathering statistics
language_urls = {
    'AGS Script': 'https://en.wikipedia.org/wiki/Adventure_Game_Studio',
    'ActionScript': 'https://en.wikipedia.org/wiki/ActionScript',
    'Ada': 'https://en.wikipedia.org/wiki/Ada_(programming_language)',
    'AngelScript': 'https://en.wikipedia.org/wiki/AngelScript',
    'Assembly': 'https://en.wikipedia.org/wiki/Assembly_language',
    'AWK': 'https://en.wikipedia.org/wiki/AWK',
    'Basic': 'https://en.wikipedia.org/wiki/BASIC',
    'Blender Script': 'https://en.wikipedia.org/wiki/Blender_(software)',
    'BlitzMax': 'https://en.wikipedia.org/wiki/Blitz_BASIC',
    'C': 'https://en.wikipedia.org/wiki/C_(programming_language)',
    'C#': 'https://en.wikipedia.org/wiki/C_Sharp_(programming_language)',
    'C++': 'https://en.wikipedia.org/wiki/C%2B%2B',
    'Clojure': 'https://en.wikipedia.org/wiki/Clojure',
    'CoffeeScript': 'https://en.wikipedia.org/wiki/CoffeeScript',
    'ColdFusion': 'https://en.wikipedia.org/wiki/ColdFusion_Markup_Language',
    'D': 'https://en.wikipedia.org/wiki/D_(programming_language)',
    'DM': 'http://www.byond.com/docs/guide/',
    'Dart': 'https://en.wikipedia.org/wiki/Dart_(programming_language)',
    'Elm': 'https://en.wikipedia.org/wiki/Elm_(programming_language)',
    'Emacs Lisp': 'https://en.wikipedia.org/wiki/Emacs_Lisp',
    'F#': 'https://en.wikipedia.org/wiki/F_Sharp_(programming_language)',
    'GDScript': 'https://en.wikipedia.org/wiki/Godot_(game_engine)#Scripting',
    'Game Maker Script': 'https://en.wikipedia.org/wiki/GameMaker#GameMaker_Language',
    'Go': 'https://en.wikipedia.org/wiki/Go_(programming_language)',
    'Groovy': 'https://en.wikipedia.org/wiki/Apache_Groovy',
    'Haskell': 'https://en.wikipedia.org/wiki/Haskell_(programming_language)',
    'Haxe': 'https://en.wikipedia.org/wiki/Haxe',
    'Io': 'https://en.wikipedia.org/wiki/Io_(programming_language)',
    'Java': 'https://en.wikipedia.org/wiki/Java_(programming_language)',
    'JavaScript': 'https://en.wikipedia.org/wiki/JavaScript',
    'Kotlin': 'https://en.wikipedia.org/wiki/Kotlin_(programming_language)',
    'Lisp': 'https://en.wikipedia.org/wiki/Lisp_(programming_language)',
    'Lua': 'https://en.wikipedia.org/wiki/Lua_(programming_language)',
    'MoonScript': 'https://moonscript.org/',
    'OCaml': 'https://en.wikipedia.org/wiki/OCaml',
    'Objective-C': 'https://en.wikipedia.org/wiki/Objective-C',
    'ooc': 'https://ooc-lang.org/',
    'PHP': 'https://en.wikipedia.org/wiki/PHP',
    'Pascal': 'https://en.wikipedia.org/wiki/Pascal_(programming_language)',
    'Perl': 'https://en.wikipedia.org/wiki/Perl',
    'Python': 'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'QuakeC': 'https://en.wikipedia.org/wiki/QuakeC',
    "Ren'Py": 'https://en.wikipedia.org/wiki/Ren%27Py',
    'Ruby': 'https://en.wikipedia.org/wiki/Ruby_(programming_language)',
    'Rust': 'https://en.wikipedia.org/wiki/Rust_(programming_language)',
    'Scala': 'https://en.wikipedia.org/wiki/Scala_(programming_language)',
    'Scheme': 'https://en.wikipedia.org/wiki/Scheme_(programming_language)',
    'Script': 'https://en.wikipedia.org/wiki/Scripting_language',  # for all script/shell dialects that aren't listed separately
    'Swift': 'https://en.wikipedia.org/wiki/Swift_(programming_language)',
    'TorqueScript': 'https://en.wikipedia.org/wiki/Torque_(game_engine)',
    'TypeScript': 'https://en.wikipedia.org/wiki/TypeScript',
    'Vala': 'https://en.wikipedia.org/wiki/Vala_(programming_language)',
    'Visual Basic': 'https://en.wikipedia.org/wiki/Visual_Basic',
    'XUL': 'https://en.wikipedia.org/wiki/XUL',
    'ZenScript': 'https://github.com/CraftTweaker/ZenScript'
}

known_languages = tuple(sorted(list(language_urls.keys()), key=str.casefold)) + ('None', '?')

# known licenses, anything outside of this will result in a warning during a maintenance operation
# only these will be used when gathering statistics
known_licenses = (
    '2-clause BSD', '3-clause BSD', '4-clause BSD', 'AFL-3.0', 'AGPL-3.0', 'Apache-2.0', 'Artistic License-1.0', 'Artistic License-2.0',
    'Boost-1.0', 'CC-BY-NC-3.0', 'CC-BY-NC-SA-2.0', 'CC-BY-NC-SA-3.0', 'CC-BY-SA-3.0', 'CC-BY-NC-SA-4.0', 'CC-BY-NC-ND-4.0',
    'CC-BY-SA-4.0', 'CC0', 'Custom', 'EPL-2.0', 'GPL-2.0', 'GPL-3.0', 'IJG', 'ISC', 'Java Research License', 'LGPL-2.0',
    'LGPL-2.1', 'LGPL-3.0', 'MAME', 'MIT', 'MPL-1.1', 'MPL-2.0', 'MS-PL', 'MS-RL', 'NetHack General Public License',
    'None', 'NPOSL-3.0', 'Proprietary', 'Public domain', 'SWIG license', 'Unlicense', 'WTFPL', 'wxWindows license', 'zlib', '?')

license_urls_repo = {
    '2-clause BSD': 'https://en.wikipedia.org/wiki/BSD_licenses#2-clause_license_(%22Simplified_BSD_License%22_or_%22FreeBSD_License%22)',
    '3-clause BSD': 'https://en.wikipedia.org/wiki/BSD_licenses#3-clause_license_(%22BSD_License_2.0%22,_%22Revised_BSD_License%22,_%22New_BSD_License%22,_or_%22Modified_BSD_License%22)',
    '4-clause BSD': 'https://en.wikipedia.org/wiki/BSD_licenses#4-clause_license_(original_%22BSD_License%22)',
    'AFL': 'https://en.wikipedia.org/wiki/Academic_Free_License',
    'AGPL': 'https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License',
    'Apache': 'https://en.wikipedia.org/wiki/Apache_License',
    'Artistic License': 'https://en.wikipedia.org/wiki/Artistic_License',
    'Boost': 'https://en.wikipedia.org/wiki/Boost_(C%2B%2B_libraries)#License',
    'CC': 'https://en.wikipedia.org/wiki/Creative_Commons_license',
    'EPL': 'https://en.wikipedia.org/wiki/Eclipse_Public_License',
    'GPL': 'https://en.wikipedia.org/wiki/GNU_General_Public_License',
    'IJG': 'https://spdx.org/licenses/IJG.html',
    'ISC': 'https://en.wikipedia.org/wiki/ISC_license',
    'Java Research License': 'https://en.wikipedia.org/wiki/Java_Research_License',
    'LGPL': 'https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License',
    'MAME': 'https://docs.mamedev.org/license.html',
    'MIT': 'https://en.wikipedia.org/wiki/MIT_License',
    'MPL': 'https://en.wikipedia.org/wiki/Mozilla_Public_License',
    'MS': 'https://en.wikipedia.org/wiki/Shared_Source_Initiative#Microsoft_Public_License_(Ms-PL)',
    'Nethack': 'https://en.wikipedia.org/wiki/NetHack#Licensing,_ports,_and_derivative_ports',
    'Public domain': 'https://en.wikipedia.org/wiki/Public_domain',
    'Unlicense': 'https://en.wikipedia.org/wiki/Unlicense',
    'WTFPL': 'https://en.wikipedia.org/wiki/WTFPL',
    'wxWindows': 'https://en.wikipedia.org/wiki/WxWidgets#License',
    'zlib': 'https://en.wikipedia.org/wiki/Zlib_License'
}


def get_license_url(license):
    if license not in known_licenses:
        raise RuntimeError('Unknown license')
    for k, v in license_urls_repo.items():
        if license.startswith(k):
            return v
    return None


license_urls = {license: get_license_url(license) for license in known_licenses if get_license_url(license) is not None}

# valid multiplayer modes (can be combined with "+" )
valid_multiplayer_modes = (
    'competitive', 'co-op', 'hotseat', 'LAN', 'local', 'massive', 'matchmaking', 'online', 'split-screen')

# TODO put the abbreviations directly in the name line (parenthesis maybe), that is more natural
# this is a mapping of entry name to abbreviation and the abbreviations are used when specifying code dependencies
code_dependencies_aliases = {'Simple DirectMedia Layer': ('SDL', 'SDL2'), 'Simple and Fast Multimedia Library': ('SFML',),
                             'Boost (C++ Libraries)': ('Boost',), 'SGE Game Engine': ('SGE',), 'MegaGlest': ('MegaGlest Engine',)}

# no developers needed for libraries

# these are code dependencies that won't get their own entry, because they are not centered on gaming
general_code_dependencies_without_entry = {'OpenGL': 'https://www.opengl.org/',
                                   'GLUT': 'https://www.opengl.org/resources/libraries/',
                                   'WebGL': 'https://www.khronos.org/webgl/',
                                   'Unity': 'https://unity.com/solutions/game',
                                   '.NET': 'https://dotnet.microsoft.com/', 'Vulkan': 'https://www.khronos.org/vulkan/',
                                   'KDE Frameworks': 'https://kde.org/products/frameworks/',
                                   'jQuery': 'https://jquery.com/',
                                   'node.js': 'https://nodejs.org/en/',
                                   'GNU Guile': 'https://www.gnu.org/software/guile/',
                                   'tkinter': 'https://docs.python.org/3/library/tk.html',
                                   'Boost': 'https://www.boost.org/'}

# they are too abundant and quite general (and we should remove them if they occur)
ignored_code_dependencies = ('OpenAL', 'libcurl', 'libfreetype', 'libogg', 'libpng', 'libvorbis', 'libxml', 'zlib')

# build system urls
build_system_urls = {
    'CMake': 'https://cmake.org/',
    'Make': 'https://en.wikipedia.org/wiki/Make_(software)',
    'Autoconf': 'https://en.wikipedia.org/wiki/Autoconf',
    'Gradle': 'https://gradle.org/',
    'Visual Studio': 'https://en.wikipedia.org/wiki/Microsoft_Visual_Studio',
    'setup.py': 'https://packaging.python.org/tutorials/packaging-projects/#configuring-metadata',
    'Scons': 'https://scons.org/',
    'Ant': 'http://ant.apache.org/',
    'Maven': 'https://maven.apache.org/index.html',
    'Meson': 'https://mesonbuild.com/',
    'premake': 'https://premake.github.io/',
    'QMake': 'https://doc.qt.io/qt-5/qmake-manual.html',
}

# developer information (in the file all fields will be capitalized)
essential_developer_fields = ('Name', 'Games')
optional_developer_fields = ('Home', 'Contact', 'Organization')
valid_developer_fields = essential_developer_fields + optional_developer_fields
url_developer_fields = ('Home',)

# inspiration/original game information (in the file all fields will be capitalized)
essential_inspiration_fields = ('Name', 'Inspired entries')
optional_inspiration_fields = ('Media','Included')
valid_inspiration_fields = essential_inspiration_fields + optional_inspiration_fields
url_inspiration_fields = ('Media',)