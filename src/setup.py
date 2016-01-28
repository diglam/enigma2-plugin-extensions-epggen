""""setup for packaging."""

from distutils.core import setup, Extension
import setup_translate


dreamcrc = Extension('Extensions/EPGregen/dreamcrc',
                     sources=['dreamcrc.c'])

pkg = 'Extensions.EPGregen'
setup(name='enigma2-plugin-extensions-epgregen',
      version='0.0.1',
      description='C implementation of Dream CRC32 algorithm',
      package_dir={pkg: 'EPGepg'},
      packages=[pkg],
      package_data={pkg: ['*.png', 'locale/*/LC_MESSAGES/*.mo']},
      ext_modules=[dreamcrc],
      cmdclass=setup_translate.cmdclass,  # for translation
      )
