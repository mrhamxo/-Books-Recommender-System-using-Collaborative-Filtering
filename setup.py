from setuptools import find_packages, setup

# Safely read dependencies from requirements.txt, excluding "-e ."
def load_requirements(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        return [line.strip() for line in lines if line.strip() and not line.startswith("-e")]

setup(
    name="books_recommendation",
    version="0.1.0",
    author="Muhammad Hamza",
    author_email="mr.hamxa942@gmail.com",
    description="A machine learning based book recommendation system using collaborative filtering.",
    long_description="""
        This is a machine learning project that provides personalized book recommendations 
        based on user ratings using K-Nearest Neighbors (KNN) and collaborative filtering techniques.
    """,
    long_description_content_type="text/markdown",
    url="https://github.com/mrhamxo/-Books-Recommender-System-using-Collaborative-Filtering",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.9",
    install_requires=load_requirements("requirements.txt")
)
