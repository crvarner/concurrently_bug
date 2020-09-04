# concurrently_bug
minimum bug reproduction

to reproduce [issue#241](https://github.com/kimmobrunfeldt/concurrently/issues/241)

```
(py3_venv)$ git clone https://github.com/crvarner/concurrently_bug.git
(py3_venv)$ pip install flask
(py3_venv)$ npm install
(py3_venv)$ npm start
```
refresh http://localhost:5000/

setting raw flag produces expected behavior without the pretty colors
```
(py3_venv)$ npm run raw
```
