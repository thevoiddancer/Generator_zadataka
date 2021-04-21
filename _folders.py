
# Rađenje foldera za kategorije
import os

# Složiti getFolders kao rekurziju i smisliti prikaz foldera
def getFolders(folder = None):
  return [i.name for i in os.scandir(folder) if i.is_dir() and i.name[0] not in [".", "_"]]

def categories():
  folders = {}
  for root in getFolders():
    folders[root] = getFolders(root)
  return folders

#def showCategories()

def addCategory(name):
  try:
    os.mkdir(name)
    return True
  except FileExistsError:
    return False

def delCategory(name):
  try:
    os.rmdir(name)
    return True
  except:
    return False

def addSubCategory(category, name):
  try:
    os.mkdir(category + '/' + name)
    return True
  except FileExistsError:
    return False

def delSubCategory(category, name):
  try:
    os.rmdir(category + '/' + name)
    return True
  except:
    return False

