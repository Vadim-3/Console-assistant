from setuptools import setup, find_namespace_packages

setup(
    name='console_assistant',
    version='0.5',
    description='executes the specified commands',
    url='https://github.com/Vadim-3/Console-assistant.git',
    author='Team "InnowateHer"',
    author_email='bezhukvadim.56@gmail.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'],
    packages=find_namespace_packages(),
    data_files=('console_assistant', ['console_assistant/notes.json']),
    include_package_data=True,
    entry_points={'console_scripts': [
        'start=console_assisatant.main:main']}  # main.py
)
