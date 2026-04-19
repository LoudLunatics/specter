# Maintainer: LoudLunatics <nauvalazfa@proton.me>
pkgname=specter
pkgver=1.2.0
pkgrel=1
pkgdesc="Ghost Network Recon Engine"
arch=('any')
url="https://github.com/LoudLunatics/specter"
license=('MIT')
depends=('python' 'python-dotenv' 'python-rich' 'nmap')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')

source=("$pkgname-main.tar.gz::https://github.com/LoudLunatics/$pkgname/archive/refs/heads/main.tar.gz")
sha256sums=('SKIP')

build() {
  cd "$pkgname-main"
  # Pastikan kita membangun dari folder yang ada setup.py nya
  python -m build --wheel --no-isolation
}

package() {
  cd "$pkgname-main"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
