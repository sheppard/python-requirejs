# python-requirejs

Run RequireJS (r.js) from Python without requiring Node or Rhino.  Leverages [PyMiniRacer] plus a minimal [JS environment][env.js] to make r.js think it's running in node.

[![Latest PyPI Release](https://img.shields.io/pypi/v/requirejs.svg)](https://pypi.python.org/pypi/requirejs)
[![Release Notes](https://img.shields.io/github/release/wq/python-requirejs.svg)](https://github.com/wq/python-requirejs/releases)
[![License](https://img.shields.io/pypi/l/requirejs.svg)](https://github.com/wq/python-requirejs/blob/master/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/wq/python-requirejs.svg)](https://github.com/wq/python-requirejs/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/wq/python-requirejs.svg)](https://github.com/wq/python-requirejs/network)
[![GitHub Issues](https://img.shields.io/github/issues/wq/python-requirejs.svg)](https://github.com/wq/python-requirejs/issues)

[![Travis Build Status](https://img.shields.io/travis/wq/python-requirejs/master.svg)](https://travis-ci.org/wq/python-requirejs)
[![Python Support](https://img.shields.io/pypi/pyversions/requirejs.svg)](https://pypi.python.org/pypi/requirejs)

## Usage

`python-requirejs` (will soon be) available via PyPI:

```bash
pip install requirejs
```

### API

```python
import requirejs


requirejs.optimize(
    appDir=".",
    baseUrl="js/",
    modules=[{
        "name": "main",
    }]
    dir="../build",
)
```

[PyMiniRacer]: https://github.com/sqreen/PyMiniRacer
[env.js]: https://github.com/wq/python-requirejs/blob/master/requirejs/env.js
