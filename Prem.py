import platform, os

def __main__():
  try:
    __import__('Instagram').__masuk__()
  except Exception as e:
    exit(f"\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m {e}")

if __name__=='__main__':
  if '64bit' in str(platform.architecture()):
    os.system('git pull');__main__()
  else:
    exit("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Gunakan Perangkat 64bit")
