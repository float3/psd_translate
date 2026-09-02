{
  description = "psd_translate";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
      python = pkgs.python3;
    in {
      formatter = pkgs.alejandra;

      devShells.default = pkgs.mkShell {
        packages = [
          python
          pkgs.ruff
          python.pkgs.pip
          python.pkgs.virtualenv
        ];

        shellHook = ''
          if [ ! -d .venv ]; then
            ${python}/bin/python -m venv .venv
          fi
          source .venv/bin/activate
        '';
      };
    });
}
