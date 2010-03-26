from setuptools import setup, find_packages
 
setup(
    name='django-paypal',
    version='0.1',
    description='Python/Vimeo interface to advanced API v2 + OAuth.',
    author='John Boxall',
    author_email='john@mobify.me',
    url='http://bitbucket.org/johnboxall/django-paypal/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
)
