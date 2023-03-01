import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mypythonlibrary',
    version='0.0.1',
    author='Kody Anderson',
    author_email='kanderson@ihmc.org',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/KodyAnderson1/test_pip',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    # },
    license='MIT',
    packages=['mypythonlib'],
    install_requires=[],
)

# https://git.ihmc.us/human-performance/projects/augmentics/proteus/live-testbed-data-management/analytics/testbed-analytics.git