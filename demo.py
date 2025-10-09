
import os, sys

def main():
   
    context = os.environ.get("function_param")
    if not context:
        print("Missing exported function_param!")
        return

    # 2 or 3 params
    args = sys.argv[1:]
    if len(args) not in (2, 3):
        print("missing function parameters")
        return

    print("Success!")

if __name__ == "__main__":
    main()
