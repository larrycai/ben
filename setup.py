import setuptools

setuptools.setup(
    name="ben",
    version="0.4.0",
    description="bridge engine - ai system",
    packages=setuptools.find_packages(include=['src/*']),
    package_dir={'ben':'src'},
#    install_requires=[
#        'requests',
#        'markdown'
#    ],
    python_requires='>=3.8',
)
