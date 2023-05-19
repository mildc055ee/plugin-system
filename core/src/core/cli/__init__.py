import sys
import importlib

def main():
    target = "main"
    if len(sys.argv) > 1:
        target = sys.argv[1]

    module = importlib.import_module(f"core.packages.{target}")

    module.call()
