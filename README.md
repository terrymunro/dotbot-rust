# Dotbot `rust` plugin

Plugin for [dotbot](https://github.com/anishathalye/dotbot) that adds a `rustup` and `cargo` directive, to allow you to install:

* rustup
    * toolchains
    * targets
    * components
* cargo
    * binaries

## Installation

Add it as a submodule of your dotfiles repositories.

```sh
git submodule add https://github.com/terrymunro/dotbot-rust.git
```

Modify your `install` script, to enable the plugin.

```sh
"${BASEDIR}/${DOTBOT_DIR}/${DOTBOT_BIN}" \
    --package-dir dotbot-rust \
    -d "${BASEDIR}" \
    -c "${CONFIG}" \
    "${@}"
```

## Usage

### Full example

```yaml

```

### Minimal example

```yaml
- rustup:
    install: true



```
