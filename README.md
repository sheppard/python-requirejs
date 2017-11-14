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

`python-requirejs` is available via PyPI:

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

Hopefully, all of the [available build options for r.js](http://requirejs.org/docs/optimization.html#options) will Just Work.  If you find any discrepancies, please [open a ticket](https://github.com/wq/python-requirejs/issues) to let us know.

This library is meant to be a drop-in replacement for `node r.js -o app.build.json`, and is tested by comparing its output with that command.  However, since the optimize API is being called as a function, you may need to set the working directory explicitly to avoid any unexpected differences in how relative paths are computed:

```python
import requirejs
import json

with open('app/app.build.json') as f:
    config = json.load(f)

requirejs.optimize(
    config,
    working_directory="app/"  # Unique to python-requirejs
)
```


[PyMiniRacer]: https://github.com/sqreen/PyMiniRacer
[env.js]: https://github.com/wq/python-requirejs/blob/master/requirejs/env.js
