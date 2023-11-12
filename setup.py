import setuptools

setuptools.setup(
    name="bridgeai-ben", # Replace with your own username
    description="bridge engine - ai system",
    packages=setuptools.find_packages(include=['src']),
#    install_requires=[
#        'requests',
#        'markdown'
#    ],
    python_requires='>=3.8',
)
