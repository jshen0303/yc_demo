#!/usr/bin/env python3
import os, sys

def main():
    # Check for exported secret
    secret = os.environ.get("function_param")
    if not secret:
        print("Missing exported function_param!")
        return

    # Require 2 or 3 positional parameters
    args = sys.argv[1:]
    if len(args) not in (2, 3):
        print("missing function parameters")
        return

    # (Do whatever you want here; we just confirm success)
    print("Success!")

if __name__ == "__main__":
    main()
