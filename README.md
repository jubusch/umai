
# UMAI

UMAI is a user model artificial intelligence implemented in the cognitive architecture act-r. It is modeled to compute activations from an action stream which is tracked from interaction with EXTRA. EXTRA (EXercise TRAiner) is a serious game which is intended to teach economic production processes. 
UMAI is architectured as an independend microservice and makes an API available to front end designers. This API supports modification of act-r settings like noise or threshold and accessing the activation values of chunks created during a simulation. 

## Getting Started

Install [Flask Rest Plus](http://flask-restplus.readthedocs.io/en/stable/) : 

```
pip install flask-restplus
```

Install [Flask Cors](https://flask-cors.readthedocs.io/en/latest/) :

```
pip install -U flask-cors
```


### Prerequisites

* Python 2.7 (this project only runs in 2.7. due to CCM!)
* [CCM](https://github.com/tcstewar/ccmsuite) for Python 2.7
    
## Deployment

In the root directory run 
```
python cogarch_api.py
```


## Contributing

Please read [CONTRIBUTING.md]() for details on our code of conduct.

## Authors

**Julius Busch** 
julius.busch@gmail.com


## License

see the [LICENSE.md](LICENSE.md) file for details



