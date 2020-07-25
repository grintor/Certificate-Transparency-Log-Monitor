# Certificate-Transparency-Log-Monitor
A native Certificate Transparency Log Monitor written in python

This is a script I scratched together from my research online while learning how the concept of Certificate Transparency works.
It is a kind of neat toy that will display the domain names in the console in real time of every new certificate issued by let's encrypt.
It does this by querying "Oak" https://letsencrypt.org/2019/05/15/introducing-oak-ct-log.html

To use:
pip install pyOpenSSL
pip install construct==2.9.52
run Certificate-Transparency-Log-Monitor.py
