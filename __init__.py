import logging
from Editor import Editor

# This is where the version of this editor is defined
major = 0
minor = 0
tiny = 4

# should read these from somewhere
project = "Zelda clone"
path = "zelda"

def main():
    """the main function"""
    print("==================================================")
    print("Green Editor v%i.%i.%i" % (major, minor, tiny))
    print("==================================================")

    ed = Editor(project, path)
    ed.start()

if __name__ == "__main__":
    main()
