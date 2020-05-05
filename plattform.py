try:
      os.environ["PROGRAMFILES(X86)"]
      bits = 64
except:
      bits = 32
      print ("Win{0}".format(bits))
