# coding: utf-8
import os, re
from setuptools import setup, find_packages, find_namespace_packages

with open(os.path.join("u3driver", "__init__.py"), encoding="utf8") as f:
  version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
  name='u3driver',
  version=version,
  python_requires='>=3.6',
  description='u3driver',
  url='http://gitlab.testplus.cn/sandin/u3driver',
  author='lds2012',
  author_email='lds2012@gmail.com',
  license='GPLv3',
  include_package_data=True, # 代码以外的文件也包含进来, 这些文件可以通过 __file__ 加相对路径找到
  packages=find_namespace_packages(include=['u3driver.*', "u3driver"]),
  install_requires='''
'''.split('\n'),
  zip_safe=False)
