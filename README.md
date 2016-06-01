#QAReplayProxy - Quality Metrics Proxy for Web Archiving Replay

A simple proxy and Browser automatization, based on [pymiprox](https://github.com/allfro/pymiproxy) to gather metrics information about the Wayback Machines.

##Introduction

QAReplayProxy is a simple program that creates a proxy that intercept traffic and gather metrics about Replay Quality. It is based on pyimprox with a specialized Interceptor, and browses archiving pages using selenium against the proxy.

##Installation Requirements

The following modules are required:

- pyOpenSSL
- selenium
- pyvirtualdisplay

A Display enviroment is needed to be configured.
The recommended backend to run is Xvfb:
```bash
$ yum install xvfb
```


##Installation

Just run the following command at the command prompt:

```bash
$ sudo python setup.py install
```

##Usage

To run mimproxy:

```bash
$ python -m miproxy.proxy
```

This will invoke pymiproxy with the ```QAReplayInterceptor``` plugin which gather metrics about the replay and then print them to files at the end of the testing. The proxy runs at port 8080.

To run browser replay:
```bash
$ python -m replay.control_browser test_urls.txt
```
