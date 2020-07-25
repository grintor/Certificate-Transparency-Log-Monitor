import json
import base64
import ctl_parser_structures
from OpenSSL import crypto
import requests
import time

def entry2domain(entry):
	leaf_cert = ctl_parser_structures.MerkleTreeHeader.parse(base64.b64decode(entry['leaf_input']))
	#print("Leaf Timestamp: {}".format(leaf_cert.Timestamp))
	#print("Entry Type: {}".format(leaf_cert.LogEntryType))

	if leaf_cert.LogEntryType == "X509LogEntryType":
		# We have a normal x509 entry
		cert_data_string = ctl_parser_structures.Certificate.parse(leaf_cert.Entry).CertData
		chain = [crypto.load_certificate(crypto.FILETYPE_ASN1, cert_data_string)]

		# Parse the `extra_data` structure for the rest of the chain
		extra_data = ctl_parser_structures.CertificateChain.parse(base64.b64decode(entry['extra_data']))
		for cert in extra_data.Chain:
			chain.append(crypto.load_certificate(crypto.FILETYPE_ASN1, cert.CertData))
	else:
		# We have a precert entry
		extra_data = ctl_parser_structures.PreCertEntry.parse(base64.b64decode(entry['extra_data']))
		chain = [crypto.load_certificate(crypto.FILETYPE_ASN1, extra_data.LeafCert.CertData)]

		for cert in extra_data.Chain:
			chain.append(
				crypto.load_certificate(crypto.FILETYPE_ASN1, cert.CertData)
			)

	# Chain is now an array of X509 objects, leaf certificate first, ready for extraction!
	
	domain = chain[0].get_subject().commonName

	return (domain)


def get_last_entry_available():
	time.sleep(1) # dumb rate limit
	return int(requests.get('https://oak.ct.letsencrypt.org/2020/ct/v1/get-sth').json()['tree_size'] - 1)
	
last_entry_displayed = get_last_entry_available()

while True:
	last_entry_available = get_last_entry_available()
	#print('last_entry_available: %s, last_entry_displayed: %s' % (last_entry_available, last_entry_displayed))
	if last_entry_displayed < last_entry_available:
		entries = requests.get('https://oak.ct.letsencrypt.org/2020/ct/v1/get-entries?start=%s&end=%s' % (last_entry_displayed, last_entry_available)).json()['entries']
		last_entry_displayed = last_entry_available + 1
		for entry in entries:
			print(entry2domain(entry))













