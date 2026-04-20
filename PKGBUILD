# Maintainer: Red Team <redteam@localhost>
pkgname=spectre-loc
pkgver=1.0.0
pkgrel=1
pkgdesc="Geolocation Surveillance & Recon Engine based on Shodan"
arch=('any')
license=('MIT')
depends=('python' 'python-dotenv' 'python-rich' 'python-shodan')

# Using the latest Arch Linux standard (PEP 517)
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
source=()

# Skipping checksum process because this is a local build
sha256sums=()

build() {
  # Enter the directory where this PKGBUILD is located
  cd "$startdir"
  # Create the .whl (Wheel) file
  python -m build --wheel --no-isolation
}

package() {
  cd "$startdir"
  # Install the .whl file to the Pacman system
  python -m installer --destdir="$pkgdir" dist/*.whl
}