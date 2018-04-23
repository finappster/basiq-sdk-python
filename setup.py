from distutils.core import setup
setup(
  name = "basiq",
  packages=["basiq/services", "basiq/utils", "basiq"], # this must be the same as the name above
  version = "0.9.3b2",
  description = "SDK Package for Basiq's HTTP API",
  author = "Nenad Lukic",
  python_requires=">=3",
  install_requires=["requests"],
  author_email = "nenad@basiq.io",
  url = "https://github.com/basiqio/basiq-sdk-python", # use the URL to the github repo
  download_url = "https://github.com/basiqio/basiq-sdk-python/archive/0.9.3b2.tar.gz", # I"ll explain this in a second
  keywords = ["basiq", "finance", "sdk", "api"], # arbitrary keywords
  classifiers = []
)