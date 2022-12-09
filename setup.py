from setuptools import setup
setup(
    name= "paquete",
    version = "0.1",
    description="Este es un paquete ejemplo",
    author="Hector Costa",
    author_email= "hola@hektorprofe.com",
    url="http://www.hektorprofe.com",
    packages=['paquete', 'paquete.hola', 'paquete.adios'],
    scripts=[]
)