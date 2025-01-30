with import <nixpkgs> {};
let
 my-python = pkgs.python3;
  mypython = my-python.withPackages (p: with p; [
	prettytable
	scipy
	sphinx
	furo
	pip
    autopep8
	sage
	pytest
  ]);
in
{ pkgs ? import <nixpkgs> {} }:

stdenv.mkDerivation {
  name = "cryptographic_estimators";
  src = ./.;

  buildInputs = [ 
    mypython
	ripgrep
	tree
  ];

  shellHook = ''
    export PIP_PREFIX=$(pwd)/_build/pip_packages
    export PYTHONPATH="$PIP_PREFIX/${mypython.sitePackages}:$PYTHONPATH"
    export PATH="$PIP_PREFIX/bin:$PATH"
    # unset SOURCE_DATE_EPOCH
  '';
}
