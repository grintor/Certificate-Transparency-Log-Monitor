# Certificate-Transparency-Log-Monitor
A native Certificate Transparency Log Monitor written in python

This is a script I scratched together from my research online while learning how the concept of [Certificate Transparency](http://www.certificate-transparency.org/) works while striving to further beef up security on [helpdeskbuttons.com](https://helpdeskbuttons.com) using the ["Expect-CT" HTTP Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expect-CT).
It is a neat toy that will print the domain names to the console (in real time) of every new certificate issued by let's encrypt. That's usually about 24 domains per second!
It does this by querying ["Oak"](https://letsencrypt.org/2019/05/15/introducing-oak-ct-log.html) according to [RFC 6962](https://tools.ietf.org/html/rfc6962)

The interesting thing here is that you can learn about all kinds of domains that were never intended to be public knowledge (just look at all these phpmyadmin.xxx.com domains), which I think demonstrates how few admins know about certificate transparency yet.

To use:

```
pip install pyOpenSSL
pip install construct==2.9.52
run Certificate-Transparency-Log-Monitor.py
```
