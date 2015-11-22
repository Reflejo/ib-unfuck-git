class IbUnfuckGit < Formula
  desc "Removes unnecessary changes from iOS/OSX repositories"
  homepage "https://github.com/Reflejo/ib-unfuck-git"
  url "https://github.com/Reflejo/ib-unfuck-git/archive/v0.1.tar.gz"

  depends_on :python if MacOS.version <= :snow_leopard
  depends_on "unidiff" => :python
  depends_on "gitpython" => :python
  depends_on "lxml" => :python

  def install
    ENV.prepend_create_path "PYTHONPATH", libexec/"lib/python2.7/site-packages"
    system "python", *Language::Python.setup_install_args(libexec)

    bin.install Dir[libexec/"bin/*"]
    bin.env_script_all_files(libexec/"bin", :PYTHONPATH => ENV["PYTHONPATH"])
  end

  test do
  end
end
