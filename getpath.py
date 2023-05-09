from DirectoryTree import TreeGenerator
import os

Tree = TreeGenerator()
# Tree.generate()
Tree.generate(os.getcwd())