import os
import sys

# Ensure repository root and App directory are available in Python sys.path
root_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(root_dir, 'App')

if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

# Import and execute App
import App
