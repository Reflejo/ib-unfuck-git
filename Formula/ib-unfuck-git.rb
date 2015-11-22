class IbUnfuckGit < Formula
  desc "Removes unnecessary changes from iOS/OSX repositories"
  homepage "https://github.com/Reflejo/ib-unfuck-git"
  url "https://github.com/Reflejo/ib-unfuck-git/archive/v0.1.tar.gz"

  depends_on :python if MacOS.version <= :snow_leopard

#  resource "unidiff" do
#    url "https://pypi.python.org/packages/source/u/unidiff/unidiff-0.5.1.tar.gz"
#    sha256 "c3d52b3656044c90af6cd01b3424d21d669e99899f1bdde82cc4bbd3fa5fda67"
#  end
#
#  resource "gitdb" do
#    url "https://pypi.python.org/packages/source/g/gitdb/gitdb-0.6.4.tar.gz"
#    sha256 "a3ebbc27be035a2e874ed904df516e35f4a29a778a764385de09de9e0f139658"
#  end
#
#  resource "smmap" do
#    url "https://pypi.python.org/packages/source/s/smmap/smmap-0.9.0.tar.gz"
#    sha256 "0e2b62b497bd5f0afebc002eda4d90df9d209c30ef257e8673c90a6b5c119d62"
#  end

  def install
    ENV.prepend_create_path "PYTHONPATH", libexec/"vendor/lib/python2.7/site-packages"
#    %w[gitdb smmap unidiff].each do |r|
#      resource(r).stage do
#        system "python", *Language::Python.setup_install_args(libexec/"vendor")
#      end
#    end

    ENV.prepend_create_path "PYTHONPATH", libexec/"lib/python2.7/site-packages"
    system "python", *Language::Python.setup_install_args(libexec)

    bin.install Dir[libexec/"bin/*"]
    bin.env_script_all_files(libexec/"bin", :PYTHONPATH => ENV["PYTHONPATH"])
  end

  test do
  end
end
