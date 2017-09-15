set -e
if [ "$LINT" ]; then
    jshint requirejs/env.js
    flake8 requirejs tests
else
    python setup.py test
fi
