from setuptools import setup, find_packages
    
    setup(
        name="profit-agent",
        version="0.1.0",
        packages=find_packages(),
        install_requires=[
            "httpx>=0.25.0",
            "python-dotenv>=1.0.0",
        ],
        entry_points={
            "console_scripts": [
                "profit-agent=agent:main",
            ],
        },
    )
    