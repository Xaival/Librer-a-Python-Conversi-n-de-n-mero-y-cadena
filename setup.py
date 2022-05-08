from setuptools import setup

setup (
    name="Secuenciador alfanumérico",
    packages=['ConvertDicc'], # Este debe ser el mismo que el nombre de la carpeta
    version="2022.05.08",
    description="Convierte de un número o números a un grupo de caracteres y viceversa",
    author="Xaival",
    author_email="xaival.dark@gmail.com",
    url='https://github.com/Xaival/Libreria-Python-Secuenciador-alfanumerico', # Usar la URL del repositorio de github
    keywords=['conversions', 'sequence', 'alphanumeric', 'binary'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)
