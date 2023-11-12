import setuptools

setuptools.setup(
    name="ben",
    version="0.2.0",
    description="bridge engine - ai system",
    packages=setuptools.find_packages(include=['ben/*']),
    #package_dir={'ben':'src'},
#    install_requires=[
#        'requests',
#        'markdown'
#    ],
    python_requires='>=3.8',
)
