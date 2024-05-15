#!/usr/bin/env python

# based on: https://fontforge.org/docs/scripting/python.html#fontforge-as-a-python-extension
# doc: https://fontforge.org/docs/scripting/python/fontforge.html

# === Prerequisite ===

# 1. FontForge and its Python bidings installed on the system:
#     sudo apt install fontforge python3-fontforge

# 2. A git worktree initialized in the public folder:
#     git checkout --orphan public
#     git reset --hard
#     git checkout main
#     git worktree add public public

from pathlib import Path
from shutil import copy
import sys
import subprocess

import fontforge


PROJECT_DIR = Path(__file__).parent
WEBSITE_DIR = PROJECT_DIR / 'website'
SOURCE_DIR = PROJECT_DIR / 'sources'
DIST_DIR = PROJECT_DIR / 'dist'
PUBLIC_DIR = PROJECT_DIR / 'public'

FONT_SVG_PATH = SOURCE_DIR / 'font.svg'
FONT_TTF_PATH = DIST_DIR / 'hexagon_drawing.ttf'
WEBSITE_CSS_PATH = WEBSITE_DIR / 'index.html'
WEBSITE_HTML_PATH = WEBSITE_DIR / 'style.css'


def build_ttf():
    FONT_TTF_PATH.parent.mkdir(parents=True, exist_ok=True)

    font = fontforge.open(str(FONT_SVG_PATH))
    font.correctDirection()
    font.generate(str(FONT_TTF_PATH))
    font.close()

def build_public():
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)

    for f in PUBLIC_DIR.iterdir():
        f.unlink()

    copy(WEBSITE_HTML_PATH, PUBLIC_DIR)
    copy(WEBSITE_CSS_PATH, PUBLIC_DIR)
    copy(FONT_TTF_PATH, PUBLIC_DIR)

def deploy():
    subprocess.check_call(['git', 'pull'], cwd=PUBLIC_DIR)
    subprocess.check_call(['git', 'commit', '--amend', '--message', 'update website'], cwd=PUBLIC_DIR)
    subprocess.check_call(['git', 'push', '--force', 'origin', 'public'], cwd=PUBLIC_DIR)

if __name__ == '__main__':
    commands = { 'ttf': build_ttf, 'public': build_public, 'deploy': deploy }

    if len(sys.argv) != 2 or sys.argv[1] not in commands:
        print(f"Usage: { sys.argv[0] } [{ ' | '.join(commands) }]")
        sys.exit(1)

    commands[sys.argv[1]]()
