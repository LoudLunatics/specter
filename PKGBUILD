pkgname=specter
pkgver=1.2.0
pkgrel=1
pkgdesc="Ghost Network Recon Engine (Standalone Nmap Scanner)"
arch=('any')
license=('MIT')

depends=('python' 'python-rich' 'nmap')

makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')

source=()
sha256sums=()

build() {
  cd "$startdir"
  rm -rf build/
  python -m build --wheel --no-isolation
}

package() {
  cd "$startdir"
  python -m installer --destdir="$pkgdir" dist/*.whl
}