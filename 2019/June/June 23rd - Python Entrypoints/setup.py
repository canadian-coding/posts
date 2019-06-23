import setuptools
def get_content(filename):
    """ Gets the content of a file and returns it as a string
    Args:
        filename(str): Name of file to pull content from

    Returns:
        str: Content from file
    """
    with open(filename, "r") as full_description:
        content = full_description.read()
    return content

setuptools.setup(
    name="entrypoint demo",
    version="0.0.1",
    author="Kieran Wood",
    author_email="canadiancoding@gmail.com",
    description="A demo for script entrypoints",
    long_description=get_content("readme.md"),
    long_description_content_type="text/markdown",
    url=r"https://github.com/canadian-coding/posts/2019/June/June%2023rd%20-%20Python%20Entrypoints",
    packages=setuptools.find_packages(),
    entry_points={
          'console_scripts': ['command_name = package.command_line_utility:main']
      },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)