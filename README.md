# plugin system demo

prepare
```
python -m venv .venv
. .venv/bin/activate

(.venv) $ cd core
(.venv) $ pip install -e .

(.venv) $ cd ../plugin
(.venv) $ pip install -e .
```

run demo command
```
(.venv) $ demo
Hello from default!

(.venv) $ demo plugin
Hello, from plugin!
```
