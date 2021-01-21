from setuptools import setup, find_packages

setup(
    name='mesa-model-assistant',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A package containing helper classes for batchruning agent-based models implemented in mesa.',
    long_description=open('README.md').read(),
    install_requires=['numpy',
                        'pandas',
                        # 'multiprocessing',
                        'mesa'
                    ],
    url="https://github.com/nikita-sivakumar/mesa-model-assistant.git",
    author='Nikita Sivakumar',
    author_email='nikita.sivakumar@gmail.com'
)