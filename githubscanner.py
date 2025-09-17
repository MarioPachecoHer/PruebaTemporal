import os
import subprocess
import time
import webbrowser
#import requests
import winreg

git_dir = r"C:\Users\mario\OneDrive\Desktop\4 Cuatri\Programacion de redes\practicagit"

repos = [name for name in os.listdir(git_dir)
         if os.path.isdir(os.path.join(git_dir, name)) and
         os.path.exists(os.path.join(git_dir, name, ".git"))]

if repos:
    print("Found the following Github repositories.")
    for idx, repo in enumerate(repos, 1):
        print(f"{idx}. {repo}") 
    else:
        print("No GitHb repositories found.")
        print("Please provide a GitHub repository")